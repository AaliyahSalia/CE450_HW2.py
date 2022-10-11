def bnc_bck_frth(k):

    count = 0
    reset = False
    
    for i in range(1, k+1):
        if i % 7 == 0 or i % 10 == 7:
            if reset == False:
                reset = True
                count += 2
            else:
                reset = False
                count -= 2
        if reset == True:
            count -= 1
        else:
            count += 1
    return count

print(bnc_bck_frth(3))