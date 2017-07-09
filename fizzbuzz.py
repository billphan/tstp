# A python program called FizzBuzz. Returns Fizz if multiple of 3 and Buzz if multiple of 5. Print FizzBuzz for multiples of both 3 and 5.

def fizz_buzz():
    for i in range(1, 101):
        if i % 3 == 0 and i % 5 == 0:
            print("FizzBuzz")
        elif i % 3 == 0:
            print("Fizz")
        elif i % 5 == 0:
            print("Buzz")
        else:
            print(i)
