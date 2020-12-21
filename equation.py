
from tkinter import *
from tkinter import ttk

# Calcula coste de viaje

class Aplicacion():
    def __init__(self):
        self.raiz = Tk()
        self.raiz.title("Equacio de segon grau")
       
        # Declara variables de control
                          
        self.a = DoubleVar(value=1)
        self.b = DoubleVar(value=1)     
        self.c = DoubleVar(value=1)
        self.solu1 = DoubleVar(value=1)     
        self.solu2 = DoubleVar(value=1)

        # Carga imagen para asociar a widget Label()
       
        tren = PhotoImage(file='pi.png')  
       
        # Declara widgets de la ventana
            
        self.imagen1 = ttk.Label(self.raiz, image=tren,
                                 anchor="center")
        self.etiq1 = ttk.Label(self.raiz, text="ax^2 + bx + c = 0")



        
        self.etiq_a = ttk.Label(self.raiz, text="a:")
        self.qa = ttk.Entry(self.raiz, textvariable=self.a,
                              width=10)
        self.etiq_b = ttk.Label(self.raiz, text="b:")
        self.qb = ttk.Entry(self.raiz, textvariable=self.b,
                              width=10) 
        self.etiq_c = ttk.Label(self.raiz, text="c:")
        self.qc = ttk.Entry(self.raiz, textvariable=self.c,
                              width=10)       
      




        self.etiq_s1 = ttk.Label(self.raiz, text="Solucio 1:")       
        self.s1 = ttk.Label(self.raiz, textvariable=self.solu1,
                               foreground="yellow", background="black",
                               borderwidth=5, anchor="e")                               
        self.separ1 = ttk.Separator(self.raiz, orient=HORIZONTAL)
        
        self.etiq_s2 = ttk.Label(self.raiz, text="Solucio 2:")       
        self.s2 = ttk.Label(self.raiz, textvariable=self.solu2,
                               foreground="yellow", background="black",
                               borderwidth=5, anchor="e")                               
        self.separ1 = ttk.Separator(self.raiz, orient=HORIZONTAL)
        
        self.boton1 = ttk.Button(self.raiz, text="Calcular",
                                 command=self.calcular)
        self.boton2 = ttk.Button(self.raiz, text="Salir",
                                 command=quit)                                

        self.imagen1.pack(side=TOP, fill=BOTH, expand=True,
                          padx=10, pady=5)                                        
        self.etiq1.pack(side=TOP, fill=BOTH, expand=True,
                        padx=10, pady=5)
        self.etiq_a.pack(side=TOP, fill=BOTH, expand=True,
                        padx=10, pady=5)
        self.qa.pack(side=TOP, fill=BOTH, expand=True,
                        padx=10, pady=5)
        self.etiq_b.pack(side=TOP, fill=BOTH, expand=True,
                        padx=10, pady=5)
        self.qb.pack(side=TOP, fill=BOTH, expand=True,
                        padx=10, pady=5)
        self.etiq_c.pack(side=TOP, fill=BOTH, expand=True,
                        padx=10, pady=5)
        self.qc.pack(side=TOP, fill=BOTH, expand=True,
                        padx=10, pady=5)


        
        self.etiq_s1.pack(side=TOP, fill=BOTH, expand=True,
                        padx=10, pady=5)
        self.s1.pack(side=TOP, fill=BOTH, expand=True,
                        padx=20, pady=5)
        self.etiq_s2.pack(side=TOP, fill=BOTH, expand=True,
                        padx=10, pady=5)
        self.s2.pack(side=TOP, fill=BOTH, expand=True,
                        padx=20, pady=5)       
        self.separ1.pack(side=TOP, fill=BOTH, expand=True,
                         padx=5, pady=5)
        self.boton1.pack(side=LEFT, fill=BOTH, expand=True,
                         padx=10, pady=10)
        self.boton2.pack(side=RIGHT, fill=BOTH, expand=True,
                         padx=10, pady=10)               
        self.raiz.mainloop()
       
    def calcular(self):
       
        # Función para validar datos y calcular importe a pagar
       
        error_dato = False
        total = 0
        try:
            a = float(self.qa.get())
            b = float(self.qb.get())
            c = float(self.qc.get())
            
        except:
            error_dato = True
        if not error_dato:
            self.solu1.set(a)
            if(b<0):
                self.solu1.set("No té solució")
            else:
                self.solu1.set("No ho sé encara")
        else:
            self.solu1.set("¡ERROR!")
           
def main():
    mi_app = Aplicacion()
    return 0

if __name__ == '__main__':
    main()
