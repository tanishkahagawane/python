def greet():
    print("hello")
    print("hello again")
    pass  #means doen't return any thing

greet()

#Variable scope: Local vs Global

def calculate_price():
    price = 100
    tax = price * 0.1
    print(f"Total: {price + tax}")

calculate_price()  # Total: 110

# This fails - price doesn't exist outside the function
# print(price)  # NameError: name 'price' is not defined


#################
counter = 0  # Global variable

def increment():
    global counter  # Declare we want to modify the global variable
    counter += 1

increment()
increment()
print(counter)  # 2

############
# return

def func(a,b):
    return a+b

print(func(a=10,b=20))