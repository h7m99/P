input_file = open("input.txt","r")


for line in input_file:
    data = line.rsplit()
    print(data)