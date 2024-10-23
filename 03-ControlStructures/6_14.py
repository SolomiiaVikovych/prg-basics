count = 0
Facebook = input('Do you have Facebook account? (Y/N) ')
if Facebook == 'Y':
    is_facebook = True
    count += 1
else:
    is_facebook = False    
Twitter = input('Do you have Twitter account? (Y/N) ')
if Twitter == 'Y':
    is_twitter = True
    count += 1
else:
    is_twitter = False    
Instagram = input('Do you have instagram account? (Y/N) ') 
if Instagram == 'Y':
    is_instagram = True
    count+= 1

if count == 3:
    print('You are a good influencer!')
    

