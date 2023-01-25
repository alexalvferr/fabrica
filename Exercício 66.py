popA=80000
taxaA=3

popB=200000
taxaB=1.5

ano=0
while popA < popB:
    ano += 1
    popA = int((1 + (taxaA/100) )* popA)
    popB = int((1 + (taxaB/100) )* popB)
#    print("Ano %d:" % ano)
#    print("Populaçao A: %d" % popA)
#    print("População B: %d\n\n" % popB)

print(f"A População do A Ultrapassa a População B daqui {ano} anos")
