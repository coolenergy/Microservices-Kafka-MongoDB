import json

def get_transformed_observation1():
    with open('Observable1JSON.json', 'r') as f:
        data = json.load(f)
    result = []
    for item in data:
        result.append({'name':item['name'],'type':item['attackType'],'description':item['sources'][0]})
    print(f"We have ingested {len(result)} items in File 1")
    return result


def get_transformed_observation2():
    with open('Observable2JSON.json', 'r') as f:
        data = json.load(f)
    result = []
    data = data['objects'][0]['external_references']
    for item in data:
        
        name, type, sources = ""
        if 'source_name' in item.keys():
            name = item['source_name']
        if 'type' in item.keys():
            type = item['type']
        if 'description' in item.keys:
            sources = item['description']
        if 'url' in item.keys:
            sources = item['url']
        result.append({'name':name,'type':type,'description':sources})
    print(f"We have ingested {len(result)} items in File 2")
    return result

