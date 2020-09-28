import pygame
import bluetooth
import sys
import time
pygame.init()
white = (255, 255, 255)
green = (0, 255, 0)
blue = (0, 0, 128)
red=(255,0,0)
pygame.mixer.init()
pygame.mixer.music.load("fire.wav")
bd_addr ="00:18:E4:40:00:06"
port = 1
sock = bluetooth.BluetoothSocket( bluetooth.RFCOMM )
sock.connect((bd_addr, port))
sock.settimeout(100)
display_surface=pygame.display.set_mode((950,600))
pygame.display.set_caption("FIRE ALERT")
font = pygame.font.Font('charbb_reg.ttf', 500)
def mssg(msg,col):
	text = font.render(msg, True,col)
	textRect = text.get_rect()
	textRect.center = (470, 300)
	display_surface.fill(white)
	display_surface.blit(text, textRect)
	c=0

def display1():
	c=0
	pygame.mixer.music.play()
	mssg('FIRE',blue)
	pygame.display.update()
	x=int(sock.recv(12))
	if(x>=1):
		display2()

def display2():
	pygame.mixer.music.pause()
	mssg('SAFE',green)
	pygame.display.update()
	x=int(sock.recv(12))
	if(x==0):
		display1()


while(sock.recv(12)):
	data = int(sock.recv(12))
	print '%d'%data
	if(data == 0):
		display1()
		print("on");
	if(data>=1):
	display2()


print("off")

for event in pygame.event.get() :
	if event.type == pygame.QUIT :
		pygame.quit()
		quit()
	pygame.display.update()
sock.close()
