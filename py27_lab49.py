# pip install pillow
from urllib2 import urlopen
from PIL import Image
import ssl

sslContext = ssl._create_unverified_context()

URL = 'https://www.cwb.gov.tw/V7/forecast/fcst/Data/I04_small.jpg'
fileToSave = urlopen(URL, context=sslContext)
image1 = Image.open(fileToSave)
# manually create a directory images
image1.save('.\\images\\orig.jpg')
# step2
double = (image1.size[0] * 2, image1.size[1] * 2)
doubleImage1 = image1.resize(double, Image.ANTIALIAS)
doubleImage1.save('.\\images\\double.jpg')
half = (image1.size[0] / 2, image1.size[1] / 2)
halfImage1 = image1.resize(half, Image.ANTIALIAS)
halfImage1.save('.\\images\\half.jpg')
rot1 = image1.transpose(Image.ROTATE_90)
rot1.save('.\\images\\r90.jpg')
rot2 = image1.transpose(Image.ROTATE_180)
rot2.save('.\\images\\r180.jpg')
rot3 = image1.transpose(Image.ROTATE_270)
rot3.save('.\\images\\r270.jpg')
rot4 = image1.rotate(37)
rot4.save('.\\images\\r37.jpg')
