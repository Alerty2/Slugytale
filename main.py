import pygame
import sys
import time
import morralla
turno = True
PANTALLA = pygame.display.set_mode((1000,600))
icono = pygame.image.load("imagenes/logo.png")
pygame.display.set_icon(icono)
img_boton = pygame.image.load("imagenes/boton.png")
#-----------DECLARAR LOS SPRITES CON CLASES---------#
#boton inicio
class Boton(pygame.sprite.Sprite):
    def __init__(self,imagen):
        super().__init__()
        #imagen
        self.image = pygame.image.load(imagen)
        self.rect = self.image.get_rect()
        boton45 = pygame.image.load("imagenes/boton.png")
            ###personajes###
#hero guerrero
class Heroe(pygame.sprite.Sprite):
    def __init__(self,imagen):
        super().__init__()
        self.image = pygame.image.load(imagen)
        self.rect = self.image.get_rect()
        self.speed = 1
            ###partes mazmorra###
#paredes
class Pared(pygame.sprite.Sprite):
    def __init__(self,imagen):
        super().__init__()
        self.image = pygame.image.load(imagen)
        self.rect = self.image.get_rect()
#suelo
class Suelo(pygame.sprite.Sprite):
    def __init__(self,imagen):
        super().__init__()
        self.image = pygame.image.load(imagen)
        self.rect = self.image.get_rect()
            ###escaleras###
#ecaleras primer piso
class Escaleras(pygame.sprite.Sprite):
    def __init__(self,imagen):
        super().__init__()
        self.image = pygame.image.load(imagen)
        self.rect = self.image.get_rect()
#momia
class momia(morralla.Enemigo):
    def __init__(self, imagen):
        super().__init__(imagen)
        self.image = pygame.image.load(imagen)
        self.rect = self.image.get_rect()
###--posibles movimientos de la momia--###
        self.abajo = abajomomia
        self.arriba = arribamomia
        self.derecha = derechamomia
        self.izquierda = izquierdamomia
    def update(self):
        pass

#----------------INICIO-------------------#
pygame.init()
#tamaño pantalla
PANTALLA = pygame.display.set_mode((1000,600))
#---------------------------------------------------------------------
#nombre ventana
pygame.display.set_caption('Spooky dungeons')
#---------------guerrero--------------------#
def game():
    personajes.add(heroe_guerrero)
    heroe_guerrero.rect.x = 350
    heroe_guerrero.rect.y = 200
    print("cacafuti")
#ICONO
#pygame.display.set_icon('')


###COLORES###
BLANCO = 255, 255, 255
NEGRO = 0, 0, 0
ROJO = 255, 0, 0
AZUL = 0, 0, 255
VERDE = 0, 255, 0
AMARILLO = 255, 255, 0
HIERBAC = 70, 87, 23
NOCHEC = 0, 0 , 102
###color de la ventana###
PANTALLA.fill(NOCHEC)
###variables##
a = 0
b = 170
Y = 0
X = 0
Z = 0
menu_principal = 1
coordenadasVX = 0
coordenadasVY = 0




#listas
listadejemplo = []
###------DECLARACION DE CLASES_Y_SPRITES---------###


###botón menu principal###
boton = Boton("imagenes/boton.png")
boton_group = pygame.sprite.Group()
boton_group.add(boton)
boton.rect.x = 250
boton.rect.y  = 300
###paredes###
personajes = pygame.sprite.Group()
paredes_tutorial = Pared("imagenes/pared_mazmorratutorial.png")
paredes_tutorial.rect.x = 170
paredes_tutorial.rect.y = 170
###suelo tutorial###
suelo_morado = Suelo("imagenes/suelo_mazmorratutorial.png")


###Heroe guerrero###
heroe_guerrero = Heroe("imagenes/heroe.png")
mazmorra = pygame.sprite.Group()
#escaleras
escaleras_n1 = Escaleras("imagenes/escaleras.png")
#momia
momia = morralla.momia("imagenes/momia1.png")

#------------------------------------------------------------
#reloj
reloj = pygame.time.Clock()
#-----------------ENEMIGOS-------------------------------------------#
#slime
#slime = #LaMorralla.Enemigo(68,12)
#slime.atacar()
pedo=1
#---------------------VARIABLES 2------------------------#
izquierdamomia = momia.rect.x - 30,momia.rect.y
derechamomia = momia.rect.x + 30, momia.rect.y
arribamomia = momia.rect.y + 30, momia.rect.x
abajomomia = momia.rect.y - 30, momia.rect.x
#-----------------BUCLE DEL JUEGO----------------------------(no tocar)----#
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
#------------------LÓGICA DEL JUEGO------------------------------#
        coordenadasAX = heroe_guerrero.rect.x
        coordenadasAY = heroe_guerrero.rect.y
###-----------------MENU PRINCIPAL--------------------###
        ###menu principal###
        if event.type == pygame.MOUSEBUTTONDOWN:
            nose = 1
            PANTALLA.fill(BLANCO)
            boton_group.remove(boton)
            bienvenida = pygame.image.load('imagenes/bienvenida.png')
            PANTALLA.blit(bienvenida,(170,0))
###----------------COMIENZA EL JUEGO---------------------###
        if event.type == pygame.KEYDOWN and nose == 1:
            nose = 0
            PANTALLA.fill(BLANCO)
            boton_group.remove(boton)
            menu_principal = 0
            #APARECER PAREDES#
            suelo_t = pygame.image.load("imagenes/suelo_mazmorratutorial.png")
            mazmorra.add(paredes_tutorial)
            #APARECER EL SUELO#
            boton_group.add(suelo_morado)
            suelo_morado.rect.x = 0
            suelo_morado.rect.y = 0
            #APARECER LAS ESCALERAS DEL NIVEL 1#
            personajes.add(escaleras_n1)
            escaleras_n1.rect.x = 650
            escaleras_n1.rect.y = 220
            #APARECER EL PERSONAJE#
            game()
            print("aejrhjek")
            ###SEGUNDO TUTORIAL###
            def tutorial2():
                print("has pasado al segundo tutorial")
                #APARECER PAREDES DE SEGUNDO TUTORIAL#
                personajes.add(paredes_tutorial)
                paredes_tutorial.rect.x = 170
                paredes_tutorial.rect.y = 170
                # APARECER SUELO DE SEGUNDO TUTORIAL#
                mazmorra.add(suelo_morado)
                personajes.add(escaleras_n1)
                # APARECER ESCALERAS DE SEGUNDO TUTORIAL#
                escaleras_n1.rect.x = 650
                escaleras_n1.rect.y = 220
                # APARECER MOMIA DE SEGUNDO TUTORIAL#
                personajes.add(momia)
                momia.rect.y = 300 
                momia.rect.x = 400
                #sistema de turnos
                if turno == False:
                    #programación de la momia
                    if key_pressed[pygame.K_UP]:
                        momia.rect.move_ip(0,-30)
                    if key_pressed[pygame.K_DOWN]:
                        momia.rect.move_ip(0,30)
                    if key_pressed[pygame.K_RIGHT]:
                        momia.rect.move_ip(-30,0)
                    if key_pressed[pygame.K_RIGHT]:
                        momia.rect.move_ip(30,0)

###-------------------EVENTOS--------------------------###
        ##movimiento###
        key_pressed = pygame.key.get_pressed()
        coordenadasVX = heroe_guerrero.rect.x
        coordenadasVY = heroe_guerrero.rect.y
        if key_pressed[pygame.K_UP]:
            heroe_guerrero.rect.move_ip(0,-30)
            #PANTALLA.fill(BLANCO)
            time.sleep(0.05)
            # -----PROGRAMACIÓN MOMIA--------#
            if key_pressed[pygame.K_UP]:
                momia.rect.move_ip(0, -30)
            if key_pressed[pygame.K_DOWN]:
                momia.rect.move_ip(0, 30)
            if key_pressed[pygame.K_RIGHT]:
                momia.rect.move_ip(-30, 0)
            if key_pressed[pygame.K_RIGHT]:
                momia.rect.move_ip(30, 0)
            coordenadasVX = coordenadasAX
            turno = False


        elif key_pressed[pygame.K_DOWN]:
            heroe_guerrero.rect.move_ip(0,30)
            #PANTALLA.fill(BLANCO)
            time.sleep(0.05)
            # -----PROGRAMACIÓN MOMIA--------#
            if key_pressed[pygame.K_UP]:
                momia.rect.move_ip(0, -30)
            if key_pressed[pygame.K_DOWN]:
                momia.rect.move_ip(0, 30)
            if key_pressed[pygame.K_RIGHT]:
                momia.rect.move_ip(-30, 0)
            if key_pressed[pygame.K_LEFT]:
                momia.rect.move_ip(30, 0)
                #colision
            if pygame.sprite.collide_mask(momia,paredes_tutorial):
                momia.rect.move_ip(0,30)
            turno = False
        elif key_pressed[pygame.K_LEFT]:
            heroe_guerrero.rect.move_ip(-30,0)
            #PANTALLA.fill(BLANCO)
            time.sleep(0.05)
            # -----PROGRAMACIÓN MOMIA--------#
            if key_pressed[pygame.K_UP]:
                momia.rect.move_ip(0, -30)
            if key_pressed[pygame.K_DOWN]:
                momia.rect.move_ip(0, 30)
            if key_pressed[pygame.K_RIGHT]:
                momia.rect.move_ip(-30, 0)
            if key_pressed[pygame.K_LEFT]:
                momia.rect.move_ip(30, 0)
            turno = False
        elif key_pressed[pygame.K_RIGHT]:
            heroe_guerrero.rect.move_ip(30,0)
            #PANTALLA.fill(BLANCO)
            time.sleep(0.05)
            #-----PROGRAMACIÓN MOMIA--------#
            if key_pressed[pygame.K_UP]:
                momia.rect.move_ip(0, -30)
            if key_pressed[pygame.K_DOWN]:
                momia.rect.move_ip(0, 30)
            if key_pressed[pygame.K_RIGHT]:
                momia.rect.move_ip(-30, 0)
            if key_pressed[pygame.K_LEFT]:
                momia.rect.move_ip(30, 0)

            turno = False
###----------------COLISIONES--------------------------###
        ###colision de personaje con paredes
        if pygame.sprite.collide_mask(heroe_guerrero,paredes_tutorial):
            print("hubo una colision wey")
            heroe_guerrero.rect.x=coordenadasVX
            heroe_guerrero.rect.y=coordenadasVY
        #escaleras nivel 1
        if pygame.sprite.collide_mask(heroe_guerrero,escaleras_n1) and menu_principal == 0:
            ganaste = pygame.image.load("imagenes/pasandoalsiguientepiso.png")
            PANTALLA.blit(ganaste,(8,8))
            time.sleep(1)
            heroe_guerrero.rect.x = coordenadasVX
            heroe_guerrero.rect.y = coordenadasVY
            personajes.remove(heroe_guerrero)
            boton_group.remove(suelo_morado)
            personajes.remove(escaleras_n1)
            print("hola")
            PANTALLA.blit(ganaste, (8, 8))
            time.sleep(1)
            PANTALLA.fill(BLANCO)
            PANTALLA.blit(ganaste, (8, 8))
            game()
            #colisión de la momia
            if pygame.sprite.collide_mask(momia,paredes_tutorial) and key_pressed[pygame.K_UP]:
                momia.rect.move_ip(0,-30)
            if pygame.sprite.collide_mask(momia,paredes_tutorial) and key_pressed[pygame.K_DOWN]:
                momia.rect.move_ip(0,30)
            if pygame.sprite.collide_mask(momia,paredes_tutorial) and key_pressed[pygame.K_RIGHT]:
                momia.rect.move_ip(-30,0)
            if pygame.sprite.collide_mask(momia,paredes_tutorial) and key_pressed[pygame.K_LEFT]:
                momia.rect.move_ip(30,0)
            #sistema de turnos

            ###PROGRAMACION DE LA MOMIA###
            if turno == False:
                pass
                # momia.rect.x = heroe_guerrero.rect.x - momia.rect.x + 10
            ###EJECUTAR EL SEGUNDO TUTORIAL###
            tutorial2()
        #SISTEMA DE TURNOS
    ###-----------ACTUALIZAR PANTALLA-----------------###
    pygame.display.flip()
    boton_group.draw(PANTALLA)
    mazmorra.draw(PANTALLA)
    personajes.draw(PANTALLA)
    #Fotogramas por segundo
    reloj.tick(60)
