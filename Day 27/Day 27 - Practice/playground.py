


# unlimited positional argument - args
def add(*args):
    ans = 0
    for n in args:
        ans += n
    print(ans)

add(4,5)

# many keyword arguments - **kwargs

def calculate(n,**kwargs):
    n += kwargs["add"]
    n *= kwargs["multiply"]
    print(n)



calculate(4,add=3,multiply=5)


class Car:

    def __init__(self,**kwargs):
        self.make = kwargs.get("make")
        self.model = kwargs.get("model")



my_car = Car(make="test",model="gtr")

print(my_car.make)