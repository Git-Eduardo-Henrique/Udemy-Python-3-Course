import aula096_099_package
from aula096_099_package import module
from aula096_099_package.module import somar

print("Este é o modulo: ", __name__)
print(100 * "=")

print("Usando função do modulo:")
print(module.somar(2, 2))
print(somar(21, 21))

print(100 * "=")
print("Usando função do __init__:")
print(f"dobro de 2: {aula096_099_package.dobrar(2)}")
print(100 * "=")