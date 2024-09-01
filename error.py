class Error(Exception):
    pass
        
class DimensionError(Error):
    def __init__(self, mensaje: str, dimension: int, maximo: int) -> None:
        self.mensaje = mensaje
        self. dimension = dimension
        self.maximo = maximo
    def __str__(self):
        if self.dimension is None and self.maximo is None:
            return super.__str__()
        else:
            msj = self.mensaje
            if self.dimension:
                msj += self.dimension
            if self.maximo:
                msj += self.maximo
            return msj