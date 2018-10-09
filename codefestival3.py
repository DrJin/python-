S = input()

ands = S.split("&&")

eqtup = []
noteqtup = []
for x in ands:
    if("==" in x):
        eq = x.split("==")
        eqtup.append((eq[0],eq[1]))
    else:
        noteq = x.split("!=")
        noteqtup.append((noteq[0],noteq[1]))

for x in eqtup:
    x[0]

