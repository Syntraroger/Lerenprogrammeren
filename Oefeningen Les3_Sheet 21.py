a = 203
b = 202

# Long version
"""f b>a:
    print('b is greater than a')
elif a==b:
    print('a adn b are equal')
else:
    print('a is greater tha b')"""

# Short version
if a>b: print('a is greater than b')
print(a) if a<b else print('B is groter', b)