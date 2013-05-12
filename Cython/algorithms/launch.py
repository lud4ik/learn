import time

from dijkstra import Extract


if __name__ == "__main__":
    start = time.time()
    Extract().get_path("input.txt", "A", "F")
    stop = time.time()
    print("{:.10f}".format(stop - start))