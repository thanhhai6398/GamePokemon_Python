# -*- coding: utf-8 -*-
"""
Created on Tue Jun  1 15:42:34 2021

@author: HP
"""

import pygame,sys
from pygame.constants import QUIT
pygame.init()
form = pygame.display.set_mode((600,400))
pygame.display.set_caption ("Me")
image= pygame.image.load("time_clock.png")
image = pygame.transform.scale(image,(600,400))

pygame.font.init()
text = pygame.font.SysFont("Times New Roman", 50)
text1 = text.render("Com", True, (0,0,0))
text2 = text.render("ca", True, (0,0,0))
form.blit(text1, (20,50))
form.blit(text2, (30,50))

while True:
    form.blit(image,(0,0))
    form.blit(text1,(300,300))
    form.blit(text2,(200,200))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    pygame.display.update()