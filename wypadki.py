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
wypadki_wina = 0
kolizje_wina = 0

for zd in root:
    czy_wypadek = False
    czy_z_rowerem = False
    ucz = zd.find(".//UCZESTNICY")
    poj = zd.find(".//POJAZDY")
    id_row = []
    for pojazd in poj:
        try:
            rodzaj = pojazd.find(".//RODZAJ_POJAZDU").text
        except:
            rodzaj = ""
        if rodzaj in ["IS201", "IS101", "IS01"]:
            id_row.append(pojazd.find(".//ID").text)
            czy_z_rowerem = True
    wina = False
    if czy_z_rowerem:
        for osob in ucz:
            czy_to_rower = False
            try:
                if osob.find(".//ZSPO_ID").text in id_row:
                    czy_to_rower = True
            except:
                pass
            try:
                stan = osob.find(".//STUC_KOD").text
                czy_wypadek = True
            except:
                stan = ""
            if czy_to_rower:
                if stan == "ZC":
                    print(zd[0].text)
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
                try:
                    if osob.find(".//SRUZ_KOD") is not None:
                        wina = True
                except:
                    pass
        
        if czy_wypadek:
            wypadki += 1
            if wina:
                wypadki_wina += 1
        else:
            kolizje += 1
            if wina:
                kolizje_wina += 1
        czy_z_rowerem = False
        czy_wypadek = False
        wina = False
    
print(f"kolizje: {kolizje}")
print(f"kolizje_wina: {kolizje_wina}")
print(f"wypadki: {wypadki}")
print(f"wypadki_wina: {wypadki_wina}")
print(f"zc: {zc}")
print(f"zm: {zm}")
print(f"rl: {rl}")
print(f"rc: {rc}")