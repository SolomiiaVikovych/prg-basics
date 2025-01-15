speeds = [48,47,54,50,42,68,39,46]
over_limit = filter(lambda x: x>50,speeds)
print(','.join(map(str,over_limit)))