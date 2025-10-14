    def agregar_producto(self, nombre, precio, cantidad): # tengo la duda de si aqui se añade todo el diccionario(las key y los value o se deja tal cual)
        for producto in self.inventario:
            if producto["nombre"].lower() == nombre.lower():
                producto["cantidad"] += cantidad #revisar si hay que poner entre corchetes la cantidad actualizada o cantidad
                print(f" Cantidad del producto '{nombre}' actualizada. Nuevo stock: {producto['cantidad']}.")
            return
        nuevo_producto = {"nombre": "calcetines", "precio": 1.0, "cantidad": 10}
        self.inventario.append(nuevo_producto)
        print(f" Producto '{nombre}' agregado al inventario.")