import xml.etree.ElementTree as ET

xmlTree = ET.parse('edited.xml')
root = xmlTree.getroot()

new_sum = 0
new_sum_rows = 0

for i in root:
    for head in i:
        if head.tag == "Item":
            for atributes in head:
                if(atributes.tag == "QNT"):
                    new_sum += float(atributes.text.replace(',', "."))
                if(atributes.tag == "QNTRows"):
                    new_sum_rows += int(atributes.text)
print(new_sum)
print(new_sum_rows)

for i in root:
        if i.tag == "Summary":
            for head in i:
                if head.tag == "Summ":
                    head.text = str(new_sum)
                if head.tag == "SummRows":
                    head.text = str(new_sum_rows).replace('.', ',')
xmlTree.write('answer.xml', encoding='UTF-8')