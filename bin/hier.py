from __future__ import print_function

# Parse file
fr = open("test_hier.txt")
mydict = {}
keys = []
for line in fr:
    line = line.strip()
    k,v = line.split(",")
    keys.append(k)
    if len(v) > 0:
        if k in mydict:
            tmp_v = mydict[k]
            mydict[k] = v+","+tmp_v
        else:
            mydict[k] = v
fr.close()
print (mydict)

# Process file
for key in mydict.keys():
    rolling_list = [key]
    print ("\n-------------------- {0}".format(key))

    output_dict = []
    while len(rolling_list) > 0:
        myk = rolling_list.pop()
        if myk in mydict:
            v = mydict[myk]
            newlist = v.split(",")

            for value in newlist:
                if value not in output_dict:
                    output_dict.append(value)

                rolling_list.append(value)

    print (output_dict)

