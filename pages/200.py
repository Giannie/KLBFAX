import gmail
from os.path import join,expanduser
from colours import Foreground,Background

details = []
with open(join(expanduser("~"),".klb/gmail")) as f:
    for line in f.readlines():
        details.append(line.strip("\n"))

g = gmail.login(details[0],details[1])


unread = g.inbox().mail(unread=True)

with open(join(expanduser("~"),".klb/emails")) as f:
    letters = f.read()

for mail in unread:
    mail.fetch()
    lines = "".join(mail.body.split("\r")).split("\n")
    if lines[0] == "EVENT" and "matthew.scroggs.14@ucl.ac.uk" in mail.fr:
      try:
        with open('/var/www/klb/events','a') as f:
            for line in lines:
                if line!="EVENT":
                    f.write(line+"""
""")
        mail.read()
      except:
        pass
    elif lines[0] == "CARD" and "matthew.scroggs.14@ucl.ac.uk" in mail.fr:
        with open('/home/pi/cards/'+lines[1],"w") as f:
            f.write(lines[2])
    else:
        newletter = ""
        for line in lines:
            while len(line)>79:
                newletter += line[:79]+"""
"""
                line=line[79:]
            newletter+=line+"""
"""

        letters=newletter+"""
"""+Foreground.YELLOW+"""from """+mail.fr+Foreground.DEFAULT+"""
----------------------------------------
"""+letters
        mail.read()

letters = letters.split("\n")
if len(letters)>100:
    letters = letters[:100]
letters = """
""".join(letters)

with open(join(expanduser("~"),".klb/emails"),"w") as f:
    f.write(letters)
        
page = Foreground.RED+"""LETTERS"""+Foreground.DEFAULT+"""
"""+letters
tag = "Email klbscroggsbot@gmail.com and your letter will appear here"
