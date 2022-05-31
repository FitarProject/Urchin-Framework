import subprocess

from window.func.exec_command import LogThread, ExecThread, ReadQueueThread

from PyQt5.Qt import *
from multiprocessing import Process, Queue
from string import Template
import json, psutil, time, os, threading


class TaskThread(QThread):
    # trigger_out = pyqtSignal(str)
    # trigger_err = pyqtSignal(str)

    trigger_log = pyqtSignal(str, str)
    trigger_status = pyqtSignal(str, str)
    trigger_section = pyqtSignal(str, str)
    trigger_timer = pyqtSignal(str, int)

    def __init__(self, parent, task_input_dict, func_detatil):
        super(QThread, self).__init__(parent)
        # self.parent_ = parent
        self.task_input_dict = task_input_dict
        self.func_detatil = func_detatil
        self.task_dir = self.log_mkdir()
        self.curr_result_file = None
        self.pause_flag = False
        # self.pid = os.getpid()

        with open('config/tools_buttons_tool.json', 'r', encoding='utf-8') as f:
            self.tool_config = json.load(f)
        with open('config/tools_buttons_tunnel.json', 'r', encoding='utf-8') as f:
            self.tunnel_config = json.load(f)
        with open('config/tools_buttons_component.json', 'r', encoding='utf-8') as f:
            self.component_config = json.load(f)

    def run(self):
        print(os.getpid())
        # print(os.getppid())
        # print('task_input_dict:', self.task_input_dict)
        # print('func_detatil:', self.func_detatil)
        # print('tool_config:', self.tool_config)
        # 定时
        if self.task_input_dict['set_timer'] == True:
            self.start_timer()
        print('任务开始：' + self.task_input_dict['task_name'])
        self.trigger_status.emit(self.task_input_dict['task_name'], '进行中')
        try:
            # 日志线程
            self.thread_log = LogThread(self)
            self.thread_log.trigger.connect(self.log_emit)
            self.thread_log_no = 0
            curr_section = 0
            all_section = len(self.func_detatil['config'])
            self.thread_log.run_('###################    任务名称： ' + self.task_input_dict['task_name'] + '    ###################')
            self.thread_log.run_('###################    任务目录： logs/' + self.task_dir + '    ###################')
            for part in self.func_detatil['config']:
                # print('new_section')
                curr_section += 1
                self.trigger_section.emit(self.task_input_dict['task_name'], str(curr_section) + '/' + str(all_section))
                if part['type'] == 0:
                    object_name = part['button_num']
                    var_map = {}
                    for variable_value in part['variable_value']:
                        if variable_value == '手动输入':
                            index = part['variable_value'].index(variable_value)
                            position = self.func_detatil['config'].index(part) + 1
                            for variable in self.task_input_dict['variable']:
                                if variable['position'] == str(position) and variable['name'] == part['variable'][index]:
                                    variable_name = part['variable'][index].lstrip('$')
                                    var_map[variable_name] = variable['value']
                                    break
                        elif variable_value == '交互输入':
                            # self.
                            pass
                            continue
                        elif variable_value == '不使用' or variable_value == '':
                            continue
                        else:
                            # print('任务变量测试(工具)：', variable_value)
                            result_name = variable_value.lstrip('$')
                            index = part['variable_value'].index(variable_value)
                            variable_name = part['variable'][index].lstrip('$')
                            var_map[variable_name] = result_name
                    command_init = self.tool_config[object_name]['command_template'][part['command_num']]
                    command = Template(command_init).safe_substitute(var_map)
                    # for component_object in part['component']:
                    #     if self.component_config[component_object]['type'] == 0:
                    #         command = self.component_config[component_object][input] + command
                    #     elif self.component_config[component_object]['type'] == 1:
                    #         command = command + self.component_config[component_object][input]
                    #     else:
                    #         pass
                    if part['result_name'][0].startswith('$'):
                        self.curr_result_file = part['result_name'][0].lstrip('$') + '.txt'
                    else:
                        self.curr_result_file = 'tool_logs_' + self.tool_config[part['button_num']]['name']
                    self.thread_log_no += 1
                    self.thread_log.run_('###################    当前阶段： ' + str(curr_section) + '/' + str(all_section) + '    ###################')
                    self.thread_log.run_('> ' + command)
                    self.exec_command(command)
                elif part['type'] == 1:
                    for tunnel_part in part['tunnel']:
                        index_tunnel = part['tunnel'].index(tunnel_part)
                        object_name = tunnel_part
                        input_list = []
                        output_list = []
                        for variable_value in part['input_value'][index_tunnel]:
                            if variable_value == '手动输入':
                                index = part['input_value'][index_tunnel].index(variable_value)
                                position = str(self.func_detatil['config'].index(part) + 1) + '-' + str(index_tunnel)
                                for variable in self.task_input_dict['variable']:
                                    if variable['position'] == str(position) and variable['name'] == self.tunnel_config[object_name]['input'][index]:
                                        input_list.append(variable['value'])
                                        break
                            elif variable_value == '不使用' or variable_value == '':
                                input_list.append('')
                                continue
                            elif variable_value.startswith('$'):
                                input_list.append(variable_value)
                                continue
                            else:
                                print('通道输入变量有误！')
                        for result_value in part['result_name'][index_tunnel]:
                            if result_value == '不使用' or result_value == '':
                                output_list.append('')
                                continue
                            elif result_value.startswith('$'):
                                output_list.append(result_value)
                                continue
                            else:
                                print('通道结果变量有误！')
                        self.write_tunnel(self.tunnel_config[tunnel_part]['position'], input_list, output_list)
                        command = 'python ./logs/tmp/tunnel_tmp.py'
                        self.curr_result_file = 'tunnel_logs_' + self.tunnel_config[tunnel_part]['name']
                        self.thread_log_no += 1
                        self.thread_log.run_('###################    当前阶段： ' + str(curr_section) + '/' + str(all_section) + '    ###################')
                        self.thread_log.run_('> ' + command)
                        self.exec_command(command)
                else:
                    print('type error!')
            print('任务结束：' + self.task_input_dict['task_name'])
            self.thread_log.run_('###################    任务完成    ###################')
            self.thread_log.run_('###################    任务目录： logs/' + self.task_dir + '    ###################')
            self.trigger_status.emit(self.task_input_dict['task_name'], '已完成')
        except Exception as e:
            print(e, 'TaskThread', 'run')

    # 定时任务开始倒计时
    def start_timer(self):
        try:
            self.remain_time = self.task_input_dict['time']
            while self.remain_time:
                self.remain_time -= 1
                time.sleep(1)
                self.trigger_timer.emit(self.task_input_dict['task_name'], self.remain_time)
        except Exception as e:
            print(e, 'TaskThread', 'start_timer')

    # 停止计时，立即执行任务
    def stop_timer(self):
        try:
            self.remain_time = 0
        except Exception as e:
            print(e, 'TaskThread', 'stop_timer')

    # 任务暂停
    def task_suspend(self):
        try:
            self.pause_flag = True
            # self.pause.suspend()
            self.trigger_status.emit(self.task_input_dict['task_name'], '暂停中')
        except Exception as e:
            print(e, 'TaskThread', 'task_suspend')

    # 任务继续
    def task_continue(self):
        try:
            self.pause_flag = False
            # self.pause.resume()
            self.trigger_status.emit(self.task_input_dict['task_name'], '进行中')
        except Exception as e:
            print(e, 'TaskThread', 'task_continue')

    def log_emit(self, message):
        self.trigger_log.emit(self.task_input_dict['task_name'], message)
        # print(message)

    def log_mkdir(self):
        try:
            time = QDateTime.currentDateTime().toString('yyyy_MM_dd_hh_mm_ss')
            task_dir = self.task_input_dict['task_name'] + '_' + time
            os.mkdir('logs/' + task_dir)
            # if os.path.exists(path):
            #     pass
            return task_dir
        except Exception as e:
            print(e, 'TaskThread', 'log_mkdir')

    def write_tunnel(self, tunnel_dir, input_list, output_list):
        try:
            tunnel_tmp_func = []
            tunnel_tmp_input = ''
            tunnel_tmp_output = ''
            tunnel_tmp_main = f'''

if __name__ == '__main__':
    # try:
'''
            tunnel_tmp_main_head = ''
            tunnel_tmp_main_body = ''
            tunnel_tmp_main_tail = ''
            # 读取结果文件
            index = 0
            for i in input_list:
                if i.startswith('$'):
                    tunnel_tmp_main_head += f'''
    with open('./logs/{self.task_dir}/{i.lstrip('$')}.txt', 'r', encoding='utf-8') as f:
        input_{str(index + 1)} = f.read()
'''
                else:
                    tunnel_tmp_main_head += f'''
    input_{str(index + 1)} = '{i}'
'''
                tunnel_tmp_input += 'input_' + str(index + 1)
                if index < len(input_list) - 1:
                    tunnel_tmp_input += ', '
                index += 1
            # 写入结果文件
            index = 0
            for i in output_list:
                if i.startswith('$'):
                    tunnel_tmp_main_tail += f'''
    with open('./logs/{self.task_dir}/{i.lstrip('$')}.txt', 'w', encoding='utf-8') as f:
        f.write({'output_' + str(index + 1)})
'''
                tunnel_tmp_output += 'output_' + str(index + 1)
                if index < len(output_list) - 1:
                    tunnel_tmp_output += ', '
                index += 1
            # 执行函数
            tunnel_tmp_main_body += f'''
        {tunnel_tmp_output} = deal_data({tunnel_tmp_input})
'''
            # 连接三部分到脚本主函数中
            tunnel_tmp_main = tunnel_tmp_main + tunnel_tmp_main_head + tunnel_tmp_main_body + tunnel_tmp_main_tail + '''
    # except Exception as e:
    #     print(e)
    #     exit(0)
            '''
            # print(tunnel_tmp_main)
            with open(tunnel_dir, 'r', encoding='utf-8') as f:
                tunnel_tmp_func = f.readlines()
            with open('logs/tmp/tunnel_tmp.py', 'w', encoding='utf-8') as f:
                f.writelines(tunnel_tmp_func)
                f.write(tunnel_tmp_main)
            pass
        except Exception as e:
            print(e, 'TaskThread', 'write_tunnel')
            print('通道出错')

    def to_out(self, line):
        self.thread_log_no += 1
        self.thread_log.run_(line)
        # print('get：' + line)
        with open('logs/' + self.task_dir + '/' + self.curr_result_file, 'a', encoding='utf-8') as f:
            f.write(line + '\n')

    def to_err(self, line):
        self.thread_log_no += 1
        self.thread_log.run_(' !!! error: ' + line)
        with open('logs/' + self.task_dir + '/err_logs', 'a', encoding='utf-8') as f:
            f.write(self.curr_result_file + '：' + line + '\n')

    def exec_command(self, command):
        try:
            self.start_RealSignal_out = threading.Event()
            self.stop_RealSignal_out = threading.Event()
            self.start_RealSignal_err = threading.Event()
            self.stop_RealSignal_err = threading.Event()
            # 创建队列并执行
            self.queue_out = Queue()
            self.queue_err = Queue()
            print(2)
            self.exec_cmd = ExecThread(self, self.queue_out, self.queue_err, command)
            self.pause = psutil.Process(self.exec_cmd.pid)
            self.exec_cmd.start()
            print(3)
            # 创建队列读取函数并弹出日志
            self.thread_queue_out = ReadQueueThread(self.start_RealSignal_out, self.stop_RealSignal_out, self.ueue_out)
            self.thread_queue_err = ReadQueueThread(self.start_RealSignal_err, self.stop_RealSignal_err, self.queue_out)
            self.thread_queue_out.trigger.connect(self.to_out)
            self.thread_queue_err.trigger.connect(self.to_err)
            print(4)
            self.stop_RealSignal_out.set()
            self.start_RealSignal_out.clear()
            self.stop_RealSignal_err.set()
            self.start_RealSignal_err.clear()
            self.thread_queue_out.start()
            self.thread_queue_err.start()
            self.thread_queue_out.exit()
            self.thread_queue_err.exit()

            self.exec_cmd.join()
            while self.pause.is_running() or self.pause_flag:
                # print(self.pause_flag)
                time.sleep(0.5)
        except Exception as e:
            print(e, 'TaskThread', 'write_tunnel')


class CommandExecutionException(Exception):
    def __init__(self, command: str, exit_code: int) -> None:
        super().__init__(f"command executed fail with exit-code={exit_code}: {command}")


class TextReadLineThread(threading.Thread):
    def __init__(self, readline, callback, *args, **kargs) -> None:
        super().__init__(*args, **kargs)
        self.readline = readline
        self.callback = callback

    def run(self):
        for line in iter(self.readline, ""):
            if len(line) == 0:
                break
            self.callback(line)
