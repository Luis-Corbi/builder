class Vehiculo:
    def __init__(self, builder):
        self.tipo = builder.tipo
        self.marca = builder.marca
        self.modelo = builder.modelo
        self.color = builder.color
        self.año = builder.año
    
    def __str__(self):
        return f"Tipo: {self.tipo}\nMarca: {self.marca}\nModelo: {self.modelo}\nColor: {self.color}\nAño: {self.año}\n"

class VehiculoBuilder:
    def __init__(self):
        self.tipo = None
        self.marca = None
        self.modelo = None
        self.color = None
        self.año = None

    def whit_tipo(self, tipo):
        self.tipo = tipo
        return self

    def whit_marca(self, marca):
        self.marca = marca
        return self

    def whit_modelo(self, modelo):
        self.modelo = modelo
        return self

    def whit_color(self, color):
        self.color = color
        return self

    def whit_año(self, año):
        self.año = año
        return self

    def build(self):
        return Vehiculo(self)

vehiculo1 = VehiculoBuilder().whit_tipo("Auto").whit_marca("Toyota").whit_modelo("Corolla").whit_color("Azul").whit_año(2023).build()

vehiculo2 = VehiculoBuilder().whit_tipo("Auto").whit_marca("Audi").whit_modelo("RS5").whit_color("Negro").whit_año(2023).build()

vehiculo3 = VehiculoBuilder().whit_tipo("Moto").whit_marca("Honda").whit_modelo("CB300F").whit_color("Rojo").whit_año(2023).build()

print("Vehiculo 1")
print(vehiculo1)

print("Vehiculo 2")
print(vehiculo2)

print("Vehiculo 3")
print(vehiculo3)