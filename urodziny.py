import random

ilosc_osob = 20
ilosc_losowan = 1000
osoby = []
znaleziono = 0


for i in range(ilosc_losowan):
    osoby = []
    for data in range(0,ilosc_osob):    
        osoby.append(random.randint(1,365))
    for i in range(0,ilosc_osob):
        for j in range(0,ilosc_osob):
            if osoby[i] == osoby[j] and i != j:
                print(f"Znaleziono tą samą datę: {osoby[i]} = {osoby[j]}")
                znaleziono += 1
                break
        if osoby[i] == osoby[j] and i != j:
            break

print(f"Przy {ilosc_losowan} losowan  {znaleziono} ")
