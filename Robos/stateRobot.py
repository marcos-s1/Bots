import json


def save(content):
    with open(file='content.json', mode='w', encoding='utf8') as f:
        return json.dump(obj=content, fp=f, indent=4, ensure_ascii=False)


def saveScript(content):
    with open(file='content.js', mode='w', encoding='utf8') as f:
        return f.write("var content="+str(content))


def load():
    with open(file='content.json', mode='r', encoding='utf8') as f:
        return json.load(fp=f)
