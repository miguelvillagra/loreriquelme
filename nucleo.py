#!/usr/bin/env python
from abc import ABCMeta, abstractmethod
class Empresa (metaclass=ABCMeta):
	'''Esta clase representa una abstracción de una empresa'''
	def __init__(self, nombre, dirección):
		self.nombre = nombre #String
		self.dirección = dirección #String
		pass
class Pinturería (Empresa) :
	'''Esta clase representa una abstracción de una pinturería'''
	def __init__(self, productos = [], clientes = []) :
		self.productos = productos 
		self.clientes  = clientes
		pass
class Producto :
	'''Esta clase representa una abstracción de productos'''
	def __init__(self, nombre, tipo, codigoProducto, precio, marca = []) :
		self.nombre = nombre #String
		self.tipo = tipo #String
		self.codigo_producto = codigo_producto #Number
		self.precio = precio #Number
		self.marca = marca 
		pass
class Pintura (Producto) :
	'''Esta clase representa una abstracción de pintura'''
	def __init__(self, producto, color=[], tamaño=[] ):
		self.color = color
		self.tamaño = tamaño #TamañoPintura[]
		self.producto =  producto #String
		pass
class AccesorioPintura (Producto) :
	'''Esta clase representa una abstracción de accesorio de pintura'''
	def __init__(self, producto) :
		self.producto = producto #String
		pass
class SistemaVenta :
	'''Esta clase representa una abstracción de sistema de ventas'''
	def __init__(self) :
		pass
	def vender_producto (self):
		# returns 
		pass
	def consultar_producto (self) :
		# returns 
		pass
	def aplicar_descuento (self) :
		# returns 
		pass
class Cliente :
	'''Esta clase representa una abstracción de cliente'''
	def __init__(self, cédula, nombre) :
		self.cédula = cédula #Number 
		self.nombre = nombre #String 
		pass
	def ComprarProductos (self) :
		# returns 
		pass
class ClienteNoRegistrado (Cliente) :
	'''Esta clase representa una abstracción de cliente no registrado'''
	def __init__(self, nroCompra, cliente, codigoCliente, nroTarjeta) :
		self.nro_compra = nro_compra #Number 
		self.cliente = cliente
		self.codigo_cliente = codigo_cliente#Number 
		self.nro_tarjeta = nro_tarjeta #Number 
		pass
class ClienteRegistrado :
	'''Esta clase representa una abstracción de cliente registrado'''
	def __init__(self, clienteNoRegistrado) :
		self.cliente_no_registrado = cliente_no_registrado #Number
		pass
