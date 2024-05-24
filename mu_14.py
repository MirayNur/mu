from random import *

KART_SAYISI = 4
RKU = 121
WIDTH = KART_SAYISI * RKU
HEIGHT = 121
kartlar = []

def kart_destesi_olustur():
    global kartlar
    kart_resimleri = []
    for i in range(KART_SAYISI):
        kart_resimleri.append("resim"+str(i))
    yeni_liste = []
    while len(kart_resimleri)>0:
        yeni_liste.append(kart_resimleri.pop(randrange(len(kart_resimleri))))
    kart_resimleri = yeni_liste
    kartlar = []
    for i in range(KART_SAYISI):
        cekilen_resim = kart_resimleri.pop()
        yeni_kart = Actor(cekilen_resim)
        yeni_kart.topleft = (i*RKU,0)
        kartlar.append(yeni_kart)

kart_destesi_olustur()

def draw():
    screen.clear()
    for kart in kartlar:
        kart.draw()

def on_mouse_down(button):
    if button == mouse.LEFT:
        kart_destesi_olustur()
