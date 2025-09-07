def c_to_f(c):
    return c * 9 / 5 + 32

def f_to_c(f):
    return (f - 32) * 5 / 9

choice = input("Convert (1) C→F or (2) F→C? ")
value = float(input("Enter value: "))

if choice == "1":
    print("Result:", round(c_to_f(value), 2), "F")
elif choice == "2":
    print("Result:", round(f_to_c(value), 2), "C")
else:
    print("Invalid choice")
