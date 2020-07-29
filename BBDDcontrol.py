from tkinter import *  
from tkinter import messagebox
import sqlite3
from datetime import *


mes=datetime.now().strftime('_%h_%Y')
mes_actual=datetime.now().strftime('%h-%Y') 


#------------root------------------


root=Tk()
root.title("Base de datos Control de Empleados")
root.geometry("+300+150")
root.resizable(0,0)
root.wm_attributes('-alpha', 0.7)

barraMenu=Menu(root) 
  
root.config(menu=barraMenu) 


#-----------variables globales---

idVar=StringVar()
nombreVar=StringVar()
cargoVar=StringVar()
faltasVAR=StringVar()
horas_extraVar=StringVar()





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
                CREATE TABLE CONTROL_PERSONAL'''+mes+''' (
                ID INTEGER PRIMARY KEY AUTOINCREMENT,
                NOMBRE_EMPLEADO VARCHAR(50) NOT NULL,
                CARGO VARCHAR(20),
                FALTAS VARCHAR(100),
                HORAS_EXTRA VARCHAR(5))
                ''')

            messagebox.showinfo("Conectar","Control de personal "+mes_actual+" creada exitosamente")

        except:

            messagebox.showinfo("Conectar","Conectado a CONTROL_PERSONAL"+mes) 

        
        conexion.commit()



#----------------BORRAR CAMPOS------------------------------------------------

def borrar_campos():
    idVar.set("")
    nombreVar.set("")
    cargoVar.set("")
    faltasVAR.set("")
    horas_extraVar.set("")
 

def crear():
    go=messagebox.askyesno("Crear nuevo","¿Desea crear nuevo registro con los datos ingresados?")
    if go == True:

        conexion=sqlite3.connect("PERSONAL")
        cursor=conexion.cursor()

        #listas para insertar
        control=nombreVar.get(),cargoVar.get()


    #Escribir en control   
        try:

            cursor.execute('''INSERT INTO CONTROL_PERSONAL'''+mes+''' VALUES (NULL,?,?,NULL,NULL)''',(control))
            conexion.commit()

            messagebox.showinfo("Crear registro","Registro nuevo creado exitosamente")
        
        except:
            messagebox.showerror("Error","No se pudo insertar el registro")     




def busca_ID():
    conexion=sqlite3.connect("PERSONAL")
    cursor=conexion.cursor()
    check=0

    try:
            
        cursor.execute('''SELECT * FROM CONTROL_PERSONAL'''+mes+''' WHERE ID='''+idVar.get())

        control=cursor.fetchall()
        
        for var in control:

            nombreVar.set(var[1])
            cargoVar.set(var[2])
            faltasVAR.set(var[3])
            horas_extraVar.set(var[4])
                    

        conexion.commit()
        check=check+1

    except:
        pass




def busca_nombre():

    conexion=sqlite3.connect("PERSONAL")
    cursor=conexion.cursor()

    cursor.execute('''SELECT * FROM CONTROL_PERSONAL'''+mes+''' WHERE NOMBRE_EMPLEADO="'''+nombreVar.get()+'''"''')

    control=cursor.fetchall()

    for var in control:

        idVar.set(var[0])
        cargoVar.set(var[2])
        faltasVAR.set(var[3])
        horas_extraVar.set(var[4])

    conexion.commit()

    #except:
        #messagebox.showerror("error","Nombre de empleado no encontrado")            
     #   pass


def actualizar():
    go=messagebox.askyesno("Actualizar datos","¿Desea actualizar el registro con los datos ingresados?")
    if go == True:

        conexion=sqlite3.connect("PERSONAL")
        cursor=conexion.cursor()


        control=nombreVar.get(),faltasVAR.get(),horas_extraVar.get()

        #CONTROL
        try:
            cursor.execute('''UPDATE CONTROL_PERSONAL'''+mes+''' SET NOMBRE_EMPLEADO=?,FALTAS=?,HORAS_EXTRA=?'''+
            '''WHERE ID='''+idVar.get(),control)

            conexion.commit()

            messagebox.showinfo("Actualizar","Información actualizada exitosamente")

        except:
            messagebox.showerror("Error","No se ha podido actualizar la información de Control")




def eliminar():

    messagebox.showerror("Acceso denegado","Sólo el manager puede eliminar registros")
"""
    conexion=sqlite3.connect("PERSONAL")
    cursor=conexion.cursor()


    try:
        cursor.execute('''DELETE FROM CONTROL_PERSONAL'''+mes+''' WHERE ID='''+idVar.get())

        conexion.commit()

        messagebox.showinfo("Eliminar","Registro eliminado con éxito")

        borrar_campos()
    
    except:
        messagebox.showerror("Eliminar","Error al eliminar el registro")
"""
 
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


#Cargo
cargotxt=Label(frame,text="Cargo:", font=(18))
cargotxt.grid(row=2, column=1, padx=10, pady=20,columnspan=1,sticky="e")

cargobox=Entry(frame,textvariable=cargoVar,width=25, font=(18))
cargobox.grid(row=2, column=2, padx=10, pady=20,columnspan=1)



#Faltas
faltastxt=Label(frame,text="Faltas este mes:", font=(18))
faltastxt.grid(row=3, column=1, padx=10, pady=20,columnspan=1,sticky="e")

faltasbox=Entry(frame,textvariable=faltasVAR,width=25, font=(18))
faltasbox.grid(row=3, column=2, padx=10, pady=20,columnspan=1)


#Horas extra
extratxt=Label(frame,text="Horas extra este mes:", font=(18))
extratxt.grid(row=4, column=1, padx=10, pady=20,columnspan=1,sticky="e")

extrabox=Entry(frame,textvariable=horas_extraVar,width=25, font=(18))
extrabox.grid(row=4, column=2, padx=10, pady=20,columnspan=1)




#-----------Botones--------------------


#Crear
botoncrear=Button(frame,text="Crear nuevo", font=(19),width=16,command=lambda:crear())
botoncrear.grid(row=7, column=1, padx=10,pady=20)

#Actualizar
botonactualizar=Button(frame,text="Actualizar", font=(19),width=16,command=lambda:actualizar())
botonactualizar.grid(row=8, column=1, padx=10,pady=20)


#Buscar
botonbuscaID=Button(frame,text="Buscar por ID", font=(19),width=16,command=lambda:busca_ID())
botonbuscaID.grid(row=7, column=2, padx=10,pady=20,columnspan=1)


botonbuscanombre=Button(frame,text="Buscar por nombre", font=(19),width=16,command=lambda:busca_nombre())
botonbuscanombre.grid(row=8, column=2, padx=10,pady=20,columnspan=1)

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