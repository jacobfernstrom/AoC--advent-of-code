f = open('day3data.txt', 'r')
data = f.readlines()

def value_letter (letter):
    global count
    count = 1
    for i in abc:
        if i == letter:
            
            break
        count +=1
    

data2 = []
data3 = []
sum = 0
sum2 = 0
abc = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'

for line in data:
    length = int(len(line) / 2)
    first_part = line[:length]
    second_part = line[length:]
    data2.append((first_part.strip('\n'),second_part.strip('\n')))

for lines in data2:
    common = ''.join(set(lines[0]).intersection(lines[1]))
    value_letter(common)
    sum += count

print('round 1', sum)

for i in range(len(data)):
    count = 0
    if i % 3 == 0:
        data3.append((data[i].strip('\n'),data[i+1].strip('\n'), data[i+2].strip('\n')))

for lines in data3:
    
    for letter in lines[0]:
        print(lines)
        if letter in lines[1] and letter in lines[2]:
            
            value_letter(letter)
            sum2 += count
            break
    

print('round 2',sum2) 