# Generators
def generator(n):
    for i in range(n):
        yield (i+1)**2

numbers = generator(5)
for number in numbers:
    print(f"{number}")

for number in numbers:
    print(number)


#Using *args, **kwargs
def summarise(*args):
    total = sum(args)
    print(f"Count : {len(args)} | Total : {total} | Average : {(total/len(args)):.2f}")
summarise(5,4,6,2,6,7,1,34,8,7)


def create_profile(**kwargs):
    for key, value in kwargs.items():
        print(f"{key:<15} : {value}")
        
print(f"=== Profile ===")
create_profile(name="Manan", university="LUT", goal="ML engineer", phase="1")



#Context managers

phases = ["Setup", "Python & Git", "Data Fluency", "Classical ML"]
hours = [10, 36, 54, 72]

with open("hours.txt", "w") as f:
    for phase, hour in zip(phases, hours):
        f.write(f"{phase}: {hour} hrs\n")

with open("hours.txt","r") as f:
    lines = f.readlines()
    for line in lines: print(line.strip())


#working with paths

from pathlib import Path

p = Path("hours.txt")
if p.exists():
    print(f"{p.read_text()}")
    print(f"\nFile name: {p.name}, Stem : {p.stem}, Suffix : {p.suffix}")
else:
    print("File does not exist!!")

folder = Path(".")
for file in folder.glob("*.py"):
    print(f"{file.name}")


# Generators
import time

def timer(func):
    def inner(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        print(f"finished in {end - start:.4f} seconds")
        return result
    return inner

@timer
def count_up(n):
    total = 0
    for i in range(n):
        total += i
    return total

result = count_up(1000000)