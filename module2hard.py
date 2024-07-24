print('Not time to die!')
num = int(input("Enter number fastly! It's: "))
first_result = []
element = []
for i in range(1, num + 1):
    if num % i == 0:
        for j in range(1, i//2 + 1):
            if j != i - j:
                element = [j, i - j]
                first_result.extend([element])
    first_result = sorted(first_result)
result = first_result[0]
for k in range(1,len(first_result)):
    result = result + first_result[k]
print('Use so more fastly! Your code is: ',*result,sep='')
