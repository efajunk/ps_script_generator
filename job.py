# initiate func, that will make a rows of scripts for each folder
def script_constructor(list_of_paths, filename, group_asking=None, set_group=None):
    write_row(filename, '# Start\n')
    enter_message = input('Set one group for all folders? (enter to skip): ')
    for path in list_of_paths:
        while True:
            if enter_message:
                set_group = True
            if set_group is None:
                group_asking = input(f'Group to add access for: "{path}" (q - exit, s - skip): ')
            else:
                group_asking = input(f'Group to add access for the rest of folders: (enter to skip): ')
            if group_asking == 'q':
                return
            elif group_asking == 's':
                break
            # if group_asking == 'ag':
            #     print([i for i in get_access(filename, path)])
            ps_get_acl = f'$acl = Get-Acl "{path}";'
            ps_access_rule = f'$AccessRule = New-Object System.Security.AccessControl.FileSystemAccessRule("oasiscatalog\{group_asking}", "ReadAndExecute", "Allow");'
            ps_set_access_rule = '$acl.SetAccessRule($AccessRule);'
            ps_set_acl = f'$acl | Set-Acl "{path}";'
            rows_list = [ps_get_acl, ps_access_rule, ps_set_access_rule, ps_set_acl]
            for row in rows_list:
                write_row(filename, row)
            if set_group is None:
                if input(f'Is there other groups to add?(enter to skip): '):
                    continue
            break
    return

# Getting paths to folders from acl_data file and pass to script_constructor
def get_path(filename):
    with open(filename, "r", encoding="utf-16") as file:
        index_slice_start_from = 0
        list_of_paths = []
        for i in file.readlines():
            if "Path" in i:
                index_slice_start_from = i.rfind(":")
                list_of_paths.append(i[index_slice_start_from - 1:].strip())
        return list_of_paths

# getting actual access to folder
# def get_access(filename, path):
#     with open(filename, "r", encoding="utf-16") as file:
#         index_slice_start_from = 0
#         list_of_access = []
#         for i in file.readlines():
#             while 'Audit' not in i:
#                 if path in i:
#                     index_slice_start_from = i.rfind(":")
#                     list_of_access.append(i[index_slice_start_from - 1:].strip())
#         return list_of_access

def write_row(filename, row):
    with open(filename, "a", encoding="utf-16") as file:
        file.writelines(row + '\n')
    pass

file = input('Enter file name, or path to: ')
# default filename in folder with script
# file = 'acl_share_Обмен.txt'
# default output filename in folder with script
output_file = 'script_output.txt'

script_constructor(get_path(file), output_file)