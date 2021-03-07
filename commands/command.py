import time

from utils import ProcessManager


process_manager = None

def kick_process():
    global process_manager
    process_manager = ProcessManager(is_use_pipe=True)
    process_manager.kick(target=chile_process)

def get_status():
    global process_manager
    is_alive = False
    if process_manager is not None:
        is_alive = process_manager.is_alive()
    return is_alive

def exit_process():
    global process_manager
    if process_manager.is_alive() is not None:
        packet = {
            "is_exit": True
        }
        process_manager.send_packet(packet)

def chile_process(args):
    child_conn = args["child_conn"]
    sleep_time = 3
    is_exit = False
    while is_exit == False:
        print("[child_process] wake up...")
        if child_conn.poll(sleep_time):
            packet = child_conn.recv()
            if packet is not None:
                keys = packet.keys()
                if "test_data" in keys:
                    print("[test_data] " + packet["test_data"])
                if "is_exit" in keys:
                    is_exit = packet["is_exit"]
                
