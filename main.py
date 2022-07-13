import json
import os 

def find_matches_in_operator(json_string, tel_num):
    tel_num = str(tel_num)
    json_object = json.loads(json_string)
    if '46' not in json_object: #must have value 46 (local)
        raise SystemExit(json_object['operator'] + '.json does not have "46" route')
    
    keys = list(json_object.keys())

    #finds all the possible matches for the phone number which start with the keys in the json object 
    matches = list(filter(None,map(lambda x: x if(tel_num.find(x) == 0) else None, keys))) 
    
    if(len(matches) == 0):
        longest_match = '46' #if there are no matches assume it is local
        result_final_tel_num = longest_match + tel_num
    else:
        longest_match = max(matches,key = len)
        result_final_tel_num = tel_num

    #finalizing the result object 
    result_object = dict()
    result_object.update({'operator': json_object['operator']})
    result_object.update({'phone_num': result_final_tel_num})
    result_object.update({'code_match': longest_match})
    result_object.update({'code_match_len': len(longest_match)})
    result_object.update({'match_count': len(matches)})
    result_object.update({'price': float(json_object[longest_match])})

    return json.dumps(result_object)

def compare_operators(tel_num):
    #use proper naming convention. The json file names should always start with 'operator_'
    operator_files = [filename for filename in os.listdir('tests') if filename.startswith("operator_")]

    final_result = {
        'operator': '',
        'phone_num': '',
        'code_match': '',
        'code_match_len': 0,
        'match_count': 0,
        'price' : 0
        }

    for operator_file in operator_files: 
        with open('tests/'+operator_file) as f:
            base_name = os.path.basename(operator_file)
            json_object = json.load(f)
            #the below update is usefull if the json file is generated randomly. If operator exists then it just gets updated
            json_object.update({'operator': os.path.splitext(base_name)[0]})
            json_string = json.dumps(json_object)

            #finds the longest operator-code match for the operator
            match_result = find_matches_in_operator(json_string,tel_num)
            match_result = json.loads(match_result)
            #print(match_result)

            if(int(match_result['match_count']) == 0):
                if int(final_result['match_count']) == 0 and (float(final_result['price']) > float(match_result['price']) or float(final_result['price']) == 0) :
                    final_result = match_result
            else:
                if(int(final_result['match_count']) == 0):
                    final_result = match_result
                else:
                    if(int(final_result['code_match_len']) < int(match_result['code_match_len'])):
                        final_result = match_result
                    else:
                        if(float(final_result['price']) > float(match_result['price'])):
                            final_result = match_result
                        elif(float(final_result['price']) == float(match_result['price'])):
                            final_result['operator'] == final_result['operator'] + ' or ' + match_result['operator']
             
    return final_result


if __name__ == "__main__":
    try:
        tel_num = input('Enter a Telephone Number (only integer) of format "country_code areacode digits": \n')
        #if a number starts with 0 assume it is local number
        if(tel_num.startswith('0')):
            tel_num = int(tel_num.replace('0','46',1))
        else:
            tel_num = int(tel_num)

        #compares all the operators and gets the result
        compared_result = compare_operators(tel_num)
        print("Use operator " + compared_result['operator'] + " for Phone-number " + compared_result['phone_num'] + " with a price of " + str(round(compared_result['price'],2)) + '$/min')
    except ValueError as e:
        raise SystemExit('entered telephone number is invalid please use only intergers with format of "country_code areacode digits"')


        


