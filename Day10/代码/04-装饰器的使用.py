#  在不修改原有代码的情况下，增加判断逻辑

def can_play(fn):
    def inner(x, y, *args, **kwargs):
        # clock = args[0]   #方式一
        # clock = kwargs['clock']  # 方式二  会出现bug,如果调用时,没有传名为'clock'的参数会报错
        clock = kwargs.get('clock',22)     #方式三 该方式是解决方式二出现的bug问题，使用get方式获取，可以设置默认值
        if clock < 22:
            fn(x, y)
        else:
            print("太晚了，不能玩了")

    return inner


@can_play
def play_game(name, game):
    print("{}正在玩{}".format(name, game))


# play_game("张三", "王者荣耀", 18)     #方式一
# play_game("张三", "王者荣耀", clock=20)  # 方式二
play_game("张三", "王者荣耀", clock=20)  # 方式三
play_game("李四", "梦幻西游")  # 方式三


