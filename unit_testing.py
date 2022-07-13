import json
import os 
import main

def test_matches_in_operator():
    with open('tests/operator_a.json') as f:
        json_object = json.load(f)
        json_object.update({'operator': 'operator_a'})
        json_string = json.dumps(json_object)
        tel_num = 46727734709
        match_result = main.find_matches_in_operator(json_string,tel_num)
        match_result = json.loads(match_result)
        price_expected = 1.2440932853887698
        expected_operator = 'operator_a'
        expected_code_match = '4672'

        if price_expected != match_result['price'] :
            raise SystemExit('The expected_price is ' + price_expected + ' got ' + match_result['price'])
        if expected_operator != match_result['operator'] :
            raise SystemExit('The expected_operator is ' + expected_operator + ' got ' + match_result['operator'])
        if expected_code_match != match_result['code_match'] :
            raise SystemExit('The expected_code_match is ' + expected_code_match + ' got ' + match_result['code_match'])
        
        print('everything matched correctly')

        #print(match_result)

def test_compare():
    tel_num = 46727734709
    compared_result = main.compare_operators(tel_num)
    expected_price = 0.8827718165059815
    expected_operator = 'operator_c'
    expected_code_match = '46727'
    if expected_price != compared_result['price'] :
        raise SystemExit('The expected_price is ' + price_expected + ' got ' + compared_result['price'])
    if expected_operator != compared_result['operator'] :
        raise SystemExit('The expected_operator is ' + expected_operator + ' got ' + compared_result['operator'])
    if expected_code_match != compared_result['code_match'] :
        raise SystemExit('The expected_code_match is ' + expected_code_match + ' got ' + compared_result['code_match'])
        
    print('comparision worked correctly')




if __name__ == "__main__":
    test_matches_in_operator()
    test_compare()