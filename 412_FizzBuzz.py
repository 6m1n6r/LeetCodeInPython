def fizzbuzz(n):
    string = []
    for each in range(n):
        if each % 3 != 0 and each % 5 != 0:
            print each
        elif each % 3 == 0:
            print("Fizz")
        elif each % 5 == 0:
            print("Buzz")


n = input("please input number")
fizzbuzz(n)
