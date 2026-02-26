import tkinter as tk
import sympy as sp

#Crear la venatana principal
root = tk.Tk()
root.title("Ecuaciones Diofanticas")
root.geometry("1080x720")

#Crear los labels y entradas para los coeficientes
label_a = tk.Label(root, text="Coeficiente a:")
label_a.pack()
entry_a = tk.Entry(root)
entry_a.pack()

label_b = tk.Label(root, text="Coeficiente b:")
label_b.pack()
entry_b = tk.Entry(root)
entry_b.pack()

label_c = tk.Label(root, text="Coeficiente c:")
label_c.pack()
entry_c = tk.Entry(root)
entry_c.pack()

label_ecuacion = tk.Label(root, text="Ecuación: ax + by = c")
label_ecuacion.pack()

#Crear el botón para resolver la ecuación


def resolver_ecuacion():
    a = int(entry_a.get())
    b = int(entry_b.get())
    c = int(entry_c.get())
    
    #Obtener r y s del teorema de Bezout
    r, s, d = sp.gcdex(a, b)
    benzout_label.config(text=f"Teorema de Bezout: r = {r}, s = {s}, d = {d}")
    
    #Solucion: x = a + t*(b/d), y = b - t*(a/d)
    t = sp.symbols('t')
    x = r + t * (b // d)
    y = s - t * (a // d)
    solucion = f"x = {x}, y = {y}"
    
    resultado_label.config(text=f"Solución: {solucion}")


benzout_label = tk.Label(root, text="")
benzout_label.pack()
resultado_label = tk.Label(root, text="")
resultado_label.pack()
resolver_button = tk.Button(root, text="Resolver", command=resolver_ecuacion)
resolver_button.pack()

#Calcular el inverso de x en modulo n

label_x = tk.Label(root, text="Valor de x (inverso):")
label_x.pack()
entry_x = tk.Entry(root)
entry_x.pack()

label_n = tk.Label(root, text="Valor de n (módulo):")
label_n.pack()
entry_n = tk.Entry(root)
entry_n.pack()


def calcular_inverso():
    x = int(entry_x.get())
    n = int(entry_n.get())
    
    inverso = sp.mod_inverse(x, n)
    inverso_label.config(text=f"{inverso}")
  
    
inverso_label = tk.Label(root, text="")
inverso_label.pack()
inverso_button = tk.Button(root, text="Calcular Inverso", 
                           command=calcular_inverso)
inverso_button.pack()

#Iniciar el bucle principal de la aplicación
root.mainloop()
