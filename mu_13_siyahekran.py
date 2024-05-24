import random
WIDTH = 265
HEIGHT = 265
koordinatlar = []
for x in range(100 , 161 , 15):
    koordinatlar.append((x , HEIGHT//2))
gecikme_suresi = 0
harfler = "abcdefghijklmnoöprs"
harf_listesi = []
basildi = False
def draw():
    screen.fill("black")
    i = 0
    for harf in harf_listesi:
        screen.draw.text(harf , koordinatlar[i] , color="green")
        i += 1
def on_mouse_down():
    global basildi
    if basildi:
        basildi = False
    else:
        basildi = True
def update(dt):
    global harf_listesi , gecikme_suresi
    if gecikme_suresi > 0.1:
        gecikme_suresi = 0
        if basildi:
            harf_listesi = random.sample(harfler , 5)
    gecikme_suresi += dt
