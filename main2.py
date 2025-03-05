with open("./text.txt", "r", encoding="utf-8") as forrasfajl, \
    open("./text.txt", "w", encoding="utf-8") as celfajl:
    for sor in forrasfajl:
        print(sor.strip(), file=celfajl)