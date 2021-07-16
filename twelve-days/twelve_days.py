def recite(start_verse, end_verse):
    lyrics =["a Partridge in a Pear Tree.",
        "two Turtle Doves, ",
        "three French Hens, ",
        "four Calling Birds, ",
        "five Gold Rings, ",
        "six Geese-a-Laying, ",
        "seven Swans-a-Swimming, ",
        "eight Maids-a-Milking, ",
        "nine Ladies Dancing, ",
        "ten Lords-a-Leaping, ",
        "eleven Pipers Piping, ",
        "twelve Drummers Drumming, ",
        "and a Partridge in a Pear Tree."]

    days = ['zero','first','second','third','fourth','fifth','sixth','seventh','eighth','ninth','tenth','eleventh','twelfth']

    # if start_verse == 1 and end_verse == 1:
    #     return [f"On the {days[start_verse]} day of Christmas my true love gave to me: "+
    #             lyrics[end_verse-1]]
    # elif start_verse == 2 and end_verse == 2:
    #     return [f"On the {days[start_verse]} day of Christmas my true love gave to me: "+
    #             lyrics[end_verse-1]+lyrics[-1]]
    # elif start_verse == 3 and end_verse == 3:
    #     return [f"On the {days[start_verse]} day of Christmas my true love gave to me: "+
    #             lyrics[end_verse-1]+lyrics[end_verse-2]+lyrics[-1]]
    # elif start_verse == 4 and end_verse == 4:
    #     return [f"On the {days[start_verse]} day of Christmas my true love gave to me: "+
    #             lyrics[end_verse-1]+lyrics[end_verse-2]+lyrics[end_verse-3]+lyrics[-1]]

    if start_verse == end_verse:
        if start_verse == 1 and end_verse == 1:
            return [f"On the {days[start_verse]} day of Christmas my true love gave to me: " +
                    lyrics[end_verse-1]]
        else:
            out1 = [f"On the {days[start_verse]} day of Christmas my true love gave to me: "]
            # out2 = [lyrics[end_verse-i]+lyrics[-1] for i in range(1,end_verse)]
            out2 = [lyrics[-1]]
            for i in range(1,end_verse):
                out2.insert(i-1,lyrics[end_verse-i])
            out2 = ''.join(out2)
            return [out1[0]+out2]
    else:
        out_for_n = []
        for i in range(start_verse, end_verse + 1):
            out_for_n.append(f"On the {days[i]} day of Christmas my true love gave to me: "+ ''.join(reversed(lyrics[1:i]))+lyrics[-1])
        if start_verse == 1:
            out_for_n[0] = f"On the {days[1]} day of Christmas my true love gave to me: "+lyrics[0]

        return out_for_n

        #return [f"On the {days[i]} day of Christmas my true love gave to me: " + ''.join(lyrics[start_verse:i])+lyrics[-1] for i in range(start_verse,end_verse+1)]

