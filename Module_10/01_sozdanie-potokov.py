import time
from threading import Thread


def output(tpl):
    for el in tpl:
        print(el, flush=True)
        time.sleep(1)


thread = Thread(target=output, args=(range(1, 11), ))
thread.start()
time.sleep(0.001)
output((chr(i) for i in range(ord('a'), ord('a') + 10)))
thread.join()
