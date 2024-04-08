import time
from threading import Thread


def output(tpl=None):
    for el in tpl:
        print(el, flush=True)
        time.sleep(1)


thread = Thread(target=output, kwargs=dict(tpl=(range(1, 11))))
thread.start()
time.sleep(0.5)
output((chr(i) for i in range(ord('a'), ord('a') + 10)))
thread.join()
