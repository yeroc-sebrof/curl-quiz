## Curl Challenge

This lab should be easy enough, apply some CLI knowledge and the man page for curl to get the encoding/encryption challenges. Once you have the challenge you need to decode it to get the flag. Your target is the web server at 192.168.22.100



### Challenge 1 - Different port + GET Param and Atbash

To get the encoding challenge for this one send a GET request to 192.168.22.100/challenge1 with a two parameters, one called encoding2 with the value "ElectricBoogaloo" and the other called Delimiters with the value "AreEasy"

##### Answer

`curl http://192.168.22.100/challenge2?encoding=isCool`

Then Atbash is the reversing of an alphabet to make z>a == a>z

##### Flask

https://stackoverflow.com/questions/24892035/how-can-i-get-the-named-parameters-from-a-url-using-flask


### Challenge 2 - HTTP/1.0 and Caesar Cipher

To get the encoding challenge make a HTTP/1.0 request to http://192.168.22.100/challenge1, for extra style points you can do this using netcat

##### Answer

https://stackoverflow.com/questions/45390338/how-to-use-curl-to-generate-http-1-0-request-for-a-file-without-a-leading-slash

Then Rot 10

##### Flask

`request.environ.get('SERVER_PROTOCOL') # Search for HTTP/1.0 only`

##### Encoding Challenge

MXE-MEKBT-XQLU-ADEMD-JXQJ-ZKBYKI-SQUIQH'I-SYFXUH-MEKBT-RU-IE-FEFKBQH-QBB-JXUIU-OUQHI-BQJUH.QDOMQO-LQKBJYDW-TYIJEHJ-THKCCEDT-YI-JXU-VBQW.AUUF-JXU-TQIXUI

> Decodes to:
>
> Who would have known that Julius Caesar's cipher would be so popular all these years later. Anyway Vaulting Distort Drummond is the flag. Keep the dashes



### Challenge 3 - PATCH request and MD5 secret

Make a HTTP PATCH request to http://192.168.22.100/challenge3

##### Answer

`curl -X PATCH https://example/contact`

##### Flask

https://stackoverflow.com/questions/49093115/put-request-python-flask/49093353


##### Encryption Challenge

 5c577753706cdcef8621a9c0c1922158 == md5 is broken



### Challenge 4 - POST Request with JSON content and Base64 + Base85

POST some JSON content for this one, similar to above where encoding was set to isCool, now set "WeGonnaRockDownTo" to "ElectricBoogaloo"

##### Answer

`curl -X POST -H "Content-Type: application/json" -d '{"json": true}' https://example/contact`

##### Flask

https://techtutorialsx.com/2017/01/07/flask-parsing-json-data/

##### Encoding Challenge 

`JSON is cool` < `SlNPTiBpcyBjb29s` < `;f#3*<,"[<@sLCU@PTrb`



### Challenge 5 - Provide Site HTTPS Certificate Manually and Vigenere Cipher

https://192.168.22.100/challenge5

##### Answer

`curl -E wk.cert https://192.168.22.100/challenge5`

##### Flask




##### Encryption Challenge





### Challenge 6 - HTTP 2.0 and a Header + Sub Cipher

http://192.168.22.100/challenge6

##### Answer

`curl --http2 http://192.168.22.100/challenge6`

##### Flask




##### Encryption Challenge





### Challenge 7 - PUT a file then GET and XOR

http://192.168.22.100/challenge7

##### Answer

`curl http://192.168.22.100/challenge7`

##### Flask

https://stackoverflow.com/questions/49093115/put-request-python-flask/49093353


##### Encryption Challenge

