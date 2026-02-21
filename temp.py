import requests

apikey = "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"

word= input("enter the word")

res = requests.get(f"https://api.dictionaryapi.dev/api/v2/entries/en/{word}")

print("status_code:",res.status_code)
if res.status_code ==200:
    meanings = res.json()[0]["meanings"]

    for meaning in meanings:
        defn = meaning["definitions"]
        for d in defn:
            print(d['definition']) 
else:
    print("word not found in dictionary")
#print(res.status_code)