def f1x():
    print("hola")
def f2x():
    f2z()
x=2
y=1
print(f1x())
from b.c.z import f2z # si importo todo las funciones llamadas en la otra pagina se van a mostrar tambien porque importas todo, tendrias que importar solo la funcion
f2x()