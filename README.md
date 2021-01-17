# curl-quiz

A quiz where you need to learn quiz to get to each question

## Curl Challenge

This lab should be easy enough, apply some CLI knowledge and the man page for curl to get the encoding/encryption challenges. Once you have the challenge you need to decode it to get the flag. Your target is the web server at 192.168.22.100



### Challenge 1 - Different port + GET Param and Atbash

To get the encoding challenge for this one send a GET request to 192.168.22.100/challenge2 with a two parameters, one called encoding2 with the value "ElectricBoogaloo" and the other called Delimiters with the value "AreEasy"

##### Answer

http://192.168.22.100/challenge2?encoding2=ElectricBoogaloo

Then Atbash is the reversing of an alphabet to make z>a == a>z

##### Flask





### Challenge 2 - HTTP/1.0 and Caesar Cipher

To get the encoding challenge make a HTTP/1.0 request to http://192.168.22.100/challenge1, for extra style points you can do this using netcat

##### Answer

https://stackoverflow.com/questions/45390338/how-to-use-curl-to-generate-http-1-0-request-for-a-file-without-a-leading-slash

Then Rot 10

##### Flask

`request.environ.get('SERVER_PROTOCOL') # Search for HTTP/1.0 only`

##### Encoding Challenge

GRY GYEVN RKFO UXYGX DRKD TEVSEC MKOCKB'C MSZROB GYEVN LO CY ZYZEVKB KVV DROCO IOKBC VKDOB. KXIGKI FKEVDSXQ NSCDYBD NBEWWYXN SC DRO PVKQ. UOOZ DRO CZKMOC

> Decodes to:
>
> Who would have known that Julius Caesar's cipher would be so popular all these years later. Anyway Vaulting Distort Drummond is the flag. Keep the spaces



### Challenge 3 - PATCH request and MD5 secret

Make a HTTP PATCH request to http://192.168.22.100/challenge3

##### Answer



##### Flask

https://stackoverflow.com/questions/49093115/put-request-python-flask/49093353



##### Encryption Challenge

 5c577753706cdcef8621a9c0c1922158 == md5 is broken



### Challenge 4 - POST Request with JSON content and XOR

```
curl -X POST -H "Content-Type: application/json" \    -d '{"name": "linuxize", "email": "linuxize@example.com"}' \    https://example/contact
```
