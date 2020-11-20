def can_play():
    print("can_play最外层被调用了")

    def handle_action(fn):
        print("handle_action被调用了")
        def do_action(name, game,**kwargs):
            clock = kwargs.get("clock",15)
            if clock > 20:
                print("太晚了，不能玩游戏了")
            else:
                fn(name, game)

        return do_action

    return handle_action


@can_play()
def play_game(name, game):
    print("{}正在玩{}".format(name, game))


play_game("张三", "王者荣耀",clock = 22)
