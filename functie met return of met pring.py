def oppv_driehoek_print(b,h):
    print('print')
    print(b*h/2)


def oppv_driehoek_return(b,h):
    print('return')
    return b*h/2



oppv_driehoek_print(5,4)
r=oppv_driehoek_return(10,4)

print('functie aanroep resultaat: ',r)