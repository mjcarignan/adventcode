

from itertools import chain

newrange = chain(range(30), range(2000, 5002))

x = 5002
print(x in newrange)