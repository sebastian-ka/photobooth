from magicktools import Magicktools
from magicktools import Layout


mt = Magicktools()

filenames = ["img1.png", "img2.png","img3.png","img4.png"]

mt.createStrip(Layout.One,filenames[:1],400,800)
mt.createStrip(Layout.Two,filenames[:2],400,800)
mt.createStrip(Layout.Three,filenames[:3],400,800)
mt.createStrip(Layout.Four,filenames[:4],400,800)
