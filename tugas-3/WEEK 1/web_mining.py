import requests
r = requests.get("http://www.vit.ac.in")

import re
result = re.findall('<a .*? href="(.*?)" .*?>', r.text)


for i in result:
	print(i)
fp = open('web_mining_links.txt', 'w')
for i in result:
	fp.write(i)
	fp.write('\n')
fp.close()
