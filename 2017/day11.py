from

def occurences(liste):
    occ = {}

    for char in liste:
        if char not in occ:
            occ[char] = 1
        else:
            occ[char] += 1

    return occ

def parser_occurences(occ):
    if occ["ne"] > occ["sw"]:
        occ["ne"] = occ["ne"] - occ["sw"]
        occ["sw"] = 0
    else:
        occ["sw"] = occ["sw"] - occ["ne"]
        occ["ne"] = 0

    if occ["n"] > occ["s"]:
        occ["n"] = occ["n"] - occ["s"]
        occ["s"] = 0
    else:
        occ["s"] = occ["s"] - occ["n"]
        occ["n"] = 0

    if occ["nw"] > occ["se"]:
        occ["nw"] = occ["nw"] - occ["se"]
        occ["se"] = 0
    else:
        occ["se"] = occ["se"] - occ["nw"]
        occ["nw"] = 0

    return occ

