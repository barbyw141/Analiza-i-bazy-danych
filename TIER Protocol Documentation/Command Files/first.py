
plik = open(r"C:\Users\Admin\Desktop\Analiza i Bazy Danych\Lab 1 - tidy data\TIER Protocol Documentation\Original Data\weather.txt",'r')

tab2 = []
for linia in plik:
	tab2.append(linia)
tab2=tab2[1668:1683]
tab=[]
for linia in tab2:
    tymcz = linia.split("  ")
    tab.append(tymcz)
for linia in tab:
    linia.insert(1,linia[0][21:26])
    linia.insert(1,linia[0][17:21])
    linia.insert(1,linia[0][15:17])
    linia.insert(1,linia[0][11:15])
    linia[0]=linia[0][0:2]+linia[0][6:11]
for linia in tab :
    if linia[3]==('PRCP'):
        tab.remove(linia)
for linia in tab:    
    for elem in linia:
        if elem == ('') or elem == ('S') or elem == (' \n'):
            linia.remove(elem)



plik.close()
plik = open(r"C:\Users\Admin\Desktop\Analiza i Bazy Danych\Lab 1 - tidy data\TIER Protocol Documentation\Analysis Data\first_data.txt",'w')
for element in tab: plik.write(str(element) + '\n')
plik.close()