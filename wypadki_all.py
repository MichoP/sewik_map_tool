import xml.etree.ElementTree as ET

file = r"export.xml"

tree = ET.parse(file)
root = tree.getroot()

zc = 0
zm = 0
rl = 0
rc = 0
wypadki = 0
kolizje = 0

for zd in root:
    czy_wypadek = False
    ucz = zd.find(".//UCZESTNICY")
    poj = zd.find(".//POJAZDY")
    id_row = []
    for osob in ucz:
        try:
            stan = osob.find(".//STUC_KOD").text
            czy_wypadek = True
        except:
            stan = ""         
        if stan == "ZC":
            # print(zd[0].text)
            zc += 1
        elif stan == "ZM":
            zm += 1
        elif stan == "RL":
            rl += 1
        elif stan == "RC":
            rc += 1
        else:
            # print(f"nieznany stan: {stan}")
            pass
            
    
    if czy_wypadek:
        wypadki += 1
    else:
        kolizje += 1
    czy_wypadek = False

print(f"zdarzenia: {kolizje + wypadki}")
print(f"kolizje: {kolizje}")
print(f"wypadki: {wypadki}")
print(f"rl: {rl}")
print(f"rc: {rc}")
print(f"zc: {zc}")
print(f"zm: {zm}")
