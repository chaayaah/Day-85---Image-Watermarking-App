from PIL import Image, ImageDraw, ImageFont
from tkinter import filedialog
from tkinter import Tk

root = Tk()
root.withdraw()
filename = filedialog.askopenfilename(initialdir='/Users/Justine/Downloads', title='Select Image')

def add_watermark(image, wm_text):
    #1. Create the Image Object
    opened_image = Image.open(image)

    #2. Get the image Size
    image_width, image_height = opened_image.size

    #3. Draw on image
    draw = ImageDraw.Draw(opened_image)

    #4. Specify the font size
    font_size = int(image_width/12)

    #5. Specify the  font
    font = ImageFont.truetype('arial.ttf', font_size)

    #6. Specify the coordinates where we want the image
    x, y = int(image_width/2), int(image_height/2)

    #7. Add the watermark
    draw.text((x,y), wm_text, font=font, fill='#FFF', stroke_width=5, stroke_fill='#222', anchor='ms')

    #8. Show the new image
    opened_image.show()

add_watermark(filename, 'karljustinerobin.com')