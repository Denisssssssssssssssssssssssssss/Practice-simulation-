from random import randint as rd, choice as ch
from os import system as sys
import pygame
from math import *
pygame.init()
global blus
global reds
blus = []
reds = []
blucords = []
redcords = []
p = 0
q = 0
class Green():
	def __init__(self, x, y):
		self.x = x
		self.y = y
		self.is_atk = False
		self.color = (0, 255, 0)
		self.pos = (self.x, self.y, 10, 10)
		self.type = 'green'
		self.is_dead = False

	def go(self, users):
		for user in users:
			if (user.x == self.x)&(user.y == self.y):
				self.is_atk = True
				self.dead = True
				self.color = (0,0,0)
				break

class Blu():
	def __init__(self, x, y):
		self.x = x
		self.y = y
		self.speed = 5
		self.tar_x = None
		self.tar_y = None
		self.color = (0, 0, 255)
		self.pos = (self.x, self.y, 20, 20)
		self.type = 'blu'
		self.energy = 1000

	def decrease_energy(self):
		self.energy -= self.speed
		if self.energy == 0:
			self.color = (0,0,0)


	def go(self):
		if self.tar_x != None:
			if (self.tar_x != None) & (self.tar_y != None):

				if (self.x != self.tar_x) & (self.y != self.tar_y):
					var = rd(0, 2)
					if var:  # по х
						if self.x < self.tar_x:
							self.x += self.speed
						elif self.x > self.tar_x:
							self.x -= self.speed
					if not (var):  # по y
						if self.y < self.tar_y:
							self.y += self.speed
						elif self.y > self.tar_y:
							self.y -= self.speed

				elif (self.x != self.tar_x):
					if self.x < self.tar_x:
						self.x += self.speed
					elif self.x > self.tar_x:
						self.x -= self.speed

				elif (self.y != self.tar_y):
					if self.y < self.tar_y:
						self.y += self.speed
					elif self.y > self.tar_y:
						self.y -= self.speed

				elif (self.x == self.tar_x) & (self.y == self.tar_y):
					self.tar_x = None
					self.tar_y = None
		self.pos = (self.x, self.y, 10, 10)

class Red():
	def __init__(self, x, y):
		self.x = x
		self.y = y
		self.speed = 5
		self.tar_x = None
		self.tar_y = None
		self.color = (255, 0, 0)
		self.pos = (self.x, self.y, 10, 10)
		self.type = 'red'
		self.energy = 1000

	def decrease_energy(self):
		self.energy -= self.speed
		if self.energy == 0:
			self.color = (0,0,0)

	def go(self):
		if self.tar_x != None:
			if (self.tar_x != None)&(self.tar_y != None):
		
				if (self.x != self.tar_x)&(self.y != self.tar_y):
					var = rd(0,2)
					if var: # по х
						if self.x < self.tar_x:
							self.x += self.speed
						elif self.x > self.tar_x:
							self.x -= self.speed
					if not(var): # по y
						if self.y < self.tar_y:
							self.y += self.speed
						elif self.y > self.tar_y:
							self.y -= self.speed

				elif (self.x != self.tar_x):
					if self.x < self.tar_x:
						self.x += self.speed
					elif self.x > self.tar_x:
						self.x -= self.speed

				elif (self.y != self.tar_y):
					if self.y < self.tar_y:
						self.y += self.speed
					elif self.y > self.tar_y:
						self.y -= self.speed

				elif (self.x == self.tar_x)&(self.y == self.tar_y):
					self.tar_x = None
					self.tar_y = None
		
		self.pos = (self.x, self.y, 10, 10)
class Blucord():
	def __init__(self,x,y):
		self.x = x
		self.y = y

class Redcord():
	def __init__(self,x,y):
		self.x = x
		self.y = y
blucords.append(Blucord(1050,100))
redcords.append(Redcord(1050,300))

sc = pygame.display.set_mode((1500, 900))
pygame.display.set_caption("Nature")
clock = pygame.time.Clock()
FPS = 75
mln = 10000000
num = 0


for i in range(10):
	blus.append(Blu(rd(0, 90)*10, rd(0, 89)*10))


for i in range(10):
	reds.append(Red(rd(0, 90)*10, rd(0, 89)*10))


def get_greens():
	global greens, Green
	greens = []
	mas = [(0,0)]
	for i in range(100):
		x = rd(0, 90)*10
		y = rd(0, 89)*10
		if (x,y) in mas:
			while (x, y) in mas:
				x = rd(0, 149)*10
				y = rd(0, 89)*10
		greens.append(Green(x,y))
get_greens()

def check_greens(greens, reds):
	flag = False
	flag2 = False
	for gre in greens:
		if gre.is_atk == False:
			flag = True
	for red in reds:
		if (red.x != red.tar_x) or (red.y != red.tar_y):
			flag2 = True
	if flag or flag2:
		return True
	else:
		return False

def check_go(greens):
	flag = False
	for i in greens:
		if i.is_dead == False:
			flag = True
	return flag == True

def search_eat(greens, reds):
	global mln, num
	x1 = greens[i].x # x и y цели
	y1 = greens[i].y
	x2 = reds[user_num].x # x и y хищника
	y2 = reds[user_num].y

	# нужно сравнить расстояние от цели
	l1 = max(x1,x2)-min(x1,x2)
	l2 = max(y1,y2)-min(y1,y2)
	ln = sqrt(l1**2 + l2**2)

	if ln<mln:
		mln = ln
		num = i

def search_eat1(greens, blus):
	global mln, num
	x1 = greens[i].x # x и y цели
	y1 = greens[i].y
	x2 = blus[user_num].x # x и y хищника
	y2 = blus[user_num].y

	# нужно сравнить расстояние от цели
	l1 = max(x1,x2)-min(x1,x2)
	l2 = max(y1,y2)-min(y1,y2)
	ln = sqrt(l1**2 + l2**2)

	if ln<mln:
		mln = ln
		num = i

flag = True
running = True
gameplay = True


label = pygame.font.Font('Zlusa_font.ttf', 50)
blue_label = label.render('Добавить синих: ' + str(p), False, (255,255,255))
get_blu = blue_label.get_rect(topleft=(blucords[0].x, blucords[0].y))

red_label = label.render('Добавить красных: ' + str(q), False, (255,255,255))
get_red = blue_label.get_rect(topleft=(redcords[0].x, redcords[0].y))



while running:

	sc.fill((0, 0, 0))
	pygame.draw.rect(sc, 'White', (930, 0, 3, 900))
	pygame.draw.rect(sc, 'White', (1050, 650, 50, 50))
	pygame.draw.polygon(sc, 'White', ((1320, 650), (1320, 700), (1370, 675)))
	sc.blit(blue_label, (blucords[0].x, blucords[0].y))
	sc.blit(red_label, (redcords[0].x, redcords[0].y))

	mouse = pygame.mouse.get_pos()
	if 1050<mouse[0]<1100 and 650<mouse[1]<700  and pygame.mouse.get_pressed()[0]:
		gameplay = False
	if 1320 < mouse[0] < 1370 and 650 < mouse[1] < 700 and pygame.mouse.get_pressed()[0]:
		gameplay = True

	clock.tick(FPS)
	if check_go(greens) == False:
		get_greens()

	for i in range(len(reds)):
		if reds[i].color == (0, 0, 0):
			for j in range(len(greens)):
				if reds[i].tar_x == greens[j].x:
					if reds[i].tar_y == greens[j].y:
						greens[j].is_atk = False

	for i in range(len(blus)):
		if blus[i].color == (0, 0, 0):
			for j in range(len(greens)):
				if blus[i].tar_x == greens[j].x:
					if blus[i].tar_y == greens[j].y:
						greens[j].is_atk = False

	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			running = False

	p = len([blu for blu in blus if blu.color != (0, 0, 0)])
	q = len([red for red in reds if red.color != (0, 0, 0)])
	blue_label = label.render('Добавить синих:  ' + str(p), False, (255, 255, 255))
	red_label = red_label = label.render('Добавить красных: ' + str(q), False, (255, 255, 255))

	mouse = pygame.mouse.get_pos()
	if (get_blu.collidepoint(mouse)) and pygame.mouse.get_pressed()[0]:
		blus.append(Blu(rd(0, 90) * 10, rd(0, 89) * 10))
	if (get_red.collidepoint(mouse)) and pygame.mouse.get_pressed()[0]:
		reds.append(Red(rd(0, 90) * 10, rd(0, 89) * 10))

	if gameplay:
		if check_greens(greens, reds):
			for user_num in range(len(reds)):
				if (reds[user_num].tar_x == None):  # если нужна новая цель

					for git in greens:
						if git.is_atk == False:
							flag = True
							break

					if flag:  # если есть свободные цели
						mln = 1000000
						for i in range(len(greens)):

							if (greens[i].is_atk == False):  # если цель свободна
								search_eat(greens, reds)

						reds[user_num].tar_x = greens[num].x
						reds[user_num].tar_y = greens[num].y
						greens[num].is_atk = True
						mln = 0
						ln = 0
				if reds[user_num].color != (0, 0, 0):
					reds[user_num].go()
					reds[user_num].decrease_energy()
					pygame.draw.rect(sc, reds[user_num].color, reds[user_num].pos)

			for i in range(len(greens)):
				greens[i].go(reds)
				for user in reds:
					if (user.x == greens[i].x) & (user.y == greens[i].y):
						greens[i].is_dead = True
						user.energy += 50
				if not (greens[i].is_dead):
					pygame.draw.rect(sc, greens[i].color, greens[i].pos)

		if check_greens(greens, blus):
			for user_num in range(len(blus)):
				if (blus[user_num].tar_x == None):  # если нужна новая цель

					for git in greens:
						if git.is_atk == False:
							flag = True
							break

					if flag:  # если есть свободные цели
						mln = 1000000
						for i in range(len(greens)):
							if (greens[i].is_atk == False):  # если цель свободна
								search_eat(greens, blus)

						blus[user_num].tar_x = greens[num].x
						blus[user_num].tar_y = greens[num].y
						greens[num].is_atk = True
						mln = 0
						ln = 0
				if blus[user_num].color != (0, 0, 0):
					blus[user_num].go()
					blus[user_num].decrease_energy()
					pygame.draw.rect(sc, blus[user_num].color, blus[user_num].pos)
			for i in range(len(greens)):
				greens[i].go(blus)
				for user in blus:
					if (user.x == greens[i].x) & (user.y == greens[i].y):
						greens[i].is_dead = True
						user.energy += 50
				if not (greens[i].is_dead):
					pygame.draw.rect(sc, greens[i].color, greens[i].pos)
		pygame.display.update()

pygame.quit()