import os


MainPath = os.getcwd()
OptionalPath = input("Enter Optional Directory")


def count_lines(file_name):
    with open(file_name) as f:
        return f'{file_name}: {sum(1 for _ in f)} lines'


for file in os.listdir(MainPath):
    if file.endswith(".txt"):
        print(count_lines(file))

os.chdir(OptionalPath)

for file in os.listdir(OptionalPath):
    if file.endswith(".txt"):
        print(count_lines(file))