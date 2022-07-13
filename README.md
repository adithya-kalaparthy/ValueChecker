# ValueChecker
Objective of this task is to determine which Operator is the most cost effective for a given certain number

Generate operator json files:
1. As the first step in executing the application make sure 
   json files containing routes and prices are there in the tests folder
2. To randomly generate the json files please uchange output_file_name variable and range() in 
   "generate_random_tests.py" inside tests folder and run it
3. If you want to input the values and routes manually please put them in a txt file with syntax "operator_code price"
   in each line. Add "operator <operator_name>" in the txt file and run convert_to_json.py inside convert_txt_to_json folder
   syntax to run this file is python convert_to_json.py <input_file_path> and Move the generated json files to tests folder
   Example is inside the repo

Running the application:
1. After making sure that operator json files are correct, to get value for only one phone number please run "python main.py"
2. If you wish to check multiple phone numbers at once, please create a txt file containing numbers in each line
   and run "python multiple_phone_numbers.py <phone_number_txt_path>"

Expected output:
If everystep has been successfull then we expect the script to provide result like 
"Use operator operator_c for Phone-number 46727734709 with a price of 0.88$/min"
