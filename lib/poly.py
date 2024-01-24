class Poligono:
    def __init__(self, numLado, sizeLado):
    
        self.numLado = numLado
        self.sizeLado = sizeLado
        pass

    def __str__(self):
        return f"Numero de Lados: {self.numLado} y Tamaño del lado: {self.sizeLado} "

    def nomPoly( self ):
        match self.numLado:
            case 3:
                return "Tu poligono es un triangulo"
            case 4:
                return "Tu poligono es un cuadrado"
            case 5:
                return "Tu poligono es un pentagono"
            case 6:
                return "Tu poligono es un hexagono"
            
    def periPoly: (self):
      return f"El perimetro es : {self.numLado * self.sizeLado}"
        
class PoligonoRegular( Poligono ):
    def __init__(self, numLado, sizeLado, apotema):
       super().__init__(numLado, sizeLado)
       self.apotema = apotema
       pass

    def __str__(self):
        return f"Num Lado: {self.numLado}, Size Lado: {self.sizeLado},"

        