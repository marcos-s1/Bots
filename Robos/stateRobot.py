import json


def save(content):
    with open(file='content.json', mode='w', encoding='utf8') as f:
        return json.dump(obj=content, fp=f, indent=4, ensure_ascii=False)


def load():
    with open(file='content.json', mode='r', encoding='utf8') as f:
        return json.load(fp=f)
