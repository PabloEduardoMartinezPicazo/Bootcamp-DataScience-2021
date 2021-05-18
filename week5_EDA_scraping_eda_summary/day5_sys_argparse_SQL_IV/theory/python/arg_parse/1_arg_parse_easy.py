import argparse
from my_module import exponent 

parser = argparse.ArgumentParser()
parser.add_argument("-x", "--x", type=int, help="the base")
parser.add_argument("-y", "--y", type=int, help="the exponent", required=True) #required obligatorio
parser.add_argument("-v", "--v", default=0, type=int, help="the result will be multiplied by 'v'")
args = vars(parser.parse_args())

print("####################\n")
print(type(args))
print(args)

v = args["v"]
y = args["y"]
x = args["x"]
print("x:", x)
print("y:", y)
print("z:", z)
