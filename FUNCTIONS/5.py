def isPanagram(strr):
    sting = ""+strr
    sting.lower()
    sett = set(sting)
    len_of_set = len(sett)

    if ' ' in sett:
        if len_of_set == 27:
            return "YES"
        else:
            return "NO"
    else:
        if len_of_set == 26:
            return "YES"
        else:
            return "NO"
        
strr = input()

print(isPanagram(strr))
