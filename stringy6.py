test1 = "12345"
test2 = "123abc"
test3 = "3.14"
for t in [test1, test2, test3]:
    if t.replace(".", "").isdigit():
        print(t,"obsahuje cislice")
    else:
        print(t,"neobsahuje cislice")