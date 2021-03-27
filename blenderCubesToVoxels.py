import bpy
import json

data = {}

count = 0



for i in bpy.context.selected_objects:
    count += 1
    
    iposition = {}
    
    iposition["x"] = i.location[0]
    
    iposition["y"] = i.location[2] * 3
    
    iposition["z"] = i.location[1]
    
    idata = {}
    
    idata["part"] = "3005"
    idata["position"] = iposition
    
    data[str(count)] = idata

print(json.dumps(data))