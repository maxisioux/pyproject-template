"""
@Author: Sioux
@File: logger.py
@Time: 2024/5/10 22:12
@Desc: It's a logger base on loguru.
@Refer: https://loguru.readthedocs.io/en/stable/overview.html
"""
import datetime
import os
import sys
from functools import wraps

import loguru

"""
github: https://github.com/Delgan/loguru
Python loguru有以下优点
简单易用：Loguru 提供了简洁明了的 API，只需导入模块，一行代码即可调用。
灵活性：Loguru 支持多种输出方式（如控制台、文件等），并且可以自定义输出格式和级别。
高效性：Loguru 使用了异步 I/O 技术，可以提高日志记录的效率。
兼容性：Loguru 兼容 Python 3.5+ 版本，可以在各种环境下使用。
功能丰富：Loguru 支持多种日志级别、过滤器、上下文管理，捕获异常等功能，可以满足不同场景的需求
"""

"""
# rotation='00:00': 设置每天 0 点新创建一个 log 文件
# retention='15 days': 设置日志文件最长保留 15 天
# enqueue = True: Asynchronous, Thread-safe, Multiprocess-safe
# backtrace=True: Logging exceptions by logger.exception("What?!")
"""

###############################################################################
DEFAULT_LEVEL="TRACE"

DEFAULT_FORMAT=(
    "<g>{time:YYYY-MM-DD HH:mm:ss.SSS}</g>"
    "<lr>|</lr>"
    "{process.id}"
    "<lr>|</lr>"
    # "{thread}"
    # "<lr>|</lr>"
    "<level>{level.name:<8}</level>"
    "<lr>|</lr>"
    "<c><{file}:{line}></c>"
    "{level.icon:^3}"
    "<level>{message}</level>"
)


# 单例类的装饰器
def singleton_logger_decorator(cls):
    """
    装饰器，单例类的装饰器
    """
    # 在装饰器里定义一个字典，用来存放类的实例。
    _instance = {}

    # 装饰器，被装饰的类
    @wraps(cls)
    def wrapper_class(*args, **kwargs):
        # 判断，类实例不在类实例的字典里，就重新创建类实例
        if cls not in _instance:
            # 将新创建的类实例，存入到实例字典中
            _instance[cls] = cls(*args, **kwargs)
        # 如果实例字典中，存在类实例，直接取出返回类实例
        return _instance[cls]

    # 返回，装饰器中，被装饰的类函数
    return wrapper_class


@singleton_logger_decorator
class Logger:
    """
    Loguru 简单封装
    """
    def __init__(self):
        self.remove_all()
        self.set_icon()
        self.add_console()
        self.add_file()

        loguru.logger.info(self.get_log_path())

    def set_icon(self):
        loguru.logger.level("TRACE", icon="🦉")
        loguru.logger.level("SUCCESS", icon="🐉")
        loguru.logger.level("DEBUG", icon="🔧")
        loguru.logger.level("INFO", icon="😋")
        loguru.logger.level("ERROR", icon="❌")
        loguru.logger.level("WARNING", icon="⛔")
        loguru.logger.level("CRITICAL", icon="🐛")

    def get_project_path(self, project_path=None):
        if project_path is None:
            # 当前项目文件的，绝对真实路径
            # 路径，一个点代表当前目录，两个点代表当前目录的上级目录
            project_path = os.path.realpath("..")
        # 返回当前项目路径
        return project_path

    def get_log_path(self):
        # 项目目录
        project_path = self.get_project_path()
        # 项目日志目录
        project_log_dir = os.path.join(project_path, "log")
        # 日志文件名
        project_log_filename = f"app_{datetime.date.today()}.log"
        # 日志文件路径
        project_log_path = os.path.join(project_log_dir, project_log_filename)
        # 返回日志路径
        return project_log_path

    def remove_all(self):
        loguru.logger.remove()

    def add_console(self):
        loguru.logger.add(
            # 水槽，分流器，可以用来输入路径
            sink=sys.stdout,
            # 默认输出级别
            level=DEFAULT_LEVEL,
            # 默认输出格式
            format=DEFAULT_FORMAT,
            # 具有使日志记录调用非阻塞的优点
            enqueue=True,
            # logging 异常
            backtrace=True,
            # 分颜色输出
            colorize=True,
        )

    def add_file(self):
        loguru.logger.add(
            # 水槽，分流器，可以用来输入路径
            sink=self.get_log_path(),
            # 默认输出级别
            level=DEFAULT_LEVEL,
            # 默认输出格式
            format=DEFAULT_FORMAT,
            # 日志创建周期
            rotation="00:00",
            # 保存
            retention="30 days",
            # 文件的压缩格式
            # compression='zip',
            # 编码格式
            encoding="utf-8",
            # 具有使日志记录调用非阻塞的优点
            enqueue=True,
            # logging 异常
            backtrace=True,
        )

    @property
    def get_logger(self):
        return loguru.logger


"""
# 实例化日志类
"""
logger = Logger().get_logger


if __name__ == "__main__":
    logger.success("success message")
    logger.trace("trace message")
    logger.debug("debug message")
    logger.info("info message")
    logger.warning("warning message")
    logger.error("error message")
    logger.critical("critical message")

    try:
        a = 5 / 0
    except ZeroDivisionError:
        logger.exception("What?!")

    """
    在其他.py文件中，只需要直接导入已经实例化的logger类即可
    例如导入访视如下：
    from project.logger import logger
    然后直接使用logger即可
    """
    logger.info("----原始测试----")
