class Perro(): #Por convenio el nombre de la clase va siempre en mayúsculas.
    def __init__(self, nombre, edad, peso): #Siempre empieza con esta función constructora.
        self.nombre = nombre
        self.edad = edad
        self.peso = peso
# Nos va a permitir crear instancias.
    
    def ladrar(self): # Siempre hay que poner como primer parámetro en la definición la clase entre ().
        if self.peso >= 8:
            print("GUAU, GUAU")
        else:
            print ("guau, guau")
    # para llamar a esta función hay que nombrar primero a la instancia: salchicho.ladrar()
    
    def __str__(self):
        return "Perro {}, edad: {}, peso: {}".format(self.nombre, self.edad, self.peso)
    
class PerroAsistencia(Perro): #Así decimos que la clase PerroAsistencia hereda de la clase Perro
    def __init__(self, nombre, edad, peso, amo):
        Perro.__init__(self, nombre, edad, peso)
        self.amo = amo
        self.__trabajando = False

    def __str__(self): #Sobreescribir un método
        return "Perro de asistencia {}, edad: {}, peso: {}, amo: {}".format(self.nombre, self.edad, self.peso, self.amo)

    def pasear(self):
            print("Ayudo a mi dueño {} a pasear".format(self.amo))
            
    def ladrar(self):
        if self.__trabajando:
            print("No puedo ladrar.")
        else:
            Perro.ladrar(self)
            
    def trabajando(self, valor = None):
        if valor == None:
            return self.__trabajando
        else:
            self.__trabajando = valor
    
    