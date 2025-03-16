#Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/134.0.0.0 Safari/537.36 this is user agent
#id=wob_tm
from requests_html import HTMLSession
import speech_to_text_p6
s=HTMLSession()
query="banglore"
url=f'https://www.google.com/search?q=weather+{query}'
r=s.get(url,headers={'user-agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/134.0.0.0 Safari/537.36'})
temp=r.html.find('span#wob_tm',first=True).text
print(temp)
unit=r.html.find('div.vk_bk.wob-unit span.wob_t',first=True).text
print(unit)
desc=r.html.find('span#wob_tm',first=True).text
print(desc)