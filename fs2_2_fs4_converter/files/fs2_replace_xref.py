def fs2_xref_elements(output_file):
    search_line = '[xref][element]'
    replace_line = '[tm_airport_pd_xref][element]'
    
    with open(output_file, 'r') as file:
            fs2_content = file.read().replace(search_line,replace_line)
    
    new_content = fs2_content
    
    with open(output_file, 'w') as file:
            file.write(new_content)