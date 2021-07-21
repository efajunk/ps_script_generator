with open("acl_data.txt", "r", encoding="utf-16") as file:
    index_slice_start_from = 0
    for i in file.readlines():
        if "Path" in i:
            index_slice_start_from = i.rfind(":")
            print(i[index_slice_start_from:])

