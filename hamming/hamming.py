def distance(strand_a, strand_b):
    compte =0
    
    if len(strand_a) == len(strand_b):
        for i,j in zip(strand_a,strand_b):
            if i!=j:
                compte +=1
            elif strand_a == strand_b:
                compte=0
    else: 
        raise ValueError("error")

    return compte


