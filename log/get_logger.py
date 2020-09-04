# 导包
import logging.handlers  # 导入logging时，logging的handler不会自动导入，所以handler需要单独导入
import os
from config import BASE_PATH

# 定义类


class GetLogger:
    # 定义日志器变量
    __logger=None
    # 获取日志器的方法
    @classmethod
    def get_logger(cls):
        # 判断日志器为空
        if cls.__logger is None:
            # 1.获取日志器
            cls.__logger=logging.getLogger()
            # 2.设置日志器默认级别
            cls.__logger.setLevel(logging.INFO)
            # 3.获取处理器handler  --此处使用的是以时间切割的处理器
            file_path=BASE_PATH + os.sep + "log" + os.sep + "hmtt.log"
            th=(logging.handlers.TimedRotatingFileHandler(filename=file_path,
                                                          when='midnight',
                                                          interval=1,
                                                          backupCount=3,
                                                          encoding='utf-8'))
            # 4.获取格式器formatter
            fmt="%(asctime)s %(levelname)s [%(filename)s %(funcName)s %(lineno)s] - %(message)s"
            fm=logging.Formatter(fmt)
            # 5.将格式器添加到处理器
            th.setFormatter(fm)
            # 6.将处理器添加到日志器
            cls.__logger.addHandler(th)
        # 返回日志器
        return cls.__logger


if __name__ == '__main__':
    log=GetLogger.get_logger()
    log.info('this info...')
    log.error('this is error...')
