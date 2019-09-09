import json


with open('timeline_data.json') as file:
    data = json.load(file)
actual_data = data['data']
new_data = []
print(data)
print(actual_data)
for item in actual_data:
    item['id'] = 'http://resource.geosciml.org/classifier/ics/ischart/' + item['id']
    item['broad'] = ['http://resource.geosciml.org/classifier/ics/ischart/' + child_item for child_item in item['broad']]
    item['narrow'] = ['http://resource.geosciml.org/classifier/ics/ischart/' + child_item for child_item in
                     item['narrow']]
    new_data.append(item)
print(new_data)
json.dump(new_data, open('timeline_data_new.json', 'w'))