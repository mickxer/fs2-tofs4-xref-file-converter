def fs2_vector3(output_file):
    search_line = '[vector3_float64]'
    replace_line = '[vector2_float64]'
    
    with open(output_file, 'r') as file:
            fs2_content = file.read().replace(search_line,replace_line)
    
    new_content = fs2_content
    
    with open(output_file, 'w') as file:
            file.write(new_content)