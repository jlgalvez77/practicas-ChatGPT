import json
from order import Order

class OrderBook:
    def __init__(self):
        self.orders = []    # Lista para almacenar las órdenes

    def add_order(self, order):
        '''Agrega una nueva orden al libro de ordenes'''
        self.orders.append(order)

    def remove_order(self, order_id):
        '''Elimina una orden del libro de órdenes'''
        self.orders = [order for order in self.orders if order.order_id != order_id]

    def update_order_status(self, order_id, new_status):
        '''Actualiza el estado de una orden'''
        for order in self.orders:
            if order.order_id == order_id:
                order.update_status(new_status)

    def show_orders(self, order_type=None):
        '''Muestra todas las órdenes o filtra ppor tipo ("buy" o "sell")'''
        if not self.orders:
            print('No hay ordenes registradas.\n')
            return
        print('ORDENES REGISTRADAS:')
        for order in self.orders:
            if order_type is None or order.order_type == order_type:
                order.show_details()

    def save_orders(self):
        '''Guarda la órdenes en un archivo JSON'''
        with open('orders.json', 'w') as file:
            json.dump([order.__dict__ for order in self.orders], file)

    def load_orders(self):
        '''Carga las órdenes desde un archivo JSON'''
        try:
            with open('orders.json', 'r') as file:
                orders_data = json.load(file)
                for order_data in orders_data:
                    order = Order(order_data['order_type'], order_data['price'], order_data['quantity'])
                    order.order_id = order_data['order_id']
                    order.status = order_data['status']
                    self.orders.append(order)
        except FileNotFoundError:
            print('No se encontró el archivo orders.json.')
    
    def generate_report(self):
        '''Genera un reporte de las ordenes completadas'''
        completed_orders = [order for order in self.orders if order.status == 'completada']

        if not completed_orders:
            print('No hay órdenes completadas.\n')
            return
        
        print("📑 REPORTE DE ÓRDENES COMPLETADAS:")
        for order in completed_orders:
            print(f"ID: {order.order_id} | Tipo: {order.order_type} | Precio: {order.price} | Cantidad: {order.quantity} | Total: {order.get_total()} USDT")

        # Opcional: Exportar a archivo de texto
        with open("completed_orders_report.txt", "w") as file:
            for order in completed_orders:
                file.write(f"ID: {order.order_id} | Tipo: {order.order_type} | Precio: {order.price} | Cantidad: {order.quantity} | Total: {order.get_total()} USDT\n")
        print("✅ Reporte guardado en 'completed_orders_report.txt'.")
        