#Luis Arturo Nicolas Bernal
from abc import ABC, abstractmethod

class Empleado_L12(ABC):
    def __init__(self, rfc, apellidos, nombres):
        self.rfc = rfc
        self.apellidos = apellidos
        self.nombres = nombres

    def mostrar(self):
        return f"{self.nombres} {self.apellidos} ({self.rfc})"

    @abstractmethod
    def sueldo_neto(self):
        pass

class EmpleadoVendedor_L12(Empleado_L12):
    def __init__(self, rfc, apellidos, nombres, monto_vendido, tasa_comision):
        super().__init__(rfc, apellidos, nombres)
        self.monto = monto_vendido
        self.tasa = tasa_comision
        if self.ingresos() < 150:
            raise SalarioInvalidoExceptionL12("Ingreso menor al mínimo que es 150")

    def ingresos(self):
        return self.monto * self.tasa

    def bonificacion(self):
        if self.monto < 1000: return 0
        elif self.monto <= 5000: return self.ingresos()*0.05
        else: return self.ingresos()*0.10

    def descuentos(self):
        return self.ingresos()*(0.11 if self.ingresos() < 1000 else 0.15)

    def sueldo_neto(self):
        return self.ingresos()+self.bonificacion()-self.descuentos()


class EmpleadoPermanente_L12(Empleado_L12):
    def __init__(self, rfc, apellidos, nombres, sueldo_base, nss):
        super().__init__(rfc, apellidos, nombres)
        self.base = sueldo_base
        self.nss = nss
        if self.base < 150:
            raise SalarioInvalidoExceptionL12("Tu sueldo base  es menor al mínimo que es de 150")


    def descuentos(self):
        return self.base * 0.11
    def sueldo_neto(self):
        return self.ingresos() - self.descuentos()
    def ingresos(self):
        return self.base

if __name__ == "__main__":
    empleados = [
        EmpleadoVendedor_L12("nib2", "Bernal", "Luis", 120, 0.1), EmpleadoPermanente_L12("meb", "Martinez", "Miriam", 21, "nss77") ]

class SalarioInvalidoExceptionL12(Exception):
    pass

    total = 0
    for e in empleados:
        print(f"{e.mostrar()} Neto: {e.sueldo_neto():.2f}")
        total += e.sueldo_neto()

    print(f"Total planta: {total:.2f}")
