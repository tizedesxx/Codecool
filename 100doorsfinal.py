for i in range(1, 101):
    if i**0.5 % 1:
        state='closed'
    else:
        state='opened'
    print("Door {} is {}".format(i, state))