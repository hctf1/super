skladniki = [4, -2, 3213123, 42, 42.01, 22, 0, -3, -4, 213, 756, 6, -8, 543, 876,0.1, 2413,-533]

### SORTOWANIE BĄBELKOWE ###

rozmiar = len(skladniki)

for i in range(0, rozmiar):
    for j in range(0, rozmiar-i-1):
        if skladniki[j] > skladniki[j+1]:
            skladniki[j], skladniki[j+1] = skladniki[j+1], skladniki[j]

print("Po sortowaniu:", skladniki)

