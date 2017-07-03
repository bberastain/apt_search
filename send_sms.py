from twilio.rest import Client
import re

i = 0
f = open('practice/practice.json').read()
lines = re.findall('href.*"(.*html)', f)
link = 'https://sfbay.craigslist.org' + lines[i]
i += 1

client = Client("AC476add24a162a8d6b5e9ea8ed5d4f31b",
                "4a574f381aa19af685f14a6f4d3112ba")
client.messages.create(to="+19256422649",
                       from_="+19254063140",
                       body=link)
