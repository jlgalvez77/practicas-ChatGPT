import json
from order import Order

class OrderBook:
    def __init__(self):
        self.orders = []    # Lista para almacenar las órdenes

    def add_order(self, order):
        '''Agrega una nueva orden al libro'''
        self.orders.append(order)
        print(f'Orden {order.order_id} añadida con éxito.\n')

    def show_orders(self, order_type=None):
        '''Muestra todas las órdenes o filtra ppor tipo ("buy" o "sell")'''
        if not self.orders:
            print('No hay ordenes registradas.\n')
            return
        print('ORDENES REGISTRADAS:')
        for order in self.orders:
            if order_type is None or order.order.order_type == order_type:
                order.show_details()

    def find_order(self, order_id):
        '''Busca una orden por su ID'''
        for order in self.orders:
            if order.order_id == order_id:
                return order
        return None
    
    def remove_order(self, order_id):
        '''Elimina una orden por su ID'''
        order = self.find_order(order_id)
        if order:
            self.orders.remove(order)
            print(f'Orden {order_id} eliminada con éxito.\n')
        else:
            print('Orden no encontrada.\n')
    
    def update_order_status(self, order_id, new_status):
        '''Actualiza el estado de una orden'''
        order = self.find_order(order_id)
        if order:
            order.update_status(new_status)
        else:
            print('Orden no encontrada.\n')

    def save_orders(self, filename='orders.json'):
        '''Guarda todas las órdenes en un archivo JSON'''
        data = [
            {
                'order_id': order.order_id,
                'order_type': order.order_type,
                'price': order.price,
                'quantity': order.quantity,
                'status': order.status
            }
            for order in self.orders
        ]
        with open(filename, 'w') as file:
            json.dump(data, file, indent=4)
        print(f'Órdenes guardadas en {filename}\n')

    def load_orders(self, filename='orders.json'):
        '''Carga órdenes desde un archivo JSON'''
        try:
            with open(filename, 'r') as file:
                data = json.load(file)
                for item in data:
                    order = Order(item['order_type'], item['price'], item['quantity'])
                    order.order_id = item['order_id']   # Restaura el ID
                    order.status = item['status']   # Restaura el estado
                    self.orders.append(order)
            print(f'Órdenes cargadas desde {filename}\n')
        except FileNotFoundError:
            print('No se encontró el archivo, iniciando sin órdenes previas.\n')