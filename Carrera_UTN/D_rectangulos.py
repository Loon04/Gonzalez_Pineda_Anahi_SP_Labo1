import pygame
#from colores import *

lista_para_blitear = []


pygame.init()

pygame.font.get_fonts()

myfont_pequeña = pygame.font.SysFont("Calibri", 20)
myfont = pygame.font.SysFont("Calibri", 30)
myfontGrande = pygame.font.SysFont("Calibri", 40)
my_font_titulo = pygame.font.Font("Font nueva/CHAINREACT BLOCK BOXTER REGULAR.OTF",80) #para fonts dercargados
myfont_arcade = pygame.font.Font("Font nueva/CHAINREACT BLOCK BOXTER REGULAR.OTF", 30)


x_rect_imagen = 150
y_rect_imagen = 200

x_rec_personaje_inicio = 100
y_rec_personaje_inicio = 200


x_preguntas = 350
y_preguntas = 50
width_preguntas = 180
height_preguntas = 100

x_cuadro_res = 220
y_cuadro_res = 480
width_res = 60
height_res = 30



def crear_rectangulo(x:int,y:int,width:int,height:int):
    rectangulo = pygame.Rect(x,y,width,height)
    return rectangulo

def render_texto(texto,color,fuente):
    texto_renderizado = fuente.render(str(texto),True,color)
    return texto_renderizado

def blit_cuadro_con_texto(ventana:pygame.Surface,texto:str,rectangulo,color,mostar_draw:bool):
    if mostar_draw:
        pygame.draw.rect(ventana,color,(rectangulo.x,rectangulo.y,rectangulo.width,rectangulo.height))
    ventana.blit(texto,(rectangulo.x+(rectangulo.width-texto.get_width())/2, rectangulo.y+(rectangulo.height-texto.get_height())/2))


#ESCENARIO 0

rectangulo_nombre_del_juego = crear_rectangulo(400,80,200,80)

rectangulo_ingreso = crear_rectangulo(300,440-100,400,100)

rectangulo_texto_nombre_del_jugador = crear_rectangulo(400,240-80,200,80)

rectangulo_empezar = crear_rectangulo(600,550,180,100)


#ESCENARIO 1

rec_1 =  crear_rectangulo(x_rect_imagen,y_rect_imagen,100,80)

rec_2 = crear_rectangulo(x_rect_imagen+105,y_rect_imagen,100,80)

rec_3 = crear_rectangulo(x_rect_imagen+210,y_rect_imagen,100,80)

rec_4 = crear_rectangulo(x_rect_imagen+310,y_rect_imagen,100,80)

rec_5 = crear_rectangulo(x_rect_imagen+410,y_rect_imagen,100,80)

rec_6 = crear_rectangulo(x_rect_imagen+510,y_rect_imagen,100,80)
rec_6_texto = crear_rectangulo(x_rect_imagen+510,y_rect_imagen,100,80)

rec_7 = crear_rectangulo(x_rect_imagen+610,y_rect_imagen,100,80)

rec_8 = crear_rectangulo(x_rect_imagen+710,y_rect_imagen,100,80)

rec_9 =  crear_rectangulo(x_rect_imagen,y_rect_imagen+110,100,80)

rec_10 = crear_rectangulo(x_rect_imagen+100,y_rect_imagen+110,100,80)

rec_11 = crear_rectangulo(x_rect_imagen+210,y_rect_imagen+110,100,80)

rec_12 = crear_rectangulo(x_rect_imagen+310,y_rect_imagen+110,100,80)
rec_12_texto = crear_rectangulo(x_rect_imagen+310,y_rect_imagen+110,100,80)

rec_13 = crear_rectangulo(x_rect_imagen+410,y_rect_imagen+110,100,80)

rec_14 = crear_rectangulo(x_rect_imagen+510,y_rect_imagen+110,100,80)

rec_15 = crear_rectangulo(x_rect_imagen+610,y_rect_imagen+110,100,80)

rec_16 = crear_rectangulo(x_rect_imagen+710,y_rect_imagen+110,100,80)

rec_meta = crear_rectangulo(x_rect_imagen-100,y_rect_imagen+110,100,80)

rec_personaje = crear_rectangulo(x_rec_personaje_inicio,y_rec_personaje_inicio,30,50)

pared_derecha = crear_rectangulo(950,300,1,500)

pared_izquierda = crear_rectangulo(155,200,1,300)

rectangulo_terminar = crear_rectangulo(500,550,180,100)

rectangulo_pregunta_en_lista = crear_rectangulo(450,50,100,30)

rectangulo_dato_a = crear_rectangulo(x_cuadro_res,y_cuadro_res,width_res,height_res)

rectangulo_dato_b = crear_rectangulo(x_cuadro_res+250,y_cuadro_res,width_res,height_res)

rectangulo_dato_c = crear_rectangulo(x_cuadro_res+510,y_cuadro_res,width_res,height_res)

rectangulo_tema_pregunta = crear_rectangulo(100,580,100,30)

#SCORE
rectangulo_score = crear_rectangulo(840,500,50,30)

rectangulo_SCORE_int = crear_rectangulo(820,140,100,50)

#TIEMPO

rectangulo_tiempo = crear_rectangulo(820,90,100,50)


#ESCENARIO 2

rectangulo_volver = crear_rectangulo(600,550,180,100)

rectangulo_tabla_de_puntos = crear_rectangulo(200,200,200,400)

rectangulo_texto_puntos = crear_rectangulo(200,0,200,100)