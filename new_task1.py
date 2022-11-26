
from functools import reduce
print(sum(i for i in range(1,1000) if i%3 == 0 or i%5 == 0 ))
print(sum([i for i in range(1,1000) if i%3 == 0 or i%5 == 0] ))
print(sum({i for i in range(1,1000) if i%3 == 0 or i%5 == 0} ))
print(sum(filter(lambda i: i%3 == 0 or i%5 == 0, range(1,1000))))
print(sum(map(lambda i: i if i%3 == 0 or i%5 == 0 else 0, range(1, 1000))))
print(reduce(lambda x, y: x+y if y%3 == 0 or y%5 == 0   else x , range(1,1000), 0))
print( sum( set( range(3, 1000, 3) ) | set( range(5,1000,5) ) ) )
print(sum(set([*range(3, 1000, 3)]+[*range(5, 1000, 5)])))
