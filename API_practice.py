from urllib2 import Request, urlopen


request = Request('http://placekitten.com/')

response = urlopen(request)
kittens = response.read()

print kittens[559:1000]