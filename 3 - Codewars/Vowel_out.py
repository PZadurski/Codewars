def disemvowel(string_):
    x = string_
    for nstr in range (len(string_)):
        if string_[nstr] in "aeiouAEIOU":
            x[nstr] == " "
            print(nstr)
        else:
            x[nstr]

    print(x)
    return x


disemvowel("ilkjfdsusfnidsufids")