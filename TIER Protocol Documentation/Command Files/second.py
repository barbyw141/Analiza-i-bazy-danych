
plik = open(r"C:\Users\Admin\Desktop\Analiza i Bazy Danych\Lab 1 - tidy data\TIER Protocol Documentation\Analysis Data\first_data.txt",'r')

tab2 = []
for linia in plik:
	tab2.append(linia)

tab=[]
for linia in tab2:
    tymcz = linia.split(",")
    tab.append(tymcz)

tab3=[]
for linia in tab:
    tymcz2=[]
    for element in linia:
        element = element.replace("'",'')
        element = element.replace("[",'')
        element = element.replace("]",'')
        element = element.replace(" ",'')
        tymcz2.append(element)
    tab3.append(tymcz2)

final_tab=[]
for linia in tab3:
    for elem in linia:
        if elem != ('-9999') and elem != (' -9999') and elem != ('S-9999') and elem != ('-9999\n') and elem != ('S-9999\n') and linia.index(elem)>3:
            tymcz=[]
            tymcz[0:4]=linia[0:4]
            tymcz.append(linia.index(elem)-3)
            tymcz.append(elem)
            final_tab.append(tymcz)
final_tab2=[]
for linia in final_tab:
    tymcz=[]
    tymcz.append(linia[0])
    tymcz.append(linia[3])
    tymcz.append(linia[5])
    linia[4]=str(linia[4])
    tymcz.append(linia[1]+'-'+linia[2]+'-'+linia[4])
    final_tab2.append(tymcz)
            
plik.close()
plik = open(r"C:\Users\Admin\Desktop\Analiza i Bazy Danych\Lab 1 - tidy data\TIER Protocol Documentation\Analysis Data\melt.txt",'w')
for element in final_tab2: plik.write(str(element) + '\n')
plik.close()