from error import DimensionError

class Foto():
    MAX = 2500

    def __init__(self, ancho: int, alto: int, ruta: str) -> None:
        self.__ancho = ancho
        self.__alto = alto
        ruta = ruta

    @property
    def ancho(self) -> int:
        return self.__ancho

    @ancho.setter
    def ancho(self, ancho) -> None:
        if 1 < ancho < self.MAX:
            self.__ancho = ancho
        else:
            raise DimensionError(dimension="ancho", maximo = self.MAX, mensaje = "Ancho no esta en el rango establecido")

    @property
    def alto(self) -> int:
        return self.__alto

    @alto.setter
    def alto(self, alto) -> None:
        if 1 < alto < self.MAX:
            self.__ancho = alto
        else:
            raise DimensionError(dimension="alto", maximo = self.MAX, mensaje = "Alto no esta en el rango establecido")