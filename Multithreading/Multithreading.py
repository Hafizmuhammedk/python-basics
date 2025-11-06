import multiprocessing

import time


def square_numbers():
    for i in range(5):
        time.sleep(1)
        print(f"Hey this is the square. Square is {i * i}")


def cube_numbers():
    for i in range(5):
        time.sleep(1.5)
        print(f"Hey this is the cube. Cube is {i * i * i}")


if __name__ == "__main__":

    t1 = time.time()

    p1 = multiprocessing.Process(target=square_numbers)
    p2 = multiprocessing.Process(target=cube_numbers)

    p1.start()
    p2.start()

    p1.join()
    p2.join()

    t2 = time.time()
    print(f"Total time taken: {t2 - t1}")
