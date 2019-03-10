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

