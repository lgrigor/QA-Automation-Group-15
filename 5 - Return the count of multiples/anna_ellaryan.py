_numbers = (78, 90, 65, 35, 72, 28, 82, 64, 33, 45, 38, 40, 81, 1, 75, 34, 16, 20, 98, 7, 21)
a = [i for i in _numbers if i % 3 == 0]
b = [i for i in _numbers if i % 5 == 0]
c = [i for i in _numbers if i % 5 == 0 and i % 3 == 0]
print('Multiples of tree:', len(a))
print('Multiples of five:', len(b))
print('Multiples of tree and five:', len(c))

