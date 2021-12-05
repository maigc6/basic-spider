from requests import *
import json
head = {"Referer":"https://findcumt.libsp.com/",
        "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.55 Safari/537.36 Edg/96.0.1054.34",
        "groupCode":"200069"}
data = {"searchFieldContent":"python","searchField":"keyWord","page":3}
r = post("https://findcumt.libsp.com/find/unify/search",json = data,headers =head)
text = json.loads(r.text)
read = text["data"]["searchResult"]
for i in range(len(read)):
    list ={}
    list["bookId"]=(read[i]["recordId"])
    list["name"]=(read[i]['title'])
    list["isbn"]=(read[i]["isbn"])
    print(list)

data1 = {"recordId":"1154642"}
r2 = post("https://findcumt.libsp.com/find/physical/groupitems",json = data1,headers =head)
text1 = json.loads(r2.text)
read1 = text1["data"]
print(read1)
for i in range(len(read1)):
    list ={}
    list["索书号"]=(read1[i]["barcode"])
    list["name"]=(read1[i]['locationName'])


