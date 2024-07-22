import tkinter as tk


def main():

    window = tk.Tk()
    # Definición de resolución y que no sea ajustable la ventana
    window.geometry("800x600")
    window.resizable(False, False)

    # Sección con los datos del cliente y fecha
    frame_data = tk.Frame(
        window, width=800, height=100, bd=1, relief="solid", bg="gray"
    )
    frame_data.grid_propagate(False)  # Evita que el frame se ajuste al contenido
    frame_data.grid(row=0, column=0)

    # Label y entry dentro de frame_data

    # Etiqueta cliente
    client_label = tk.Label(frame_data, text="CLIENTE:")
    client_label.configure(bg="gray", pady=10, font=("Helvetica", 14, "bold"))
    client_label.grid(row=0, column=0, padx=10)

    # Entrada cliente
    client_entry = tk.Entry(frame_data, width=30, font=("Helvetica", 10, "bold"))
    client_entry.grid(row=0, column=1, padx=10)

    # Etiqueta fecha
    fecha_label = tk.Label(frame_data, text="FECHA: 26-08")
    fecha_label.configure(bg="gray", pady=10, font=("Helvetica", 10, "bold"))
    fecha_label.grid(row=1, column=0, padx=10, pady=5)

    # Sección pedidos
    frame_order = tk.Frame(window, width=800, height=500, bd=1, relief="solid")
    frame_order.grid_propagate(False)  # Evita que el frame se ajuste al contenido
    frame_order.grid(row=1, column=0, pady=2)

    # Lista que recibe pedidos en forma de dicts
    orders = []

    # Cantidad
    cant_label = tk.Label(frame_order, text="Cantidad")
    cant_label.grid(row=0, column=0, padx=15, pady=5)

    # Descripción
    desc_label = tk.Label(frame_order, text="Descripción")
    desc_label.grid(row=0, column=1, padx=120, pady=5)

    # Precio
    precio_label = tk.Label(frame_order, text="Precio")
    precio_label.grid(row=0, column=2, padx=50, pady=5)

    # Subtotal
    subtotal_label = tk.Label(frame_order, text="Subtotal")
    subtotal_label.grid(row=0, column=3, padx=50, pady=5)

    window.mainloop()


if __name__ == "__main__":
    main()
