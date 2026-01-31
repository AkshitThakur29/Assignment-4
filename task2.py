data = input("enter the text :")
with open('output.txt','wt') as file:
    file.write(data + '\n')

data2 = input("enter additional text :")
with open('output.txt','at') as file:
    file.write(data2 + '\n')

print("final content of file is :")
with open('output.txt','rt') as file:
    print(file.read())
