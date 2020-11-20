import os

old_file_name = input("请输入要复制的文件名")

if os.path.isfile(old_file_name):  # 判断是否是文件
    old_file = open(old_file_name, encoding='utf-8')

    # sss.txt ==> sss.bak.txt
    file_par = old_file_name.rpartition('.')
    new_file_name = file_par[0] + '.bak' + file_par[1] + file_par[2]
    new_file = open(new_file_name, 'w', encoding='utf-8')
    new_file.write(old_file.read())

    new_file.close()
    old_file.close()
else:
    print("要复制的文件不存在")
