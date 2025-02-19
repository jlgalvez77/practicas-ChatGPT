import uuid

class Order:
    def __init__(self, order_type, price, quantity):
        # Validación del tipo de orden
        if order_type not in ["buy", "sell"]:
            raise ValueError("El tipo de orden debe ser 'buy' o 'sell'.")

        # Validación del precio
        if price <= 0:
            raise ValueError("El precio debe ser mayor que 0.")

        # Validación de la cantidad
        if quantity <= 0:
            raise ValueError("La cantidad debe ser mayor que 0.")

        self.order_id = str(uuid.uuid4())  # Genera un ID único
        self.order_type = order_type  # 'buy' o 'sell'
        self.price = price
        self.quantity = quantity
        self.status = "pendiente"  # Estado inicial

    def show_details(self):
        """Muestra los detalles de la orden"""
        print(f"Orden ID: {self.order_id}")
        print(f"Tipo: {self.order_type}")
        print(f"Precio: {self.price}")
        print(f"Cantidad: {self.quantity}")
        print(f"Total: {self.get_total()} USDT")
        print(f"Estado: {self.status}\n")

    def update_status(self, new_status):
        """Actualiza el estado de la orden"""
        if new_status in ["pendiente", "completada", "cancelada"]:
            self.status = new_status
            print(f"Estado actualizado a: {self.status}")
        else:
            print("Estado no válido")

    def get_total(self):
        """Calcula el total de la orden"""
        return self.price * self.quantity
