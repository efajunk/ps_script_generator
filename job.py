with open("acl_data.txt", "r") as file:
    index_slice_start_from = 0
    for i in file.readline():
        if "::" in i:
            index_slice_start_from = i.index("::")
            print(i[index_slice_start_from:])