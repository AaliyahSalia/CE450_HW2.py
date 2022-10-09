def pay_change(paid, price):
    # set up the change and an empty dictionary for result
    global change
    change = paid - price
    bills = ['$20', '$10', '$5', '$2', '$1']

    # create a function to calculate the change for each bills
    def f(x):
        global change
        result = divmod(change, x)[0]
        change = divmod(change, x)[1]
        return result
    temp = list(map(f, (20, 10, 5, 2, 1)))

    # generate the final result as a dictionary
    result = dict(zip(bills, temp))

    # present the result, do not show if value is 0
    for k, v in result.items():
        if v != 0:
            print('Need', v, 'bills of', k)

pay_change(4, 6)