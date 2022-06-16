from Interfazpintura import InterfazPintura

class ControladorProducto(object):
	"""docstring for ControladorProducto"""
	def __init__(self):
		self.interfazpintura = InterfazPintura()
	def procesar_gestion(self): 
		opcion = input("Seleccione una opcion: \n 1 - Gestionar compra \n 0 - Salir \n ")
		self.interfazpintura.elegir_opcion(
			lambda: print("Seleccionó la opcion:" + opcion ))

		while  opcion == "1":

			print("Gestionar compra")
			producto = input("Introducir nombre del producto:")
			precio = input("Introducir precio del producto:")	
			opcion = input("Desea cargar otro producto?: \n 1 - Si \n 0 - No \n ")

			if opcion == "0":

				print("Seleccionó la opción continuar")
				opcion = input('''Seleccione una opcion: \n 1 - Consultar cedula \n 2 - Registrar cliente \n 3 - Borrar cliente \n 4 - Consultar sin registro \n 5 - Salir \n ''')
				#print("Seleccionó la opcion:", + opcion)
				self.interfazpintura.elegir_opcion(
					lambda: print("Seleccionó la opcion:" + opcion ))
				if opcion == "1":
					input("Introducir numero de cedula")	
				if opcion == "2":
					print("Proceder a registrar cliente")
					cedula= input("Introducir cedula del cliente:")
					nombre= input("Introducir nombre del cliente:")
					apellido= input("Introducir apellido del cliente:")
				if opcion == "3":
					print("Borrado exitoso")
				if opcion == "4":
					print("Proceder a consultar sin registro")
				if opcion == "5":
					print("Salir")
			if opcion != "1" and  opcion !="0":
				print("Intentelo de nuevo")
				
