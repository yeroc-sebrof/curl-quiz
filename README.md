## Curl Challenge

This lab should be easy enough, apply some CLI knowledge and the man page for curl to get the encoding/encryption challenges. Once you have the challenge you need to decode it to get the flag. Your target is the web server at 192.168.22.100

Don't forget to use Curl's man page if you need some help!

---

### Challenge 1 - Different port + GET Param and Atbash

To get the encoding challenge for this one send a GET request to 192.168.22.100/challenge1 with a two parameters, one called whoAreYou with the value AHacker and the other called areYouSure with the value yes

<details>
 <summary markdown="span">Answer</summary>

`curl http://192.168.22.100/challenge1?whoAreYou=AHacker&areYouSure=yes`

- **NOTE**: slashes are required in front of the `?` and `&` symbols (`\?` and `\&` respectively)

- Challenge String: hfkvi-xllo-xozhhrx-xrksvi
- Atbash is the reversing of an alphabet to make z>a == a>z
    - http://rumkin.com/tools/cipher/atbash.php
- Resolves to: super-cool-classic-cipher
</details>

---

### Challenge 2 - HTTP/1.0 and Caesar Cipher

To get this encoding challenge make a HTTP/1.0 request to http://192.168.22.100/challenge2. Curl will default to doing a HTTP/1.1 request

<details>
 <summary markdown="span">Answer</summary>

`curl --http1.0 http://192.168.22.100/challenge2`

- Challenge String: `MXE-MEKBT-XQLU-ADEMD-JXQJ-ZKBYKI-SQUIQH'I-SYFXUH-MEKBT-RU-IE-FEFKBQH-QBB-JXUIU-OUQHI-BQJUH.QDOMQO-LQKBJYDW-TYIJEHJ-THKCCEDT-YI-JXU-VBQW.AUUF-JXU-TQIXUI`
- A Rotation of 10 characters using the Caesar/Rot13 Cipher
- Resolves to: `Who would have known that Julius Caesar's cipher would be so popular all these years later. Anyway Vaulting Distort Drummond is the flag. Keep the dashes`
</details>

---

### Challenge 3 - PATCH request and MD5 secret

HTTP 1.1 has a fair few methods that are documented but anyone could make any method they wanted. In this case make a HTTP PATCH request to http://192.168.22.100/challenge3

<details>
 <summary markdown="span">Answer</summary>

`curl -X PATCH http://192.168.22.100/challenge3`

- Challenge String: 5c577753706cdcef8621a9c0c1922158
- https://www.md5online.org/md5-decrypt.html is the first result on Google when searching "md5 decrypt"
- Decodes to: md5 is broken
</details>

---

### Challenge 4 - POST Request with JSON content and Base64 + Base85

POST some JSON content for this one (in a similar fashion to above where encoding was set to whoAreYou) now in your POST Requests JSON body, set "WeGonnaRockDownTo" to "ElectricBoogaloo"

<details>
 <summary markdown="span">Answer</summary>

`curl -X POST -H "Content-Type: application/json" -d '{"WeGonnaRockDownTo":"ElectricBoogaloo"}' http://192.168.22.100/challenge4`

- Challenge String: `;f#3*<,"[<@sLCU@PTrb`
- Base85 Decode to: `SlNPTiBpcyBjb29s`
- Base64 Decode to: `JSON is cool`
</details>

---

### Challenge 5 - Request a different TCP Port and Vigenere Cipher

An easy challenge now that we're near the end. Send a GET request to port 8080 for this one

- FIXME: `curl: (7) Failed to connect to 192.168.0.113 port 8080 after 0 ms: Connection refused`

<details>
 <summary markdown="span">Answer</summary>

`curl "http://192.168.22.100:8080/challenge5"`

- Challenge String: `Vjgfqgug it a qugwvy dopo vrql`
- https://www.boxentriq.com/code-breaking/vigenere-cipher has an auto-solver
- The secret key is `ababdcdc`
- Decodes to: `vigenere is a pretty cool tool`
</details>

---

### Challenge 6 - PUT and XOR

Start by running `echo "superMegaFinalFlagFile" > file.txt` then upload that file using the HTTP PUT method to challenge6

<details>
 <summary markdown="span">Answer</summary>

`curl -T ./file.txt -X PUT http://172.18.0.2/challenge6` or `curl --upload-file ./file.txt -X PUT http://172.18.0.2/challenge6`

- Challenge String: `07 0d 0a 06 72 1d 1c 17 63 10 1c 06 1c 01 0a 1b 15 65 00 11 16 13 14 65 1a 16 63 02 1b 09 17 65 0a 75 11 04 1d 11 63 17 17 09 1a 13 06 75 1a 0a 04 65 14 10 1e 09 73 0c 17 75 05 0a 01 0e 10 75 13 0b 17 65 0b 1a 05 65 00 00 00 00 00 00 73 0c 17 75 1b 16 73 11 0c 1a 7c 65 1d 0a 17 1c 11 00 73 0d 0c 02 72 0c 73 10 10 10 72 11 1b 00 63 1e 17 1c 73 0c 0d 75 06 0d 16 65 17 10 0a 11 73 04 0d 11 72 11 1b 00 0d 75 06 0d 16 65 17 10 0a 11 73 11 16 07 1c 16 73 0c 0d 01 1d 65 63 62 10 75 13 0b 0a 12 02 0c 72 11 1b 00 63 13 1e 04 14 65 0a 06 72 1d 1c 17 6e 1c 01 68 10 0a 0c 19 7c 65 12 0b 07 75 06 0d 12 11 64 06 72 11 1b 00 63 13 1b 0b 12 09 63 13 1e 04 14 65 0c 13 72 11 1b 0c 10 75 11 0d 12 09 0f 10 1c 02 16 65 0a 75 1a 0a 03 00 63 0c 1d 10 74 13 06 75 17 0b 19 0a 1a 10 16 65 12 0b 07 75 1b 65 12 09 10 1a 72 0d 1c 15 06 75 06 0d 1a 16 63 1c 01 65 16 0b 0c 00 15 0d 73 11 06 0d 06 65 07 0a 63 18 13 0e 16 65 1b 1a 00 65 11 17 16 01 17 65 15 0a 11 16 17 65 12 0b 63 1a 02 11 1a 0a 0d`
- `https://gchq.github.io/CyberChef/#recipe=From_Hex('Auto')XOR(%7B'option':'UTF8','string':'SECURE'%7D,'Standard',false)&input=MDcgMGQgMGEgMDYgNzIgMWQgMWMgMTcgNjMgMTAgMWMgMDYgMWMgMDEgMGEgMWIgMTUgNjUgMDAgMTEgMTYgMTMgMTQgNjUgMWEgMTYgNjMgMDIgMWIgMDkgMTcgNjUgMGEgNzUgMTEgMDQgMWQgMTEgNjMgMTcgMTcgMDkgMWEgMTMgMDYgNzUgMWEgMGEgMDQgNjUgMTQgMTAgMWUgMDkgNzMgMGMgMTcgNzUgMDUgMGEgMDEgMGUgMTAgNzUgMTMgMGIgMTcgNjUgMGIgMWEgMDUgNjUgMDAgMDAgMDAgMDAgMDAgMDAgNzMgMGMgMTcgNzUgMWIgMTYgNzMgMTEgMGMgMWEgN2MgNjUgMWQgMGEgMTcgMWMgMTEgMDAgNzMgMGQgMGMgMDIgNzIgMGMgNzMgMTAgMTAgMTAgNzIgMTEgMWIgMDAgNjMgMWUgMTcgMWMgNzMgMGMgMGQgNzUgMDYgMGQgMTYgNjUgMTcgMTAgMGEgMTEgNzMgMDQgMGQgMTEgNzIgMTEgMWIgMDAgMGQgNzUgMDYgMGQgMTYgNjUgMTcgMTAgMGEgMTEgNzMgMTEgMTYgMDcgMWMgMTYgNzMgMGMgMGQgMDEgMWQgNjUgNjMgNjIgMTAgNzUgMTMgMGIgMGEgMTIgMDIgMGMgNzIgMTEgMWIgMDAgNjMgMTMgMWUgMDQgMTQgNjUgMGEgMDYgNzIgMWQgMWMgMTcgNmUgMWMgMDEgNjggMTAgMGEgMGMgMTkgN2MgNjUgMTIgMGIgMDcgNzUgMDYgMGQgMTIgMTEgNjQgMDYgNzIgMTEgMWIgMDAgNjMgMTMgMWIgMGIgMTIgMDkgNjMgMTMgMWUgMDQgMTQgNjUgMGMgMTMgNzIgMTEgMWIgMGMgMTAgNzUgMTEgMGQgMTIgMDkgMGYgMTAgMWMgMDIgMTYgNjUgMGEgNzUgMWEgMGEgMDMgMDAgNjMgMGMgMWQgMTAgNzQgMTMgMDYgNzUgMTcgMGIgMTkgMGEgMWEgMTAgMTYgNjUgMTIgMGIgMDcgNzUgMWIgNjUgMTIgMDkgMTAgMWEgNzIgMGQgMWMgMTUgMDYgNzUgMDYgMGQgMWEgMTYgNjMgMWMgMDEgNjUgMTYgMGIgMGMgMDAgMTUgMGQgNzMgMTEgMDYgMGQgMDYgNjUgMDcgMGEgNjMgMTggMTMgMGUgMTYgNjUgMWIgMWEgMDAgNjUgMTEgMTcgMTYgMDEgMTcgNjUgMTUgMGEgMTEgMTYgMTcgNjUgMTIgMGIgNjMgMWEgMDIgMTEgMWEgMGEgMGQ`
- Decodes to: `THIS XOR ENCODING STUFF IS WILD I CANT BELIVE HOW WELL IT WORKS AND HOW SECURE IT IS TOO. NOTICE HOW I USE THE KEY IN THE TEXT AND THEN THE TEXT TURNS INTO 0'S ANYWAY THE FLAG IS XOR-IS-COOL. AND THAT'S THE FINAL FLAG OF THIS CHALLENGE I HOPE YOU'VE ENJOYED AND I ALSO HOPE THIS IS ENOUGH TEXT TO MAKE XOR BRUTE FORCE AN OPTION`
</details>
