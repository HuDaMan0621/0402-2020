# Add the odd numbers between 0 and 500

#setup
result = 0
# Work!
# Let's look at the numbers from 0 to 5000
num = 0
while num <= 5000:
    is_odd = num % 2 != 0
    if is_odd:
        print(num)
    num = num +1
    #num += 1

#return/ print the result
print(result)