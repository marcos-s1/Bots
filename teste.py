from random import randint

from PIL import Image, ImageDraw, ImageFont, ImageFilter
import os


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


os.chdir(r'C:\Users\Marcos\Pictures')


text = "Michael Joseph Jackson Gary, 29 de agosto de 1958 â€” Los Angeles, 25 de junho de 2009 foi um cantor, " \
       "compositor e danÃ§arino estadunidense. "
# create image object from the input image path
image = Image.open('img-1.jpg')


image_W, image_H = image.size

copyImage = image.copy()

copyImage = copyImage.filter(ImageFilter.BLUR)

copyImage = copyImage.resize((1920, 1080))

copyImage.paste(image, (960-(image_W//2), 540-(image_H//2)))

copyImage.save('teste.jpg')

im = Image.new('RGBA', (1920, 400), (0, 0, 0, 0))
im_W, im_H=im.size

x_min = (im.size [0] * 8) // 100
x_max = (im.size [0] * 25) // 100

ran_x = randint (x_min, x_max)

font_path = 'font/arialbd.ttf'
font = ImageFont.truetype(font=font_path, size=60)

lines = text_wrap(text, font, im.size[0]-ran_x)
line_height = font.getsize('hg')[1]

y_min = (im.size[1] * 4) // 100   # 4% from the top
y_max = (im.size[1] * 90) //100   # 90% to the bottom
y_max -= (len(lines)*line_height)  # Adjust
ran_y = randint(y_min, y_max)      # Generate random point

# Create draw object
draw = ImageDraw.Draw(im)

# Draw text on image
color = 'rgb(0,0,0)'  # Red color
x = ran_x
y = ran_y
for line in lines:
    draw.text((x, y), line, fill=color, font=font)
    y = y + line_height  # update y-axis for new line
# Redefine x and y-axis to insert author's name
author = "- Eyong Kevin"
y += 5  # Add some line space
x += 20  # Indent it a bit to the right
draw.text((x, y), author, fill=color, font=font)
draw.line([(0, 0), (im_W-1, 0), (im_W-1, im_H-1), (0, im_H-1), (0, 0)], fill=(0,0,0), width=5)
im.show()
