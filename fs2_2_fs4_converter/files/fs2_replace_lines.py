def xref_flow32_direction(output_file): 
    line = 0
    while line < 361:
        
        with open('fs2_xref_flow32_direction.txt', 'r') as file2:
            search_files = file2.readlines()
    
        with open('fs4_xref_flow64_direction.txt', 'r') as file3:
            replace_files = file3.readlines()
            
        x = search_files[line]
        y = replace_files[line]
    
        with open(output_file, 'r') as file:
            fs2_content = file.read().replace(x,y)
            new_content = fs2_content

        line = line + 1
        
        new_content = fs2_content
    
        with open(output_file, 'w') as file:
            file.write(new_content)

    new_content = fs2_content
    
    with open(output_file, 'w') as file:
        file.write(new_content)
         
    file.close()
    file2.close()
    file3.close()