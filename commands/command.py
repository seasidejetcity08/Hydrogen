import time

from utils import ProcessManager


process_manager = None

def kick_process():
    global process_manager
    args = {}
    args["hoge"] = "hoge"
    process_manager = ProcessManager(is_use_pipe=True)
    process_manager.kick(target=chile_process, args=args)
    return

def chile_process(args):
    is_exit = False
    sleep_time = 1
    child_conn = args["child_conn"]
    print(args["hoge"])
    while is_exit == False:
        time.sleep(sleep_time)
        bean = child_conn.recv()
        print("[child] Data1 : " + bean["Data1"])
        

# API's
