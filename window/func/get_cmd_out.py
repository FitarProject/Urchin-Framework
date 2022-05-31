import logging
import subprocess
import shlex
import threading

# _logger_trans = {
#     "DEBUG": "DBG",
#     "INFO": "INF",
#     "WARNING": "WAR",
#     "CRITICAL": "ERR"
# }
# _old_factory = logging.getLogRecordFactory()
#
#
# def factory(name, level, fn, lno, msg, args, exc_info, func=None, sinfo=None, **kwargs) -> logging.LogRecord:
#     record = _old_factory(name, level, fn, lno, msg, args, exc_info, func, sinfo, **kwargs)
#     record.shortlevelname = _logger_trans[record.levelname]
#     return record
#
#
# logging.setLogRecordFactory(factory)
# logging.basicConfig(
#     level=logging.DEBUG,
#     format='[%(asctime)s %(shortlevelname)s] %(message)s',
#     datefmt="%Y/%m/%d %H:%M:%S"
# )


class CommandExecutionException(Exception):
    def __init__(self, command: str, exit_code: int) -> None:
        super().__init__(f"command executed fail with exit-code={exit_code}: {command}")


_logger = logging.getLogger(__name__)


class TextReadLineThread(threading.Thread):
    def __init__(self, readline, callback, *args, **kargs) -> None:
        super().__init__(*args, **kargs)
        self.readline = readline
        self.callback = callback

    def run(self):
        for line in iter(self.readline, ""):
            if len(line.encode('utf-8')) == 0:
                break
            self.callback(line.encode('utf-8'))


def cmd_exec(command: str, ensure_success: bool=True) -> int:
    _logger.info("############ executing command: {} ############\n".format(command))

    cmd = shlex.split(command)

    process = subprocess.Popen(
        cmd,
        shell=True,
        text=True,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        )

    # _logger.debug("started command")

    def log_warp(func):
        def _wrapper(line: str):
            return func(line.strip().decode('utf-8'))
        return _wrapper

    read_stdout = TextReadLineThread(process.stdout.readline, log_warp(_logger.info))
    read_stderr = TextReadLineThread(process.stderr.readline, log_warp(_logger.warning))
    read_stdout.start()
    read_stderr.start()

    read_stdout.join()
    # _logger.debug("stdout reading finish")
    read_stderr.join()
    # _logger.debug("stderr reading finish")
    try:
        outs, errs = process.communicate(timeout=15)
    except subprocess.CalledProcessError:
        process.kill()
        outs, errs = process.communicate()
        read_stdout.terminate()
        read_stderr.terminate()
        print(outs, errs)
    ret = process.wait()
    # _logger.debug("process finish")

    _logger.info("\n############ executed command with exit-code={} ############".format(ret))
    if ensure_success and ret != 0:
        raise CommandExecutionException(command=command, exit_code=ret)
    return ret


# if __name__ == '__main__':
#     _logger_trans = {
#             "DEBUG": "DBG",
#             "INFO": "INF",
#             "WARNING": "WAR",
#             "CRITICAL": "ERR"
#         }
#     _old_factory = logging.getLogRecordFactory()
#     def factory(name, level, fn, lno, msg, args, exc_info, func=None, sinfo=None, **kwargs)->logging.LogRecord:
#         record = _old_factory(name, level, fn, lno, msg, args, exc_info, func, sinfo, **kwargs)
#         record.shortlevelname = _logger_trans[record.levelname]
#         return record
#     logging.setLogRecordFactory(factory)
#     logging.basicConfig(
#         level=logging.DEBUG,
#         format='[%(asctime)s %(shortlevelname)s] %(message)s',
#         datefmt="%Y/%m/%d %H:%M:%S"
#     )
#     cmd_exec("ping localhost1", ensure_success=False)
