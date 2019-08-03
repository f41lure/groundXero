
import urllib.request as ur

url = 'http://www.oldbaileyonline.org/browse.jsp?id=t17800628-33&div=t17800628-33'

response = ur.urlopen(url)
webContent = response.read()

print(webContent[0:300])
