from __future__ import unicode_literals
import json
import urllib
from urllib.request import urlopen

url="https://www.youtube.com/feed/subscriptions"
resp=urlopen(url).read()

print(resp)