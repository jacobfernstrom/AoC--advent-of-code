data = open('day1data.txt', 'r') 

lines = data.readlines()

summa = 0
list_of_sums = []

for line in lines:
    try:
        summa = summa + int(line)
        
    except:
        list_of_sums.append(summa)
        
        summa = 0

list_of_sums = sorted(list_of_sums, reverse=True)

print(list_of_sums[0]+list_of_sums[1]+list_of_sums[2])