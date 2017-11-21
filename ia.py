
from metodos import Funciones, Operaciones, Util, Perceptron

"""
util = Util()

method_to_call = util.get_method_to_call(name = "satlins", fn = Funciones())

op = Operaciones()

x = [0.23, 0.71, 0.19, 0.52]
w = [[0.5, 0.3, 0.2], [0.6, -0.4, 0.1], [0.2, -0.3, 0.6], [0.7, 0.5, -0.2]]
b = [2, 3, 1]

y = method_to_call(op.suma(op.producto(x, w), b))
v = [[0.5, 0.3], [0.6, -0.4], [0.2, -0.3]]
c = [10, 5]

print(y)

method_to_call = util.get_method_to_call(name = "satlin")

z = method_to_call(op.suma(op.producto(y, v), c))

print(z)


"""

p = Perceptron()

a = []
a.append([[1, 1], 1])
a.append([[1, 0], 1])
a.append([[0, 1], 1])
a.append([[0, 0], 0])

p.proceso(a)