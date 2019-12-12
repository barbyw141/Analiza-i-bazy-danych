plik = open(r"C:\Users\Admin\Desktop\Analiza i Bazy Danych\Lab 1 - tidy data\TIER Protocol Documentation\Analysis Data\melt.txt",'r')

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
        element = element.replace("\n",'')        
        tymcz2.append(element)
    tab3.append(tymcz2)

fin_tab=[]
done=0
pusta=[0,0,0,0]
pierwsza=['id','date','tmax','tmin']
fin_tab.append(pierwsza)
for linia in tab3:
    for linia2 in fin_tab:
        if linia[3] == linia2[1]:
            if linia[1] == ('TMAX'):
                linia2[2]=linia[2]
            else:
                linia2[3]=linia[2]
            done=1
    if done == 0:
        tymcz=[]
        tymcz.append(linia[0])
        tymcz.append(linia[3])
        if linia[1] == ('TMAX'):
            tymcz.append(linia[2])
            tymcz.append(0)
        else:
            tymcz.append(0)
            tymcz.append(linia[2])
        fin_tab.append(tymcz)
    else:
        done=0
for linia in fin_tab:
    if fin_tab.index(linia)!=0:
        linia[2]=int(linia[2])/10
        linia[3]=int(linia[3])/10    

plik.close()
plik = open(r"C:\Users\Admin\Desktop\Analiza i Bazy Danych\Lab 1 - tidy data\TIER Protocol Documentation\Documents\Final Paper.txt",'w')
for element in fin_tab: plik.write(str(element) + '\n')
plik.close()