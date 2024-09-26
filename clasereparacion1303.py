# CLASE
class reparacion1303:
    def __init__(self, ID1303, Fecha1303, IDrel1303, Desc1303, costorep1303, tiemporep1303,estadorep1303):
        self.ID1303 = ID1303
        self.Fecha1303 = Fecha1303
        self.IDrel1303 = IDrel1303
        self.Desc1303  =  Desc1303
        self.costorep1303  = costorep1303
        self.tiemporep1303  =  tiemporep1303
        self.estadorep1303  =  estadorep1303

# MOSTRAR
    def mostrar(self):
        print("ID: ", self.ID1303)
        print("Fecha: ", self.Fecha1303)
        print("ID de reloj: ", self.IDrel1303)
        print("Descripcion del problema: ", self.Desc1303)
        print("Costo de reparacion: ", self.costorep1303)
        print("Tiempo de reparacion: ", self.tiemporep1303)
        print("Estado de reparacion: ", self.estadorep1303)

# LISTA
    def clientes1303(self):
        clientes = ["Roberto", "Nicolas", "Janna", "Ariel", "Cesarin", "Dulce", "Micky"]
        print(clientes)
        for cli in clientes:
            print(cli)

# TUPLA   
    def Relojes1303(self):
        relojes = ("Santos", "Love", "Cartier" , "Sky", "FERNO" , "Mullian", "Venatto")
        print(relojes)
        for reloj in relojes:
            print(reloj)

# CONJUNTO   
    def Empleado1303(self):
        empleados = {"Rober", "Michael", "Orlando" , "Luis", "Saul" , "Sofia", "Lesly"}
        print(empleados)
        for empl in empleados:
            print(empl) 

# DICCIONARIO
    def dic_proveedor(self):
        proveedor = {
            "Proveedor 1": 21,
            "Proveedor 2": 50,
            "Proveedor 3": 43,
            "Proveedor 4": 10,
            "Proveedor 5": 89,
            "Proveedor 6": 121,
            "Proveedor 7": 34,
            
        }
        print(proveedor)
        for prov, rel in proveedor.items():
            print(f"{prov}, Cantidad de Relojes: {rel}")

    # REPARACION EXITOSA
    def repaexit(self):
        print("REPARACION CON EXITO")
        print("")

    # REPARACION SIN EXITO
    def repasinexit(self):
        print("REPARACION SIN EXITO")
        print("")
        
# Instancia la clase
dat1303 = reparacion1303(1902350, "26/09/2024", 401754,"Una manecilla del reloj no funciona.", 22000, "12 HORAS","Nuevo")

# Llama a las funciones
print("DATOS DE REPARACION")
print("")
dat1303.mostrar()
print("")
print("")
print("LISTA DE NUESTROS CLIENTES")
print("")
dat1303.clientes1303()
print("")
print("")
print("MODELOS DE RELOJES")
print("")
dat1303.Relojes1303()
print("")
print("")
print("EMPLEADOS")
print("")
dat1303.Empleado1303()
print("")
print("")
print("DICCIONARIO DE PROVEEDORES")
print("")
dat1303.dic_proveedor()
print("")
print("")
print("REPARACION OPERADA CON EXITO")
dat1303.repaexit()
print("REPARACION OPERADA SIN EXITO")
dat1303.repasinexit()


