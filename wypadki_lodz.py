import xml.etree.ElementTree as ET

folder = '2024'
file = r"2024\SEWIK_EXP_N_XML_02_WOJ__ŁÓDZKIE_2024.xml"

tree = ET.parse(file)
root = tree.getroot()
root = root[0]

test = root.findall(".//ZDARZENIE")
i = 0
for child in test:
    try:
        tmp_txt = child.find(".//POWIAT").text
    except:
        tmp_text = ""
    if tmp_txt != "POWIAT ŁÓDŹ":
        try:
            root.remove(child)
        except:
            print(f"coś się nie udało w {child[0].text}")
        i += 1
tree = ET.ElementTree(root)
with open('export.xml', 'wb') as f:
    tree.write(f, encoding='utf-8')

print(i)