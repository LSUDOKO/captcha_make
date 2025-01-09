from captcha.image import ImageCaptcha
import random

image =ImageCaptcha(width=450,height=100)
def generate():
    char="abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890"
    cap=''.join(random.choice(char) for i in range(6))
    return cap

cap_text=generate()
data=image.generate(cap_text)
image.write(cap_text,"cap.png")
from PIL import Image
Image.open("cap.png")