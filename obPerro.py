class Perro(): #Por convenio el nombre de la clase va siempre en mayúsculas.
    def _init_(self, nombre, edad, peso): #Siempre empieza con esta función constructora.
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
    
    def _str_(self):
        return "Perro {}, edad: {}, peso: {}".format(self.nombre, self.edad, self.peso)