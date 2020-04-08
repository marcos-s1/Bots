import json
import pprint
from googleapiclient.discovery import build
import asyncio
from Robos import stateRobot


def seachImagesFromCustomSeach(query):
    import json
    with open(r'C:\Users\Marcos\Documents\Credenciais\credenciais.json') as json_file:
        dados = json.load(json_file)
        key_id = dados["Google_ID"]
        cse_id = dados["CSE_ID"]

    service = build(serviceName="customsearch", version='v1', developerKey=key_id).cse()
    res = service.list(q=query, cx = cse_id, num=2, imgSize='huge', searchType='image').execute()
    pprint.pprint(res, indent=4)
    arrayImages = []
    '''for i in range(len(res["items"])):
        arrayImages.append(res["items"][i]['link'])
    return arrayImages'''


async def fechtImagesForAllSentenes(content):
    for i in range(len(content['Informations'])):
        if len(content["Informations"][i]['keywords']) != 0:
            query = content["Informations"][i]['Sentence'] + ' ' + content["Informations"][i]['keywords'][0]['text']
        else:
            query = content["Informations"][i]['Sentence']
        seachImagesFromCustomSeach(query=query)
        '''content["Informations"][i]['urlImages'] = results'''

    return content


content = stateRobot.load()
array = asyncio.run(fechtImagesForAllSentenes(content=content))

print(json.dumps(array, indent=4))
