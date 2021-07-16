def is_isogram(string):
    if len(string)!= 0:
        string= string.lower().strip().replace(' ','').replace('-','')
        iso=[string.count(e) for e in string]
        if max(iso) > 1:
            return False
        else:
            return True
    else:
        return True