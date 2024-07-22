import tkinter as tk
from tkinter import messagebox


def order_gui() -> dict:
    """Interfaz grafica para que  el usuario pueda agregar un pedido a la factura
    contiene entrys para cantidad,producto,precio,subtotal.

    Returns:
        dict: {cantidad: int, producto: str, precio: float, subtotal: float}
    """
    # Init
    window = tk.Tk()
    # Definición de resolución y que no sea ajustable la ventana
    window.geometry("800x600")
    window.resizable(False, False)

    # Cliente entry
    cantidad = tk.Label(window, text="Cantidad")
    cantidad.grid(row=0, column=0, padx=10, pady=5)
    cantidad_ent = tk.Entry(window)
    # cantidad_ent.insert(0,0)
    cantidad_ent.grid(row=0, column=1)

    # Producto entry
    producto = tk.Label(window, text="Producto")
    producto.grid(row=1, column=0, padx=10, pady=5)
    producto_ent = tk.Entry(window)
    producto_ent.grid(row=1, column=1)

    # Precio entry
    precio = tk.Label(window, text="Precio")
    precio.grid(row=2, column=0, padx=10, pady=5)
    precio_ent = tk.Entry(window)
    # precio_ent.insert(0,0)
    precio_ent.grid(row=2, column=1)

    # Subtotal
    subtotal = tk.Label(window, text=f"Subtotal: 0.0")
    subtotal.grid(row=2, column=3, padx=10, pady=5)

    def actualizar_subtotal(event=None):
        """Actualizar el valor de "subtotal" intentando convertir el valor de
        cantidad_val a int y precio_val a float.

        Args:
            event Defaults to None.
        """
        try:
            cantidad_val = int(cantidad_ent.get())
            precio_val = float(precio_ent.get())
            subtotal.config(text=f"Subtotal: ${precio_val * cantidad_val:.2f}")
        except ValueError:
            subtotal.config(text="Subtotal: 0.0")

    # Bind para actualizar el valor de subtotal usando la funcion actualizar_subtotal()
    cantidad_ent.bind("<KeyRelease>", actualizar_subtotal)
    precio_ent.bind("<KeyRelease>", actualizar_subtotal)

    btn_final = tk.Button(window, text="FINALIZAR")

    # Obtener orden y salir de la ventana

    def get_order() -> dict:
        """Generar un diccionario con la informacion obtenida por los entrys.
        si esta todo correcto retorna en forma de dict el pedido y cierra la ventana

        Raises:
            ValueError: Si no puedo transformar cantidad_ent y precio_ent
            y si producto_val == ""

        Returns:
            dict:
                "cantidad": cantidad_val,
                "producto": producto_val.strip().title(),
                "precio": precio_val,
                "subtotal": cantidad_val * precio_val,
        """
        try:
            cantidad_val = int(cantidad_ent.get())
            precio_val = float(precio_ent.get())
            producto_val = producto_ent.get()

            if producto_val == "" or producto_val.isspace():
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
            messagebox.showinfo("Información", "Faltan rellenar campos!")

    btn_final.configure(command=get_order)
    btn_final.grid(row=3, column=1)

    window.order = None
    window.mainloop()
    return window.order
