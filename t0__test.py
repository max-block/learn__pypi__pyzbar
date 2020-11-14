from PIL import Image
from pyzbar.pyzbar import decode

res = decode(Image.open("tmp/1.png"))
print(res)
