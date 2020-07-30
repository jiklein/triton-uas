import json

f =  open("jsonfile1.json", "r")
data = f.read()

jsondata = json.loads(data)

print jsondata  # all json file
print "*********************"
print jsondata["Records"]  # list after dictionary
print "*********************"
print jsondata["Records"][0]  # first element of list
print "*********************"
print jsondata["Records"][1]["ID"]
print jsondata["Records"][0]["state1"][0]["event5"]

for record in records:
    print record.keys()[0]






f.close()
