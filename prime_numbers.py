lower_range =int(input('Enter a number: '))
upper_range =int(input('Enter a number: '))
count=0
for num in range(lower_range,upper_range+1):
    if num > 1:
        for i in range(2,num):
            if (num % i) == 0:
                print(num,'is composite')
                count+=1
                break
        else:
            print(num,'is prime')
print('count= {} composite and {} prime in the range ({},{})'.format(count,upper_range-lower_range-count+1,lower_range,upper_range))