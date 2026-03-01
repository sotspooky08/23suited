import pygame as pg
import random
import tkinter as tk
from tkinter import messagebox

pg.init()
pg.font.init()

screen = pg.display.set_mode((960,540), pg.RESIZABLE)
fullscreen = False
pg.display.set_caption("potato fries")

font = pg.font.SysFont(None,44)

blank_card = pg.image.load("texture/blank_card.png").convert()
back_card = pg.image.load("texture/card_back.png").convert()

heart = pg.image.load("texture/heart.png").convert_alpha()
spade = pg.image.load("texture/spade.png").convert_alpha()
diamond = pg.image.load("texture/diamond.png").convert_alpha()
clover = pg.image.load("texture/clover.png").convert_alpha()
houses = {"heart":heart, "spade":spade,"diamond":diamond,"clover":clover}

class card:
    def __init__(self, rank, house):
        self.card_rank = self.assign_rank(rank)
        self.card_house = pg.image
        
        self.card_show = True
        self.pos = (0,0)
        self.properties = [self.pos]

        if house in houses:
            self.card_house = pg.transform.scale(houses[house],(25,25))
        else:
            messagebox.showerror("invalid house")
        #messagebox.showinfo("the card is: "+ self.card_rank + " of " + house+"s")
    def assign_rank(self, rank_1):
        dict_1 = {1:"A", 11:"J", 12:"Q", 13:"K"}
        if rank_1<14 and rank_1 >0:
            return dict_1.get(rank_1, str(rank_1))
        else:
            messagebox.showerror("invalid rank number: "+str(rank_1))
            return "0"
    def blitcard(self,pos):
        self.pos = pos
        house_poslist = list(self.pos)
        house_poslist[0] +=50
        house_pos = tuple(house_poslist)

        rank_font = font.render(self.card_rank, True,(0,0,0))
        house_poslist[0] -= + (pg.Surface.get_width(rank_font))
        rank_pos = tuple(house_poslist)

        if self.card_show:
            screen.blit(blank_card, self.pos)
            screen.blit(self.card_house, house_pos)
            screen.blit(rank_font,rank_pos)
        elif self.card_show == False:
            screen.blit(back_card,self.pos)
    def flip(self):
        self.card_show = not self.card_show


def load_card_stack(stack):
    for x in houses:
        i = 1
        while i<14:
            stack.append(card(i,x))
            i+=1
    return stack

run = True
blit_stack = {card(1,'spade'):(0,0)}
card_stack = []
init_blitstack = False

while run:
    screen.fill((0,0,0))
    for event in pg.event.get():
        if event.type == pg.QUIT:
            run = False
            exit()
        if event.type == pg.KEYDOWN:
            if event.key == pg.K_F11:
                fullscreen = not fullscreen
                if fullscreen:
                    pg.display.set_mode((0,0),pg.FULLSCREEN)
                else:
                    pg.display.set_mode((960,540), pg.RESIZABLE)
            if event.key == pg.K_LCTRL:
                load_card_stack(card_stack)
                init_blitstack = not init_blitstack
            if event.key == pg.K_LSHIFT:
                blit_stack[card_stack[0]].flip()
                print(card_stack[0].card_show)
    xoffset = 0
    
    for cards in card_stack:
        ### blit_stack.update({cards:(xoffset,0)})
        
        xoffset+=80
    if init_blitstack:
        for key,value in blit_stack.items():
            key.blitcard(value)
    pg.display.update()
pg.quit()
