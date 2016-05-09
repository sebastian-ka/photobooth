from wand.image import Image
from wand.color import Color

class Layout(object):
	One = 1
	Two = 2
	Three = 3
	Four = 4

class Magicktools (object):
	
	def createStrip(self,layout = Layout.Four, filenames = ["img.png"], s_width = 400, s_height = 800):
		try:
			#if layout is Layout.One :
				#self.createStripOne(filenames, s_width, s_height)
			#if layout is Layout.Two :
				#self.createStripTwo(filenames, s_width, s_height)
			#if layout is Layout.Three :
				#self.createStripThree(filenames, s_width, s_height)
			if layout is Layout.Four :
				self.createStripFour(filenames, s_width, s_height)
						
		except Exception, err:
			print(err)	
			
	
	def createStripFour(self, filenames = ["img.png"], s_width = 400, s_height = 800):
		offset = 0.9
		try:
			with Color('white') as bg_c:
				with Image(width = s_width, height = s_height, background= bg_c) as strip:
					pos = 0
					for fn in filenames:
						print(fn)
						try:
							with Image(filename=fn) as pic:
								with pic.clone() as pc :
									pc_width = int(s_width * 0.5)
									pc_height = int(s_height * 0.5)
									pc.resize(int(pc_width * offset), int(pc_height * offset))
									pc_pos = self.__getPositionFour(pos, s_width, s_height)
									strip.composite(pc, left = pc_pos['left'],top = pc_pos['top'] )
						except Exception, err:
							print(err)
						pos+=1
					strip.save(filename="strip.png")
		except Exception, err:
			print(err)
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
	
	def createStripThree(self, filenames = ["img.png"], s_width = 400, s_height = 800):
		return None
	
	def createBackground(self, color = 'white', s_width = 400, s_height = 800):
		try:
			with Color(color) as bg_c:
				with Image(width = s_width, height = s_height, background= bg_c) as strip:
					return strip
		except Exception, err:
			print(err)
					
				
		
		
		