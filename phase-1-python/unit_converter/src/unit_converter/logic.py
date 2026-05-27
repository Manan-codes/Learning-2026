def temp_converter(temp: float, choice: int) -> None | float:
    """Takes in Temperature in Celsius or Fahrenheit and returns in converted units"""
    if choice == 1:
        return (temp * 9/5) + 32
    elif choice == 2: 
        return (temp - 32) * 5/9
    else:
        print("Invalid choice!")
        return None    



def distance_converter():
    """Converts Distance into chosen unit, prints the results"""
    option = int(input("Choose your option:"
    "\n1. Feet to Meters"
    "\n2. Meters to Kilometers"
    "\n3. Kilometers to Meters"
    "\n4. Meters to Feet"))

    dist = float(input("Enter Distance: "))
    match option:
        case 1:
            print(f"{dist} feet is {dist/3.281:.2f} Meters")
        case 2:
            print(f"{dist} Meters is {dist/1000:.2f} Kilometers")
        case 3:
            print(f"{dist} Kilometers is {dist*1000:.2f} Meters")
        case 4:
            print(f"{dist} Meters is {dist*3.281:.2f} Feet")



def weight_converter(weight: float, choice: int) -> float | None :
    """Takes in weight in Kgs or Lbs and returns other in other units"""
    if choice == 1:
        return weight*2.205  # approximate conversion
    elif choice == 2:
        return weight/2.205
    else:
        print("Invalid choice!")
        return None



if __name__ == "__main__":
    print("=== Welcome to the Unit Converter ===")
    while (1):
        try: 
            option = int(input("Enter the option you want to choose:" \
            "\n1. Convert Temperature" \
            "\n2. Convert Distance" \
            "\n3. Convert Weight" \
            "\n0. Exit Program\n"))
        except:
            print("Invalid!!! Enter an Integer!\n")
            continue

        match option:
            case 1:
                print("\n== Converting Temperature ==")
                choice = int(input("Choose your option:"
                "\n1. Celsius to Fahrenheit"
                "\n2. Fahrenheit to Celsius\n"))
                temp = float(input("Enter Temperature: "))
                result = temp_converter(temp, choice)
                if choice == 1:
                    print(f"Temperature in Fahrenheit: {result:.2f}")
                elif choice == 2:
                    print(f"Temperature in Celsius: {result:.2f}")



            case 2: 
                print("\n== Converting Distance ==")
                distance_converter()

            case 3: 
                print("\n== Converting Weight ==")
                choice = int(input("Choose your option:" \
                "\n1. Kilograms to Pounds" \
                "\n2. Pounds to Kilograms\n"))
                weight = float(input("Enter Weight: "))
                
                result = weight_converter(weight, choice)

                if choice == 1:
                    print(f"Converted value: {result:.2f} lbs")
                    print("\n")
                elif choice == 2:
                    print(f"Converted value: {result:.2f} kgs")
                    print("\n")


            case 0:
                print("Exiting program...")
                break
