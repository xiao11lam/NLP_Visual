a = ["我", "爱", "东", "哥", "哥", "B"]
b = ["我", "爱", "东", "哥", "哥", "B"]
c = ["我", "爱", "东", "哥", "哥", "B"]
d = ["我", "爱", "东", "哥", "哥", "B"]
e = ["我", "爱", "东", "哥", "哥", "B"]
f = ["我", "爱", "东", "哥", "哥", "B"]

for path_num_a in range(len(a)):
    for path_num_b in range(len(b)):
        for path_num_c in range(len(c)):
            for path_num_d in range(len(d)):
                for path_num_e in range(len(e)):
                    for path_num_f in range(len(f)):
                        print(a[path_num_a],b[path_num_b],c[path_num_c],d[path_num_d],e[path_num_e],f[path_num_f])
    # for a[i], j in enumerate(a):
        # print(a[i],j)