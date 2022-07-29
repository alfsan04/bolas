import pygame as pg
import random

class Bola:
    def __init__(self, x, y, w=25, h=25, color = (255, 255, 255), vx = 0, vy = 0):
        self.x = x
        self.y = y
        self.w = w
        self.h = h
        self.color = color
        self.vx = vx
        self.vy = vy

    '''def velocidad(self, vx, vy):
        self.vx = vx
        self.vy = vy'''

    def mover(self):
        self.x += self.vx
        self.y += self.vy
        if self.x >= tam[0] - self.w or self.x <= 0:
            self.vx = -self.vx
        if self.y >= tam[1] - self.h or self.y <= 0:
            self.vy = -self.vy
    def dibujar(self, pantalla):
        pg.draw.rect(pantalla, self.color, (self.x, self.y, self.w, self.h))
        
pg.init()
cantidad_bolas = 100
tam = (800, 600)
diccionario = {}
pantalla_principal = pg.display.set_mode(tam)
pg.display.set_caption('Bolitas rebotando')
for i in range (cantidad_bolas):
    color = (random.randint(0,255),random.randint(0,255), random.randint(0,255))
    velocidad = (random.uniform(-1,1),random.uniform(-1,1))
    diccionario[i] = Bola(400, 300, color = color, vx = velocidad[0], vy = velocidad[1])


game_over = False

while not game_over:
    for evento in pg.event.get():
        if evento.type == pg.QUIT:
            game_over = True

    pantalla_principal.fill((0,0,255))
    for i in range(100):
        diccionario[i].dibujar(pantalla_principal)
        diccionario[i].mover()

    
    pg.display.flip()

pg.quit()

