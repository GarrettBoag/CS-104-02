#PythonQueue
#Garrett Boag

names = []


for i in range(10):
    add_name = input("Add name to queue")
    names.append(add_name)
    
print(names)

for i in range(10):
    print(names.pop(0))
