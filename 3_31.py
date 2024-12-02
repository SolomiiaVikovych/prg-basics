arr = [[-38, 19], [5,40],[-7,11],[29,16]]
row_count_max=1
row_count_min = 1
column_count_max=1
column_count_min = 1
current_count_c_max=1
current_count_r_max =1
current_count_c_min=1
current_count_r_min =1
max_el=0
min_el = 0
for row in arr:
    for i in row:
        if current_count_c_max >=3:
             current_count_c_max = 1
        
        if i > max_el:
            max_el = i
            
            column_count_max = current_count_c_max
            
            row_count_max = current_count_r_max
        current_count_c_max +=1
    current_count_r_max +=1

for row in arr:
    for i in row:
        if current_count_c_min >=3:
                current_count_c_min = 1
        if i < min_el:
            min_el = i
            if current_count_c_min >=3:
                current_count_c_min = 1
            column_count_min = current_count_c_min
            row_count_min = current_count_r_min
        current_count_c_min +=1
    current_count_r_min +=1

for row in arr:
    print(' '.join(map(str,row)))

print(f' max element = {max_el}, position: row {row_count_max}, column {column_count_max}')
print(f' min element: {min_el}, position: row: {row_count_min}, column: {column_count_min}')

