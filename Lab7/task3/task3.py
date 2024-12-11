import json

def Add(dict, id, items):
    total = 0
    for i in items:
        total += int(i['quantity']) * int(i['price'])
    new_dict = {'id': id, 'total': total, 'items': items}

    dict['invoices'].append(new_dict)
    return dict

file_path = 'ex_3.json'
new_file = 'new_ex_3.json'

with open(file_path) as f:
    data = json.load(f)

Add(data, data['invoices'][-1]['id'] + 1, [{'name': 'item 4', 'quantity': 10, 'price': 15.0}])

print(data)

with open(new_file, 'w') as f:
    json.dump(data, f, indent=2)