import json
import sys

if __name__ == "__main__":
    input_file_path = sys.argv[1] #uses argument passed while running the script
    with open(input_file_path) as f:
        lines = f.readlines() #reads all the lines and puts them in a list
        final_dict = dict()
        for line in lines:
            key,value = line.split(' ') #splits based on the space
            if(key.strip() == 'operator'):
                final_dict.update({key.strip(): value.strip()})
            else:
                try:
                    final_dict.update({key.strip(): float(value.strip())})
                except ValueError:
                    raise SystemExit(input_file_path + ' does not have valid value for ' + key + '. Please add the correct value and retry')

    if 'operator' not in final_dict: #must have value operator
        raise SystemExit(input_file_path + ' does not have operator name')
    
    if '46' not in final_dict: #must have value 46 (local)
        raise SystemExit(input_file_path + ' does not have "46" route')

    output_file_name = 'operator_' + final_dict['operator'] +'.json'
    json_object = json.dumps(final_dict, indent = 4)
    with open(output_file_name, "w") as outfile:
        outfile.write(json_object)

    print(output_file_name + " is ready")