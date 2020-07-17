mylist = [12,23,45,66,78,90,99,44,36,777,59,62,121,300]

num_div_by_2 = []

for i in mylist:
    if i % 2 == 0:
        num_div_by_2.append(i)

print(num_div_by_2)

print([x for x in mylist if x%2 == 0])

print(list(filter(lambda x: x%2 == 0, mylist)))

print(tuple(filter(lambda x: x%2 == 0, mylist)))

print(set(filter(lambda x: x%2 == 0, mylist)))

import datetime

x = datetime.datetime.now()

print(x)
print(x.year)
print(x.strftime("%A"))
print(x.strftime("%a"))
print(x.strftime("%Y"))
print(x.strftime("%y"))
print(x.strftime("%H"))
print(x.strftime("%M"))
print(x.strftime("%S"))
print(x.strftime("%h"))
print(x.strftime("%m"))


x = datetime.datetime(2020, 5, 17)

print(x)

print(x.strftime("%d %B, %Y")) 