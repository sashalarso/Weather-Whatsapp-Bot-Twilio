import sys
import json
import urllib.request
import os
a=os.listdir("C:/Users/Sasha/Documents/Python")
print(a)
a=open("C:/Users/Sasha/Documents/Python/keycr.txt","r").read().rstrip("\n")
print(a)
print("salut")
with open("C:/Users/Sasha/Documents/Python/keycr.txt") as key :
    sashakey=key.read().rstrip("\n")
    print(sashakey)
    url="https://api.clashroyale.com/v1"
    endpoint="/clans/%23LPCG9LPC"
    request=urllib.request.Request(url+endpoint,None,{"Authorization": "Bearer %s" % sashakey}) 
    response=urllib.request.urlopen(request).read().decode("utf-8")
    data=json.loads(response)
    print(data)
    for item in data["memberList"]:
        print("%s [%d]" % (item["name"], item["donations"]))


with open("keycr.txt") as key :
    sashakey=key.read().rstrip("\n")
    print(sashakey)
    url="https://api.clashroyale.com/v1"
    endpoint="/players/%23Y9CCVR8GJ"
    request=urllib.request.Request(url+endpoint,None,{"Authorization": "Bearer %s" % sashakey}) 
    response=urllib.request.urlopen(request).read().decode("utf-8")
    data=json.loads(response)
    print(data["tag"])
    compteur =0
    print(data)
    for item in data['cards'] :
        print(item['name'] +  str(item['level']))
        if item['level']==14:
            print("la carte " + item['name'] +" est level 14")
            compteur+=1
        if item['name']=='Valkyrie' :
            print(item['iconUrls'])
print("vous avez ",compteur,"cartes niveau 14")


with open("keycr.txt") as key :
    sashakey=key.read().rstrip("\n")
    print(sashakey)
    url="https://api.clashroyale.com/v1"
    endpoint="/globaltournaments"
    request=urllib.request.Request(url+endpoint,None,{"Authorization": "Bearer %s" % sashakey}) 
    response=urllib.request.urlopen(request).read().decode("utf-8")
    data=json.loads(response)
    print(data)
    for item in data["memberList"]:
        print("%s [%d]" % (item["name"], item["donations"]))