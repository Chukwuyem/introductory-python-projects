class Room(object): #Room class is created
	def __init__(self, desc, short_desc):
		self.__desc= desc
		if not isinstance(self.__desc, str):
			raise TypeError('You did not enter a string')
		if self.__desc== '':
			raise ValueError('You entered an empty string')
		self.__short_desc= short_desc
		if not isinstance(self.__short_desc, str):
			raise TypeError('You did not enter a string')
		if self.__short_desc== '':
			raise ValueError('You entered an empty string')	
		self.__n= None
		self.__s= None
		self.__e= None
		self.__w= None
		self.inventory= set()
		self.__gate_n= None
		self.__gate_s= None
		self.__gate_e= None
		self.__gate_w= None
	def return_desc(self):
		return self.__desc
	def set_n(self, room_):
		#if the room_ in the argument is an instance of Room
		if isinstance(room_, Room): 
			if self.__n== None: #if self has no room assigned to cardinal North
				self.__n= room_ #self.__n is assigned to room_
				if room_.s() != self: 
					room_.set_s(self) #room_ does the same to self
			elif self.__n: #if self.__n already has a room_
				b= self.n() #b is the initial self.__n room_
				b.set_s(None) 
				#since b will has self as its south, b's south is set to None
				self.__n= room_ 
				#since b has let go of self, self let's go of b and changes to room_
				if room_.s() != self: 
					room_.set_s(self) #room_ does the same to self
		elif room_== None: #if the room argument is a None, the same sequence occurs,
			#except that the reciprocal set_s() function of room_ is not 
			#called on self because None doesn't have the function
			if self.__n== None:
				self.__n= room_
			elif self.__n:
				b= self.n()
				b.set_s(None)
				self.__n= room_
		else:
			raise TypeError('It\'s not a room')	
	def set_s(self, room_):
		if isinstance(room_, Room):
			if self.__s== None:
				self.__s= room_
				if room_.n() != self:
					room_.set_n(self)
			elif self.__s:
				b= self.s()
				b.set_n(None)
				self.__s= room_
				if room_.n() != self:
					room_.set_n(self)
		elif room_== None:
			if self.__s== None:
				self.__s= room_
			elif self.__s:
				b= self.s()
				b.set_n(None)
				self.__s= room_
	def set_e(self, room_):			
		if isinstance(room_, Room): #if argument is a room instance
			if self.__e== None: #if self does not already has __e assigned
				self.__e= room_ #self.__e is assigned to room_
				if room_.w() != self:
					room_.set_w(self)
			elif self.__e:
				b= self.e()
				b.set_w(None)
				self.__e= room_
				if room_.w() != self:
					room_.set_w(self)
		elif room_== None:
			if self.__e== None:
				self.__e= room_
			elif self.__e:
				b= self.e()
				b.set_w(None)
				self.__e= room_
	def set_w(self, room_):
		if isinstance(room_, Room):
			if self.__w== None:
				self.__w= room_
				if room_.e() != self:
					room_.set_e(self)
			elif self.__w:
				b= self.w()
				b.set_e(None)
				self.__w= room_
				if room_.e() != self:
					room_.set_e(self)
		elif room_== None:
			if self.__w== None:
				self.__w= room_
			elif self.__w:
				b= self.w()
				b.set_e(None)
				self.__w= room_
	def set_gate_n(self, gem): #set gate function sets a gate to be a gem
		if self.__n== None:
			raise AttributeError('No room exists in that direction.')
		elif self.__n:	
			if gem== None:
				self.__gate_n= None
			elif isinstance(gem, GateGem):
				self.__gate_n= gem
				if self.__n.__gate_s != gem:
					self.__n.set_gate_s(gem)
			else:
				raise TypeError('You did not enter the correct gem type.')
	def set_gate_s(self, gem):			
		if self.__s== None:
			raise AttributeError('No room exists in that direction.')
		elif self.__s:	
			if gem== None:
				self.__gate_s= None
			elif isinstance(gem, GateGem):
				self.__gate_s= gem
				if self.__s.__gate_n != gem:
					self.__s.set_gate_n(gem)
			else:
				raise TypeError('You did not enter the correct gem type.')
	def set_gate_e(self, gem):					
		if self.__e== None:
			raise AttributeError('No room exists in that direction.')
		elif self.__e:	
			if gem== None:
				self.__gate_e= None
			elif isinstance(gem, GateGem):
				self.__gate_e= gem
				if self.__e.__gate_w != gem:
					self.__e.set_gate_w(gem)
			else:
				raise TypeError('You did not enter the correct gem type.')
	def set_gate_w(self, gem):
		if self.__w== None:
			raise AttributeError('No room exists in that direction.')
		elif self.__w:	
			if gem== None:
				self.__gate_w= None
			elif isinstance(gem, GateGem):
				self.__gate_w= gem
				if self.__w.__gate_e != gem:
					self.__w.set_gate_e(gem)
			else:
				raise TypeError('You did not enter the correct gem type.')
	def n(self): #cardinal point function returns the room at that point
	#as self.__n is not accessible from outside
		if self.__n:
			return self.__n
		else:
			return None
	def s(self):
		if self.__s:
			return self.__s
		else:
			return None
	def e(self):
		if self.__e:
			return self.__e
		else:
			return None
	def w(self):
		if self.__w:
			return self.__w
		else:
			return None
	def return_gate_n(self): #to test if a gate exists
		if self.__gate_n:
			return True
		else:
			return False
	def get_gate_n(self): #function to return the gate itself
		return self.__gate_n
	def return_gate_s(self):
		if self.__gate_s:
			return True
		else:
			return False
	def get_gate_s(self):
		return self.__gate_s
	def return_gate_e(self):
		if self.__gate_e:
			return True
		else:
			return False
	def get_gate_e(self):
		return self.__gate_e
	def return_gate_w(self):
		if self.__gate_w:
			return True
		else:
			return False
	def get_gate_w(self):
		return self.__gate_w
	def inventory_str(self):
		i= 0
		c= len(self.inventory)
		for x in self.inventory:
			i += 1
			c= 'Gem ' + str(i) + ': ' + x.__str__
			return c
	def __str__(self): #overriding the __str__ function to a certain way
		a= self.__desc
		if self.__n:
			if self.__gate_n:
				b= 'To the north, you see a ' + self.__gate_n.colour +\
					' door.'
			else:
				b= 'To the north, you see a' + self.__n.__short_desc
		else:
			b= 'To the north there is nothing; total blackness.'
		if self.__s:
			if self.__gate_s:
				c= 'To the south, you see a ' + self.__gate_s.colour +\
					' door.'
			else:		
				c= 'To the south you see a' + self.__s.__short_desc
		else:
			c= 'To the south there is nothing; total blackness.'
		if self.__e:
			if self.__gate_e:
				d= 'To the east, you see a ' + self.__gate_e.colour +\
					' door.'
			else:		
				d= 'To the east, you see a ' + self.__e.__short_desc
		else:
			d= 'To the east there is nothing; total blackness.'
		if self.__w:
			if self.__gate_w:
				f= 'To the west, you see a ' + self.__gate_w.colour +\
					' door.'
			else:		
				f= 'To the west you see ' + self.__w.__short_desc
		else:
			f= 'To the west there is nothing; total blackness.'
		v= ' '	
		if self.inventory == set():
			v += 'no '
		elif self.inventory != set():	
			for x in self.inventory:
				v += 'a '+ x.colour + ', '
		u= 'This room possesses'
		q= 'grandeur key.'
		return a + '\n'+'\n' + b + '\n' + c +'\n'+ d + '\n'+ f + '\n'+ u + v + q
class GateGem(object):
	def __init__(self, colour):
		self.colour= colour
		if not isinstance(colour, str):
			raise TypeError('You did not enter a colour.')
	def __str__(self):
		return 'This is a '+ self.colour + 'gate gem.'
	def __eq__(self, other):
		if isinstance(other, GateGem)== False:
			return False
		elif self.colour== other.colour:
			return True
		elif self.colour != other.colour:
			return False
	def __hash__(self):
		return hash(self.colour)
class Player(object):
	def __init__(self, location):
		self.location= location
		if not isinstance(location, Room):
			raise TypeError('The location entered is invalid.')
		self.inventory= set()
	def inventory_str(self):
		i= 0
		c= len(self.inventory)
		for x in self.inventory:
			i += 1
			c= 'Gem ' + str(i) + ': ' + x.__str__
			return c
class ExitRoom(Room):
	def __init__(self, desc, short_desc, death_note):
		super(ExitRoom, self).__init__(desc, short_desc)
		self.__death_note= death_note
	def return_death_note(self):
		return self.__death_note
	
def main():
	X1= Room('\n'+'A large gallery with vintage musical instruments.\
 It is brightly lit by open fire wall lamps. There is a faint\
 smell of a woman\'s perfume. There is faint ochestra music\
 playing, like a strange mixture of Yanni, Mozart and Lord\
 of the Rings.', 'Music gallery.')
	M2= Room('\n'+'A big parlour with very well arranged furniture.\
 There is a horrible smell of rotting flesh. The lights are\
 from the gold chandeliers on the ceiling, from which two\
 dead bodies are hanging, probably been there a month or\
 two.', 'Living room.')
	M1= Room('\n'+'A fairly large dining room with a very strong bad\
 smell of spoilt food. The only thing that prevents you from\
 noticing the contrast between the arranged table and all\
 the other furniture scattered is the dead body slumped on the\
 sink; the gunshot wound on the head is very conspicuous. The\
 room is foggy.', 'Dining room.')
	Y1= Room('\n'+'A very big bedroom, dimly lit by two big gas lamps\
and one small petrol lamp. There is a very large king size\
bed in the middle of the room. There is portrait of a french \
naval captain opposite the bed. There is also a very faint\
smell of gun powder and explosives.','Bedroom.')
	M3= Room('\n'+'A very large gallery/showroom, neatly arrranged\
 with lots of french paintings, most of which depict the\
 sea. It smells heavily of fish. It is dimly lit.', 'Art\
 gallery/showroom.')
	M4= Room('\n'+'A fairly small art studio, overflowing with art\
 supplies... and naval ammunition. It smells of fresh blood.\
 The room is well lit by lots of hanging lamps.','Art studio.')
	M5= Room('An ernomous passage that is total empty but for three\
 doors. It is fairly bright though there are no lamps. The floor\
 is covered in soil. There is, thankfully, no smell. The wall\
 on the Northern side is covered with a floor to ceiling mural\
 of a bay.', 'Large empty passageway.')
	M6= Room('\n'+'A large, well arranged library. It is dimly lit.\
 Everything seems to be in order except for the smell of fresh\
 ink and a heap of book, scattered beside the eastern\
 door.', 'Library.')
	M7= Room('\n'+'A dark, theatre-like room, with cushioned-seats\
 and furniture scattered around. It smells heavily of sulphur\
 and gun powder. There is a goey, liquid substance on the floor\
 but you cannot see it because it\'s dark. The only light is\
 the one overflowing from the closed doors on all the four\
 sides of the room.', 'Theatre.')
	M8= Room('\n'+'A poorly lit wine cellar, with light coming from a\
 make-shift kerosene lamp, with wine as its fuel. It smells of\
 beautiful wine. There are red footprints leading to the southern\
 door. There is creaking noise in the ceiling. There is hanging\
 rope tied in a know above a trap door in the corner.', 'Wine cellar')
	M9= Room('\n'+'A very small, dark room and that is absolutely empty\
 except for three doors. A lamp is attached to a door. Below the\
 lamp is pieces of paper soaked in what looks like blood, attached\
 to a real human head, hanging from the lamp. The room reeks of\
 rotting flesh.', 'Small empty room.')
	X4= Room('\n'+'A congregation-like room with seats well arranged, facing\
 what looks like an altar. There is an open coffin in front of the\
 altar with a dead body in it; the horrible smell of blood is fresh so\
 whoever that is, he/she was murdered in the last hour. There is a large\
 on the eastern wall and beside it is a door.', 'Church hall.')
	E1= ExitRoom('\n'+'A big, bright hallway with the smell of fresh air. The\
 sound waves is very clear. There is an open door. On the other side\
 of the door, there are stairs leading up. Freedom!', 'Escape room.', 'There\
 it is: daylight, real light from the sun, the smell of real fresh air, that\
 does not contain some form of air-borne poison, the smell of freedom. Grandeur\
 is smart, but wasn\'t smart enough to keep you here. Congratulations, you\'re\
 free.')
	b5= ExitRoom('\n'+'A very small toilet. It is dark and reeks of hydrogen\
 cyanide.', 'A toilet.', 'You start to look around for a door, you begin\
 to feel very faint and a strong pain in your chest. You try to turn around\
 to go back but you can\'t. You black out. You\'re dead, much thanks to Grandeur\'s\
 cyanide poison.')
	b8= ExitRoom('\n'+'A very dark small room. There is a little box in the\
 middle of the room. It has the strong smell of a woman\'s\
 perfume.', 'A cinema.', 'You are looking around trying to see something\
 in this dark room. All of a sudden, a bright light from the projector blinds\
 you. The last thing you see are red strands of hair and a dagger sheath. You\'re\
 dead; cause of death is unknown.')
	b7= ExitRoom('\n'+'A large, dimly lit chamber. There is are a lot\
 high-tech military weapons scattered around.', 'First stora\
 ge chamber.', 'You are looking through boxes, trying to find\
 something that might help you make sense of things. Then you see\
 the laser, you hear the beep and then the pop... You\'re dead.')
	b6= ExitRoom('\n'+'A fairly large with blinding light coming from the top.\
 The sound of a sonar, coming from nowhere, is deafening.', 'Soundcheck.', 'The\
 moment you walk in, the light from the ceiling blinds you and then from\
 nowhere, a very loud sonar... BOOM! You\'re dead.')
	b1= ExitRoom('\n'+'A very small, dimly lit room. There are german flags hanging,\
 stained with blood. It reeks of sarin gas.', 'Second storage chamber.', 'You\
 walk in, you hear a hissing sound and all of a sudden, you have a running nose,\
 you feel a bit of pain in the chest and then you\'re jittery. Next, You\'re dead.')
	b2= ExitRoom('\n'+'A small bunker with steel walls. There is a faint smell of coal.',\
 'Bunker.', 'You walk in, smell the coal; you don\'t suspect it and then you\
 you see the light. No time to think fast. Then, there is the bright yellow explosion.\
 You\'re dead.')
	#connecting rooms
	b2.set_n(None)
	b2.set_s(None)
	b2.set_w(None)
	b2.set_e(X1)
	X1.set_n(M2)
	X1.set_s(None)
	X1.set_e(None)
	M2.set_n(M3)
	M2.set_w(None)
	M2.set_e(M1)
	M1.set_e(Y1)
	M1.set_n(None)
	M1.set_s(None)
	Y1.set_e(b1)
	Y1.set_n(None)
	Y1.set_s(None)
	b1.set_n(None)
	b1.set_e(None)
	b1.set_s(None) #not on board
	M3.set_w(b6)
	M3.set_n(M4)
	M3.set_e(None)
	b6.set_n(None)
	b6.set_s(None)
	b6.set_w(None)
	M4.set_n(None)
	M4.set_w(None)
	M4.set_e(M5)
	M5.set_n(b5)
	M5.set_e(M6)
	M5.set_s(None)
	b5.set_n(None)
	b5.set_w(None)
	b5.set_e(None)
	M6.set_n(None)
	M6.set_e(M7)
	M6.set_s(None)
	M7.set_e(M8)
	M7.set_n(X4)
	M7.set_s(b7)
	X4.set_n(None)
	X4.set_w(None)
	X4.set_e(b8)
	b7.set_s(None)
	b7.set_w(None)
	b7.set_e(M9)
	b8.set_n(None)
	b8.set_s(M8)
	b8.set_e(None)
	M8.set_e(None)
	M8.set_s(M9)
	M9.set_s(None)
	M9.set_e(E1)
	E1.set_n(None)
	E1.set_s(None)
	E1.set_e(None)
	#GateGem instances
	blue_k1= GateGem('blue')
	blue_k2= GateGem('blue')
	green_k= GateGem('green')
	red_k1= GateGem('red')
	red_k2= GateGem('red')
	yellow_k= GateGem('yellow')
	#creating gates
	b2.set_gate_e(blue_k1)
	X1.set_gate_n(None)
	M2.set_gate_n(blue_k1)
	M2.set_gate_s(None)
	M2.set_gate_e(None)
	M1.set_gate_e(None)
	M1.set_gate_w(None)
	Y1.set_gate_e(None)
	Y1.set_gate_w(None)
	b1.set_gate_w(None)
	b6.set_gate_e(red_k1)
	M3.set_gate_n(None)
	M4.set_gate_s(None)
	M4.set_gate_e(green_k)
	M5.set_gate_n(red_k1)
	M5.set_gate_e(red_k1)
	M6.set_gate_e(None)
	M7.set_gate_n(None)
	M7.set_gate_s(yellow_k)
	M7.set_gate_e(blue_k1)
	M7.set_gate_w(None)
	M8.set_gate_n(yellow_k)
	M8.set_gate_s(yellow_k)
	b7.set_gate_e(None)
	M9.set_gate_e(green_k)
	M9.set_gate_w(None)
	X4.set_gate_s(None)
	X4.set_gate_e(green_k)
	#putting grandeur keys(gems) in rooms
	X1.inventory.add(blue_k1)
	M3.inventory.add(red_k1)
	M4.inventory.add(red_k2)
	M6.inventory.update([blue_k2, yellow_k])
	M7.inventory.add(green_k)

	#create player instance
	Harvey= Player(Y1)
	re_try= 'y'
	while re_try== 'y': #while loop to control deaths, in case user wants to try again
		#while the player is in Room, that is, while he is still playing
		while not isinstance(Harvey.location, ExitRoom): 
			print 'You are in' + str(Harvey.location)
			if len(Harvey.location.inventory) != 0:
				gem_var= raw_input('\n'+'Enter Y if you want to pick up a gem.-> ' )
				while gem_var== 'Y' or gem_var== 'y':
					getgem= raw_input('\n'+'Which gem do want to take?(Enter the first\
 letter of the colour. e.g. b for a blue gem.) ->' )
					hash1_set= set() #set that will contain hashes of the room's gems
					for x in Harvey.location.inventory:
						c= hash(x)
						hash1_set.add(c) #adding those hashes to the set
					hash2_set= set() #set that will contain hashes of the player's gems
					for x in Harvey.inventory:
						p= hash(x)
						hash2_set.add(p) #adding those hashes to the set
					i_set= hash1_set.intersection(hash2_set) #hashes of gems possessed by both
					if getgem== 'b' or getgem== 'B': #if gem being asked for is blue
						if hash(blue_k1) in i_set: #if player already has it
							return 'You cannot carry two gems of the same colour.'
						else: #if player does not have it
							for x in Harvey.location.inventory: #looking for gem in room's inventory
								if hash(x)== hash(blue_k1): #when found
									Harvey.inventory.add(x) #add to player
									print 'You have ' + str(len(Harvey.inventory)) + ' grandeur keys.'
									print 'You\'ve picked up a blue grandeur key'
					elif getgem== 'g' or getgem== 'G': #if gem being asked for is green
						if hash(green_k) in i_set: #if player already has it
							return 'You cannot carry two gems of the same colour.'
						else: #if player does not have it
							for x in Harvey.location.inventory: #looking for gem in room's inventory
								if hash(x)== hash(green_k): #when found
									Harvey.inventory.add(x) #add to player
									print 'You have' + str(len(Harvey.inventory)) + 'grandeur keys.'
									print 'You\'ve picked up a green grandeur key'
					elif getgem== 'r' or getgem== 'R':
						if hash(red_k1) in i_set: #if player already has it
							return 'You cannot carry two gems of the same colour.'
						else: #if player does not have it
							for x in Harvey.location.inventory: #looking for gem in room's inventory
								if hash(x)== hash(red_k1): #when found
									Harvey.inventory.add(x) #add to player
									print 'You have' + str(len(Harvey.inventory)) + 'grandeur keys.'
									print 'You\'ve picked up a red grandeur key'
					elif getgem== 'y' or getgem== 'Y':
						if hash(yellow_k) in i_set: #if player already has it
							return 'You cannot carry two gems of the same colour.'
						else: #if player does not have it
							for x in Harvey.location.inventory: #looking for gem in room's inventory
								if hash(x)== hash(yellow_k): #when found
									Harvey.inventory.add(x) #add to player
									print 'You have' + str(len(Harvey.inventory)) + 'grandeur keys.'
									print 'You\'ve picked up a yellow grandeur key'
					gem_var= raw_input('\n'+'Do you want to pick another gem? Enter Y if yes and\
 any other key for no.-> ' )
			valid_move= False
			while valid_move== False:
				dir_move= raw_input('\n'+'Where do you want to go? (Enter n for north, s for south,\
 e for east and w for west) -> ' )

				if dir_move=='n':
					if Harvey.location.n() != None: #if a room exists in that direction
						if Harvey.location.return_gate_n(): #if a gate exists between
							for x in Harvey.inventory:
								if x== Harvey.location.get_gate_n():
									Harvey.location.set_gate_n(None) #remove gate
									Harvey.location= Harvey.location.n() #change rooms
									valid_move= True
							print 'You do not have a gem to open this door. You need\
 to go get a gem to open it.', '\n'
						else:
							Harvey.location= Harvey.location.n() #change rooms
							valid_move= True
					else:
						print 'Nothing exists in that direction. It is total blackness.'+'\n'

				elif dir_move=='e':
					if Harvey.location.e() != None: #if a room exists in that direction
						if Harvey.location.return_gate_e(): #if a gate exists between
							for x in Harvey.inventory:
								if x== Harvey.location.get_gate_e():
									Harvey.location.set_gate_e(None) #remove gate
									Harvey.location= Harvey.location.e() #change rooms
									valid_move= True
							print 'You do not have a gem to open this door. You need\
 to go get a gem to open it.', '\n'
						else:
							Harvey.location= Harvey.location.e() #change rooms
							valid_move= True
					else:
						print 'Nothing exists in that direction. It is total blackness.'+'\n'

				elif dir_move=='s':
					if Harvey.location.s() != None: #if a room exists in that direction
						if Harvey.location.return_gate_s(): #if a gate exists between
							for x in Harvey.inventory:
								if x== Harvey.location.get_gate_s():
									Harvey.location.set_gate_s(None) #remove gate
									Harvey.location= Harvey.location.s() #change rooms
									valid_move= True
							print 'You do not have a gem to open this door. You need\
 to go get a gem to open it.', '\n'
						else:
							Harvey.location= Harvey.location.s() #change rooms
							valid_move= True
					else:
						print 'Nothing exists in that direction. It is total blackness.'+'\n'

				elif dir_move=='w':
					if Harvey.location.w() != None: #if a room exists in that direction
						if Harvey.location.return_gate_w(): #if a gate exists between
							for x in Harvey.inventory:
								if x== Harvey.location.get_gate_w():
									Harvey.location.set_gate_w(None) #remove gate
									Harvey.location= Harvey.location.w() #change rooms
									valid_move= True
							print 'You do not have a gem to open this door. You need\
 to go get a gem to open it.', '\n'
						else:
							Harvey.location= Harvey.location.w() #change rooms
							valid_move= True
					else:
						print 'Nothing exists in that direction. It is total blackness.'+'\n'

		if Harvey.location is not E1:
			print Harvey.location.return_desc() + '\n' + Harvey.location.return_death_note()
			re_try= raw_input('\n'+'Do you want you try again? (Enter y for yes, n for no.) -> ' )
			if re_try== 'y':
				Harvey.location= Y1
			else:
				print '\n'+'Take heart. Very few have ever survived the devil\'s hole.'
		elif Harvey.location is E1:
			re_try= 'n'
			print  Harvey.location.return_desc() + '\n' + Harvey.location.return_death_note()