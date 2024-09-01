from error import DimensionError
from foto import Foto

ancho = -100
alto = 200
ruta = "c:/windows/fernando.jpg"
try:
    foto_nueva = Foto(ancho, alto, ruta)
    foto_nueva.alto=alto
    foto_nueva.ancho=ancho
    foto_nueva.ruta=ruta
except DimensionError as e:
    print(e.mensaje)

print(foto_nueva)