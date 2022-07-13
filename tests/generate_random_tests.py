import json
import random
 
output_file_name = "operator_c.json"
# Data to be written
final_dict = dict()

for i in range (566,56800):
    if(i%1000 == 0):
        i = int(i/1000)
    elif(i%100 == 0):
        i = int(i/100)
    else:
        pass

    key = str(i)
    final_dict.update({key: random.uniform(0.4,1.9)})

json_object = json.dumps(final_dict, indent = 4)


with open(output_file_name, "w") as outfile:
    outfile.write(json_object)

print(output_file_name + " is ready")

'''
dictionary ={
    "name" : "sathiyajith",
    "rollno" : 56,
    "cgpa" : 8.6,
    "phonenumber" : "9976770500"
}
  
# Serializing json 
json_object = json.dumps(dictionary, indent = 4)
  
# Writing to sample.json
with open("sample.json", "w") as outfile:
    outfile.write(json_object)

'''