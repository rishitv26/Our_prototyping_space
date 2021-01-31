# create a list that will act like database:
db = ['billy', 'sam', 'rishit', 'dhawan', 'ragav']

# create an empty list to store filtered data:
verified = []
error = False
run = True

# here is the proccess:
while run:
    inputE = input('> ')
    if inputE != '':
        for i in db:
            check = inputE in i
            # print(check)
            if check:
                print(i)