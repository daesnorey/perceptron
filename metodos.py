import random

class Funciones(object):

    def __init__(self):
        pass
    
    def hardlim(self, matrix):
        print("hardlim")
        resultado = []
        for x in matrix:
            if x < 0:
                resultado.append(0)
            else:
                resultado.append(1)

        return resultado

    def hardlims(self, matrix):
        print("hardlims")
        resultado = []
        for x in matrix:
            if(x < 0):
                resultado.append(-1)
            else:
                resultado.append(1)

        return resultado

    def poslin(self, matrix):
        print("poslin")
        resultado = []
        for x in matrix:
            if(x < 0):
                resultado.append(0)
            else:
                resultado.append(x)

        return resultado

    def purelin(self, matrix):
        print("purelin")
        resultado = []
        for x in matrix:
            resultado.append(0)

        return resultado
        
    def satlin(self, matrix):
        print("satlin")
        resultado = []
        for x in matrix:
            if x < 0:
                resultado.append(0)
            elif x > 1:
                resultado.append(1)
            else:
                resultado.append(x)

        return resultado

    def satlins(self, matrix):
        print("satlins")
        resultado = []
        for x in matrix:
            if x < -1:
                resultado.append(-1)
            elif x > 1:
                resultado.append(1)
            else:
                resultado.append(x)

        return resultado

class Operaciones(object):

    def __init__(self):
        pass

    def producto(self, input, w):
        print("inicia producto")

        resultado = []

        size_x = len(w)
        size_y = len(w[0])

        for y in range(size_y):
            resultado.append(0)
            for x in range(size_x):
                resultado[y] += input[x] * w[x][y]

            resultado[y] = round(resultado[y], 2)
        print(resultado)

        return resultado

    def suma(self, i1, i2):
        print("inicia suma")
        
        resultado = []
        
        for i in range(len(i1)):
            valor = i1[i] + i2[i]
            resultado.append(round(valor, 2))
        
        print(resultado)

        return resultado

class Util:

    def __init__(self):
        pass

    def get_method_to_call(self, name, fn = False):
        if fn is not False:
            self.fn = fn
        
        return getattr(self.fn, name)

class Perceptron(object):
    """
    Clase encargada de validar ...
    """

    def __init__(self):
        self.W = []
        self.b = 0

    def proceso(self, datos, pesos=None, b=None):
        print("datos", datos)
        if len(datos) > 0 and len(datos[0]):
            size = len(datos[0][0])
        else:
            raise ValueError("No se informaron datos")

        if not pesos or not b:
            self.calcula_pesos(tam=size)
        else:
            self.W = pesos
            self.b = b

        cont = 0
        for i in range(len(datos)):
            p = datos[i]
            valores = p[0]
            esperado = p[1]
            while True:
                valor = self.evalua(valores)
                print("valor", valor)
                e = self.valida_hardlim(valor, esperado)
                print("error", e)
                if e != 0:
                    print "-"
                    self.calcula_pesos(size, valores, e)
                    cont += 1
                else:
                    break
            if cont > 100:
                break
            print "-" * 150
            print "-" * 150
        print("cont", cont)

    def calcula_pesos(self, tam=2, valores=[], e=0):
        if not self.W:
            for i in range(tam):
                self.W.append(self.obtiene_n_aleatorio())
            self.b = self.obtiene_n_aleatorio()
        else:
            __matriz = []
            for i in range(len(valores)):
                __matriz.append(valores[i] * e)

            for i in range(len(__matriz)):
                self.W[i] = self.W[i] + __matriz[i]

            self.b = self.b + e

        print("calcula_pesos", self.W, self.b, valores)

    def obtiene_n_aleatorio(self):
        return random.uniform(-1, 1)

    def evalua(self, valores):
        print("evalua", "valores", valores)
        valor = 0
        for i in range(len(valores)):
            valor += self.W[i] * valores[i]
        valor += self.b
        print("evalua", "valor", valor)
        return valor

    def valida_hardlim(self, n, esperado):
        f = Funciones().hardlim([n])[0]
        print("f>hardlim", f, esperado)
        return esperado - f

    def valida_hardlims(self, n, esperado):
        f = Funciones().hardlims([n])[0]
        return esperado - f