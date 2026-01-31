from pathlib import Path

file= Path('D:/Projects/Assignments/Assignment-4/sample.txt')
try:
    with open(file,'rt') as fh:
        lines=fh.readlines()
except FileNotFoundError:
    print(f'{file} not found')
else:
    for line in lines:
        print(line.rstrip())


