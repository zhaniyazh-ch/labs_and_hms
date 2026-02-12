with open("data.txt", "r", ) as file:
    content = file.read()
print(content)#1

with open("file.txt", "w")as file:
    for i in range(1, 11):
        file.write(str(i) + "\n")
with open("file.txt", "r")as file:
    content = file.read()
print(content)#2

names = ["zhaniya","asem","sholpan"]
with open("names.txt", "w") as file:
    for name in names:
        file.write(name + "\n")
with open("names.txt", "r") as file:
    for line in file:
        print(line.strip().capitalize())#3