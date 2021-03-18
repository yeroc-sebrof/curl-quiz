from flask import Flask, render_template, request
from flask_httpauth import HTTPBasicAuth
from flask_wtf import Form
from random import choice as pick_one
from werkzeug.security import generate_password_hash, check_password_hash
import re
import os

app = Flask(__name__)
auth = HTTPBasicAuth()

# Password is in this list https://github.com/danielmiessler/SecLists/blob/master/Passwords/Common-Credentials/500-worst-passwords.txt
users = {
    "real": generate_password_hash("sunshine")
}

every_method = ['GET', 'HEAD', 'POST', 'PUT', 'DELETE', 'CONNECT', 'OPTIONS', 'TRACE', 'PATCH']

app.config['SECRET_KEY'] = 'totallysecure'

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
                "big error, much problem",
                """
<html><body>
                16.06.20 JOB00375 ---- THURSDAY,  11 MAR 2021 ----                              <br>
16.06.20 JOB00375  IRR010I  USERID JAKE     IS ASSIGNED TO THIS JOB.            <br>
16.06.20 JOB00375  ICH70001I JAKE     LAST ACCESS AT 16:06:19 ON THURSDAY, MARCH<br>
16.06.20 JOB00375  $HASP373 EXECPGM  STARTED - INIT 1    - CLASS A        - SYS <br>
16.06.20 JOB00375  CSV003I REQUESTED MODULE VOLDATA  NOT FOUND                  <br>
16.06.20 JOB00375  CSV028I ABEND806-04  JOBNAME=EXECPGM   STEPNAME=STEP01       <br>
16.06.20 JOB00375  IEA995I SYMPTOM DUMP OUTPUT  915                             <br>
   915             SYSTEM COMPLETION CODE=806  REASON CODE=00000004             <br>
   915              TIME=16.06.20  SEQ=00229  CPU=0000  ASID=001B               <br>
   915              PSW AT TIME OF ERROR  070C1000   812D3852  ILC 2  INTC 0D   <br>
   915                NO ACTIVE MODULE FOUND                                    <br>
   915                NAME=UNKNOWN                                              <br>
   915                DATA AT PSW  012D384C - 8400181E  0A0D18FB  180C181D      <br>
   915                AR/GR 0: 001FBFFF/00001F00   1: 00000000/84806000         <br>
   915                      2: 00000000/00000000   3: 00000000/00000000         <br>
   915                      4: 00000000/00000000   5: 00000000/008CBEC0         <br>
   915                      6: 00000000/000000FF   7: 00000000/00000000         <br>
   915                      8: 00000000/7F6B5050   9: 00000000/012D3D78         <br>
   915                      A: 00000000/00000000   B: 00000000/00000000         <br>
   915                      C: 00000000/00000000   D: 00000000/7F6B5050         <br>
   915                      E: 00000000/84806000   F: 00000000/00000004         <br>
   915              END OF SYMPTOM DUMP    <br>
</body></html>
                """
            ]

#############################################

@app.route('/', methods=['GET'])
def index():
    return render_template("index.html")

@app.errorhandler(404)
def not_found(e):
    return pick_one(not_right)

@app.errorhandler(405)
def method_not_allowed(e):
    return pick_one(not_right)

#############################################

if (os.getenv("PORT") == "8080"):
    @app.route('/challenge5', methods=['GET'])
    def challenge5():
        return "Challenge String: Vjgfqgug it a qugwvy dopo vrql"

    @app.route('/challenge5/hint1', methods=every_method)
    def challenge5hint1():
        if (re.search('(curl|wget)\/*', request.headers.get('User-Agent').lower())):
            return "Have a look at old encoding methods, this ones been around for almost 2000 years"
        else:
            return "Are you using Curl or wget? I don't think you are"

    @app.route('/challenge5/hint2', methods=every_method)
    def challenge5hint2():
        if (re.search('(curl|wget)\/*', request.headers.get('User-Agent').lower())):
            return "Have a look at old encoding methods, this ones been around for almost 2000 years"
        else:
            return "Are you using Curl or wget? I don't think you are"

    if __name__ == '__main__':
        app.run(debug=True, host='0.0.0.0', port=8080)
        exit(0)

#############################################

@app.route('/challenge1', methods=['GET'])
def challenge1():
    if (request.args.get("whoAreYou") == "AHacker" and request.args.get("areYouSure") == "yes" and re.search('(curl|wget)\/*', request.headers.get('User-Agent').lower())):
        return "Challenge String: hfkvi-xllo-xozhhrx-xrksvi"
    else:
        return pick_one(not_right)

@app.route('/challenge1/hint1', methods=every_method)
def challenge1hint1():
    if (re.search('(curl|wget)\/*', request.headers.get('User-Agent').lower())):
        return "Have a look at this https://www.seobility.net/en/wiki/GET_Parameters#Using_Get_Parameters, also think about how your Curl command is being interpreted on the CLI"
    else:
        return "Are you using Curl or wget? I don't think you are"

@app.route('/challenge1/hint2', methods=every_method)
def challenge1hint2():
    return "Have a look at old encoding methods, this ones been around for 3000 years so will be super secure."

#############################################

@app.route('/challenge2', methods=['GET'])
def challenge2():
    if (request.environ.get('SERVER_PROTOCOL') == "HTTP/1.0" and re.search('(curl|wget)\/*', request.headers.get('User-Agent').lower())):
        return "Challenge String: MXE-MEKBT-XQLU-ADEMD-JXQJ-ZKBYKI-SQUIQH'I-SYFXUH-MEKBT-RU-IE-FEFKBQH-QBB-JXUIU-OUQHI-BQJUH.QDOMQO-LQKBJYDW-TYIJEHJ-THKCCEDT-YI-JXU-VBQW.AUUF-JXU-TQIXUI"
    else:
        return pick_one(not_right)

@app.route('/challenge2/hint1', methods=every_method)
def challenge2hint1():
    if (re.search('(curl|wget)\/*', request.headers.get('User-Agent').lower())):
        return "Make sure to run `man curl`"
    else:
        return "Are you using Curl or wget? I don't think you are"

@app.route('/challenge2/hint2', methods=every_method)
def challenge2hint2():
    return "Have a look at old encoding methods, this ones only been around for almost 2000 years. Even the Romans know how to decrypt it"

#############################################

@app.route('/challenge3', methods=every_method)
def challenge3():
    if (request.method == "PATCH" and re.search('(curl|wget)\/*', request.headers.get('User-Agent').lower())):
        return "Challenge String: 5c577753706cdcef8621a9c0c1922158"
    else:
        return pick_one(not_right)

@app.route('/challenge3/hint1', methods=every_method)
def challenge3hint1():
    if (re.search('(curl|wget)\/*', request.headers.get('User-Agent').lower())):
        return "Make sure to run `man curl`"
    else:
        return "Are you using Curl or wget? I don't think you are"

@app.route('/challenge3/hint2', methods=every_method)
def challenge3hint2():
    return "Look into encryption that provides a string of the same length, Cyberchef has some good tools for identifying this but you might need to google for something else"

# https://www.md5online.org/md5-decrypt.html

#############################################

@app.route('/challenge4', methods=['GET', 'POST'])
def challenge4():
    if (request.method == "POST" and re.search('(curl|wget)\/*', request.headers.get('User-Agent').lower())):
        if (request.content_type == "application/json"):
            try:
                request.get_json(force=True)
            except:
                return "I'd never recommend reading RFC 8259 as it's a boring memo but your JSON isn't valid"

            content = request.get_json()

            try:
                if (content['WeGonnaRockDownTo'] == "ElectricBoogaloo"):
                    return "Challenge String: ;f#3*<,\"[<@sLCU@PTrb"
            except:
                pass
                            
            return content
        else:
            # Give a little hint for those who are halfway there
            return "I've never heard of %s" % request.content_type
    else:
        return pick_one(not_right)

@app.route('/challenge4/hint1', methods=every_method)
def challenge4hint1():
    if (re.search('(curl|wget)\/*', request.headers.get('User-Agent').lower())):
        return "Make sure to run `man curl`"
    else:
        return "Are you using Curl or wget? I don't think you are"

@app.route('/challenge4/hint2', methods=every_method)
def challenge4hint2():
    return "Look into encoding methods like Base64"

#############################################

@app.route('/challenge5/hint1', methods=every_method)
def challenge5hint1():
    return "Have a look into common TCP ports"

# if (request.headers.get('User-Agent').toLower() == "curl/*" or request.headers.get('User-Agent').toLower() == "wget/")

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=80)
