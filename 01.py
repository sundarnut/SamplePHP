for i in 5, 4, 3, 2, 1, 'hey!' do:
    print(i)

# Next

quotes = [
    "2 + 2 = 5 for very large values of 2.",
    "You're so artificial, the wool that you pull over my eyes is half rayon",
    "A woman may be an occasional pleasure, but a cigar is always a smoke"
    ]
print(quotes[2])

# Next

canards = {
    "Huey": "Let's get unca Donald!",
    "Dewey": "Yeah, what?",
    "Louie": "Uh oh, uh oh, uh oh!"
    }
duck = "Louie"
print(duck, "said", canards[duck])

# Next

import json
from urllib.request import urlopen
url = "https://gdata.youtube.com/feeds/api/standardfeeds/top_rated?v=2&alt=json"
response = urlopen(url)
contents = response.read()
text = contents.decode('utf8')
data = json.loads(text)
for video in data['feed']['entry'][0:10]:
    print(video['title']['$t'])

# Next

import requests
url = "https://gdata.youtube.com/feeds/api/standardfeeds/top_rated?alt=json"
response = requests.get(url)
data = response.json()
for video in data['feed']['entry'][0:10]:
    print(video['title']['$t'])

# Next

karma = 101
print("Karma %s Python rocks" % karma)

# Integer division
print(10 // 3)
# 3

# Power
print(2**10)
# 1024

# Binary
print(0B10000)
# 16

# Octal
print(0o20)
# 16

# Hexadecimal
print(0xff)
# 255

# Mod
print(11 % 3)
# 2

# Type
print(type('abc'))
# <class 'str'>

# To get truncated quotient and remainder as a tuple
print(divmod(13, 3))
# (4, 1)

# int conversion
print(int(False))
# 0

# int conversion not possible
print(int('0x10h'))
# Error

