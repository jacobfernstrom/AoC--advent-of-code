f = open('day2data.txt', 'r')
data = f.readlines()

#X for Rock, Y for Paper, and Z for Scissors.
#A for Rock, B for Paper, and C for Scissors
sum = 0
sum2 = 0
for line in data:
    if ('X' in line and 'C' in line) or ('Y' in line and 'A' in line) or ('Z' in line and 'B' in line):
        sum += 6
    elif ('X' in line and 'A' in line) or ('Y' in line and 'B' in line) or ('Z' in line and 'C' in line):
        sum += 3
   
print(sum)

for line in data:
    if 'X' in line:
        sum += 1
    if 'Y' in line:
        sum += 2
    if 'Z' in line:
        sum += 3

print('sum1', sum)

for line in data:
    if ('Z' in line):
        sum2 += 6
    if 'Y' in line:
        sum2 += 3

print(sum2)
for line in data:
    if 'X' in line:
        if 'A' in line:
            sum2 += 3
        if 'B' in line:
            sum2 += 1
        if 'C' in line:
            sum2 += 2
    if 'Y' in line:
        if 'A' in line:
            sum2 += 1
        if 'B' in line:
            sum2 += 2
        if 'C' in line:
            sum2 += 3
    if 'Z' in line:
        if 'A' in line:
            sum2 += 2
        if 'B' in line:
            sum2 += 3
        if 'C' in line:
            sum2 += 1
print('sum2', sum2)