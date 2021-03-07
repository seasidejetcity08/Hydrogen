from multiprocessing import Process, Pipe
from uuid import uuid4


class ProcessManager(object):
    def __init__(self, is_use_pipe=False):
        self.__process = None
        self.__is_use_pipe = False
        self.__parent_conn = None
        self.__child_conn = None
        if is_use_pipe == True:
            self.__create_pipe()

    @property
    def parent_conn(self):
        return self.__parent_conn
    
    @property
    def child_conn(self):
        return self.__child_conn

    def __create_pipe(self):
        self.__parent_conn, self.__child_conn = Pipe()
        self.__is_use_pipe = True

    def kick(self, target, args={}):
        if self.child_conn is not None:
            args["child_conn"] = self.child_conn
        self.__process = Process(target=target, args=(args,))
        self.__process.start()
        #self.parent_conn.send({
        #    "hoge": "hoge"
        #})
        return

    def is_alive(self):
        if self.__process is None:
            return False
        return self.__process.is_alive()

    def exitcode(self):
        if self.__process is None:
            return None
        return self.__process.exitcode()

    def send_packet(self, packet):
        if packet is not None:
            if self.parent_conn is not None:
                self.parent_conn.send(packet)