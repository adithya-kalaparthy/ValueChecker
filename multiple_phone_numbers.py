import sys
import main
import re

if __name__ == "__main__":

    input_file_path = sys.argv[1] #uses argument passed while running the script
    with open(input_file_path) as f:
        lines = f.readlines()
        final_dict = dict()
        main.load_operator_files()
        for line in lines:
            try:
                #remove spaces,'+','-' from a phone number
                tel_num = ''.join(re.findall(r'(\w+)(?=[-+\s+]|$)',line.strip()))

                #if a number starts with 0 assume it is local number
                if(tel_num.startswith('0')):
                    tel_num = int(tel_num.replace('0','46',1))
                else:
                    tel_num = int(tel_num)

                #compares all the operators and gets the result
                compared_result = main.compare_operators(tel_num)

                print("Use operator " + compared_result['operator'] + " for Phone-number " + compared_result['phone_num'] + " with a price of " + str(round(compared_result['price'],2)) + '$/min')
            except Exception:
                print(tel_num + ' is not valid or does not have a valid parameters')