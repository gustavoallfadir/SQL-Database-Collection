from tkinter import *  
from tkinter import messagebox
import sqlite3
from datetime import *


mes=datetime.now().strftime('_%h_%Y')
mes_actual=datetime.now().strftime('%h-%Y') 


#------------root------------------


root=Tk()
root.title("Datos del Personal")
root.geometry("+200+50")
root.resizable(0,0)
root.wm_attributes('-alpha', 0.7)

barraMenu=Menu(root) 
  
root.config(menu=barraMenu) 


#-----------variables globales---

idVar=StringVar()
nombreVar=StringVar()
direccionVar=StringVar()
telefonoVar=StringVar()
correoVar=StringVar()
cargoVar=StringVar()


#----------------------------COMANDOS-------------------------------------------



def salir():
    kill=messagebox.askyesno("Salir","¿Desea salir del programa?")
    if kill==True:
        root.destroy()


#----------------------------------------------------------------------
def conectar():
        
        conexion=sqlite3.connect("PERSONAL")
        cursor=conexion.cursor()


        try:
            
            cursor.execute('''
                CREATE TABLE DATOS_PERSONAL (
                ID INTEGER PRIMARY KEY AUTOINCREMENT,
                NOMBRE_EMPLEADO VARCHAR(50) NOT NULL,
                TELEFONO INTEGER(10),
                CORREO VARCHAR(50),
                DIRECCION VARCHAR(50),
                CARGO VARCHAR(20))
                ''')
            
            messagebox.showinfo("Conectar","Base de datos creada, conexión establecida")

        except:    
            messagebox.showinfo("Conectar","Conectado a la base de datos")




#----------------BORRAR CAMPOS------------------------------------------------

def borrar_campos():
    idVar.set("")
    nombreVar.set("")
    cargoVar.set("")
    direccionVar.set("")
    telefonoVar.set("")
    correoVar.set("")


def crear():
    
    datos=nombreVar.get(),telefonoVar.get(),correoVar.get(),direccionVar.get(),cargoVar.get()

    go=messagebox.askyesno("Crear nuevo registro","¿Quiere crear un nuevo registro con los datos proporcionados?")
    if go ==True:

        conexion=sqlite3.connect("PERSONAL")
        cursor=conexion.cursor()

        #Escribir en Datos
        try:
        
            cursor.execute('''INSERT INTO DATOS_PERSONAL VALUES (NULL,?,?,?,?,?)''',(datos))

            conexion.commit()
            
            messagebox.showinfo("Crear nuevo","Todos los datos han sido guardados existosamente") 

        except:
        
            messagebox.showwarning("Error","No se pudo insertar el registro en Datos")   




def busca_ID():
    conexion=sqlite3.connect("PERSONAL")
    cursor=conexion.cursor()
    check=0

    try:
        cursor.execute("SELECT * FROM DATOS_PERSONAL WHERE ID="+idVar.get())

        datos=cursor.fetchall()
        
        for var in datos:

            idVar.set(var[0])
            nombreVar.set(var[1])
            telefonoVar.set(var[2])
            correoVar.set(var[3])
            direccionVar.set(var[4])
            cargoVar.set(var[5])

    except:
        messagebox.showerror("Error","No se encontró el id")




def busca_nombre():

    conexion=sqlite3.connect("PERSONAL")
    cursor=conexion.cursor()

    
    cursor.execute('''SELECT * FROM DATOS_PERSONAL WHERE NOMBRE_EMPLEADO="'''+nombreVar.get()+'''"''')

    datos=cursor.fetchall()

    for var in datos:

        idVar.set(var[0])
        nombreVar.set(var[1])
        telefonoVar.set(var[2])
        correoVar.set(var[3])
        direccionVar.set(var[4])
        cargoVar.set(var[5])

    conexion.commit()



def actualizar():
    go=messagebox.askyesno("Actualizar","¿Desea actualizar el registro?")
    if go == True:

        conexion=sqlite3.connect("PERSONAL")
        cursor=conexion.cursor()

        datos=nombreVar.get(),telefonoVar.get(),correoVar.get(),direccionVar.get(),cargoVar.get()
        
        #DATOS
        try:
            cursor.execute('''UPDATE DATOS_PERSONAL SET NOMBRE_EMPLEADO=?,TELEFONO=?,CORREO=?,DIRECCION=?,CARGO=?'''+
            "WHERE ID="+idVar.get(),datos)

            conexion.commit()

            messagebox.showinfo("Actualizar","Todos los datos han sido actualizados con éxito")

        except:
            messagebox.showerror("Error","No se han podido actualizar los datos")


def eliminar():
    go=messagebox.askyesno("Eliminar registro","¿Desea eliminar el registro? Este cambio es irreversible")
    if go == True:

        conexion=sqlite3.connect("PERSONAL")
        cursor=conexion.cursor()

        try:
            cursor.execute('''DELETE FROM DATOS_PERSONAL WHERE ID='''+idVar.get())

            conexion.commit()

            messagebox.showinfo("Eliminar","Registro eliminado con éxito")

            borrar_campos()
        
        except:
            messagebox.showerror("Eliminar","Error al eliminar el registro")


def acerca_de():
    messagebox.showinfo("Interfaz de BBDD","Creado por Gustavo Allfadir\nTodos los derechos reservados.\n©2020")

 



#---------------Contenidos de los menus------------

menuBBDD=Menu(barraMenu, tearoff=0)

menuBBDD.add_command(label="Conectar/Crear Base de datos", command=lambda:conectar())

menuBBDD.add_command(label="Salir del programa", command=lambda:salir())

menuBorrar=Menu(barraMenu, tearoff=0)

menuBorrar.add_command(label="Borrar campos", command=lambda:borrar_campos())

menuCRUD=Menu(barraMenu, tearoff=0)
menuCRUD.add_command(label="Crear", command=lambda:crear())
menuCRUD.add_command(label="Busqueda de ID", command=lambda:busca_ID())
menuCRUD.add_command(label="Busqueda de Nombre", command=lambda:busca_nombre())
menuCRUD.add_command(label="Actualizar", command=lambda:actualizar())
menuCRUD.add_command(label="Borrar", command=lambda:borrar())


menuAyuda=Menu(barraMenu,tearoff=0)

menuAyuda.add_command(label="Acerca de...", command=lambda:acerca_de())


#----------------Textos de la barra de menu--------------

barraMenu.add_cascade(label="BBDD",menu=menuBBDD)
barraMenu.add_cascade(label="Borrar",menu=menuBorrar)
barraMenu.add_cascade(label="CRUD",menu=menuCRUD)
barraMenu.add_cascade(label="Ayuda",menu=menuAyuda)


#---------------------FRAME------------------------------------

frame=Frame(root, width=800, height=600)
frame.pack()


img_fondo=PhotoImage(file="DBbg.png")
fondo=Label(frame,image=img_fondo).place(x=-400,y=-300)




#------------------INTERFAZ GRAFICA---------------------------


#ID
IDtxt=Label(frame,text="ID:", font=(18))
IDtxt.grid(row=0, column=1, padx=10, pady=20, columnspan=1,sticky="e")

IDbox=Entry(frame,textvariable=idVar,width=25, font=(18))
IDbox.grid(row=0, column=2, padx=10, pady=20,columnspan=1)
 

#Nombre
nombretxt=Label(frame,text="Nombre:", font=(18))
nombretxt.grid(row=1, column=1, padx=10, pady=20, columnspan=1,sticky="e")

nombrebox=Entry(frame,textvariable=nombreVar,width=25, font=(18))
nombrebox.grid(row=1, column=2, padx=10, pady=20,columnspan=1)

#Telefono
telefonotxt=Label(frame,text="Teléfono:", font=(18))
telefonotxt.grid(row=2, column=1, padx=10, pady=20,columnspan=1,sticky="e")

telefonobox=Entry(frame,textvariable=telefonoVar,width=25, font=(18))
telefonobox.grid(row=2, column=2, padx=10, pady=20,columnspan=1)

#Correo
correotxt=Label(frame,text="Correo:", font=(18))
correotxt.grid(row=3, column=1, padx=10, pady=20,columnspan=1,sticky="e")

correobox=Entry(frame,textvariable=correoVar,width=25, font=(18))
correobox.grid(row=3, column=2, padx=10, pady=20,columnspan=1)

#Dirección
direcciontxt=Label(frame,text="Dirección:", font=(18))
direcciontxt.grid(row=4, column=1, padx=10, pady=20,columnspan=1,sticky="e")

direccionbox=Entry(frame,textvariable=direccionVar,width=25, font=(18))
direccionbox.grid(row=4, column=2, padx=10, pady=20,columnspan=1)


#Cargo
cargotxt=Label(frame,text="Cargo:", font=(18))
cargotxt.grid(row=5, column=1, padx=10, pady=20,columnspan=1,sticky="e")

cargobox=Entry(frame,textvariable=cargoVar,width=25, font=(18))
cargobox.grid(row=5, column=2, padx=10, pady=20,columnspan=1)




#-----------Botones--------------------


#Crear
botoncrear=Button(frame,text="Crear nuevo", font=(19),width=16,command=lambda:crear())
botoncrear.grid(row=7, column=1, padx=10,pady=20)

#Actualizar
botonactualizar=Button(frame,text="Actualizar", font=(19),width=16,command=lambda:actualizar())
botonactualizar.grid(row=8, column=1, padx=10,pady=20)


#Buscar
botonbuscaID=Button(frame,text="Buscar por ID", font=(19),width=16,command=lambda:busca_ID())
botonbuscaID.grid(row=7, column=2, padx=10,pady=20,columnspan=2)

botonbuscanombre=Button(frame,text="Buscar por nombre", font=(19),width=16,command=lambda:busca_nombre())
botonbuscanombre.grid(row=8, column=2, padx=10,pady=20,columnspan=2)

#Borrar campos
botonborrar_campos=Button(frame,text="Borrar campos", font=(19),width=16,command=lambda:borrar_campos())
botonborrar_campos.grid(row=7, column=4, padx=10,pady=20,columnspan=1)

#Eliminar
botoneliminar=Button(frame,text="Eliminar", font=(19),width=16,command=lambda:eliminar())
botoneliminar.grid(row=8, column=4, padx=10,pady=20)

#------------------Margenes---------------------

margenI=Frame(frame, width=0,height=0)
margenI.grid(row=0,column=0, rowspan=8,padx=20, pady=50,)

margenD=Frame(frame, width=0,height=0)
margenD.grid(row=0,column=5, rowspan=8,padx=20, pady=50,)



root.mainloop()