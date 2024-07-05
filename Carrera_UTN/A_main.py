import pygame
from C_datos_de_la_partida import *
from B_funciones import *

#dimensiones de la pantalla
SCREEN = pygame.display.set_mode((WIDTH,HEIGHT))
pygame.display.set_caption("Carrera UTN")

#timer_segundo = pygame.USEREVENT 
#pygame.time.set_timer(timer_segundo,1000) 

fin_tiempo = False
timer_segundos = pygame.USEREVENT #puedo agregarle +1 +2 #es un evento
pygame.time.set_timer(timer_segundos,1000) #1000 = 1seg

flag_run = True
while flag_run: #solo cambiamos el diccionario
    lista_eventos = pygame.event.get()
    for event in lista_eventos:
        cursor_pos = pygame.mouse.get_pos() ###
        if event.type == pygame.QUIT:
            
            flag_run = False

        if dic_mutable["estado_juego"] == 1:
            if event.type == pygame.MOUSEBUTTONDOWN:
                pos_click = list(event.pos)
                print(pos_click)

                update_1(pos_click,dic_mutable)

            if event.type == pygame.USEREVENT:
                fin_tiempo = tiempo(dic_mutable,fin_tiempo)


        elif dic_mutable["estado_juego"] == 0:
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_BACKSPACE:
                    dic_mutable["ingreso"] = dic_mutable["ingreso"][:-1]
                elif event.key == pygame.K_RETURN:
                    dic_mutable["estado_juego"] = 1
                else:
                    if manejar_ingreso(dic_mutable): #####################
                        dic_mutable["ingreso"] += event.unicode
            
            if event.type == pygame.MOUSEBUTTONDOWN:
                pos_click_1 = list(event.pos)

                update_0(pos_click_1,dic_mutable)

        elif dic_mutable["estado_juego"] == 2:
            if event.type == pygame.MOUSEBUTTONDOWN:

                pos_click_2 = list(event.pos)
                print(pos_click_2)
                update_2(pos_click_2,dic_mutable)

    SCREEN.fill(AZUL)


    blit_del_juego(SCREEN,dic_mutable,cursor_pos)
    pygame.display.update()

pygame.quit()
