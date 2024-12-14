#!/usr/bin/env python2

import base64
import time
import urlparse as cgi
import urllib
from Crypto.Cipher import AES
from Crypto.Signature import PKCS1_v1_5
from Crypto.Hash import SHA256
from Crypto.PublicKey import RSA
import xml.etree.cElementTree as ET

b64key = open('urlkey.b64').read()
encuri = open('url.encrypted').read()

def sign_token(token):
    key = RSA.importKey(open('private_key.der').read())
    h = SHA256.new(token)
    return PKCS1_v1_5.new(key).sign(h)

def make_ticket(username):
    # Generate an XML login ticket for the specified username, with generic metadata suitable for
    # JIT provisioning of user accounts within the target system (if enabled)
    t = time.gmtime()
    timestamp = time.strftime('%m%d%Y%H%M%S',t)

    root = ET.Element('TICKET',DOMAIN="EPICURL")
    root.set('TIMESTAMP',timestamp)

    user = ET.SubElement(root,'USER',FIRST_NAME="Epic", LAST_NAME="User")
    user.set('USERNAME', username)

    return ET.tostring(root, encoding='utf8').decode('utf8')

def decrypturl(url):
    # extract the iv and the ciphertext from the url by splitting it on the ==
    ivb = url.split('==')[0] + '==';
    datab = url.split('==')[1] + '==';

    key = base64.b64decode(b64key)
    iv = base64.b64decode(ivb)
    data = base64.b64decode(datab)
    cipher = AES.new(key, AES.MODE_CBC, iv)
    content = cipher.decrypt(data)

    return content.decode('utf-8')

def get_url(req):
    uri = decrypturl(req)
    if uri:
        vals = cgi.parse_qs(uri,True)
        if vals['login_user']:
            # Convert the login request to a single-sign-on request for the requested user
            ticket = make_ticket(vals['login_user'][0])
            sig = sign_token(ticket)

            if ticket and sig:
                # replace any existing log-in information with the SSO information
                vals['login_ticket'] = [ticket]
                vals['login_signature'] = [base64.b64encode(sig)]
                vals.pop('login_user')
                vals.pop('login_passwd')

                return urllib.urlencode(vals,True)


if __name__ == '__main__':
    print(get_url(encuri))
