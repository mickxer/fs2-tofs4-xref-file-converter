def look_for_lines(output_file):
    with open(output_file, 'w') as file:
        line = 1
        while line <= 360:
            
            print(file.write('<[float32][direction][' + str(line) + ']>\n'))
            line = line + 1
        
    file.close()     
    
def replacement_for_lines(output_file):
    with open(output_file, 'w') as file:
        line = 1
        while line <= 360:
            
            d = 0
            if line <91:
                d = 90 - line
            else:
                d = 450 - line
            
            print(file.write('<[float64][direction][' + str(d) + ']>\n'))
            line = line + 1
            
    file.close()
        

look_for_lines('fs2_xref_flow32_direction.txt')
replacement_for_lines('fs4_xref_flow64_direction.txt')