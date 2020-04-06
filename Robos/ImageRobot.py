import json
from Robos import stateRobot
from googleapiclient.discovery import build


def seachImagesFromCustomSeach(query):
    with open(r'C:\Users\Marcos\Documents\Credenciais\credenciais.json') as json_file:
        dados = json.load(json_file)
        key_id = dados["Google_ID"]
        cse_id = dados["CSE_ID"]

    service = build("customsearch", 'v1', developerKey=key_id).cse()
    res = service.list(q=query, cx=cse_id, num=2, imgSize='huge', searchType='image').execute()
    arrayImages = []
    for i in range(len(res['items'])):
        arrayImages.append(res['items'][i]['link'])
    return arrayImages


def fechtImagesForAllSentenes(content):
    for i in range(len(content['Informations'])):
        if len(content["Informations"][i]['keywords']) != 0:
            query = content["Informations"][i]['Sentence'] + ' ' + content["Informations"][i]['keywords'][0]['text']
        else:
            query = content["Informations"][i]['Sentence']
        resusts = seachImagesFromCustomSeach(query=query)
        content["Informations"][i]['urlImages'] = resusts

    return content


def ActivateImageBoot():
    content = stateRobot.load()
    content = fechtImagesForAllSentenes(content=content)
    stateRobot.save(content=content)
