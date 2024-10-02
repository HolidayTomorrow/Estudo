import chardet
from pathlib import Path
import os

# local = os.path.dirname(__file__)
local = Path(__file__).parent
# local = "c:\\Users\\marcelo.rlopes\\Documents\\Estudos\\Estudo\\Python\\Web_Scraping\\"
# print(local)

with open(local+ '\\text.txt', 'rb') as file:
    raw_content = file.read()
    encoding = chardet.detect(raw_content)
    encoding["encoding"]
    print(encoding)


with open(local+ '\\text.txt', 'rb') as file:
    raw_content = file.read()
    content_string = raw_content.decode(encoding["encoding"])
    print('\n',content_string)


with open(local+ '\\text2.txt', 'wb') as file:
    file.write(content_string.encode('utf8'))