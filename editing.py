import json
import copy

g = open("itemInfotags.json")

obj = json.load(g)
#print (type(obj))

template={"Key":False}

new_tags = []
# sortList = []
# for valve in obj['tags']:
#     if (valve['name'][0] == 'V' or valve['name'][0] == 'Y') and len(valve['name']) == 5:
#       #template['value']=valve['name']
#       #template['label']=valve['name']
#       #new_tags.append(template.copy())
#       sortList.append(valve['name'])
# sortList.sort()
# sortList.append('M0139')
# sortList.append('M0940')
# sortList.append('M0941')
# sortList.append('WATER_PUMP')

# for valve in sortList:
#     templateCopy = copy.deepcopy(template)
#     templateCopy['viewParams']['valve']=valve
#     templateCopy['name']=valve
#     new_tags.append(templateCopy)
#print(obj['tags'][0]['tags'])
jString = "{"
for i,key in enumerate(obj['tags'][0]['tags']):
    if i < len(obj['tags'][0]['tags'])-1:
      jString += ("{\""+key['name']+"\":False},")
    else:
      jString += ("{\""+key['name']+"\":False}")
    print(key['name'])
jString += "}"
print(jString)
obj=jString

json_formatted_str = json.dumps(obj, indent=4)

with open("finished.json","w") as f:
    f.write(str(json_formatted_str))