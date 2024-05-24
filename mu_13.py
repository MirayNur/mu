WIDTH = 400
HEIGHT = 600
oyuncu = Actor("player" , (WIDTH//2 , HEIGHT-50))
lazer_listesi = []
def draw():
    screen.fill("blue")
    oyuncu.draw()
    for lazer in lazer_listesi:
        lazer.draw()
def update():
    if keyboard.left:
        oyuncu.x -= 5
    if keyboard.right:
        oyuncu.x += 5
    if oyuncu.left > WIDTH:
        oyuncu.right = 0
    if oyuncu.right < 0:
        oyuncu.left = WIDTH
    if keyboard.space:
        lazer = Actor("laser_red")
        lazer.midbottom = oyuncu.midtop
        lazer_listesi.append(lazer)
    for lazer in lazer_listesi:
        lazer.y -= 10
        if lazer.bottom < 0:
            lazer_listesi.remove(lazer)
