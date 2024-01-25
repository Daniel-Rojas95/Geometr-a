from lib import *

#hw()
obj_rect = Rectangulo(10,5)
print(obj_rect)

print("Ancho: "+str(obj_rect.ancho))
print("Largo: "+str(obj_rect.largo))

obj_rect_2 = Rectangulo(25,15)
print(obj_rect_2)
print("Ancho: "+str(obj_rect_2.ancho)+"[cm^2]")
print("Largo: "+str(obj_rect_2.largo)+"[cm^2]")
print("Perimetro: "+str(obj_rect_2.Perimetro())+"[cm^2]")
print("Area: "+str(obj_rect_2.Area())+"[cm^2]")
      



from lib import*

obj_poly_1= Poligono(5,18)
print(obj_poly_1)
print(f"Num Lados: {obj_poly_1.numLado }")

print(f"Num lados: {obj_poly_1.numLado}")


print("Clase prueba")
