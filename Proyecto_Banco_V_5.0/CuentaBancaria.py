from io import open
from datetime import date
from datetime import datetime,timedelta

import random



class CuentaBancaria():

	def __init__(self,nCuenta=" ",nombre=" ",apellido=" ",ciudad=" ",estatus=" ",saldo=500):
	        self.NumeroCuenta=nCuenta
	        self.Nombre=nombre
	        self.Apellido=apellido
	        self.Ciudad=ciudad	
	        self.Estatus=estatus
	        self.Saldo=saldo

	def registrarCuenta(self,nombreVN,apellidoVN,ciudadVN,saldoVN):
	 	if int(saldoVN)<500:
	 		messagebox.showerror("Registro de Cuenta", "El saldo inicial es inferior al mínimo")
	 	else:
	 		archivo = open("data/CuentasBanco.txt", "r")
	 		cadena = archivo.readlines()
	 		archivo.close()
	 		NuevoNum=random.randint(10000,49999)
	 		for i in range(len(cadena)):
	 			if cadena[i].split(",")[0]==NuevoNum:
	 				NuevoNum=randint(10000,49999)
	 		self.t_cuenta = NuevoNum
	 		DatosNuevo=str(self.t_cuenta)+","+str(nombreVN)+","+str(apellidoVN)+","+str(ciudadVN)+",Activa,"+str(saldoVN)+"\n"
	 		archivo = open("data/CuentasBanco.txt", "a")
	 		archivo.write(DatosNuevo)
	 		archivo.close()
	 		messagebox.showinfo("Registro de cuenta", "Cuenta registrada con éxito.")

	def RealizarDeposito(self, cuenta , valor):

	        
	        valor = int(valor)
	        archivo = open("data/CuentasBanco.txt", "r+")
	        cadena = archivo.readlines()
	        archivo.close()
	        for i in range(len(cadena)):
	            j = cadena[i].count(cuenta)
	            if j == 1:
	                break
	        if j==1:
	            if str(cadena[i].split(",")[4]) == "Activa":

	                saldoViejo = int(cadena[i].split(",")[5])
	                saldo_viejo = valor + saldoViejo

	                cadena[i] = cadena[i].replace("," + str(saldoViejo), "," + str(saldo_viejo), 1)

	                nuevaCadena = ""
	                for i in cadena:
	                    nuevaCadena = nuevaCadena + i

	                archivo = open("data/CuentasBanco.txt", "w")
	                archivo.write(nuevaCadena)
	                archivo.close()
	                self.enviar_depositoCuenta(cuenta,valor)
	                messagebox.showinfo("Deposito de dinero", "Deposito realizado con éxito.")
	            else:

	                saldoViejo = int(cadena[i].split(",")[5])
	                saldo_viejo = valor + saldoViejo

	                if  saldo_viejo > 500:
	                    cadena[i] = cadena[i].replace("," + str(saldoViejo), "," + str(saldo_viejo), 1)
	                    cadena[i] = cadena[i].replace("," + "Inactiva", "," + "Activa", 1)

	                    nuevaCadena = ""
	                    for i in cadena:
	                        nuevaCadena = nuevaCadena + i

	                    archivo = open("data/CuentasBanco.txt", "w")
	                    archivo.write(nuevaCadena)
	                    archivo.close()
	                    self.enviar_depositoCuenta(cuenta,valor)
	                    messagebox.showinfo("Deposito de dinero", "Deposito realizado con éxito.\nLa cuenta pasa a estar Activa")
	                else:
	                    saldoViejo = int(cadena[i].split(",")[5])
	                    saldo_viejo = valor + saldoViejo

	                    cadena[i] = cadena[i].replace("," + str(saldoViejo), "," + str(saldo_viejo), 1)

	                    nuevaCadena = ""
	                    for i in cadena:
	                        nuevaCadena = nuevaCadena + i

	                    archivo = open("data/CuentasBanco.txt", "w")
	                    archivo.write(nuevaCadena)
	                    archivo.close()
	                    self.enviar_depositoCuenta(cuenta,valor)
	                    messagebox.showinfo("Deposito de dinero", "Deposito realizado con éxito.\nLa cuenta sigue Inactiva")
	        else:
	            messagebox.showerror("Deposito de dinero", "La cuenta no existe")

	def enviar_depositoCuenta(self,cuenta,valor):
	 		registro = str(cuenta) + ',' + datetime.today().strftime('%m/%d/%y') + ',' + str(valor) + ',deposito'
	 		self.guardarEnArchivoTxt(registro)

	def guardarEnArchivoTxt(self, registro):
	        archivo = open('data/MovimientosCuentas.txt', 'a')
	        archivo.write(registro + '\n')
	        archivo.close()


	def RealizarRetiro(self, cuenta , valor):
	        valor = int(valor)
	        archivo = open("data/CuentasBanco.txt", "r+")
	        cadena = archivo.readlines()
	        archivo.close()
	        for i in range(len(cadena)):
	            j = cadena[i].count(cuenta)
	            if j == 1:
	                break
	        if j==1:
	            if str(cadena[i].split(",")[4]) == "Activa":
	                saldoViejo = int(cadena[i].split(",")[5])
	                estatus = cadena[i].split(",")[4]
	                saldo_viejo = saldoViejo - valor
	                if  saldo_viejo < 500:  #Si el saldo al retirar la cantidad no es menor al mínimo
	                    #messagebox.showerror("Retiro de dinero", "El saldo al retirar esa cantidad es menor al mínimo")
	                    cadena[i] = cadena[i].replace("," + str(saldoViejo), "," + str(saldo_viejo), 1)
	                    cadena[i] = cadena[i].replace("," + str(estatus), "," + "Inactiva", 1)

	                    nuevaCadena = ""
	                    for i in cadena:
	                        nuevaCadena = nuevaCadena + i

	                    archivo = open("data/CuentasBanco.txt", "w")
	                    archivo.write(nuevaCadena)
	                    archivo.close()
	                    self.enviar_retiroCuenta(cuenta,valor)
	                    messagebox.showinfo("Retiro de dinero", "Retiro realizado con éxito.\nCuenta pasa a estado Inactivo \npor Saldo Inferior al Minimo ")
	                else:    
	                    cadena[i] = cadena[i].replace("," + str(saldoViejo), "," + str(saldo_viejo), 1)

	                    nuevaCadena = ""
	                    for i in cadena:
	                        nuevaCadena = nuevaCadena + i

	                    archivo = open("data/CuentasBanco.txt", "w")
	                    archivo.write(nuevaCadena)
	                    archivo.close()
	                    self.enviar_retiroCuenta(cuenta,valor)
	                    messagebox.showinfo("Retiro de dinero", "Retiro realizado con éxito.")
	            else:
	                messagebox.showerror("Retiro de dinero", "La cuenta esta Inactiva")
	        else:
	            messagebox.showerror("Retiro de dinero", "La cuenta no existe")


	def enviar_retiroCuenta(self,cuenta,valor):
	        registro = str(cuenta) + ',' + datetime.today().strftime('%m/%d/%y') + ',' + str(valor) + ',retiro'
	        self.guardarEnArchivoTxt(registro)


            









            

            
            
                
                    
                          
            
            
            
            
            











                
        







