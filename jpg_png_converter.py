import sys
import os
from PIL import Image




jpegfolder = (sys.argv[1]) 
pngfolder  = (sys.argv[2])

dir_list = os.listdir(jpegfolder)



if not os.path.exists(pngfolder):
    os.makedirs(pngfolder)


for filename in dir_list:
  img = Image.open(f'{jpegfolder}{filename}')
  clean_name = os.path.splitext(filename)[0]
  img.save(f'./{pngfolder}{clean_name}.png', 'png')
  print('File completed')








