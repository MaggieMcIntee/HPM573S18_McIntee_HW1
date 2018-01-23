yours = ['Yale', 'MIT', 'Berkeley']

mine = ['Boston College', 'Saint Johns University', 'College of Saint Benedict']

ours1 =  yours + mine

print(ours1)

ours2 = []

ours2.append(yours)

ours2.append(mine)

print(ours2)

yours[1] = 'Harvard'

print(yours)

print(ours1)
print(ours2)