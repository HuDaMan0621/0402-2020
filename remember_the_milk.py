#setup
count = 0
groceries = ''

#Do the work
while count <3:
    groceries = groceries + input('What do you need from the store? ')
    groceries = groceries + '\n' #Add a line break after each groceries
    count = count + 1

#result
print(f'Here is your grocery list:\n{groceries}')
