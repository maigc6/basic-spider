from requests import *
import json

head = {"Referer":"https://findcumt.libsp.com/",
        "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.55 Safari/537.36 Edg/96.0.1054.34",
        "groupCode":"200069"}
url = "https://findcumt.libsp.com/find/book/getDuxiuImageUrl?isbn="+"7-5083-0580-9"+"&title="+"Python语言入门"+"&recordId="+"151681"
r = get(url,headers =head)
text = json.loads(r.text)
read = text["data"]
print(read)
