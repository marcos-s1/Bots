from Robos import stateRobot
from googleapiclient.discovery import build
import os
from random import randint
from PIL import Image, ImageDraw, ImageFont, ImageFilter

os.chdir(r'C:\Users\Marcos\Pictures\ImagensROBO\ ')


def text_wrap(text, font, max_width):
    """Wrap text base on specified width.
    This is to enable text of width more than the image width to be display
    nicely.
    @params:
        text: str
            text to wrap
        font: obj
            font of the text
        max_width: int
            width to split the text with
    @return
        lines: list[str]
            list of sub-strings
    """
    lines = []

    # If the text width is smaller than the image width, then no need to split
    # just add it to the line list and return
    if font.getsize(text)[0] <= max_width:
        lines.append(text)
    else:
        # split the line by spaces to get words
        words = text.split(' ')
        i = 0
        # append every word to a line while its width is shorter than the image width
        while i < len(words):
            line = ''
            while i < len(words) and font.getsize(line + words[i])[0] <= max_width:
                line = line + words[i] + " "
                i += 1
            if not line:
                line = words[i]
                i += 1
            lines.append(line)
    return lines


def convertSentence(sentence, sentenceIndex):
    templateSettings = {
        0: {
            'size': (1920, 400),
            'FontSize': 60
        },
        1: {
            'size': (1920, 1080),
            'FontSize': 100
        },
        2: {
            'size': (800, 1080),
            'FontSize': 60
        },
        3: {
            'size': (1920, 400),
            'FontSize': 60
        },
        4: {
            'size': (1920, 1080),
            'FontSize': 100
        },
        5: {
            'size': (800, 1080),
            'FontSize': 60
        },
        6: {
            'size': (1920, 400),
            'FontSize': 60
        }
    }

    # Criando Imagem de texto
    im = Image.new('RGBA', templateSettings[sentenceIndex]['size'], (0, 0, 0, 0))
    #w,h=im.size

    # Definindo x minimo e maximo
    x_min = (im.size[0] * 8) // 100
    x_max = (im.size[0] * 25) // 100

    ran_x = randint(x_min, x_max)

    font_path = 'font/arialbd.ttf'
    font = ImageFont.truetype(font=font_path, size=templateSettings[sentenceIndex]['FontSize'])

    lines = text_wrap(sentence, font, im.size[0] - ran_x)
    line_height = font.getsize('hg')[1]

    y_min = (im.size[1] * 4) // 100  # 4% from the top
    y_max = (im.size[1] * 90) // 100  # 90% to the bottom
    y_max -= (len(lines) * line_height)  # Adjust
    ran_y = randint(y_min, y_max)  # Generate random point

    # Create draw object
    draw = ImageDraw.Draw(im)

    # Draw text on image
    color = 'rgb(0,0,0)'  # Red color
    x = ran_x
    y = ran_y
    for line in lines:
        draw.text((x, y), line, fill=color, font=font)
        y = y + line_height  # update y-axis for new line

    #draw.line([(0, 0), (w-1, 0), (w-1, h-1), (0, h-1), (0, 0)], fill=(0, 0, 0), width=5)
    #im.show()
    im.save('text-img-'+str(sentenceIndex)+'.png')


def createAllSentenceImages(content):
    for sentenceIndex in range(len(content["Informations"])):
        convertSentence(content["Informations"][sentenceIndex]["Sentence"], sentenceIndex)


def convertImage(sentenceIndex):
    # Abrindo imagem
    image = Image.open('img-' + str(sentenceIndex) + '.jpg')

    # Salvando suas dimensoes
    image_W, image_H = image.size

    image_H = int(image_H * 1.25)
    image_W = int(image_W * 1.25)

    # copiando imagem
    copyImage = image.copy()
    image = image.resize((image_W, image_H))

    # Borrando a imagem copiada
    copyImage = copyImage.filter(ImageFilter.BLUR)

    # Alterando seu tamanho
    copyImage = copyImage.resize((1920, 1080))

    # colando no fundo da imagem original
    copyImage.paste(image, (960 - image_W // 2, 540 - image_H // 2))

    # Salvando Imagem
    copyImage.save('img-' + str(sentenceIndex) + '-converted.jpg')


def convertAllImages(content):
    for sentenceIndex in range(len(content["Informations"])):
        convertImage(sentenceIndex)
    return


async def downloadImage(imgURL, name):
    import urllib.request

    opener = urllib.request.build_opener()
    opener.addheaders = [('User-Agent',
                          'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) '
                          'Chrome/36.0.1941.0 Safari/537.36')]
    urllib.request.install_opener(opener)

    # local = r'C:\Users\Marcos\Pictures\ImagensROBO\ ' + name + '.jpg'
    local = name + '.jpg'
    await urllib.request.urlretrieve(imgURL, local)


async def downloadAllImages(content):
    arrayImages = []
    for i in range(len(content["Informations"])):
        image = content["Informations"][i]["urlImages"]
        for imgURL in range(len(image)):
            try:
                if image[imgURL] not in arrayImages:
                    await downloadImage(imgURL=image[imgURL],
                                        name='img' + '-' + str(len(arrayImages)))
                    arrayImages.append(image[imgURL])
                    break
                print('Imagem ja baixada', end='|')
                raise NameError()

            except NameError:
                print('erro ao baixar')
                pass

    return arrayImages


def seachImagesFromCustomSeach(query):
    import json
    with open(r'C:\Users\Marcos\Documents\Credenciais\credenciais.json') as json_file:
        dados = json.load(json_file)
        key_id = dados["Google_ID"]
        cse_id = dados["CSE_ID"]

    service = build(serviceName="customsearch", version='v1', developerKey=key_id).cse()
    res = service.list(q=query, cx=cse_id, num=2, searchType='image', imgSize='xlarge').execute()
    # res = service.list(q=query, cx=cse_id, num = 2,imgSize='huge', searchType='image').execute()
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


async def ActivateImageBoot():
    content = stateRobot.load()
    # await fechtImagesForAllSentenes(content=content)
    # await downloadAllImages(content=content)
    convertAllImages(content=content)
    createAllSentenceImages(content=content)
    stateRobot.save(content=content)
