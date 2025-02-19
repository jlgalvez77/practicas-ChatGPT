from order_book import OrderBook
from order import Order

def main():
    order_book = OrderBook()
    order_book.load_orders()  # Cargar órdenes previas si existen

    while True:
        print("\n MENÚ PRINCIPAL")
        print("1. Crear una nueva orden")
        print("2. Mostrar todas las órdenes")
        print("3. Mostrar órdenes de compra")
        print("4. Mostrar órdenes de venta")
        print("5. Actualizar estado de una orden")
        print("6. Eliminar una orden")
        print("7. Generar reporte de órdenes completadas")
        print("8. Simulación de mercado")
        print("9. Guardar y salir")
        
        opcion = input("\nElige una opción: ")

        if opcion == "1":
            order_type = input("Tipo de orden (buy/sell): ").strip().lower()
            if order_type not in ["buy", "sell"]:
                print("Error: El tipo de orden debe ser 'buy' o 'sell'.")
                continue  # Volver al menú

            try:
                price = float(input("Precio: "))
                quantity = float(input("Cantidad: "))
                
                new_order = Order(order_type, price, quantity)  # Esto lanzará un error si es inválido
                order_book.add_order(new_order)
                print("Orden creada con éxito!")

            except ValueError as e:
                print(f"Error: {e}")
            except Exception as e:
                print(f"Error inesperado: {e}")

        elif opcion == "2":
            order_book.show_orders()

        elif opcion == "3":
            order_book.show_orders("buy")

        elif opcion == "4":
            order_book.show_orders("sell")

        elif opcion == "5":
            order_id = input("ID de la orden a actualizar: ")
            new_status = input("Nuevo estado (pendiente/completada/cancelada): ").strip().lower()
            order_book.update_order_status(order_id, new_status)

        elif opcion == "6":
            order_id = input("ID de la orden a eliminar: ")
            order_book.remove_order(order_id)

        elif opcion == "7":
            order_book.generate_report()

        elif opcion == "8":
            num_orders = int(input("Cantidad de órdenes a generar: "))
            interval = float(input("Tiempo entre órdenes (segundos): "))
            order_book.simulate_market(num_orders, interval)

        elif opcion == "9":
            order_book.save_orders()
            print("Órdenes guardadas. Saliendo del programa...")
            break

        else:
            print("Opción no válida. Inténtalo de nuevo.")

if __name__ == "__main__":
    main()