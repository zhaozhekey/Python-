import file_manager

def show_manager():
    print("正在登录")
    content = file_manager.read_file("students_page.txt")
    print(content)
