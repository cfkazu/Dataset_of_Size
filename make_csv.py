from __future__ import annotations
import json
import csv

from unicodedata import name
class size:
    def __init__(self,value,unit):
        self.value = str(value)
        self.unit = unit
    def to_str(self):
        return "{} {}".format(self.value,self.unit)
class item:
    def __init__(self,Weight,Height,Length,Width,Name,Product_type,Category):
        self.weight = Weight
        self.height = Height
        self.length = Length
        self.width = Width
        self.name = Name.replace('"','""')
        self.product_type = Product_type.replace('"','""')
        self.category = Category.replace('"','""')
    def display(self):
        print("Item Name:{} Product_type is {} ,and the size is {} * {} * {}".format(self.name,self.product_type, self.height.to_str(),self.width.to_str(),self.length.to_str()))
        print("Product Category is {} and weight is {}",self.category,self.weight.to_str())
    def to_csv_format(self)->list[str]:
        #順番は、Name,Product Type,Category,Height,Length,Width,HeightUnit(Inch),LengthUnit,WidthUnit,Weight,WeightUnit
        return [self.name,self.product_type,self.category,self.height.value,self.length.value,self.width.value,self.height.unit,self.length.unit,self.width.unit,self.weight.value,self.weight.unit]


def json_to_item(filename:str)->list[item]:
    data = {}
    items = []
    with open(filename)as fin:
        data = json.load(fin)
    for dat in data:
        if   'item_name' in dat and ('item_weight'in dat or 'item_dimensions' in dat):
            if 'item_dimensions' in dat:
                height = size(dat['item_dimensions']['height']['value'],dat['item_dimensions']['height']['unit'])
                length = size(dat['item_dimensions']['length']['value'],dat['item_dimensions']['length']['unit'])
                width  = size(dat['item_dimensions']['width']['value'],dat['item_dimensions']['width']['unit'])
            else:
                height = size(-1,"NONE")
                length = size(-1,"NONE")
                width  = size(-1,"NONE")
            if 'item_weight' in dat:
                weight = size(dat['item_weight'][0]['value'],dat['item_weight'][0]['unit'])
            else:
                weight = size(-1,"NONE")
            product_type = ""
            if 'product_type' in dat:
                product_type = dat['product_type'][0]['value']
            if product_type == None:
                product_type = ""
            category = ""
            if 'node' in dat:
                category = dat['node'][0]['node_name']
            if category == None:
                category = ""
            name = dat['item_name'][0]['value']
            for namekouho in dat['item_name']:
                if namekouho['language_tag'].split('_')[0] == "en":
                    name = namekouho['value']
                    break
            nitem = item(weight,height,length,width,name,product_type,category)
            items.append(nitem)
    return items

#%%
json_path = "work.json"
items = json_to_item(json_path)
with open("myrawdata.csv", mode="w") as file:
    writer = csv.writer(file)
    file.write("Name,Product Type,Category,Height,Length,Width,HeightUnit(Inch),LengthUnit,WidthUnit,Weight,WeightUnit\n")
    for i in items:
        writer.writerow(i.to_csv_format())
print(len(items))
# %%
