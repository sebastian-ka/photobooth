from wand.image import Image
from wand.color import Color

class Layout(object):
	One = 1
	Two = 2
	Three = 3
	Four = 4

class Magicktools (object):
	#creates a photostrip of either 1, two, 1x3, 2x2 pictures
	#phtoto strips gets saved in working directory
	#todo: option to add path, count files in array, crop pics not just resize
	def createStrip(self,layout = Layout.Four, filenames = ["img.png"], s_width = 400, s_height = 800):
		bgColor = "white"
		picsPerRow = 1
		picsPerCol = 1
		if layout is Layout.One :
			picsPerRow = 1
			picsPerCol = 1
		if layout is Layout.Two :
			picsPerRow = 1
			picsPerCol = 2
		if layout is Layout.Three :
			picsPerRow = 1
			picsPerCol = 3
		if layout is Layout.Four :
			picsPerRow = 2
			picsPerCol = 2

		offset = 0.9
		try:
			with Color(bgColor) as bg_c:
				with Image(width = s_width, height = s_height, background= bg_c) as strip:
					pos = 0
					for fn in filenames:
						print(fn)
						try:
							with Image(filename=fn) as pic:
								with pic.clone() as pc :
									pc_width = int(s_width /picsPerRow)
									pc_height = int(s_height /picsPerCol)
									pc.resize(int(pc_width * offset), int(pc_height * offset))
									pc_pos = self.__getPosition(layout, pos, s_width, s_height)
									strip.composite(pc, left = pc_pos['left'],top = pc_pos['top'] )
						except Exception, err:
							print(err)
						pos+=1
					strip.save(filename=str("strip-"+str(layout)+".png") )
		except Exception, err:
			print(err)			

	#returns the position of the pic
	#just calls the internal methods for each strip layout
	def __getPosition(self,layout, pos, w,h):
		
		if layout is Layout.One:
			return self.__getPositionOne(pos, w, h)
		elif layout is Layout.Two:
			return self.__getPositionTwo(pos, w, h)
		elif layout is Layout.Three:
			return self.__getPositionThree(pos, w, h)
		elif layout is Layout.Four:
			return self.__getPositionFour(pos, w, h)
		
		#todo: this should probably be handled by an exception
		else:
			return self.__getPositionOne(pos, w, h)
			
			
	#pos gets ignored, because it should only be 0
	def __getPositionOne(self, pos, w, h):
		left = 0
		top = 0
		offset = 0.9
		pic_w = int(w)
		pic_h = int(h)
		
		left += int((1-offset)*0.5*pic_w)
		top  += int((1-offset)*0.3*pic_h)
		return {'left':left,'top':top}
	
	def __getPositionTwo(self, pos, w, h):
		left =0
		top = 0
		offset = 0.9
		pic_w = int(w)
		pic_h = int(h/2)
		
		if pos == 1 :
			top = pic_h
			
		left += int((1-offset)*0.5*pic_w)
		top  += int((1-offset)*0.3*pic_h)
		return {'left':left,'top':top}
	
	def __getPositionThree(self, pos, w, h):
		left =0
		top = 0
		offset = 0.9
		pic_w = int(w)
		pic_h = int(h/3)
		
		if pos == 1 :
			top = pic_h
		if pos == 2 :
			top = pic_h * 2
		left += int((1-offset)*0.5*pic_w)
		top  += int((1-offset)*0.3*pic_h)
		return {'left':left,'top':top}
		
	#get positions for a 2x2 photostrip
	def __getPositionFour(self,pos, w, h):
		left =0
		top = 0
		offset = 0.9
		pic_w = int(w/2)
		pic_h = int(h/2)

		if(pos == 1 or pos == 3):
			left = pic_w
		if(pos == 2 or pos == 3) :
			top = pic_h
		
		left += int((1-offset)*0.5*pic_w)
		top  += int((1-offset)*0.3*pic_h)
		
		return {'left':left,'top':top}
