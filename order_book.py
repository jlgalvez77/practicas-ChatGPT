import random
import time
import json
import csv
from order import Order

class OrderBook:
    def __init__(self):
        self.orders = []    # Lista para almacenar las órdenes

    def generate_report(self):
        """Genera un reporte de las ordenes completadas en TXT y CSV con timestamps"""
        completed_orders = [order for order in self.orders if order.status == "completada"]

        if not completed_orders:
            print("No hay ordenes completadas.\n")
            return

        # Mostrar en consola
        print("REPORTE DE ORDENES COMPLETADAS: ")
        for order in completed_orders:
            print(f"ID: {order.order_id} | Tipo: {order.order_type} | Precio: {order.price} | Cantidad: {order.quantity} | Total: {order.get_total()} EUR | Timestamp: {order.timestamp}")

        # Guardar en un archivo TXT
        with open("completed_orders_report.txt", "w") as file:
            for order in completed_orders:
                file.write(f"ID: {order.order_id} | Tipo: {order.order_type} | Precio: {order.price} | Cantidad: {order.quantity} | Total: {order.get_total()} EUR | Timestamp: {order.timestamp}\n")
        print("Reporte guardado en 'completed_orders_report.txt'.")

        # Guardar en archivo CSV
        with open("completed_orders_report.csv", "w", newline="") as file:
            writer = csv.writer(file)
            writer.writerow(["ID", "Tipo", "Precio", "Cantidad", "Total (EUR)", "Timestamp"]) # Encabezado
            for order in completed_orders:
                writer.writerow([order.order_id, order.order_type, order.price, order.quantity, order.get_total(), order.timestamp])
        print("Reporte guardado en 'completed_orders_reports.csv'.")

    def add_order(self, order):
        """Agrega una nueva orden al libro de ordenes"""
        self.orders.append(order)

    def match_orders(self):
        """Empareja automaticamente ordenes de compra y venta"""
        buy_orders = sorted([o for o in self.orders if o.order_type == "buy" and o.status == "pendiente"], key=lambda x: x.price, reverse=True)
        sell_orders = sorted([o for o in self.orders if o.order_type == "sell" and o.status == "pendiente"], key=lambda x: x.price)

        matched_orders = []

        while buy_orders and sell_orders and buy_orders[0].price >= sell_orders[0].price:
            buy_order = buy_orders.pop(0)
            sell_order = sell_orders.pop(0)

            quantity_traded = min(buy_order.quantity, sell_order.quantity)
            total_price = round(quantity_traded * sell_order.price, 2)

            buy_order.update_status("completada")
            sell_order.update_status("completada")

            matched_orders.append((buy_order, sell_order, total_price))

        if matched_orders:
            print("Se han ejecutado órdenes automáticamente: ")
            for buy, sell, total in matched_orders:
                print(f"{buy.quantity} unidades compradas a {sell.price} EUR por {total} EUR")
        else:
            print("No hay órdenes coincidentes en este momento")

    def simulate_market(self, num_orders=10, interval=2):
        """Genera órdenes aleatorias y las procesa en tiempo real."""
        print(f"🚀 Iniciando simulación de mercado con {num_orders} órdenes...\n")

        for i in range(num_orders):
            order_type = random.choice(["buy", "sell"])
            price = round(random.uniform(90, 110), 2)
            quantity = round(random.uniform(0.1, 5), 2)

            order = Order(order_type, price, quantity)
            self.add_order(order)

            print(f"🆕 Orden generada: {order.order_type.upper()} {quantity} unidades a {price} USDT")

            # Intentamos hacer matching después de cada orden
            self.match_orders()

            time.sleep(interval)  # Simula tiempo real entre órdenes

        print("\n✅ Simulación finalizada.")
    def remove_order(self, order_id):
        """Elimina una orden del libro de órdenes"""
        self.orders = [order for order in self.orders if order.order_id != order_id]

    def update_order_status(self, order_id, new_status):
        """Actualiza el estado de una orden"""
        for order in self.orders:
            if order.order_id == order_id:
                order.update_status(new_status)

    def show_orders(self, order_type=None):
        """Muestra todas las órdenes o filtra ppor tipo ("buy" o "sell")"""
        if not self.orders:
            print('No hay ordenes registradas.\n')
            return

        print('ORDENES REGISTRADAS:')
        for order in self.orders:
            if order_type is None or order.order_type == order_type:
                order.show_details()

    def save_orders(self):
        """Guarda la órdenes en un archivo JSON"""
        with open('orders.json', 'w') as file:
            json.dump([order.__dict__ for order in self.orders], file)

    def load_orders(self):
        """Carga las órdenes desde un archivo JSON"""
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
        """Genera un reporte de las ordenes completadas"""
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
        