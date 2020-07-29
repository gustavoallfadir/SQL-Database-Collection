from tkinter import *  
from tkinter import messagebox
import sqlite3
from datetime import *


mes=datetime.now().strftime('_%h_%Y')
mes_actual=datetime.now().strftime('%h-%Y') 


#------------root------------------


root=Tk()
root.title("Base de datos Pagos")
root.geometry("+200+50")
root.resizable(0,0)
root.wm_attributes('-alpha', 0.7)

barraMenu=Menu(root) 
  
root.config(menu=barraMenu) 


#-----------variables globales---

idVar=StringVar()
nombreVar=StringVar()
cargoVar=StringVar()
sueldo_baseVar=StringVar()
faltasVAR=StringVar()
horas_extraVar=StringVar()
nominaVar=StringVar()
quin1Var=StringVar()
quin2Var=StringVar()
bonoVar=StringVar()
sueldo_totalVar=StringVar()




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
                CREATE TABLE PAGOS_PERSONAL'''+mes+''' (
                ID INTEGER PRIMARY KEY AUTOINCREMENT,
                NOMBRE_EMPLEADO VARCHAR(50) NOT NULL,
                CARGO VARCHAR(20) NOT NULL,
                CUENTA_NOMINA INTEGER(20) NOT NULL,
                SUELDO_BASE INTEGER(15),
                HORAS_EXTRA INTEGER(15),
                BONO INTEGER(15),
                PAGO_TOTAL INTEGER(15),
                PAGO1 BOOLEAN,
                PAGO2 BOOLEAN)
                ''')
            
            conexion.commit()

            messagebox.showinfo("Conectar","Se ha creado la base de datos PAGOS_PERSONAL"+mes_actual)

        except:
            messagebox.showinfo("Conectar","Base de datos existente, conexión establecida")
            


                
        
        if datos_creada==TRUE and control_creada==True and pagos_creada==True:

            messagebox.showinfo("Conectar","No se encontraron datos existentes. Bases de datos creadas con éxito")


#----------------BORRAR CAMPOS------------------------------------------------

def borrar_campos():
    idVar.set("")
    nombreVar.set("")
    cargoVar.set("")
    nominaVar.set("")
    sueldo_baseVar.set("")
    sueldo_totalVar.set("")
    faltasVAR.set("")
    horas_extraVar.set("")
    bonoVar.set("")
    quin1Var.set("")
    quin2Var.set("")
    



def crear():
    
        #listas para insertar
    pagos=nombreVar.get(),cargoVar.get(),nominaVar.get(),sueldo_baseVar.get()

    go=messagebox.askyesno("Crear nuevo registro","¿Quiere crear un nuevo registro con los datos proporcionados?")
    
    if go ==True:    
        
        conexion=sqlite3.connect("PERSONAL")
        cursor=conexion.cursor()


        #Escribir en pagos
        try:
            cursor.execute('''INSERT INTO PAGOS_PERSONAL'''+mes+'''  VALUES (NULL,?,?,?,?,NULL,NULL,NULL,NULL,NULL)''',(pagos))

            conexion.commit()
    
        except:

            messagebox.showwarning("Error","No se pudo insertar el registro")  
        


def busca_ID():

    conexion=sqlite3.connect("PERSONAL")
    cursor=conexion.cursor()



    cursor.execute('''SELECT * FROM PAGOS_PERSONAL'''+mes+''' WHERE ID='''+idVar.get())

    pagos=cursor.fetchall()

    for var in pagos:

        nombreVar.set(var[1])
        cargoVar.set(var[2])
        nominaVar.set(var[3])
        sueldo_baseVar.set(var[4])
        horas_extraVar.set(var[5])
        bonoVar.set(var[6])
        sueldo_totalVar.set(var[7])
        quin1Var.set([8])
        quin2Var.set(var[9])
            
            
        conexion.commit()



def busca_nombre():

    conexion=sqlite3.connect("PERSONAL")
    cursor=conexion.cursor()


    cursor.execute('''SELECT * FROM PAGOS_PERSONAL'''+mes+''' WHERE NOMBRE_EMPLEADO="'''+nombreVar.get()+'''"''')

    pagos=cursor.fetchall()

    for var in pagos:

        
        idVar.set(var[0])
        cargoVar.set(var[2])
        nominaVar.set(var[3])
        sueldo_baseVar.set(var[4])
        horas_extraVar.set(var[5])
        bonoVar.set(var[6])
        sueldo_totalVar.set(var[7])
        quin1Var.set(var[8])
        quin2Var.set(var[9])

    conexion.commit()

 


def actualizar():
    go=messagebox.askyesno("Actualizar","¿Desea actualizar el registro?")
    if go == True:

        conexion=sqlite3.connect("PERSONAL")
        cursor=conexion.cursor()

        pagos=nombreVar.get(),cargoVar.get(),nominaVar.get(),sueldo_baseVar.get(),horas_extraVar.get(),bonoVar.get(),sueldo_totalVar.get(), quin1Var.get(),quin2Var.get()

        #PAGOS
        try:
            cursor.execute('''UPDATE PAGOS_PERSONAL'''+mes+''' SET NOMBRE_EMPLEADO=?,CARGO=?,CUENTA_NOMINA=?,SUELDO_BASE=?, HORAS_EXTRA=?,BONO=?, PAGO_TOTAL=?,PAGO1=?,PAGO2=?'''+
            "WHERE ID="+idVar.get(),pagos)

            conexion.commit()

            messagebox.showinfo("Actualizar","Datos actualizados exitosamente")

        except:
            messagebox.showerror("Error","No se ha podido actualizar la información de Pagos")



def eliminar():
    messagebox.showerror("Eliminar registro","No tiene autorización para eliminar registros")
    """
    if go == True:

        conexion=sqlite3.connect("PERSONAL")
        cursor=conexion.cursor()

        try:
            cursor.execute('''DELETE FROM DATOS_PERSONAL WHERE ID='''+idVar.get())
            cursor.execute('''DELETE FROM CONTROL_PERSONAL'''+mes+''' WHERE ID='''+idVar.get())
            cursor.execute('''DELETE FROM PAGOS_PERSONAL'''+mes+''' WHERE ID='''+idVar.get())
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

#Bono
bonotxt=Label(frame,text="Bono mensual:", font=(18))
bonotxt.grid(row=1, column=3, padx=10, pady=20,columnspan=1,sticky="e")

bonobox=Entry(frame,textvariable=bonoVar,width=25, font=(18))
bonobox.grid(row=1, column=4, padx=10, pady=20,columnspan=1)



#-----------Segunda Columna-------------------------------------


#Nomina
nominatxt=Label(frame,text="Cta. de nómina:", font=(18))
nominatxt.grid(row=3, column=1, padx=10, pady=20, columnspan=1,sticky="e")

nominabox=Entry(frame,textvariable=nominaVar,width=25, font=(18))
nominabox.grid(row=3, column=2, padx=10, pady=20,columnspan=1)
 

#Sueldo base
sueldobasetxt=Label(frame,text="Sueldo base:", font=(18))
sueldobasetxt.grid(row=4, column=1, padx=10, pady=20, columnspan=1,sticky="e")

sueldobasebox=Entry(frame,textvariable=sueldo_baseVar,width=25, font=(18))
sueldobasebox.grid(row=4, column=2, padx=10, pady=20,columnspan=1)

#Pago quincena1
quincena1txt=Label(frame,text="Pago primera quincena:", font=(18))
quincena1txt.grid(row=2, column=3, padx=10, pady=20,columnspan=1,sticky="e")

quincena1box=Entry(frame,textvariable=quin1Var,width=25, font=(18))
quincena1box.grid(row=2, column=4, padx=10, pady=20,columnspan=1)

#Pago quincena2
quincena2txt=Label(frame,text="Pago segunda quincena:", font=(18))
quincena2txt.grid(row=3, column=3, padx=10, pady=20,columnspan=1,sticky="e")

quincena2box=Entry(frame,textvariable=quin2Var,width=25, font=(18))
quincena2box.grid(row=3, column=4, padx=10, pady=20,columnspan=1)


#Horas extra
extratxt=Label(frame,text="Horas extra este mes:", font=(18))
extratxt.grid(row=0, column=3, padx=10, pady=20,columnspan=1,sticky="e")

extrabox=Entry(frame,textvariable=horas_extraVar,width=25, font=(18))
extrabox.grid(row=0, column=4, padx=10, pady=20,columnspan=1)



#Pago total
totaltxt=Label(frame,text="Pago total "+mes_actual, font=(18))
totaltxt.grid(row=4, column=3, padx=10, pady=20,columnspan=1,sticky="e")

totalbox=Entry(frame,textvariable=sueldo_totalVar,width=25, font=(18))
totalbox.grid(row=4, column=4, padx=10, pady=20,columnspan=1)


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