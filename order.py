import uuid

class Order:
    def __init__(self, order_type, price, quantity):
        self.order_id = str(uuid.uuid4()) # Genera un ID unico
        self.order_type = order_type    # 'buy' o 'sell'
        self.price = price
        self.quantity = quantity
        self.status = 'pendiente'   # Estado Inicial

    def show_details(self):
        '''Muestra los detalles de la orden'''
        print(f'Orden ID: {self.order_id}')
        print(f'Tipo: {self.order_type}')
        print(f'Precio: {self.price}')
        print(f'Cantidad: {self.quantity}')
        print(f'Estado: {self.status}')

    def update_status(self, new_status):
        '''Actualixs rl estado de la orden'''
        if new_status in ['pendiente', 'completada', 'cancelada']:
            self.status = new_status
        else:
            print('Estado no válido')

# Ejemplo de uso
orden1 = Order('buy', 45000, 0.1)
orden1.show_details()
orden1.update_status('completada')
orden1.show_details()