# A2 - Read the file 'austen.txt' and print the amount of lines in the file

fname = input("Enter file name: ")
num_lines = 0
with open(fname, 'r') as f:
    for line in f:
        num_lines += 1
print("Number of lines:")
print(num_lines)
