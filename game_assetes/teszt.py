champions = [
    ["Champ", 100, 30, 10,20],
    ["Champ2", 100, 50, 0, 20],
    ["Champ3", 100, 10, 10, 20],
    ["Champ4", 100, 30, 10, 20],
]

hp = []
t = []
p = []
d = []
vd = p + d

for i in champions:
    sor = champions.index(i) +1
    print(sor, i[0])

v = int(input(": "))

for i in champions:
    sor = champions.index(i) +1

if v == sor:
    hp.append(i[1]),
    t.append(i[2])
    p.append(i[3])
    d.append(i[4])





print(hp,t,p,d,vd)


