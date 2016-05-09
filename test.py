from magicktools import Magicktools
from magicktools import Layout


mt = Magicktools()
filenames = ["img1.png", "img2.png","img3.png","img4.png"]
mt.createStrip(Layout.Four,filenames,400,800)
#mt.createStripFour(300,600,filenames)
