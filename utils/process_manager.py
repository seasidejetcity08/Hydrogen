from multiprocessing import Process, Pipe
from uuid import uuid4


class ProcessManager(object):
    def __init__(self):
        self.__pid = None
        self.__parent_conn = None
        self.__child_conn = None

    @property
    def parent_conn(self):
        return self.__parent_conn
    
    @property
    def child_conn(self):
        return self.__child_conn

    def __create_pipe(self, key):
        self.__parent_conn, self.__child_conn = Pipe()

    def kick(self, target, args=None):
        process = Process(target=target, args=args)
        process.start()
        self.__pid = process.pid
        return self.__pid

    def exitcode(self, pid):
        process = self.__processes[pid]
        if process is None:
            return None
        return process.exitcode()

    def is_alive(self, pid):
        process = self.__processes[pid]
        if process is None:
            return False
        return process.is_alive()
