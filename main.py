import json

student_list = []
filename = 'student.txt'


def main():
    while True:
        menu()
        try:
            choice = int(input('请选择'))
        except:
            choice = 255
            print('输入错误请重新输入')
        if choice in [0, 1, 2, 3, 4, 5, 6, 7]:
            if choice == 0:
                answer = input('您确定要退出系统吗?y/n')
                if answer == 'y' or answer == 'Y':
                    print('谢谢您的使用!')
                    break
                else:
                    continue
            elif choice == 1:
                insert()
            elif choice == 2:
                serach()
            elif choice == 3:
                delect()
            elif choice == 4:
                modify()
            elif choice == 5:
                sort()
            elif choice == 6:
                total()
            elif choice == 7:
                show()


def menu():
    print('------------------------------学生信息管理系统----------------------------------')
    print('--------------------------------功能菜单---------------------------------------')
    print('\t\t\t\t1.录入学生信息')
    print('\t\t\t\t2.查找学生信息')
    print('\t\t\t\t3.删除学生信息')
    print('\t\t\t\t4.修改学生信息')
    print('\t\t\t\t5.排序')
    print('\t\t\t\t6.统计学生总人数')
    print('\t\t\t\t7.显示所有学生信息')
    print('\t\t\t\t0.退出')
    print('------------------------------------------------------------------------------')


def insert():
    while True:
        print('------------------------------------------------------------------------------')
        while True:
            try:
                id = int(input('请输入学号:'))
            except:
                print('输入错误请重新输入')
                continue
            if not id:
                break
            check = [d for d in student_list if d.get('id') == id]
            if len(check) == 0:
                break
            else:
                print('id已存在请重新输入')
                continue
        name = input('请输入姓名:')
        if not name:
            break
        try:
            english = int(input('请输入英语成绩:'))
            chinese = int(input('请输入语文成绩:'))
            math = int(input('请输入数学成绩:'))
        except:
            print('输入无效,请重新输入')
            continue

        student = {'id': id, 'name': name, 'english': english, 'chinese': chinese, 'math': math,
                   'sum': english + chinese + math}
        student_list.append(student)
        print('录入成功')
        print('------------------------------------------------------------------------------')
        answer = input('是否继续添加?y/n')
        if answer == 'y' or answer == 'Y':
            continue
        else:
            write()
            break


def serach():
    global student_list
    while True:
        print('------------------------------------------------------------------------------')
        print('1.ID查找')
        print('2.姓名查找')
        print('0.返回上级')
        print('------------------------------------------------------------------------------')
        answer = input('请输入序号:')
        if answer == '1':
            print('------------------------------------------------------------------------------')
            try:
                id = int(input('请输入ID:'))
            except:
                print('输入错误请重新输入')
                continue
            result = [d for d in student_list if d.get('id') == id]
            print(result)
            print('------------------------------------------------------------------------------')
        elif answer == '2':
            print('------------------------------------------------------------------------------')
            name = input('请输入姓名:')
            result = [d for d in student_list if d.get('name') == name]
            print(result)
            print('------------------------------------------------------------------------------')
        elif answer == '0':
            break
        else:
            print('输入错误,请重新输入')
            continue


def delect():
    global student_list
    while True:
        print('------------------------------------------------------------------------------')
        print('1.ID删除')
        print('2.姓名删除')
        print('0.返回上级')
        print('------------------------------------------------------------------------------')
        answer = input('请输入序号:')
        if answer == '1':
            print('------------------------------------------------------------------------------')
            try:
                id = int(input('请输入ID:'))
            except:
                print('输入错误请重新输入')
                continue
            result = [d for d in student_list if d.get('id') == id]
            student_list.remove(result[0])
            for d in student_list:
                print(d)
            write()
            print('删除成功')
            print('------------------------------------------------------------------------------')
        elif answer == '2':
            print('------------------------------------------------------------------------------')
            name = input('请输入姓名:')
            result = [d for d in student_list if d.get('name') == name]
            student_list.remove(result[0])
            for d in student_list:
                print(d)
            write()
            print('删除成功')
            print('------------------------------------------------------------------------------')
        elif answer == 0:
            break

        else:
            print('输入错误,请重新输入')
            continue


# 修改
def modify():
    global student_list
    while True:
        print('------------------------------------------------------------------------------')
        print('1.根据ID修改')
        print('2.根据姓名修改')
        print('0.返回上级')
        print('------------------------------------------------------------------------------')
        answer = input('请输入序号:')
        if answer == '1':
            print('------------------------------------------------------------------------------')
            try:
                id = int(input('请输入ID:'))
            except:
                print('输入错误请重新输入')
                continue
            index = [i for i, d in enumerate(student_list) if d.get('id') == id]
            try:
                id = int(input('请输入修改后的ID:'))
            except:
                print('输入错误请重新输入')
                continue
            if not id:
                break
            name = input('请输入姓名:')
            if not name:
                break
            try:
                english = int(input('请输入修改后的英语成绩:'))
                chinese = int(input('请输入修改后的语文成绩:'))
                math = int(input('请输入修改后的数学成绩:'))
            except:
                print('输入无效,请重新输入')
                continue
            student = {'id': id, 'name': name, 'english': english, 'chinese': chinese, 'math': math}
            student_list[index[0]] = student
            write()
            print('修改成功')
            print('------------------------------------------------------------------------------')
        elif answer == 2:
            print('------------------------------------------------------------------------------')
            name = input('请输入姓名:')
            index = [i for i, d in enumerate(student_list) if d.get('name') == name]
            try:
                id = int(input('请输入修改后的ID:'))
            except:
                print('输入错误请重新输入')
                continue
            if not id:
                break
            name = input('请输入姓名:')
            if not name:
                break
            try:
                english = int(input('请输入修改后的英语成绩:'))
                chinese = int(input('请输入修改后的语文成绩:'))
                math = int(input('请输入修改后的数学成绩:'))
            except:
                print('输入无效,请重新输入')
                continue
            student = {'id': id, 'name': name, 'english': english, 'chinese': chinese, 'math': math}
            student_list[index[0]] = student
            write()
            print('修改成功')
            print('------------------------------------------------------------------------------')
        elif answer == 0:
            break
        else:
            print('输入错误,请重新输入')
            continue


# 排序

def sort():
    while True:
        print('------------------------------------------------------------------------------')
        print('1.升序')
        print('2.降序')
        print('0.返回上级')
        print('------------------------------------------------------------------------------')
        answer = input('请输入序号:')
        if answer == '1':
            while True:
                print('------------------------------------------------------------------------------')
                print('1.ID升序')
                print('2.英语升序')
                print('3.语文升序')
                print('4.数学升序')
                print('5.总成绩升序')
                print('0.返回上级')
                print('------------------------------------------------------------------------------')
                answer = input('请输入序号:')
                if answer == '1':
                    sort_list('id', False)
                elif answer == '2':
                    sort_list('english', False)
                elif answer == '3':
                    sort_list('chinese', False)
                elif answer == '4':
                    sort_list('math', False)
                elif answer == '5':
                    sort_list('sum', False)
                elif answer == '0':
                    break
                write()
                for d in student_list:
                    print(d)
        elif answer == '2':
            while True:
                print('------------------------------------------------------------------------------')
                print('1.ID降序')
                print('2.英语降序')
                print('3.语文降序')
                print('4.数学降序')
                print('5.总成绩降序')
                print('0.返回上级')
                print('------------------------------------------------------------------------------')
                answer = input('请输入序号:')
                if answer == '1':
                    sort_list('id', True)
                elif answer == '2':
                    sort_list('english', True)
                elif answer == '3':
                    sort_list('chinese', True)
                elif answer == '4':
                    sort_list('math', True)
                elif answer == '5':
                    sort_list('sum', True)
                elif answer == '0':
                    break
                write()
                for d in student_list:
                    print(d)


def sort_list(obj, upordown):
    student_list.sort(key=lambda x: x[obj], reverse=upordown)


# 统计学生人数
def total():
    num = len(student_list)
    print('------------------------------------------------------------------------------')
    print('一共有%d名学生' % num)
    print('------------------------------------------------------------------------------')


# 显示全部
def show():
    print('------------------------------------------------------------------------------')
    for d in student_list:
        print(d)
    print('------------------------------------------------------------------------------')
    while True:
        answer = input('按0退出显示界面\n')
        if answer == '0':
            break


def write():
    json_str = json.dumps(student_list)
    with open(filename, 'w') as file:
        file.write(json_str)
    file.close()


def read():
    global student_list
    with open(filename, 'r') as file:
        json_str = file.read()
        student_list = json.loads(json_str)
    file.close()


if __name__ == "__main__":
    read()
    main()
