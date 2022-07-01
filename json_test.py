#%%
import json
fake_json_path = "listings_0.json"
json_path = "work.json"
njson_path = "nwork.json"
#%%
from torch import le


with open(njson_path, "w") as fout:
    fout.write("[\n   ")
    with open(fake_json_path) as fin:
        fout.write('  ,'.join(fin.readlines()))
    fout.write("]\n")

data = {}
with open(njson_path) as fin:
    data = json.load(fin)
#%%

namelist = ["0","1","2","3","4","5","6","7","8","9","a","b","c","d","e","f"]
with open(json_path, "w") as fout:
    lines = []
    fout.write("[\n   ")
    for n in namelist:
        filename = "listings_{}.json".format(n)
        with open(filename) as fin:
            lines.append('  ,'.join(fin.readlines()))
    fout.write(' ,'.join(lines))
    fout.write("]\n")
#%%
data = {}
with open(json_path) as fin:
    data = json.load(fin)

#%%
class size:
    def __init__(self,value,unit):
        self.value = value
        self.unit = unit
    def to_str(self):
        return "{} {}".format(self.value,self.unit)
class item:
    def __init__(self,Weight,Height,Length,Width,Name,Product_type,Category):
        self.weight = Weight
        self.height = Height
        self.length = Length
        self.width = Width
        self.name = Name
        self.product_type = Product_type
        self.category = Category
    def display(self):
        print("Item Name:{} Product_type is {} ,and the size is {} * {} * {}".format(self.name,self.product_type, self.height.to_str(),self.width.to_str(),self.length.to_str()))
        print("Product Category is {} and weight is {}",self.category,self.weight.to_str())

# %%
data[2]['item_dimensions']

data[2]['item_weight']
data[2]['product_type']
data[1]['bullet_point'][0]
data[2]['item_name']

# %%

items = []
for dat in data:
    if 'product_type'in dat and'item_weight'in dat and 'item_name' in dat and 'item_dimensions' in dat:
        #print(dat['item_dimensions'])
        #print(dat['item_weight'])
        #print(dat['product_type'])
        #print(dat['item_name'])
        weight = size(dat['item_weight'][0]['value'],dat['item_weight'][0]['unit'])
        height = size(dat['item_dimensions']['height']['value'],dat['item_dimensions']['height']['unit'])
        length = size(dat['item_dimensions']['length']['value'],dat['item_dimensions']['length']['unit'])
        width  = size(dat['item_dimensions']['width']['value'],dat['item_dimensions']['width']['unit'])
        product_type = dat['product_type']
        category = None
        if 'node' in dat:
            category = dat['node']
        name = dat['item_name']
        '''
        for bullet in dat['bullet_point']:
            if bullet['language_tag'] == 'es_MX':
                print(bullet['value'])
                print(dat['item_dimensions'])
                print("----")
                break
        '''
        nitem = item(weight,height,length,width,name,product_type,category)
        items.append(nitem)

       
# %%
data[1]['bullet_point']
# %%
items[0].display()

# %%
