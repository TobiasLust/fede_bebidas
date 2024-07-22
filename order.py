import tkinter as tk
from tkinter import messagebox


def order_gui() -> dict:
    """Interfaz grafica para que el usuario pueda agregar un pedido a la factura
    contiene entrys para cantidad, producto, precio, subtotal.

    Returns:
        dict: {cantidad: int, producto: str, precio: float, subtotal: float}
    """
    # Inicialización de la ventana principal
    window = tk.Tk()
    window.geometry("800x600")
    window.resizable(False, False)

    # Definición de los widgets de entrada y sus etiquetas
    tk.Label(window, text="Cantidad").grid(row=0, column=0, padx=10, pady=5)
    cantidad_ent = tk.Entry(window)
    cantidad_ent.grid(row=0, column=1)

    tk.Label(window, text="Producto").grid(row=1, column=0, padx=10, pady=5)
    producto_ent = tk.Entry(window)
    producto_ent.grid(row=1, column=1)

    tk.Label(window, text="Precio").grid(row=2, column=0, padx=10, pady=5)
    precio_ent = tk.Entry(window)
    precio_ent.grid(row=2, column=1)

    subtotal = tk.Label(window, text=f"Subtotal: 0.0")
    subtotal.grid(row=2, column=3, padx=10, pady=5)

    def actualizar_subtotal(event=None):
        """Actualizar el valor de "subtotal" intentando convertir el valor de
        cantidad_val a int y precio_val a float."""
        try:
            cantidad_val = int(cantidad_ent.get())
            precio_val = float(precio_ent.get())
            subtotal.config(text=f"Subtotal: ${precio_val * cantidad_val:.2f}")
        except ValueError:
            subtotal.config(text="Subtotal: 0.0")

    # Bind para actualizar el subtotal cuando se cambien los valores de cantidad o precio
    cantidad_ent.bind("<KeyRelease>", actualizar_subtotal)
    precio_ent.bind("<KeyRelease>", actualizar_subtotal)

    def get_order() -> dict:
        """Generar un diccionario con la información obtenida de los entrys.
        Si todo está correcto, retorna el pedido en forma de diccionario y cierra la ventana.

        Raises:
            ValueError: Si no puede transformar cantidad_ent y precio_ent
                        o si producto_val está vacío.
        """
        try:
            cantidad_val = int(cantidad_ent.get())
            precio_val = float(precio_ent.get())
            producto_val = producto_ent.get()

            if not producto_val.strip():
                raise ValueError

            order = {
                "cantidad": cantidad_val,
                "producto": producto_val.strip().title(),
                "precio": precio_val,
                "subtotal": cantidad_val * precio_val,
            }

            window.order = order
            window.quit()
        except ValueError:
            messagebox.showinfo("Información", "¡Faltan rellenar campos!")

    # Botón para finalizar y obtener el pedido
    btn_final = tk.Button(window, text="FINALIZAR", command=get_order)
    btn_final.grid(row=3, column=1)

    window.order = None
    window.mainloop()
    return window.order
