from multiprocessing import Process, Pipe
from uuid import uuid4


class ProcessManager(object):

    __instance = None

    def __init__(self):
        self.__repository = {}
        self.__processes = {}

    def create_repository(self):
        key = uuid4()
        self.__repository[key] = {}
        return key
    
    def create_pipe(self, key):
        parent_conn, child_conn = Pipe()
        self.__repository[key]["parent_conn"] = parent_conn
        self.__repository[key]["child_conn"] = child_conn

    def get_parent_conn(self, key):
        return self.__repository[key]["parent_conn"]

    def kick(self, key, func, args={}):
        keys = self.__repository[key].keys()
        if "parent_conn" in keys and "child_conn" in keys:
            args["child_conn"] = self.__repository[key]["child_conn"]
        process = Process(target=func, args=args)
        process.start()
        self.__processes[key]["pid"] = pid
        self.__processes[key]["process"] = process
        return process.pid

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

    @classmethod
    def new(cls):
        if cls.__instance is None:
            cls.__instance = ProcessManager()
        return cls.__instance
