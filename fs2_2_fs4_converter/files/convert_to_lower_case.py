def convert_to_lower_case(output_file):
    text = open(output_file, 'r').read()
    new_content = text.lower()
    
    with open(output_file, 'w') as file:
        file.write(new_content)
         
    file.close()