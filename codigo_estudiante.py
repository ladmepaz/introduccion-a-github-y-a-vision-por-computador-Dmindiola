# -- coding: utf-8 --
"""
Created on Sat Oct  5 17:00:25 2024

@author: jfrui
"""
ruta = "/content/imagen0.png"
import numpy as np
from PIL import Image

def leer_imagen(ruta_imagen):
    """
    Lee una imagen a partir de una ruta y retorna el objeto imagen usando la librería PIL.
    
    Parámetros:
    ruta_imagen (str): Ruta de la imagen a leer.
    
    Retorna:
    img: objeto tipo Image de PIL
    """
    # Abrir la imagen
    img = Image.open(ruta_imagen)     
    return img

def obtener_info_imagen(img):
    """
    Recibe una imagen y retorna el número de canales y las dimensiones.
    
    Parámetros:
    img: objeto tipo Image de PIL
    
    Retorna:
    tuple: (num_canales, dimensiones) donde:
        - num_canales es el número de canales (1 para escala de grises, 3 para RGB, 4 para RGBA)
        - dimensiones es una tupla con las dimensiones (ancho, alto) de la imagen
    """
    
    # Obtener el número de canales
    modo = img.mode
    if modo == 'L':  # Escala de grises
        num_canales = 1 
    elif modo == 'RGB':  # Imagen RGB
        num_canales = 3 
    elif modo == 'RGBA':  # Imagen RGBA
        num_canales = 4 
    else:
        num_canales = len(modo)  # Otros modos de imagen
    
    # Obtener las dimensiones de la imagen
    dimensiones = img.size  # (ancho, alto)
    
    print(f"Número de canales: {num_canales}")
    print(f"Dimensiones: {dimensiones}")
    
    return num_canales, dimensiones

# Ruta de la imagen
ruta = "/content/imagen0.png"
img = leer_imagen(ruta)

def imagen_a_arreglo(img):
    """
    Convierte una imagen de tipo PIL a un arreglo de NumPy.
    
    Parámetros:
    img (PIL.Image): Imagen a convertir.
    
    Retorna:
    np.ndarray: Arreglo de NumPy con los datos de la imagen.
    """
    # Convertir la imagen a un arreglo de NumPy
    arreglo = np.array(img)
    print(f"Arreglo de imagen: {arreglo.shape}")  # Mostrar las dimensiones del arreglo
    return arreglo

def estadisticas_intensidad(arreglo_img):
    """
    Calcula el promedio y la desviación estándar de las intensidades de los píxeles
    en una imagen representada como un arreglo de NumPy.
    
    Parámetros:
    arreglo_img (np.ndarray): Imagen representada como arreglo de NumPy.
    
    Retorna:
    tuple: (promedio, desviación_estándar) de las intensidades de los píxeles.
    """
    # Calcular el promedio y la desviación estándar
    promedio = np.mean(arreglo_img)
    desviacion_estandar = np.std(arreglo_img)
    
    print(f"Promedio de intensidad: {promedio}")
    print(f"Desviación estándar de intensidad: {desviacion_estandar}")
    
    return promedio, desviacion_estandar

def estadisticas_por_canal(arreglo_img):
    """
    Calcula el promedio y la desviación estándar de las intensidades de los píxeles
    por canal en una imagen representada como un arreglo de NumPy.
    
    Si la imagen tiene un solo canal, calcula las estadísticas para ese canal.
    Si la imagen tiene múltiples canales, calcula las estadísticas por canal.
    
    Parámetros:
    arreglo_img (np.ndarray): Imagen representada como un arreglo de NumPy.
    
    Retorna:
    dict: Diccionario con el promedio y la desviación estándar por canal.
    """
    # Verificar el número de dimensiones del arreglo
    if len(arreglo_img.shape) == 2:
        # Imagen de un solo canal
        promedio = np.mean(arreglo_img) 
        desviacion_estandar = np.std(arreglo_img) 
        resultados = {
            'Canal_1': {
                'Promedio': promedio,
                'Desviación Estándar': desviacion_estandar
            }
        }
        print("Estadísticas para el canal único:")
        print(resultados)
    elif len(arreglo_img.shape) == 3:
        # Imagen de múltiples canales
        resultados = {}
        num_canales = arreglo_img.shape[2]
        
        for canal in range(num_canales):  # Iterar a través de los canales
            promedio = np.mean(arreglo_img[:, :, canal])
            desviacion_estandar = np.std(arreglo_img[:, :, canal])
            resultados[f'Canal_{canal+1}'] = {
                'Promedio': promedio,
                'Desviación Estándar': desviacion_estandar
            }
            print(f"Estadísticas para el Canal {canal + 1}:")
            print(resultados[f'Canal_{canal + 1}'])
    else:
        raise ValueError("El arreglo de imagen debe tener 2 o 3 dimensiones.")
    
    return resultados

# Llamar a las funciones y mostrar resultados
num_canales, dimensiones = obtener_info_imagen(img)
arreglo_img = imagen_a_arreglo(img)
promedio_intensidad, desviacion_estandar_intensidad = estadisticas_intensidad(arreglo_img)
estadisticas_por_canal(arreglo_img)