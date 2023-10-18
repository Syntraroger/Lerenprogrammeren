# Is een woord een palindroom

# def palin(woord):
#     lengte = int(len(woord)/2)
#     print(len(woord))
#     print(lengte)
#     for i in range(lengte):
#
#         if woord[i] != woord[len(woord)-i-1]:
#             return False
#         return True
#
# ja= palin('kett')
#
#
# if (ja):
#     print('yes')
# else:
#     print('no')


'''
# function to check string is
# palindrome or not
def isPalindrome(str):
    # Run loop from 0 to len/2
    for i in range(0, int(len(str) / 2)):
        if str[i] != str[len(str) - i - 1]:
            return False
    return True


# main function
s = "malayalam"
ans = isPalindrome(s)

if (ans):
    print("Yes")
else:
    print("No")
'''

# Oppervlakte van een 5-hoek
"""def vijfhoek(a,b):
    return (a*b/2)*5



a = vijfhoek(3,2)
print(a)"""
# Inhoud van een kegel
import math

def kegel():
    h=int(input('Geef de hoogte van de kegel '))
    r=int(input('geef de straal van de kegel'))
    return (((1/3*h)*math.pi)*(r**2))


a = kegel()
print(a)