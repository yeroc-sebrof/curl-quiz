## Curl Challenge

This lab should be easy enough, apply some CLI knowledge and the man page for curl to get the encoding/encryption challenges. Once you have the challenge you need to decode it to get the flag. Your target is the web server at 192.168.22.100



### Challenge 1 - Different port + GET Param and Atbash

To get the encoding challenge for this one send a GET request to 192.168.22.100/challenge1 with a two parameters, one called whoAreYou with the value AHacker and the other called areYouSure with the value yes

##### Answer

`curl http://192.168.22.100/challenge1?whoAreYou=AHacker&areYouSure=yes`

- Challenge String: hfkvi-xllo-xozhhrx-xrksvi
- Atbash is the reversing of an alphabet to make z>a == a>z
    - http://rumkin.com/tools/cipher/atbash.php
- Resolves to: super-cool-classic-cipher


### Challenge 2 - HTTP/1.0 and Caesar Cipher

To get this encoding challenge make a HTTP/1.0 request to http://192.168.22.100/challenge2. Curl will default to doing a HTTP/1.1 request

##### Answer

`curl --http1.0 http://172.17.0.2/challenge2`

- Challenge String: `MXE-MEKBT-XQLU-ADEMD-JXQJ-ZKBYKI-SQUIQH'I-SYFXUH-MEKBT-RU-IE-FEFKBQH-QBB-JXUIU-OUQHI-BQJUH.QDOMQO-LQKBJYDW-TYIJEHJ-THKCCEDT-YI-JXU-VBQW.AUUF-JXU-TQIXUI`
- A Rotation of 10 characters using the Caesar/Rot13 Cipher
- Resolves to: `Who would have known that Julius Caesar's cipher would be so popular all these years later. Anyway Vaulting Distort Drummond is the flag. Keep the dashes`

### Challenge 3 - PATCH request and MD5 secret

HTTP 1.1 has a fair few methods that are documented but anyone could make any method they wanted. In this case make a HTTP PATCH request to http://192.168.22.100/challenge3

##### Answer

`curl -X PATCH http://172.17.0.2/challenge3`

- Challenge String: 5c577753706cdcef8621a9c0c1922158
- https://www.md5online.org/md5-decrypt.html is the first result on Google when searching "md5 decrypt"
- Decodes to: md5 is broken

### Challenge 4 - POST Request with JSON content and Base64 + Base85

POST some JSON content for this one (in a similar fashion to above where encoding was set to whoAreYou) now in your POST Requests JSON body, set "WeGonnaRockDownTo" to "ElectricBoogaloo"

##### Answer

`curl -X POST -H "Content-Type: application/json" -d '{"WeGonnaRockDownTo":"ElectricBoogaloo"}' http://172.17.0.2/challenge4`

- Challenge String: `;f#3*<,"[<@sLCU@PTrb`
- Base85 Decode to: `SlNPTiBpcyBjb29s`
- Base64 Decode to: `JSON is cool`


### Challenge 5 - Request a different TCP Port and Vigenere Cipher

An easy challenge now that we're near the end. Send a GET request to port 8080 for this one

##### Answer

`curl "http://172.17.0.2:8080/challenge5"`


### Challenge 6 - PUT and XOR

Start by running `echo "superMegaFinalFlagFile" > file.txt` then upload that file using the HTTP PUT method to challenge7

##### Answer

`curl http://192.168.22.100/challenge7`

##### Flask

https://stackoverflow.com/questions/49093115/put-request-python-flask/49093353


##### Encryption Challenge

