names = ['Екатирина', 'Александр', 'Владимир', 'Анна']
one_dist = {}
for name in names:
    one_dist[name] = len(name)
print(one_dist)
two_dist = {name: len(name) for name in names}
print(two_dist)
two_dist['Екатирина'] = 2
print(two_dist)
