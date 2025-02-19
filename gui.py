import tkinter as tk
from tkinter import ttk, messagebox
from order_book import OrderBook
from order import Order

class OrderBookGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Order Book - Crypto Trading")
        self.root.geometry("600x400")

        self.order_book = OrderBook()

        # Frame para ingresar órdenes
        self.frame_top = tk.Frame(self.root)
        self.frame_top.pack(pady=10)

        tk.Label(self.frame_top, text="Tipo (buy/sell):").grid(row=0, column=0)
        self.entry_type = tk.Entry(self.frame_top)
        self.entry_type.grid(row=0, column=1)

        tk.Label(self.frame_top, text="Precio:").grid(row=0, column=2)
        self.entry_price = tk.Entry(self.frame_top)
        self.entry_price.grid(row=0, column=3)

        tk.Label(self.frame_top, text="Cantidad:").grid(row=0, column=4)
        self.entry_quantity = tk.Entry(self.frame_top)
        self.entry_quantity.grid(row=0, column=5)

        self.btn_add_order = tk.Button(self.frame_top, text="Agregar Orden", command=self.add_order)
        self.btn_add_order.grid(row=0, column=6, padx=5)

        # Tabla de órdenes
        self.tree = ttk.Treeview(self.root, columns=("ID", "Tipo", "Precio", "Cantidad", "Estado"), show="headings")
        self.tree.heading("ID", text="ID")
        self.tree.heading("Tipo", text="Tipo")
        self.tree.heading("Precio", text="Precio")
        self.tree.heading("Cantidad", text="Cantidad")
        self.tree.heading("Estado", text="Estado")
        self.tree.pack(expand=True, fill="both")

        # Botones de acciones
        self.frame_bottom = tk.Frame(self.root)
        self.frame_bottom.pack(pady=10)

        self.btn_delete = tk.Button(self.frame_bottom, text="Eliminar Orden", command=self.delete_order)
        self.btn_delete.grid(row=0, column=0, padx=5)

        self.btn_report = tk.Button(self.frame_bottom, text="Generar Reporte", command=self.generate_report)
        self.btn_report.grid(row=0, column=1, padx=5)

        self.load_orders()

    def add_order(self):
        order_type = self.entry_type.get().strip().lower()
        try:
            price = float(self.entry_price.get())
            quantity = float(self.entry_quantity.get())
            new_order = Order(order_type, price, quantity)
            self.order_book.add_order(new_order)
            self.load_orders()
        except ValueError:
            messagebox.showerror("Error", "Precio y cantidad deben ser números.")

    def delete_order(self):
        selected_item = self.tree.selection()
        if not selected_item:
            messagebox.showerror("Error", "Seleccione una orden para eliminar.")
            return
        order_id = self.tree.item(selected_item, "values")[0]
        self.order_book.remove_order(order_id)
        self.load_orders()

    def generate_report(self):
        self.order_book.generate_report()
        messagebox.showinfo("Reporte", "Reporte generado y guardado.")

    def load_orders(self):
        """Carga las órdenes en la tabla"""
        for row in self.tree.get_children():
            self.tree.delete(row)
        for order in self.order_book.orders:
            self.tree.insert("", "end", values=(order.order_id, order.order_type, order.price, order.quantity, order.status))

if __name__ == "__main__":
    root = tk.Tk()
    app = OrderBookGUI(root)
    root.mainloop()
