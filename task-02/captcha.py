import pytesseract
from PIL import Image
import re

image = Image.open("captcha.png")

expression = pytesseract.image_to_string(image)

numbers = re.findall(r'\d+', expression)
operator = re.findall(r'[+\-*/]', expression)[0]

result = eval(numbers[0] + operator + numbers[1])

print(result)
