import sys
import multiprocessing


def calculate_i_number(i: int) -> float:
    return 1/(1+((i-0.5) / int(sys.argv[1])) ** 2)


if __name__ == '__main__':
    koef = 4 / int(sys.argv[1])
    result_sum = 0.0
    with multiprocessing.Pool(multiprocessing.cpu_count())as p:
        list_sum = p.map(calculate_i_number, range(1, int(sys.argv[1]) + 1))

    for i in list_sum:
        result_sum += float(i)

    print(koef * result_sum)
