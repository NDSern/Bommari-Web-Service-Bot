import json
with open("result.json", mode='r', encoding="utf8") as f:
    data = json.load(f)
things = data["messages"]
for i in things:
    if isinstance(i["text"], str):
        i["text"] = i["text"].replace(",", ";")
    if isinstance(i["text"], list):
        i["text"] = i["text"][0].replace(",", ";") + i["text"][1]["text"].replace(",", ";") + i["text"][2]
    print(i)
with open("modified.json", 'w') as l:
    json.dump(things, l)