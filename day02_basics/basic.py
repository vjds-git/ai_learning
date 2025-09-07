# variables & types
name = "VJ"            # str
age = 34                 # int
height_m = 1.68          # float
is_learning = True       # bool

print(type(name), type(age), type(height_m), type(is_learning))

#input/output (uncomment to try)
user = input("Your name: ")
print("Hello,", user)

# arithmetic & f-strings
years = 5
print(f"In {years} years, {name} will be {age + years}")

# lists & loops
skills = ["python", "git", "docker"]
for s in skills:
    print("skill:", s.upper())

# dictionaries (key/value) + conditionals
person = {"name": name, "age": age, "city": "Toronto"}
if person["age"] > 30:
    print("30+ club!")

# functions (reusable blocks)
def bmi(height_m: float, weight_kg: float) -> float:
    return round(weight_kg / (height_m**2), 2)

print("BMI sample:", bmi(1.68, 68))
