class Student(object):
    # name String
    # score = ['math':0,'English':0,'Chinese':0]

    # 初始化函数
    def __init__(self, name, scores, average):
        self.name = name
        self.scores = scores
        self.average = average

    # 输出函数
    def print(self):
        print('{:>8}{:>8}{:>8}{:>8}{:>8}\n'.format(self.name, str(self.scores['math']), str(self.scores['English']), str(self.scores['Chinese']),str(self.average)))

        