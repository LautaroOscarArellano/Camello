import pygame 
import sys
from config import *
pygame.init()


donas=list()

for i in range(10):
    pass

screen= pygame.display.set_mode(SIZE)
pygame.display.set_caption("Donuts war")

#icono = pygame.image.load(r"simpson.war\assets\images\Godzilla-Transparent-File.png").convert_alpha()
icono=pygame.transform.scale(pygame.image.load(
    r"simpson.war\assets\images\homer_left.png").convert_alpha(),SIZE_ICON)
pygame.display.set_icon(icono)

#fondo=pygame.image.load(r"simpson.war\assets\images\fondo.jpg").convert()
fondo=pygame.transform.scale(pygame.image.load(
    r"simpson.war\assets\images\background.jpg").convert() , SIZE)

"""Creacion de Dona"""
dona=pygame.transform.scale(pygame.image.load(
    r"simpson.war\assets\images\dona.png").convert_alpha() , DONA_SIZE)
rect_dona=dona.get_rect()
rect_dona.midtop=DISPLAY_MIDTOP
flag_dona=True

"""Creacion de HOMERO"""
homero_r=pygame.transform.scale(pygame.image.load(
    r"simpson.war\assets\images\homer_right.png").convert_alpha() , HOMER_SIZE)
homero_l=pygame.transform.scale(pygame.image.load(
    r"simpson.war\assets\images\homer_left.png").convert_alpha() , HOMER_SIZE)
homero=homero_r
rectangulo_homero=homero_r.get_rect()
rectangulo_homero.midbottom=((CENTER_X, DISPLAY_BOTTOM))


font = pygame.font.Font(r"simpson.war\assets\images\simpsons.ttf",48)
score=0

"""
Para que la la hitbox de la boca empieze en la boca de homero
Boca
"""
rectangulo_boca=pygame.rect.Rect(0,0,50,10)
rectangulo_boca.x=rectangulo_homero.x + 70 #ligamento[1]
rectangulo_boca.y=rectangulo_homero.y + 130  


"""Sonido"""
sonido=pygame.mixer.Sound(r"simpson.war\assets\images\ouch.mp3")
pygame.mixer.music.load(r"simpson.war\assets\images\ouch.mp3")
flag_sonido=True

clock=pygame.time.Clock()
while True:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    """
    Controles
    """
    keys=pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:#claves son las letras , keys es un diccionario
        if rectangulo_homero.left > DISPLAY_LEFT:
            rectangulo_homero.x -= HOMER_SPEED
            rectangulo_boca.x = rectangulo_homero.x + 40 #ligamento[1]
            rectangulo_boca.y = rectangulo_homero.y + 130
            homero = homero_l

    if keys[pygame.K_RIGHT]:
        if rectangulo_homero.right < DISPLAY_RIGHT:
            rectangulo_homero.x+=HOMER_SPEED
            rectangulo_boca.x=rectangulo_homero.x + 70 #ligamento[1]
            rectangulo_boca.y=rectangulo_homero.y + 130  
            homero=homero_r


    """ Dibuja la dona que cae para abajo"""     
    if rect_dona.bottom < DISPLAY_BOTTOM:
        rect_dona.y += DONA_SPEED



    """Anti rebote del sonido y collision con la boca """
    if rectangulo_boca.colliderect(rect_dona):
        flag_dona=False
        if flag_sonido:
            score += 1
            pygame.mixer.music.play()
            pygame.mixer.music.set_pos(0.3) #que el mp3 empieze en 
        flag_sonido=False
    else:
        flag_sonido=True
    """
    Ligamento de dona que caer para abajo cuando choca con la boca 
    """
    if flag_dona:
        screen.blit(dona,rect_dona)
    



    """Dibujos en pantalla (blit)
    Fondo obligatorio que este al inicio
    """
    screen.blit(fondo, ORIGIN)
    screen.blit(homero,rectangulo_homero)
    screen.blit(font.render("Score : " + str(score) ,True , GREEN) , SCORE_POS)

    """
    Dibujo de hitbox de la boca 
    pygame.draw : solo dibuja rectangulos(check) 
    no se puede pintar en homero , lo tiene que pintar en la pantalla POR ESO USAMOS [pygame.draw]
    """
    pygame.draw.rect(screen , RED , rectangulo_boca)#LIGAMENTO[1]



    pygame.display.flip()
