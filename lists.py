demo_list = [1, "hello", 1.34, True, [1,2,3]]
colors = ['red', 'green', 'blue']

numbers_list = list((1, 2, 3, 4))
#print(number_list)

#Lista del 1 al n-1
r = list(range(1, 10))
print(r)

print(len(colors))

print(colors[1])

print('green' in colors)

colors[1] = 'yellow'
print(colors)

colors.append('violet')
print(colors)

colors.extend(['green', 'orange'])
print(colors)

colors.insert(1, 'black') 

colors.pop()

colors.remove('orange')

colors.sort()

print(colors.index('blue'))

print(colors.count('blue'))

colors.clear()