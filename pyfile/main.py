import pygame as pg
import random
import tkinter as tk
from tkinter import messagebox

pg.init()

screen = pg.display.set_mode((960,540), pg.RESIZABLE)
fullscreen = False
pg.display.set_caption("potato fries")

blank_card = pg.image.load("texture/blank_card.png").convert()
back_card = pg.image.load("texture/card_back.png").convert()

hearts = pg.image.load("texture/heart.png").convert()
spade = pg.image.load("texture/spade.png").convert()
diamond = pg.image.load("texture/diamond.png").convert()
clover = pg.image.load("texture/clover.png").convert()

class card:
    def __init__(self, rank, house):
        card_front= blank_card
        card_back= back_card
        card_rank = self.assign_rank(rank)
        card_house = pg.image
        runner = "card_house =" + house
        if house == "heart" or "spade" or "diamond" or "clover":
            exec(runner)
        else:
            messagebox.showerror("invalid house")
        messagebox.showinfo("the card is: "+ card_rank + " of " + house+"s")
    def assign_rank(self, rank_1):
        dict_1 = {1:"A", 11:"J", 12:"Q", 13:"K"}
        if rank_1<13 and rank_1 >0:
            return dict_1.get(rank_1, str(rank_1))
        else:
            messagebox.showerror("invalid rank number: "+str(rank_1))
            return "0"
run = True
while run:
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
                card(1,"spade")
    
    screen.blit(blank_card, (0,0))

    pg.display.update()
pg.quit()
