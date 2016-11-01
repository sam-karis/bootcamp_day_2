import urllib2


request = urllib2.Request('http://placekitten.com/')

response = urllib2.urlopen(request)
kittens = response.read()

print kittens[559:1000]