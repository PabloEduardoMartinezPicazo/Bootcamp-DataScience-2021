def f1z():
    f1y()
def f2z():
    f2y()
a=2.2
b=1.1
from b.y import f2y
f2y()
from b.y import f1y
f1y()