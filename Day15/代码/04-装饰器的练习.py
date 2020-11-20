user_permission = 3

# 权限因子
# 用户权限 & 权限因子 ！= 0
DEL_PERMISSION = 8
READ_PERMISSION = 4
WRITE_PERMISSION = 2
EXE_PERMISSION = 1


def check_permission(user_permission, permission):
    def handle_action(fn):
        def do_action():
            if user_permission & permission != 0:
                fn()
            else:
                print("你没有该权限")

        return do_action

    return handle_action


@check_permission(user_permission, READ_PERMISSION)
def read():
    print("我正在读取内容")


@check_permission(user_permission, WRITE_PERMISSION)
def write():
    print("我正在写入内容")


@check_permission(user_permission, EXE_PERMISSION)
def execute():
    print("我正在执行内容")


@check_permission(user_permission, DEL_PERMISSION)
def delete():
    print("我正在删除内容")


read()
write()
execute()
delete()
