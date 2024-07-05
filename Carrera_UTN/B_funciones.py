import json
import pygame
from colores import *
from imagenes import *
from D_rectangulos import *

lista_datos_personaje = []

def funcion_leer_json_array(ubicacion_archivo:str) -> list:
    """_summary_

    Args:
        ubicacion_archivo (str): _description_

    Returns:
        (list):  lista del archivo json
    """
    try:
        with open(ubicacion_archivo, 'r',encoding='utf-8') as archivo:
            datos = json.load(archivo)
            return datos
    except Exception as ex:
        print(ex)
        return []  #devuelvo una lista para que no retorne nonetype


lista_datos_personaje = funcion_leer_json_array("data_jugadores")
#dejar aca sino si se guarda el aneterior nombre de la anterior partida

lista_data = funcion_leer_json_array("data_preguntas.json")



def crear_leer_json(nombre_archivo:str,data:list):
    """creo un archivo json si existe lo sobreescribe

    Args:
        nombre_archivo (str): el nombre que quiero que tenga el archivo
        data (list): lo que quiero que tenga
    """
    with open(nombre_archivo,"w") as file:
        json.dump(data,file,indent=4)

def si_(lista):
    if type(lista) == list:
        return True
    else:
        return False

def ordenamiento_ascendente_descendente(lista:list, clave:str,ordenamiento:bool):
    """recorre la lista y oredena segun parametro ingesado,
    puede ser de forma ascendente o descendente 

    Args:
        lista (list): lista de los personajes
        clave (str): puede ser cualquier key de los diccionarios    
        ordenamiento (bool): se ingresa FALSE si es ascendete y TRUE si es descendente

    Returns:
        _type_: una NUEVA lista con las condiciones
    """
    if si_(lista) == True:
        return sorted(lista, key = lambda x: x[clave],reverse= ordenamiento) 
    else:
        return False

def lectura_posicion(pos_click:list,rect:pygame.Rect):
    lectura_boton = False
    try:
        if ((pos_click[0] > (rect.x) and pos_click[0] < (rect.x+rect.width)) and
            (pos_click[1] > rect.y and pos_click[1] < (rect.y+rect.height))):
            lectura_boton = True
    except Exception as ex:
        print(ex)
    return lectura_boton

def update_0(pos_click:list,diccionario:dict):
    lectrura_boton_empezar = lectura_posicion(pos_click,rectangulo_empezar)

    cambio_escenario(lectrura_boton_empezar,diccionario)

def update_1(pos_click:list,dic:dict):
    boton_terminar = lectura_posicion(pos_click,rectangulo_terminar)
    boton_a = lectura_posicion(pos_click,rectangulo_dato_a)
    boton_b = lectura_posicion(pos_click,rectangulo_dato_b)
    boton_c =  lectura_posicion(pos_click,rectangulo_dato_c)

    mover_personaje_con_validacion(dic,boton_a,boton_b,boton_c)
    movimineto_de_lista(boton_a,boton_b,boton_c,lista_dato_a,dic)

    cambio_escenario(boton_terminar,dic)


def update_2(pos_click:list,diccionario:dict):
    lectrura_boton_volver = lectura_posicion(pos_click,rectangulo_empezar)

    cambio_escenario(lectrura_boton_volver,diccionario)



def mover_personaje_con_validacion(dic,boton_a,boton_b,boton_c):
    validacion_respuesta(dic,lista_dato_a,lista_respuesta,boton_a)
    validacion_respuesta(dic,lista_dato_b,lista_respuesta,boton_b)
    validacion_respuesta(dic,lista_dato_c,lista_respuesta,boton_c)

    mover_personaje(rec_personaje,dic)



def movimineto_de_lista(boton_a,boton_b, boton_c,lista_largo,diccionario:dict):
    if (boton_a or boton_b or boton_c):
        diccionario["contador"] += 1

    fin_de_lista_preguntas(diccionario,lista_largo)

def fin_de_lista_preguntas(diccionario:dict,lista_largo:list):
    bandera = False
    if (diccionario["contador"] > (len(lista_largo)-1)):
        diccionario["contador"] = 0
        diccionario["estado_juego"] = 2
        crear_archivo_de_puntuacion(diccionario,lista_datos_personaje) ##############
        crear_lista_con_strings(lista_datos_personaje,lista_para_blitear)
        bandera = True
    return bandera

def crear_lista_con_puntajes(dicccionario:dict,list_con_datos:list):
    dict_con_datos = {}

    nombre = dicccionario["ingreso"]
    puntaje = dicccionario["score"]

    dict_con_datos["nombre"] = nombre
    dict_con_datos["score"] = puntaje

    list_con_datos.append(dict_con_datos)
    return list_con_datos

def cambio_escenario(boton:bool,diccionario:dict): #es solo un boton por escenario
    if diccionario["estado_juego"] == 2:
        if boton:
            reinicio_juego(diccionario)
    elif diccionario["estado_juego"] == 1:
        if boton:
            crear_archivo_de_puntuacion(diccionario,lista_datos_personaje) #las dos listas no son parametros
            crear_lista_con_strings(lista_datos_personaje,lista_para_blitear) 
            diccionario["estado_juego"] = 2
    elif diccionario["estado_juego"] == 0:
        if boton:
            diccionario["estado_juego"] = 1


def crear_archivo_de_puntuacion(diccionario_juego:dict,lista:list):
    lista_con_datos = (crear_lista_con_puntajes(diccionario_juego,lista))
    crear_leer_json("data_jugadores",lista_con_datos)



def crear_lista_con_strings(lista_con_data_perosonajes:list,lista_para_blitear_en_pantalla:list):
    lista_para_blitear_en_pantalla.clear()
    #lista_para_blitear_en_pantalla[:] = []
    #lista_para_blitear_en_pantalla = []
    lista_con_data_perosonajes = ordenamiento_ascendente_descendente(lista_con_data_perosonajes,"score",True) #rev
    for diccionarios in lista_con_data_perosonajes:
        cadena = f"Nombre:  {diccionarios['nombre']}   Puntos: {str(diccionarios['score'])}"
        lista_para_blitear_en_pantalla.append(cadena)

#rev
def blit_cuadros_de_texto_para_tabla(ventana:pygame.Surface,x:int,y:int,
    width:int,height:int,lista_de_tabla:list):
    lista_de_tabla = lista_de_tabla[:10] #################3
    for string in lista_de_tabla:
        y += 50
        texto = render_texto(string,GREENYELLOW,myfont_arcade)
        rectanglulo_prueba = crear_rectangulo(x,y,width,height)
        blit_cuadro_con_texto(ventana,texto,rectanglulo_prueba,AZUL,False)



def reinicio_juego(diccionario:dict): #reinicio
    if diccionario["estado_juego"] == 2:
        diccionario["score"] = 0
        diccionario["contador"] = 0
        diccionario["ingreso"] = ""
        diccionario["estado_juego"] = 0
        diccionario["bandera_nivel_personaje"] = True
        rec_personaje.x = x_rec_personaje_inicio
        rec_personaje.y = y_rec_personaje_inicio


def validacion_respuesta(diccionario,lista_opcion,lista_respuesta,lectura_boton:bool)-> int:
    if lectura_boton:
        if lista_opcion[diccionario["contador"]] == lista_respuesta[diccionario["contador"]]:
            diccionario["score"] = int(diccionario["score"]) + 10
            diccionario["respuesta_movimiento_correcta"] = True
            diccionario["segundos"] = "5" 
        else:
            diccionario["respuesta_movimiento_incorrecta"] = True
            diccionario["segundos"] = "5"


def buscar_claves(lista:list,clave:str):
    lista_titulos = []
    for e_lista in lista:
        lista_titulos.append(e_lista[clave])
    return lista_titulos



#rev
def animar_moviento(pantalla,lista_animaciones,rectangulo_principal):
    contador_ani = 0
    pantalla.blit(lista_animaciones[contador_ani], rectangulo_principal)


def mover_personaje(personaje:pygame.Rect,dic):
    if dic["bandera_nivel_personaje"]:
        if dic["respuesta_movimiento_correcta"]:
            personaje.x += 200
        elif dic["respuesta_movimiento_incorrecta"]:
            personaje.x -= 100
    else:
        if dic["respuesta_movimiento_correcta"]:
            personaje.x -= 200 
        elif dic["respuesta_movimiento_incorrecta"]:
            personaje.x += 100

    if personaje.colliderect(rec_6):
        personaje.x += 100
    if personaje.colliderect(rec_12):
        personaje.x += 100
    if personaje.x > pared_derecha.x and dic["bandera_nivel_personaje"] == True:
        dic["bandera_nivel_personaje"] = False
        personaje.y = 300
        personaje.x = 900
    
    if personaje.x > pared_derecha.x and dic["bandera_nivel_personaje"] == False:
        dic["bandera_nivel_personaje"] = True
        personaje.y = 200
        personaje.x = 900

    if personaje.x < pared_izquierda.x and dic["bandera_nivel_personaje"] == True:
        personaje.y = y_rec_personaje_inicio
        personaje.x = x_rec_personaje_inicio
    
    if personaje.x < pared_izquierda.x and dic["bandera_nivel_personaje"] == False:
        dic["estado_juego"] = 2
        crear_archivo_de_puntuacion(dic,lista_datos_personaje) 
        crear_lista_con_strings(lista_datos_personaje,lista_para_blitear)

    dic["respuesta_movimiento_correcta"] = False
    dic["respuesta_movimiento_incorrecta"] = False

#rev
def tiempo(dic,fin_tiempo):
    if fin_tiempo == False:
        dic["segundos"] = int(dic["segundos"])-1
        if dic["segundos"] < 1:
            dic["contador"] += 1
            fin_tiempo = True
    else:
        dic["segundos"] = 5
        fin_tiempo = False
    fin_de_lista_preguntas(dic,lista_dato_a)
    return fin_tiempo

def subir(diccionario):
        a =diccionario["ingreso"]
        diccionario["ingreso"] = a.upper()

def cambiar_color_texto(pos_mouse,rectangulo):
    if rectangulo.collidepoint(pos_mouse):
        color_pos_texto = ROJO
    else:
        color_pos_texto = NEGRO
    return color_pos_texto

def manejar_ingreso(diccionarios):
    bandera_manejo_ingreso = True
    if len(diccionarios["ingreso"]) >= 10:
        bandera_manejo_ingreso = False
    else:
        bandera_manejo_ingreso = True
    return bandera_manejo_ingreso

def blit_del_juego(SCREEN:pygame.Surface,diccionario:dict,cursor_pos):
    if diccionario["estado_juego"] == 1:
        animar_moviento(SCREEN,imagen_cuadro_azul,rec_1)
        animar_moviento(SCREEN,imagen_cuadro_azul,rec_2)
        animar_moviento(SCREEN,imagen_cuadro_azul,rec_3)
        animar_moviento(SCREEN,imagen_cuadro_azul,rec_4)
        animar_moviento(SCREEN,imagen_cuadro_azul,rec_5)
        animar_moviento(SCREEN,imagen_cuadro_verde,rec_6)
        texto_avanzar1 = render_texto("AVANZA 1",NEGRO,myfont_pequeña) 
        blit_cuadro_con_texto(SCREEN,texto_avanzar1,rec_6_texto,VERDE,False)
        animar_moviento(SCREEN,imagen_cuadro_azul,rec_7)
        animar_moviento(SCREEN,imagen_cuadro_azul,rec_8)
        animar_moviento(SCREEN,imagen_cuadro_azul,rec_16)
        animar_moviento(SCREEN,imagen_cuadro_azul,rec_15)
        animar_moviento(SCREEN,imagen_cuadro_azul,rec_14)
        animar_moviento(SCREEN,imagen_cuadro_azul,rec_13)
        animar_moviento(SCREEN,imagen_cuadro_verde,rec_12)
        texto_retroceder1 = render_texto(f"RETROCEDE 1",NEGRO,myfont_pequeña) 
        blit_cuadro_con_texto(SCREEN,texto_retroceder1,rec_12_texto,VERDE,False)
        animar_moviento(SCREEN,imagen_cuadro_azul,rec_11)
        animar_moviento(SCREEN,imagen_cuadro_azul,rec_10)
        animar_moviento(SCREEN,imagen_cuadro_azul,rec_9)
        animar_moviento(SCREEN,imagen_personaje,rec_personaje)
        animar_moviento(SCREEN,imagen_meta,rec_meta) ########

        color_pos_texto = cambiar_color_texto(cursor_pos,rectangulo_terminar) 
        texto_terminar = render_texto("TERMINAR",color_pos_texto,myfont) 
        blit_cuadro_con_texto(SCREEN,texto_terminar,rectangulo_terminar,VERDE,True)

        #cambios
        pregunta_en_lista = render_texto(lista_preguntas[diccionario["contador"]],ROJO,myfont) 
        blit_cuadro_con_texto(SCREEN,pregunta_en_lista,rectangulo_pregunta_en_lista,VERDE,False)

        color_pos_texto = cambiar_color_texto(cursor_pos,rectangulo_dato_a) 
        dato_a = render_texto(lista_dato_a[diccionario["contador"]],color_pos_texto,myfont)
        blit_cuadro_con_texto(SCREEN,dato_a,rectangulo_dato_a,VERDE,False)

        color_pos_texto = cambiar_color_texto(cursor_pos,rectangulo_dato_b) 
        dato_b = render_texto(lista_dato_b[diccionario["contador"]],color_pos_texto,myfont)
        blit_cuadro_con_texto(SCREEN,dato_b,rectangulo_dato_b,VERDE,False)

        color_pos_texto = cambiar_color_texto(cursor_pos,rectangulo_dato_c) 
        dato_c = render_texto(lista_dato_c[diccionario["contador"]],color_pos_texto,myfont)
        blit_cuadro_con_texto(SCREEN,dato_c,rectangulo_dato_c,VERDE,False)

        tema_pregunta = render_texto(lista_tema[diccionario["contador"]],ROJO,myfont)
        blit_cuadro_con_texto(SCREEN,tema_pregunta,rectangulo_tema_pregunta,VERDE,False)


        int_score_render = myfontGrande.render(f'SCORE: {str(diccionario["score"])}',True,ROJO) #NUMERO SCORE
        blit_cuadro_con_texto(SCREEN,int_score_render,rectangulo_SCORE_int,VERDE,False)


        #Tiempo
        tiempo_render = myfontGrande.render(f'TIEMPO: {str(diccionario["segundos"])}',True,ROJO)
        blit_cuadro_con_texto(SCREEN,tiempo_render,rectangulo_tiempo,VERDE,False)


    elif diccionario["estado_juego"] == 0:
        subir(diccionario) ###############################
        CARRERA_UTN = render_texto("CARRERA UTN",ROJO,my_font_titulo)
        blit_cuadro_con_texto(SCREEN,CARRERA_UTN,rectangulo_nombre_del_juego,VERDE,False)
        
        NOMBRE_DE_JUGADOR = render_texto("NOMBRE DEL JUGADOR:",ROJO,my_font_titulo)
        blit_cuadro_con_texto(SCREEN,NOMBRE_DE_JUGADOR,rectangulo_texto_nombre_del_jugador,VERDE,False)

        texto_ingreso = render_texto(diccionario["ingreso"],ROJO,my_font_titulo)
        blit_cuadro_con_texto(SCREEN,texto_ingreso,rectangulo_ingreso,NEGRO,True)

        color_pos_texto = cambiar_color_texto(cursor_pos,rectangulo_empezar)
        EMPEZAR = render_texto("EMPEZAR",color_pos_texto,myfont) 
        blit_cuadro_con_texto(SCREEN,EMPEZAR,rectangulo_empezar,VERDE,True)

    elif diccionario["estado_juego"] == 2:

        SCREEN.fill(NEGRO)
        color_pos_texto = cambiar_color_texto(cursor_pos,rectangulo_volver) 
        texto_volver = render_texto("VOLVER",color_pos_texto,myfont)
        blit_cuadro_con_texto(SCREEN,texto_volver,rectangulo_volver,VERDE,True)

        texto_mejores_puntajes = render_texto("MEJORES PUNTAJES",ROJO,myfont_arcade)
        blit_cuadro_con_texto(SCREEN,texto_mejores_puntajes,rectangulo_texto_puntos,VERDE,False)

        
        blit_cuadros_de_texto_para_tabla(SCREEN,200,40,200,50,lista_para_blitear)



lista_preguntas = buscar_claves(lista_data,"pregunta")
lista_dato_a = buscar_claves(lista_data,"a")
lista_dato_b = buscar_claves(lista_data,"b")
lista_dato_c = buscar_claves(lista_data,"c")
lista_tema = buscar_claves(lista_data,"tema")
lista_respuesta = buscar_claves(lista_data,"correcta")
