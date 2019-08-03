import requests

url = 'https://www.cnet.com/roadshow/auto/2018-dodge-challenger-srt-hellcat-widebody/preview/'
r = requests.get(url, allow_redirects=True)
open('google.html', 'wb').write(r.content)
