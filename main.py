import pygame
pygame.init()
win =pygame.display.set_mode((600,600))
pygame.display.set_caption('My First Game')
x=300
y=20
width=40
height=40
vel=10

run=True
while run:
    pygame.time.delay(100)
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            run=False


    keys=pygame.key.get_pressed()


    if keys[pygame.K_LEFT]:
        x-=vel
    if keys[pygame.K_RIGHT]:
        x+=vel
    if keys[pygame.K_UP]:
        y-=vel
    if keys[pygame.K_DOWN]:
        y+=vel

    pygame.draw.rect(win, (255, 100, 150), (x, y, width, height))
    pygame.display.update()


pygame.quit()


