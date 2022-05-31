# 用于记录所有动态创建的按钮及其坐标
class Button_list(object):
    def __init__(self, start_x=0, start_y=0, increment_x=50, increment_y=50, width=40, height=40, x_max=580, y_max=65535):
        self.start_x = start_x
        self.start_y = start_y
        self.increment_x = increment_x
        self.increment_y = increment_y
        self.width = width
        self.height = height
        self.x_max = x_max
        self.y_max = y_max
        self.list = []
        self.x = []
        self.y = []
        self.x_num = int((self.x_max - self.start_x)/self.increment_x)

    def add_button(self, button_name='new_button'):
        if len(self.list):
            self.list.append(str(button_name))
            if self.x[-1] + self.width + self.increment_x <= self.x_max:
                self.x.append(self.x[-1] + self.increment_x)
                self.y.append(self.y[-1])
                return self.x[-1], self.y[-1], self.width, self.height
            elif self.x[-1] + self.width + self.increment_x > self.x_max and self.y[-1] + self.height + self.increment_y <= self.y_max:
                self.x.append(self.start_x)
                self.y.append(self.y[-1] + self.increment_y)
                return self.x[-1], self.y[-1], self.width, self.height
            else:
                print('超过界面最大值！，无法创建按钮')
                return -1, -1, -1, -1
        else:
            self.list.append(str(button_name))
            self.x.append(self.start_x)
            self.y.append(self.start_y)
            return self.start_x, self.start_y, self.width, self.height

    def remove_button(self, button_name):
        try:
            index = self.list.index(button_name)
            self.list.pop(index)
            self.x.pop(index)
            self.y.pop(index)
            return self.check_button_position()
        except Exception as e:
            # print(e, 'remove_button')
            return 0

    def remove_button_list(self, remove_list=[]):
        if len(remove_list):
            try:
                for button_name in remove_list:
                    index = self.list.index(button_name)
                    self.list.pop(index)
                    self.x.pop(index)
                    self.y.pop(index)
                return self.check_button_position()
            except Exception as e:
                # print(e, 'remove_button_list')
                return 0
        else:
            return self.check_button_position()

    # 检测按钮位置并重构位置，然后返回坐标列表
    def check_button_position(self):
        for button_name in self.list:
            index = self.list.index(button_name)
            if index == 0 or index % self.x_num == 0:      # 判断是否为每行的起始坐标
                self.x[index] = self.start_x
                self.y[index] = self.start_y + (self.increment_y * int(index / self.x_num))
            elif index % self.x_num == self.x_num - 1:      # 判断是否为一行的最后一个
                self.x[index] = self.x[index - 1] + self.increment_x
                self.y[index] = self.y[index-1]
            else:
                self.x[index] = self.x[index-1] + self.increment_x
        return self.x, self.y

    def get_button_counts(self):
        return len(self.list)

    def get_button_name_by_number(self, num=0):
        return self.list[int(num)]

    def get_button_list(self):
        return self.list

    def get_button_position(self, button_name):
        index = self.list.index(button_name)
        return self.x[index], self.y[index]

    def get_button_x(self, button_name):
        return self.x[self.list.index(button_name)]

    def get_button_y(self, button_name):
        return self.y[self.list.index(button_name)]

    # 重设坐标增量
    def change_increment(self, increment_x, increment_y):
        self.increment_x = increment_x
        self.increment_y = increment_y
        self.x_num = int((self.x_max - self.start_x) / self.increment_x)
        self.check_button_position()

    # 重设起始坐标
    def reset_start_point(self, start_x, start_y):
        self.start_x = start_x
        self.start_y = start_y
        self.x_num = int((self.x_max - self.start_x) / self.increment_x)
        self.check_button_position()

    # 重设坐标最大值
    def reset_max_limit(self, x_max, y_max):
        self.x_max = x_max
        self.y_max = y_max
        self.x_num = int((self.x_max - self.start_x) / self.increment_x)
        self.check_button_position()

    # 重设按钮大小
    def reset_button_size(self, width, height):
        self.width = width
        self.height = height
        self.check_button_position()

    # 清空按钮
    def clear(self):
        self.list = []
        self.x = []
        self.y = []
        self.check_button_position()

# {"button_1": {"name": "button_test1", "simple_name": "b1", "introduction": "", "built-in": [], "command": "test test {test} -h", "example": "test test 111 -h"}, "button_2": {"name": "button_test2", "simple_name": "b2", "introduction": "", "built-in": [], "command": "test test {test} -h", "example": "test test 111 -h"}, "button_3": {"name": "button_test3", "simple_name": "b3", "introduction": "", "built-in": [], "command": "test test {test} -h", "example": "test test 111 -h"}, "button_4": {"name": "button_test4", "simple_name": "b4", "introduction": "", "built-in": [], "command": "test test {test} -h", "example": "test test 111 -h"}, "button_5": {"name": "button_test5", "simple_name": "b5", "introduction": "", "built-in": [], "command": "test test {test} -h", "example": "test test 111 -h"}, "button_6": {"name": "button_test6", "simple_name": "b6", "introduction": "", "built-in": [], "command": "test test {test} -h", "example": "test test 111 -h"}, "button_7": {"name": "button_test7", "simple_name": "b7", "introduction": "", "built-in": [], "command": "test test {test} -h", "example": "test test 111 -h"}, "button_8": {"name": "button_test8", "simple_name": "b8", "introduction": "", "built-in": [], "command": "test test {test} -h", "example": "test test 111 -h"}, "button_9": {"name": "button_test9", "simple_name": "b9", "introduction": "", "built-in": [], "command": "test test {test} -h", "example": "test test 111 -h"}, "button_10": {"name": "button_test10", "simple_name": "b10", "introduction": "", "built-in": [], "command": "test test {test} -h", "example": "test test 111 -h"}, "button_11": {"name": "button_test11", "simple_name": "b11", "introduction": "", "built-in": [], "command": "test test {test} -h", "example": "test test 111 -h"}, "button_12": {"name": "button_test12", "simple_name": "b12", "introduction": "", "built-in": [], "command": "test test {test} -h", "example": "test test 111 -h"}, "button_13": {"name": "button_test13", "simple_name": "b13", "introduction": "", "built-in": [], "command": "test test {test} -h", "example": "test test 111 -h"}, "button_14": {"name": "button_test14", "simple_name": "b14", "introduction": "", "built-in": [], "command": "test test {test} -h", "example": "test test 111 -h"}}
