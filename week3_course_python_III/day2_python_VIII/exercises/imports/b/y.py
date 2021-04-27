def f1y():
    f1x()
def f2y():
    f2x()
x="a"
y="b"
from a.x import f1x
print(f1x())
f1y()
from a.x import f2x
f2y()