def jijyo():
    x = input("type a number")
    x = int(x)
    return x**2

print(jijyo())


def print_string(string):
    print (string)
print_string("test:1,2,3")


def add_it(x, y, z, a=10, b=100):
    return x+y+z+a+b
result = add_it(2, 3, 4, 5, 6)
print(result)


def devide(x):
    return x//2

def multiply(x):
    return x*4

a = devide(11)
b = multiply(a)
print(b)


def convert():
    try:
        x = input("input a number:")
        x = float(x)
        print(x)
    except(ValueError):
        print("不正入力です")

convert()

print("ここまで。2020年1月5日")

