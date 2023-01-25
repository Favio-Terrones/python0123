

class Producto:
    def __init__(self,nombre,codigo):
        self.nombre = nombre
        self.codigo = codigo

    def __str__(self) -> str:
        return f"Producto: {self.nombre} con código: {self.codigo}"

    def identificarPais(self):
        pais = self.codigo.split("-")[0] 
        return pais

    def identificarLote(self):
        lote = self.codigo.split("-")[1] 
        return lote      


if __name__ == '__main__':
    producto = Producto("Motor Audi", "ARGENTINA-0015-2023")
    print(producto) 
    print(producto.identificarPais()) 
    print(producto.identificarLote()) 