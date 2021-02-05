#!D:\python
from student import Student
from utils import *
import os


# 主要数据结构
# 许多学生-students列表
# 单个学生-student对象
# 类的成员 姓名string 语数英成绩scores字典 平均分string
# student1 = Student(name,{'math':98,'English':95,'Chinese':93},average)
# 列表-学生对象-成员变量（3个）
# 主要就是列表的增删改查操作

# 将所有记录保存到文件模块
def saveInfo():
    path = './files/'
    if not os.path.exists(path):
        os.mkdir(path)
    file_name = path + getCurrentTime() + '.txt'
    with open(file_name, 'w') as f:
        f.write('\t姓名\t数学\t英语\t语文\t平均分\n')
        for student in students:
            # 格式化写入 其中的>意思是“ 对齐到右边 ”，8是特定值的宽度
            f.write('{:>8}{:>8}{:>8}{:>8}{:>8}\n'.format(student.name, str(student.scores['math']),
                                                         str(student.scores['English']), str(student.scores['Chinese']),
                                                         str(student.average)))
        f.close()

    print('成绩已保存至文件夹' + file_name)


# 从文件中读入所有记录
def readInfo():
    path = input('请输入导入文件名，例如：d:\\xds\score.txt：')
    if not os.path.exists(path):
        print('文件不存在，导入失败')
        return
    with open(path,'r') as file:
        students.clear()
        for line in file.readlines():
            line = line.strip('\n')
            # print(line)
            # print(type(line))
            if '姓名' in line:
                continue
            split = line.split()
            student = Student(split[0],{'math':split[1],'English':split[2],'Chinese':split[3]},split[4])
            students.append(student)
        print('已经成功从文件'+path.split('.txt')[0].rsplit('/',1)[-1]+'导入数据!!!')


# 输入记录模块
def inputRecord():
    isKeep = 'y'
    while (isKeep == 'y'):
        try:
            print('\n请按如下提示输入相关信息.\n')
            name = input('请输入学生姓名:')
            # 保持主键name唯一
            isNameExist = isNameExists(name, students)
            if isNameExist:
                print('该学生已存在，请重新输入\n')
                continue
            print('请输入成绩')
            math = float(input('数学：'))
            English = float(input('英语：'))
            Chinese = float(input('语文：'))
            # 平均分保留一位小数
            average = round((math + English + Chinese) / 3, 1)
            student = Student(name, {'math': math, 'English': English, 'Chinese': Chinese}, average)
            # 分数超出范围
            if outRange(math) or outRange(English) or outRange(Chinese):
                print('存在非法数据，请重新输入')
                continue
            # 新增
            students.append(student)
            print('新增一条记录!\n')
            isKeep = input('是否继续添加记录（y/n）：')
        except ValueError as e:
            # 成绩必须为浮点数
            print('成绩类型错误，请重新输入!\n')
            continue
    # for student in students:
    #     student.print()


# 显示所有记录模块
def printAllRecords():
    if len(students) == 0:
        print('很遗憾，空表中没有任何记录可供显示！')
        return
    print('\n******************显示所有记录*******************\n')
    # 一个制表符t占4格
    print('\t姓名\t数学\t英语\t语文\t平均分\n')
    for student in students:
        student.print()
    print('************************************************')


# 对所有记录进行排序模块
# 采用冒泡排序算法
def sortAllRecords():
    if len(students) == 0:
        print('很遗憾，空表中没有任何记录可供排序！')
        return
    lenth = len(students)
    for i in range(lenth):
        for j in range(0, lenth - i - 1):
            if float(students[j].average) < float(students[j + 1].average):
                students[j], students[j + 1] = students[j + 1], students[j]
    print('已按平均分由高到低排序!\n')


# 按姓名查找记录并显示模块
def queryByName():
    name = input('请输入要查询的学生姓名：')
    for student in students:
        if name in student.name:
            print('\n*********************Found*********************\n')
            print('\t姓名\t数学\t英语\t语文\t平均分\n')
            student.print()
            print('***********************************************\n')
            return
    print('您要查找的是' + name + '，很遗憾，查无此人！')


# 插入记录模块
def insertRecord():
    length = len(students)
    print('当前列表长度为' + str(length))
    index = int(input('请输入你要插入的位置(0-len)：'))
    if index >= 0 and index <= length:
        # 插入操作
        print('\n请按如下提示输入相关信息.\n')
        name = input('请输入学生姓名:')
        # 保持主键name唯一
        isNameExist = isNameExists(name, students)
        if isNameExist:
            print('该学生已存在，插入操作失败\n')
        print('请输入成绩')
        math = float(input('数学：'))
        English = float(input('英语：'))
        Chinese = float(input('语文：'))
        # 平均分保留一位小数
        average = round((math + English + Chinese) / 3, 1)
        student = Student(name, {'math': math, 'English': English, 'Chinese': Chinese}, average)
        # 分数超出范围
        if outRange(math) or outRange(English) or outRange(Chinese):
            print('存在非法数据，插入操作失败')
        # 列表插入
        students.insert(index, student)
    else:
        print('非法输入，请重新输入\n')
        insertRecord()


# 删除记录
def deleteRecordById():
    name = input('请输入你要删除的学生姓名：')
    for student in students:
        if name in student.name:
            students.remove(student)
            print('删除成功！')
            return
    print('您要删除的是' + name + '，很遗憾，查无此人！')


# 菜单显示模块
def menu():
    print("\n         ***************主菜单**************\n")
    print("             1. 输入记录\n")
    print("             2. 显示所有记录\n")
    print("             3. 对所有记录进行排序\n")
    print("             4. 按姓名查找记录并显示\n")
    print("             5. 插入记录\n")
    print("             6. 删除记录\n")
    print("             7. 将所有记录保存到文件\n")
    print("             8. 从文件中读入所有记录\n")
    print("             9. 退出\n")
    print("         ***********************************\n\n")


if __name__ == '__main__':
    students = []
    print('               欢迎来到学生成绩管理系统')
    while True:
        menu()
        choice = int(input('         请选择操作(1-9):'))
        if choice == 1:
            inputRecord()
        elif choice == 2:
            printAllRecords()
        elif choice == 3:
            sortAllRecords()
        elif choice == 4:
            queryByName()
        elif choice == 5:
            insertRecord()
        elif choice == 6:
            deleteRecordById()
        elif choice == 7:
            saveInfo()
        elif choice == 8:
            readInfo()
        elif choice == 9:
            exit()
    raw_input("Press Enter key to exit.")
