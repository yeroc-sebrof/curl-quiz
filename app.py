from flask import Flask, render_template, request
from flask_httpauth import HTTPBasicAuth
from flask_wtf import Form

from random import choice as pick_one

from werkzeug.utils import secure_filename
from werkzeug.security import generate_password_hash, check_password_hash

import hashlib
import re
import os

app = Flask(__name__)
# auth = HTTPBasicAuth()

# Password is part of this list https://github.com/danielmiessler/SecLists/blob/master/Passwords/Common-Credentials/500-worst-passwords.txt
# users = {
#     "real": generate_password_hash("sunshine")
# }

every_method = ['GET', 'HEAD', 'POST', 'PUT', 'DELETE', 'CONNECT', 'OPTIONS', 'TRACE', 'PATCH']

# UPLOADPATH = '/tmp/flask-files/'
# if not os.path.isdir("/tmp/flask-files"):
#     os.mkdir(UPLOADPATH)
# app.config['UPLOAD_FOLDER'] = UPLOADPATH

app.config['SECRET_KEY'] = '22totallysecure'
app.config['MAX_CONTENT_PATH'] = 4096

DEBUG=False

# Custom errors
not_right = [   "",
                "Nope, try again!",
                "This aint it chief",
                "That didn't work",
                "Challenge String: Not really, this is an error message. Try again",
                "Nope, that didn't work",
                "Error: Input not expected",
                "Hmm, this doesn't look right. Keep going!",
                "Not yet, keep at it",
                "Try again, but not what you just did because this didn't work",
                "No Bueno",
                "No dice",
                "wow that attempt was on fleek",
                "we stan you trying",
                "Your PC ran into a problem and needs to restart. We're just collecting some error info, and we'll restart for you.",
                "Try harder, you'll get OSCP in no time",
                "<html><body><img src='/static/hacker.gif'></body></html>",
                "<html><body><video><source src='/static/classic.mp4' type='video/mp4'></video></body><script>document.addEventListener('click', e => { document.getElementsByTagName('video')[0].play() });</script></html>",
                "Please see the following link http://nameofwebsite/help",
                "Task failed successfully",
                "Task successfully failed",
                "big error, much problem"
            ]

errormsg =[]
for i in not_right:
    errormsg.append(i + "\n") # adding newline otherwise terminal looks messy
############################################# custom error handling

@app.route('/', methods=['GET'])
def index():
    return render_template("index.html")

@app.errorhandler(404)
def not_found(e):
    return pick_one(errormsg)

@app.errorhandler(405)
def method_not_allowed(e):
    return pick_one(errormsg)

# @app.errorhandler(500)
# def internal_err(e):
#     return pick_one(not_right)

############################################# challenge 5


@app.route('/challenge5', methods=['GET'])
def challenge5():
    if (os.getenv("PORT") == '8080' and re.search('(curl|wget)\/*', request.headers.get('User-Agent').lower())):
        return "Challenge String: Vjgfqgug it a qugwvy dopo vrql\n"
    else:
        return pick_one(errormsg)

@app.route('/challenge5/hint1', methods=every_method)
def challenge5hint1():
    if (re.search('(curl|wget)\/*', request.headers.get('User-Agent').lower())):
        if (os.getenv("PORT") == '8080'):
            return "Have a look at old encoding methods, this ones been around for almost 2000 years\n"
        else:
            return "Have a look into common TCP ports\n"
    else:
        return "I wouldn't look for hints on a cURL challenge using the browser...\n" # Making it more obvious that user should curl for hints

@app.route('/challenge5/hint2', methods=every_method)
def challenge5hint2():
    if (re.search('(curl|wget)\/*', request.headers.get('User-Agent').lower())):
        return "Have you heard of Vigenere?\n"
    else:
        return "I wouldn't look for hints on a cURL challenge using the browser...\n"

@app.route('/challenge5/hint3', methods=every_method)
def challenge5hint3():
    if (re.search('(curl|wget)\/*', request.headers.get('User-Agent').lower())):
        return "The code is ababdcdc\n"
    else:
        return "I wouldn't look for hints on a cURL challenge using the browser...\n"

if (__name__ == '__main__' and os.getenv("PORT") == '8080'):
    app.run(debug=DEBUG, host='0.0.0.0', port=8080)
    exit(0)

#############################################

@app.route('/challenge1', methods=['GET'])
def challenge1():
    if (request.args.get("whoAreYou") == "AHacker" and request.args.get("areYouSure") == "yes" and re.search('(curl|wget)\/*', request.headers.get('User-Agent').lower())):
        return "Challenge String: hfkvi-xllo-xozhhrx-xrksvi\n"
    else:
        return pick_one(errormsg)

@app.route('/challenge1/hint1', methods=every_method)
def challenge1hint1():
    if (re.search('(curl|wget)\/*', request.headers.get('User-Agent').lower())):
        return "Have a look at this https://www.seobility.net/en/wiki/GET_Parameters#Using_Get_Parameters, also think about how your Curl command is being interpreted on the CLI\n"
    else:
        return "I wouldn't look for hints on a cURL challenge using the browser...\n"

@app.route('/challenge1/hint2', methods=every_method)
def challenge1hint2():
    return "Have a look at old encoding methods, this ones been around for 3000 years so will be super secure.\n"

#############################################

@app.route('/challenge2', methods=['GET'])
def challenge2():
    if (request.environ.get('SERVER_PROTOCOL') == "HTTP/1.0" and re.search('(curl|wget)\/*', request.headers.get('User-Agent').lower())):
        return "Challenge String: MXE-MEKBT-XQLU-ADEMD-JXQJ-ZKBYKI-SQUIQH'I-SYFXUH-MEKBT-RU-IE-FEFKBQH-QBB-JXUIU-OUQHI-BQJUH.QDOMQO-LQKBJYDW-TYIJEHJ-THKCCEDT-YI-JXU-VBQW.AUUF-JXU-TQIXUI\n"
    else:
        return pick_one(errormsg)

@app.route('/challenge2/hint1', methods=every_method)
def challenge2hint1():
    if (re.search('(curl|wget)\/*', request.headers.get('User-Agent').lower())):
        return "Make sure to run `man curl`\n"
    else:
        return "I wouldn't look for hints on a cURL challenge using the browser...\n"

@app.route('/challenge2/hint2', methods=every_method)
def challenge2hint2():
    return "Have a look at old encoding methods, this one's only been around for about 2000 years. Even the Romans know how to decrypt it\n"

#############################################

@app.route('/challenge3', methods=every_method)
def challenge3():
    if (request.method == "PATCH" and re.search('(curl|wget)\/*', request.headers.get('User-Agent').lower())):
        return "Challenge String: 5c577753706cdcef8621a9c0c1922158\n"
    else:
        return pick_one(errormsg)

@app.route('/challenge3/hint1', methods=every_method)
def challenge3hint1():
    if (re.search('(curl|wget)\/*', request.headers.get('User-Agent').lower())):
        return "Make sure to run `man curl` to see how to set a different HTTP method\n"
    else:
        return "I wouldn't look for hints on a cURL challenge using the browser...\n"

@app.route('/challenge3/hint2', methods=every_method)
def challenge3hint2():
    return "Look into encryption that provides a string of the same length, Cyberchef has some good tools for identifying this but you might need to google for something else\n"

# https://www.md5online.org/md5-decrypt.html

#############################################

@app.route('/challenge4', methods=['GET', 'POST'])
def challenge4():
    if (request.method == "POST" and re.search('(curl|wget)\/*', request.headers.get('User-Agent').lower())):
        if (request.content_type == "application/json"):
            try:
                request.get_json(force=True)
            except:
                return "I'd never recommend reading RFC 8259 as it's a boring memo but your JSON isn't valid\n"

            content = request.get_json()

            try:
                if (content['WeGonnaRockDownTo'] == "ElectricBoogaloo"):
                    return "Challenge String: ;f#3*<,\"[<@sLCU@PTrb\n"
            except:
                pass
                            
            return content
        else:
            # Give a little hint for those who are halfway there
            return "I've never heard of %s" % request.content_type
    else:
        return pick_one(errormsg)

@app.route('/challenge4/hint1', methods=every_method)
def challenge4hint1():
    if (re.search('(curl|wget)\/*', request.headers.get('User-Agent').lower())):
        return "Make sure to run `man curl` to see how to set content type and define a content body\n"
    else:
        return "I wouldn't look for hints on a cURL challenge using the browser...\n"

@app.route('/challenge4/hint2', methods=every_method)
def challenge4hint2():
    return "Look into encoding methods like Base64\n"


#############################################

@app.route('/challenge6', methods=['GET', 'PUT'])
def challenge6():
    if (request.method == 'PUT' and re.search('(curl|wget)\/*', request.headers.get('User-Agent').lower())):
        if hashlib.md5(request.stream.read()).hexdigest() == "96f42b4ab80191dbe644c35ddd97e1c1":
            return """Final Challenge String:
07 0d 0a 06 72 1d 1c 17 63 10 1c 06 1c 01 0a 1b 15 65 00 11 16 13 14 65 1a 16 63 02 1b 09 17 65 0a 75 11 04 1d 11 63 17 17 09 1a 13 06 75 1a 0a 04 65 14 10 1e 09 73 0c 17 75 05 0a 01 0e 10 75 13 0b 17 65 0b 1a 05 65 00 00 00 00 00 00 73 0c 17 75 1b 16 73 11 0c 1a 7c 65 1d 0a 17 1c 11 00 73 0d 0c 02 72 0c 73 10 10 10 72 11 1b 00 63 1e 17 1c 73 0c 0d 75 06 0d 16 65 17 10 0a 11 73 04 0d 11 72 11 1b 00 0d 75 06 0d 16 65 17 10 0a 11 73 11 16 07 1c 16 73 0c 0d 01 1d 65 63 62 10 75 13 0b 0a 12 02 0c 72 11 1b 00 63 13 1e 04 14 65 0a 06 72 1d 1c 17 6e 1c 01 68 10 0a 0c 19 7c 65 12 0b 07 75 06 0d 12 11 64 06 72 11 1b 00 63 13 1b 0b 12 09 63 13 1e 04 14 65 0c 13 72 11 1b 0c 10 75 11 0d 12 09 0f 10 1c 02 16 65 0a 75 1a 0a 03 00 63 0c 1d 10 74 13 06 75 17 0b 19 0a 1a 10 16 65 12 0b 07 75 1b 65 12 09 10 1a 72 0d 1c 15 06 75 06 0d 1a 16 63 1c 01 65 16 0b 0c 00 15 0d 73 11 06 0d 06 65 07 0a 63 18 13 0e 16 65 1b 1a 00 65 11 17 16 01 17 65 15 0a 11 16 17 65 12 0b 63 1a 02 11 1a 0a 0d

This one's tricky so you'll get a hint at the start here. The cipher text is represented above in Hex and a SECURE key has been used to hide its content using XOR.
"""
    return pick_one(errormsg)


@app.route('/challenge6/hint1', methods=every_method)
def challenge6hint1():
    if (re.search('(curl|wget)\/*', request.headers.get('User-Agent').lower())):
        return "Make sure to run `man curl` to see how to put a file into the request body\n"
    else:
        return "I wouldn't look for hints on a cURL challenge using the browser...\n"

@app.route('/challenge6/hint2', methods=every_method)
def challenge6hint2():
    return "There might be multiple ways of using HTTP PUT...\n" #Because I got confused I wanted to add this hint

@app.route('/challenge6/hint3', methods=every_method)
def challenge6hint3():
    return "Have a look for tools that help with XOR\n"

if __name__ == '__main__':
    app.run(debug=DEBUG,host='0.0.0.0', port=80)
