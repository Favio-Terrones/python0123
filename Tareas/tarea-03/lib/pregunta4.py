
class Catalogo:

    def __init__(self):
         self.productos = []

    def agregarProducto(self,producto):
         self.productos.append(producto)

    def mostrarProductos(self):
         for producto in self.productos:
            print(producto)     


class ProductO:
     
     def __init__(self,nombre,precio,procedencia):
          self.nombre = nombre
          self.precio = precio
          self.procedencia = procedencia

     def __str__(self) -> str:
          return f"La autoparte {self.nombre} cuesta S/{self.precio} y es {self.procedencia}"
     


if __name__ == '__main__':
     catalogo = Catalogo()

     producto1 = ProductO("Chasis","350","nacional")
     producto2 = ProductO("Sistema de frenos","400","importado")
     producto3 = ProductO("Motor","1250","importado")


     catalogo.agregarProducto(producto1)
     catalogo.agregarProducto(producto2)
     catalogo.agregarProducto(producto3)

     catalogo.mostrarProductos()



