from ast import While
from operator import truediv
from selectors import SelectorKey
from turtle import bk
import pygame
pygame.init()

win = pygame.display.set_mode((640,640))

selectedsquarex = 0
selectedsquarey = 0
selected = False
BK = 0, 0
BKimage = pygame.image.load("Desktop/Pygame Projects/BlackKing.png")

run = True
while run:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    win.fill((255, 255, 255))
    leftclick, middleclick, rightclick = pygame.mouse.get_pressed()
    if leftclick and clicked == False:
       mousex, mousey = pygame.mouse.get_pos()
       if (mousex // 80) == selectedsquarex and (mousey // 80) == selectedsquarey and selected == True:
            selected = False   
       elif selected != True:
            selected = True
       elif selected == True and selectedsquarex * 80 == BK[0] and selectedsquarey * 80 == BK[1]:
            BK = (mousex // 80) * 80, (mousey // 80) * 80
            selected = False
       selectedsquarex = (mousex // 80)
       selectedsquarey = (mousey // 80)
       clicked = True
    if not leftclick:
        clicked = False
       

    for y in range(4): 
         for i in range(4):
             pygame.draw.rect(win, (0, 0, 0), (160 * i + 80, 160 * y, 80, 80))
             pygame.draw.rect(win, (0, 0, 0), (160 * i, (160 * y) + 80, 80, 80))

    if selected:
        pygame.draw.rect(win, (150, 150, 150), (((80 * selectedsquarex)), ((80 * selectedsquarey)), 80, 80))
    
    win.blit(BKimage, BK)
    pygame.display.update()