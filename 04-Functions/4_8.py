def time_string(hours, minutes, time_format):
    if time_format == '24':
        # 24-hour format: format hours and minutes as two digits
        return f'{hours:02}:{minutes:02}'

    elif time_format == '12':
        # Determine AM or PM and adjust hours for 12-hour format
        period = 'am' if hours < 12 else 'pm'
        hours_12 = hours % 12  # Convert to 12-hour format
        if hours_12 == 0:
            hours_12 = 12  # Midnight and noon should be 12 in 12-hour format
        return f'{hours_12}:{minutes:02}{period}'

    else:
        return "Invalid time format"


print(time_string(15, 38, '24'))  
print(time_string(8, 3, '24'))    
print(time_string(0, 5, '24'))    
print(time_string(11, 15, '12')) 
print(time_string(0, 7, '12'))    
print(time_string(7, 30, '12'))   
print(time_string(12, 46, '12'))  
print(time_string(13, 10, '12'))  
print(time_string(19, 2, '12'))  
