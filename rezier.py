import os,sys
from PIL import Image

size  = (750,1334)
infolder = 'C:/Users/vld/Downloads/'
outfolder = 'C:/Users/vld/Downloads/new/'


def resize():
        dirs = os.listdir(infolder)
        #Loop through images with different dimensions
        for item in dirs:
            s = os.path.splitext(item)
            #make sure all files are images
            if s[1] == '.jpg' or s[1] == '.png' or s[1] == '.jpeg':
                img = Image.open(infolder+item)
                
                img.thumbnail(size)
                img.save(outfolder+item)
            else:
                print 'Verify the extensions of the images and check the sizes.'
resize()


