import time


def running_time(function):
    start_time = time.time()
    for i in range(20):
        function()
    end_time = time.time()
    print(end_time - start_time)