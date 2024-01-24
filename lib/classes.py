


class Rectangulo:
    def __init__(self, largo, ancho):
       self.largo = largo
       self.ancho = ancho
       pass
    def __str__(self):
        return f"Rectangulo de largo {self.largo} y ancho {self.ancho}"

    def Area(self):
        #Completar
        return(self.largo*self.ancho)
    def Perimetro(self):
        return 2*(self.largo+self.ancho)
        

    



