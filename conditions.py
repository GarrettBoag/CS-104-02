# CS104
# Garrett Boag
# conditions.py

times = 0
amount_of_program = 0

print()
print("This program will tell you what type of cloths you should wear")
print("for the current weather")
print()

times = int(input("How many times would you like to run this program? :"))

while amount_of_program < times:
    print()
    temp = int(input("Please enter the current tempature :"))

    if (temp > 90):
        print("Wear Shorts")
    elif (temp > 70):
        print("Short Sleeves are Fine")
    elif (temp > 50):
        print("Wear a jacket")
    elif (temp > 32):
        print("Wear a heavy coat")
    else:
        print("Stay Inside")
    amount_of_program = amount_of_program + 1


    
    
