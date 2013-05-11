import time

from dijkstra import get_path


if __name__ == "__main__":
    start = time.time()
    get_path("input.txt", "A", "F")
    stop = time.time()
    print("{:.10f}".format(stop - start))