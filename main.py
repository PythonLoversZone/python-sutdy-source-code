def print_hi(name):
    a = "Hello" + name
    b = "Python"

    print("a + b 输出结果：", a + b)
    print("a * 2 输出结果：", a * 2)
    print("a[1] 输出结果：", a[1])
    print("a[1:4] 输出结果：", a[1:4])

    if "H" in a:
        print("H 在变量 a 中")
    else:
        print("H 不在变量 a 中")

    if "M" not in a:
        print("M 不在变量 a 中")
    else:
        print("M 在变量 a 中")

    print(r'\n')
    print(R'\n')
    print("My name is %s and weight is %d kg!" % ('Zara', 21))


class Person:
    name: str
    age: int
    __gender: int

    def say_hello(self):
        print("hello world")


if __name__ == '__main__':
    print_hi('PyCharm')
    x = Person
    x.name = "xiaomo"
    print(x.name)
