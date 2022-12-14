from array import *
a = array('i', [10, 12, 13])
b = array('i', [2, 4, 6])

for x in a:
    for y in b:
        penjumlahan = x+y
        print(x, '+', y, '=', penjumlahan)
