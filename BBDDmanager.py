from tkinter import *  
from tkinter import messagebox
import sqlite3
from datetime import *


mes=datetime.now().strftime('_%h_%Y')
mes_actual=datetime.now().strftime('%h-%Y') 


#------------root------------------


root=Tk()
root.title("Base de datos Manager")
root.geometry("+200+50")
root.resizable(0,0)
root.wm_attributes('-alpha', 0.7)

barraMenu=Menu(root) 
  
root.config(menu=barraMenu) 


#-----------variables globales---

idVar=StringVar()
nombreVar=StringVar()
cargoVar=StringVar()
direccionVar=StringVar()
telefonoVar=StringVar()
correoVar=StringVar()
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

        datos_creada=False
        control_creada=False
        pagos_creada=False

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
            

            datos_creada=TRUE
                        
        except:
            pass

        try:
            
            cursor.execute('''
                CREATE TABLE CONTROL_PERSONAL'''+mes+''' (
                ID INTEGER PRIMARY KEY AUTOINCREMENT,
                NOMBRE_EMPLEADO VARCHAR(50) NOT NULL,
                CARGO VARCHAR(20),
                FALTAS VARCHAR(100),
                HORAS_EXTRA VARCHAR(5))
                ''')
            

            control_creada=TRUE

        except:

            pass 

        
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
            
            pagos_creada=True

        except:
            
            pass

        conexion.commit()

                
        
        if datos_creada==TRUE and control_creada==True and pagos_creada==True:

            messagebox.showinfo("Conectar","No se encontraron datos existentes. Bases de datos creadas con éxito")

        elif control_creada==True:

            messagebox.showinfo("Conectar","Se ha actualizado la tabla de Control de personal para "+mes_actual)



        elif pagos_creada==True:

            messagebox.showinfo("Conectar","Se ha actualizado la tabla de Pagos de personal para "+mes_actual)


        else:

            messagebox.showinfo("Conectar","Bases de datos ya existentes")

        
        messagebox.showinfo("Conectar","Conexión con la base de datos establecida")




#----------------BORRAR CAMPOS------------------------------------------------

def borrar_campos():
    idVar.set("")
    nombreVar.set("")
    cargoVar.set("")
    direccionVar.set("")
    telefonoVar.set("")
    correoVar.set("")
    nominaVar.set("")
    sueldo_baseVar.set("")
    sueldo_totalVar.set("")
    faltasVAR.set("")
    horas_extraVar.set("")
    bonoVar.set("")
    quin1Var.set("")
    quin2Var.set("")
    




def crear():
    
    datos=nombreVar.get(),telefonoVar.get(),correoVar.get(),direccionVar.get(),cargoVar.get()

    control=nombreVar.get(),cargoVar.get()

    pagos=nombreVar.get(),cargoVar.get(),nominaVar.get(),sueldo_baseVar.get()


    go=messagebox.askyesno("Crear nuevo registro","¿Quiere crear un nuevo registro con los datos proporcionados?")
    if go ==True:    
        conexion=sqlite3.connect("PERSONAL")
        cursor=conexion.cursor()

        #listas para insertar


        check=0

        #Escribir en Datos
        try:
        
            cursor.execute('''INSERT INTO DATOS_PERSONAL VALUES (NULL,?,?,?,?,?)''',(datos))

            check=check+1   
            
        except:
            
            messagebox.showwarning("Error","No se pudo insertar el registro en Datos")   


        #Escribir en control   
        try:

            cursor.execute('''INSERT INTO CONTROL_PERSONAL'''+mes+''' VALUES (NULL,?,?,NULL,NULL)''',(control))
            
            check=check+1
        
        except:
            messagebox.showwarning("Error","No se pudo insertar el registro en Control")     


        #Escribir en pagos
        try:
            cursor.execute('''INSERT INTO PAGOS_PERSONAL'''+mes+'''  VALUES (NULL,?,?,?,?,NULL,NULL,NULL,NULL,NULL)''',(pagos))

            check=check+1

        except:
            messagebox.showwarning("Error","No se pudo insertar el registro en Pagos")  
        

        conexion.commit()

        if check==3:
            messagebox.showinfo("Crear nuevo","Todos los datos han sido guardados existosamente")  




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

        cursor.execute('''SELECT CARGO, FALTAS, HORAS_EXTRA FROM CONTROL_PERSONAL'''+mes+''' WHERE ID='''+idVar.get())

        control=cursor.fetchall()
       
        for var in control:

            cargoVar.set(var[0])
            faltasVAR.set(var[1])
            horas_extraVar.set(var[2])
                

        cursor.execute('''SELECT CUENTA_NOMINA, SUELDO_BASE, BONO, PAGO_TOTAL, PAGO1, PAGO2 FROM PAGOS_PERSONAL'''+mes+''' WHERE ID='''+idVar.get())

        pagos=cursor.fetchall()
       
        for var in pagos:

            nominaVar.set(var[0])
            sueldo_baseVar.set(var[1])
            bonoVar.set(var[2])
            sueldo_totalVar.set(var[3])
            quin1Var.set(var[4])
            quin2Var.set(var[5])

        conexion.commit()
        check=check+1

    except:
        pass

    if check==0:
        messagebox.showerror("Error","No se ha encontrado el ID")




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


    cursor.execute('''SELECT CARGO, FALTAS, HORAS_EXTRA FROM CONTROL_PERSONAL'''+mes+''' WHERE NOMBRE_EMPLEADO="'''+nombreVar.get()+'''"''')

    control=cursor.fetchall()

    for var in control:

        cargoVar.set(var[0])
        faltasVAR.set(var[1])
        horas_extraVar.set(var[2])
            

    cursor.execute('''SELECT CUENTA_NOMINA, SUELDO_BASE, HORAS_EXTRA, BONO, PAGO_TOTAL, PAGO1, PAGO2 FROM PAGOS_PERSONAL'''+mes+''' WHERE NOMBRE_EMPLEADO="'''+nombreVar.get()+'''"''')

    pagos=cursor.fetchall()

    for var in pagos:

        print(pagos)

        nominaVar.set(var[0])
        sueldo_baseVar.set(var[1])
        horas_extraVar.set(var[2])
        bonoVar.set(var[3])
        sueldo_totalVar.set(var[4])
        quin1Var.set(var[5])
        quin2Var.set(var[6])

    conexion.commit()

    #except:
        #messagebox.showerror("error","Nombre de empleado no encontrado")            
     #   pass


def actualizar():
    go=messagebox.askyesno("Actualizar","¿Desea actualizar el registro?")
    if go == True:

        conexion=sqlite3.connect("PERSONAL")
        cursor=conexion.cursor()

        datos=nombreVar.get(),telefonoVar.get(),correoVar.get(),direccionVar.get(),cargoVar.get()
        control=nombreVar.get(),cargoVar.get(),faltasVAR.get(),horas_extraVar.get()
        pagos=nombreVar.get(),cargoVar.get(),nominaVar.get(),sueldo_baseVar.get(),horas_extraVar.get(),bonoVar.get(),sueldo_totalVar.get(), quin1Var.get(),quin2Var.get()
        check=0

        #DATOS
        try:
            cursor.execute('''UPDATE DATOS_PERSONAL SET NOMBRE_EMPLEADO=?,TELEFONO=?,CORREO=?,DIRECCION=?,CARGO=?'''+
            "WHERE ID="+idVar.get(),datos)

            conexion.commit()

            check=check+1

        except:
            messagebox.showerror("Error","No se ha podido actualizar la información de Datos")

        #CONTROL
        try:
            cursor.execute('''UPDATE CONTROL_PERSONAL'''+mes+''' SET NOMBRE_EMPLEADO=?,CARGO=?,FALTAS=?,HORAS_EXTRA=?'''+
            '''WHERE ID='''+idVar.get(),control)

            conexion.commit()

            check=check+1

        except:
            messagebox.showerror("Error","No se ha podido actualizar la información de Control")


        #PAGOS
        try:
            cursor.execute('''UPDATE PAGOS_PERSONAL'''+mes+''' SET NOMBRE_EMPLEADO=?,CARGO=?,CUENTA_NOMINA=?,SUELDO_BASE=?, HORAS_EXTRA=?,BONO=?, PAGO_TOTAL=?,PAGO1=?,PAGO2=?'''+
            "WHERE ID="+idVar.get(),pagos)

            conexion.commit()

            check=check+1

        except:
            messagebox.showerror("Error","No se ha podido actualizar la información de Pagos")

        if check==3:
            messagebox.showinfo("Actualizar","Todos los datos han sido actualizados con éxito")


def eliminar():
    go=messagebox.askyesno("Eliminar registro","¿Desea eliminar el registro? Este cambio es irreversible")
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

#Bono
bonotxt=Label(frame,text="Bono mensual:", font=(18))
bonotxt.grid(row=6, column=1, padx=10, pady=20,columnspan=1,sticky="e")

bonobox=Entry(frame,textvariable=bonoVar,width=25, font=(18))
bonobox.grid(row=6, column=2, padx=10, pady=20,columnspan=1)



#-----------Segunda Columna-------------------------------------


#Nomina
nominatxt=Label(frame,text="Cta. de nómina:", font=(18))
nominatxt.grid(row=0, column=3, padx=10, pady=20, columnspan=1,sticky="e")

nominabox=Entry(frame,textvariable=nominaVar,width=25, font=(18))
nominabox.grid(row=0, column=4, padx=10, pady=20,columnspan=1)
 

#Sueldo base
sueldobasetxt=Label(frame,text="Sueldo base:", font=(18))
sueldobasetxt.grid(row=1, column=3, padx=10, pady=20, columnspan=1,sticky="e")

sueldobasebox=Entry(frame,textvariable=sueldo_baseVar,width=25, font=(18))
sueldobasebox.grid(row=1, column=4, padx=10, pady=20,columnspan=1)

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

#Faltas
faltastxt=Label(frame,text="Faltas este mes:", font=(18))
faltastxt.grid(row=4, column=3, padx=10, pady=20,columnspan=1,sticky="e")

faltasbox=Entry(frame,textvariable=faltasVAR,width=25, font=(18))
faltasbox.grid(row=4, column=4, padx=10, pady=20,columnspan=1)


#Horas extra
extratxt=Label(frame,text="Horas extra este mes:", font=(18))
extratxt.grid(row=5, column=3, padx=10, pady=20,columnspan=1,sticky="e")

extrabox=Entry(frame,textvariable=horas_extraVar,width=25, font=(18))
extrabox.grid(row=5, column=4, padx=10, pady=20,columnspan=1)



#Pago total
totaltxt=Label(frame,text="Pago total "+mes_actual, font=(18))
totaltxt.grid(row=6, column=3, padx=10, pady=20,columnspan=1,sticky="e")

totalbox=Entry(frame,textvariable=sueldo_totalVar,width=25, font=(18))
totalbox.grid(row=6, column=4, padx=10, pady=20,columnspan=1)


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