
from array import *
array1 = array('i', [10, 20, 30, 40, 50])

# mengkalikan
perkalian = array1[1] * array1[3]
print('hasil perkalian', array1[1], 'dan', array1[3], 'adalah', perkalian)

# index
array1.insert(1, 60)


for x in array1:
    result = x ** 2
    print('Bilangan awal', x, 'hasil perpangkatan', result)
