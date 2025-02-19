from order_book import OrderBook
from order import Order

# Inicializar el OrderBook y cargar órdenes previas
order_book = OrderBook()
order_book.load_orders()

# Crear órdenes nuevas
orden1 = Order("buy", 45000, 0.1)
orden2 = Order("sell", 47000, 0.2)

# Agregar órdenes al libro
order_book.add_order(orden1)
order_book.add_order(orden2)

# Mostrar todas las órdenes
order_book.show_orders()

# Actualizar estado de una orden
order_book.update_order_status(orden1.order_id, "completada")

# Eliminar una orden
order_book.remove_order(orden2.order_id)

# Guardar órdenes en un archivo
order_book.save_orders()
