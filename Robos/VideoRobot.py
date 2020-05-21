import os
from random import randint
from PIL import Image, ImageDraw, ImageFont
from PIL.ImageFilter import BLUR

from Robos import stateRobot
import subprocess

os.chdir(r'C:\Users\Marcos\Documents\Bots\Imagens ')


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
    # w,h=im.size

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
    color = 'rgb(255,255,255)'  # black color
    x = ran_x
    y = ran_y
    for line in lines:
        draw.text((x, y), line, fill=color, font=font)
        y = y + line_height  # update y-axis for new line

    # draw.line([(0, 0), (w-1, 0), (w-1, h-1), (0, h-1), (0, 0)], fill=(0, 0, 0), width=5)
    # im.show()
    im.save(str(sentenceIndex) + '-sentence.png')


def createAllSentenceImages(content):
    for sentenceIndex in range(len(content["Informations"])):
        convertSentence(content["Informations"][sentenceIndex]["Sentence"], sentenceIndex)


def convertImage(sentenceIndex):
    os.chdir(r'C:\Users\Marcos\Documents\Bots\Imagens ')
    # Abrindo imagem
    image = Image.open(str(sentenceIndex)+'.jpg')

    # Salvando suas dimensoes
    image_W, image_H = image.size

    image_H = int(image_H * 1.25)
    image_W = int(image_W * 1.25)

    # copiando imagem
    copyImage = image.copy()
    image = image.resize((image_W, image_H))

    # Borrando a imagem copiada
    copyImage = copyImage.convert('RGB')
    copyImage = copyImage.filter(BLUR)

    # Alterando seu tamanho
    copyImage = copyImage.resize((1920, 1080))

    # colando no fundo da imagem original
    copyImage.paste(image, (960 - image_W // 2, 540 - image_H // 2))

    # Salvando Imagem
    copyImage.save(str(sentenceIndex)+'-converted.png')


def convertAllImages(content):
    for sentenceIndex in range(len(content["Informations"])):
        convertImage(sentenceIndex)
    return print("Imagens Convertidas")


def createAfterEfetctsScript(content):
    return stateRobot.saveScript(content)


def renderVideoWithAfterEfects():
    root = r'C:\Users\Marcos\Documents\Bots'
    aerenderFilePath = r'C:\Program Files\Adobe\Adobe After Effects 2020\Support Files\aerender.exe'
    templateFilePath = root + r'\templates\1\template.aep'
    destinationFilePath = root+r'\Imagens'

    print("Iniciando After Efects . . .")

    aerender = subprocess.run([aerenderFilePath,
                               '-comp', 'main',
                               '-project', templateFilePath,
                               '-output', destinationFilePath])


def ActivateVideoRobot():
    content = stateRobot.load()
    convertAllImages(content=content)
    createAllSentenceImages(content=content)
    createAfterEfetctsScript(content=content)
    renderVideoWithAfterEfects()

    os.chdir(r'C:\Users\Marcos\Documents\Bots ')
    stateRobot.save(content=content)
