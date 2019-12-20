import random as rnd
namelist = ['A','B','C']

for num, student in enumerate(namelist):
    print(f"{num} - {student}")

print(f"Viene interrogato: {namelist[rnd.randint(0,len(namelist)-1)]}")