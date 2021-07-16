def abbreviate(words):
    a= words.upper().replace('_',' ').replace('-',' ')
    b= [list(i) for i in a.split()]
    return ''.join(map(str,[i[0] for i in b]))