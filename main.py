with open("./text.txt", "a+", encoding="utf-8") as celfajl:
    celfajl.seek(0)
    print(celfajl.readline())
    print(celfajl.tell())