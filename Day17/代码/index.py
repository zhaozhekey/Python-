import sys

import file_manager
import model
import tools
import student_manager


def start():
    content = file_manager.read_file("welcome.txt")
    while True:
        operator = input(content + '\n请选择(1-3):')
        if operator == '1':
            login()
        elif operator == '2':
            register()
        elif operator == '3':
            sys.exit(0)
        else:
            print("输入有误")


def login():
    # 读取文件，查看文件里是否有数据。如果文件不存在，默认是一个字典
    data = file_manager.read_json("data.json", {})
    teacher_name = input("请输入老师账号：")
    if teacher_name not in data:
        print("登录失败!该账号没有注册!")
        return
    password = input("请输入密码：")

    if data[teacher_name] == tools.encrypt_password(password):
        print("登录成功")
        student_manager.show_manager()
    else:
        print("密码错误，登录失败！")


def register():
    # 读取文件，查看文件里是否有数据。如果文件不存在，默认是一个字典
    data = file_manager.read_json('data.json', {})
    while True:
        teacher_name = input("请输入账号(3-6位)")
        if not 3 <= len(teacher_name) <= 6:
            print("账号输入有误")
        else:
            break

    if teacher_name in data:
        print("该账号已经注册")
        return

    while True:
        teacher_password = input("请输入密码(6-12位)")
        if not 6 <= len(teacher_password) <= 12:
            print("密码输入有误")
        else:
            break

    t = model.Teacher(teacher_name, tools.encrypt_password(teacher_password))
    data[t.name] = t.password
    file_manager.write_json("data.json", data)


if __name__ == '__main__':
    start()
