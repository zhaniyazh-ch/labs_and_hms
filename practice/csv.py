with open("data.csv", "r")as file:
    content = file.read()
print(content)#1

with open("file.csv", "w")as file:
    for i in range(1, 11):
        file.write(str(i) + "\n")
with open("file.csv", "r") as file:
    content = file.read()
print(content)  # 2

names = ["zhaniya","asem","sholpan"]
with open("names.csv", "w") as file:
    for name in names:
        file.write(name + "\n")
with open("names.csv", "r") as file:
    for line in file:
        print(line.strip().capitalize())#3
