# 用户输入不同类型的数据（数字、文件名、字符串）。
#
# 程序通过异常处理来验证输入是否合法。
#
# 避免因错误输入导致程序崩溃。
def get_number():
    try:
        value = int(input("请输入一个整数: "))
        print("平方:", value ** 2)
    except ValueError:
        print("输入必须是整数！")

def safe_divide():
    try:
        a = int(input("请输入被除数: "))
        b = int(input("请输入除数: "))
        print("结果:", a / b)
    except ValueError:
        print("输入必须是整数！")
    except ZeroDivisionError:
        print("不能除以零！")

def read_file():
    filename = input("请输入文件名: ")
    try:
        with open(filename, "r",encoding='utf-8') as f:
            print("文件内容:\n", f.read())
    except FileNotFoundError:
        print("文件未找到，请检查文件名。")

class NegativeError(Exception):
    pass

def check_negative():
    try:
        num = int(input("请输入一个正数: "))
        if num<0:
            raise NegativeError("不能输入负数")
    except NegativeError as e:
        print("捕获到自定义异常")
    except ValueError:
        print("输入必须是整数！")


def main():
    print("用户输入验证系统")
    print("1.输入整数计算平方")
    print("2.安全除法")
    print("3.文件读取")
    print("4.检查正数")
    print("5.退出")

    choice_num = input("请选择功能(1-5)：")
    if choice_num == "1":
        get_number()
    elif choice_num == "2":
        safe_divide()
    elif choice_num == "3":
      read_file()
    elif choice_num == "4":
        check_negative()
    elif choice_num == "5":
        print("程序结束，再见！")
    else:
        print("无效选择")

if __name__ == "__main__":
    main()