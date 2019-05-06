
import sys
import time


class Stopwatch:

    # Construct self and start it running.
    def __init__(self):
        self._creationTime = time.time()  # Creation time

    # Return the elapsed time since creation of self, in seconds.
    def elapsedTime(self):
        return time.time() - self._creationTime


def main():
    n = int(input("enter the key"))

    total1 = 0.0
    watch1 = Stopwatch()
    for i in range(1, n + 1):
        total1 += i ** 2
    time1 = watch1.elapsedTime()

    total2 = 0.0
    watch2 = Stopwatch()
    for i in range(1, n + 1):
        total2 += i * i
    time2 = watch2.elapsedTime()

    print(total1 / total2)
    print(time1 / time2)


if __name__ == '__main__':
    main()
