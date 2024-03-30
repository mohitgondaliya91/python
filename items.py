thisdict = {
    "name":"name1",
    "course":"course1",

}
x=thisdict.items()
print(x)

thisdict["result"]="PASS"
print(x)
if "name" in thisdict:
    print ("ATKT")