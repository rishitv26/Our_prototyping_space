# create a list that will act like database:
db = ['lololololololololololol']

# create an empty list to store filtered data:
verified = []
error = False
run = True

# here is the proccess:
while run:
    entered = input("> ")

    for list in db:
        processed = entered in db
        if processed:
            verified += list
        if len(verified) == 0:
            error = True
            break
    print(verified)


if error:
    print('no results...')
    run = True