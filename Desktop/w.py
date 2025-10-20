import time

class TiendaOnline:
    """
    Representa una tienda online con funcionalidades para gestionar un
    inventario de productos.
    """
    def __init__(self):
        """
        Inicializa la tienda con un inventario vacío y ventas totales en cero.
        """
        self.inventario = []
        self.ventas_totales = 0.0

    # ------------------- MÉTODOS DE GESTIÓN DE INVENTARIO -------------------

    def agregar_producto(self, nombre, precio, cantidad):
        """
        Agrega un nuevo producto al inventario. Si el producto ya existe
        (por nombre), actualiza su cantidad.
        """
        for producto in self.inventario:
            if producto['nombre'].lower() == nombre.lower():
                # Si el producto ya existe, suma la cantidad nueva
                producto['cantidad'] += cantidad
                print(f"✅ Cantidad del producto '{nombre}' actualizada. Nuevo stock: {producto['cantidad']}.")
                return # Termina la ejecución del método
        
        # Si el bucle termina y no se encontró el producto, se agrega uno nuevo
        nuevo_producto = {'nombre': nombre, 'precio': precio, 'cantidad': cantidad}
        self.inventario.append(nuevo_producto)
        print(f"📦 Producto '{nombre}' agregado al inventario.")