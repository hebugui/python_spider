import time

# 按格式获取当前时间（精确到秒）
def getCurrentTime():
    return(time.strftime('%Y年%m月%d日%H时%M分%S秒',time.localtime(time.time())))

# 检测分数是否超出范围
def outRange(number):
    if(number>100.0 or number<0.0):
        return True
    return False

# 查询name是否已经存在
def isNameExists(name,students):
    for student in students:
        if student.name in name:
            return True
        return False
