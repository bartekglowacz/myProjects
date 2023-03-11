import math

variables = {'a': 2, 'b': 5, 'sin': math.sin}
result = eval('sin(a) + sin(b)', variables)
a = eval("sin(a)", variables)
print(f"{a = }")
print(result)
