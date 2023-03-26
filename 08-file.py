file = open("brands.txt", "w+")

brands = {"mazda": "CX-9", "Ford": "Fiesta"}

for k, v in brands.items():
    file.write(k + " " + v)
    file.write("\n")

file.close()

# read file

file = open("brands.txt")

for line in file.readlines():
    print(line.strip())

file.close()
