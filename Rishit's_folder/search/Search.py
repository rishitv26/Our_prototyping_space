# create a list that will act like database:
db = ['win', 'men', 'cans', 'lol', 'hello']

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
            verified.append[list]
        if len(verified) == 0:
            error = True
            break


if error:
    print('no results...')
    run = True