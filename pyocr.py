import sys


from pyocr import pyocr
from PIL import Image

#导入库
tools = pyocr.get_available_tools()[:]
if len(tools) == 0:
    print("No OCR tool found")
    sys.exit(1)
#查找OCR引擎
print("Using '%s'" % (tools[0].get_name()))
print(tools[0].image_to_string(Image.open('2S1485.png')))