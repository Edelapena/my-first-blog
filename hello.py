def hi(name=""):
    print("Hi " + name + "!")

hi("Emily")

girls = ['Rachel', 'Monica', 'Pheobe', 'Ola', 'Emily']
for name in girls:
    hi(name)
    print('Next girl')

for i in range(1, 6):
    print(i)