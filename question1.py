import argparse
parser = argparse.ArgumentParser(description='Problem of sets and their unique elements')
parser.add_argument('-n',type=int, help='(1 <= N <= 1000)')
parser.add_argument('-k', type=int, nargs='+', help='(-1000 <= K <= 1000)')
parser.add_argument('-f', '--filepath', help='if filepath defined disregards N and K')
"""
example file content:
4
10
10
9
8
"""


def run_question(N, K):
    """
    Problem of sets and their unique elements


    :param N: (1 <= N <= 1000)
    :param K: N Intergers (-1000 <=K <= 1000)
    :return: set of K in  ascending order
    """
    if N < 1 or N > 1000:
        raise ValueError("Invalid value for N (1 <= N <= 1000))")

    if any([True if i < -1000 or i > 1000 else False for i in K]):
        raise ValueError("Invalid value for K (-1000 <= K <= 1000))")

    if len(K) != N:
        raise ValueError("Please the K size must be equal to N ")

    result = list(set(K))
    result.sort()
    return result


def read_file(file_path):
    n, k = None, []
    with open(file_path) as file:
        count = 0
        for line in file:
            if count == 0:
                n = int(line)
            else:
                k.append(int(line))
            count += 1

    return n, k


if __name__ == '__main__':
    arguments = parser.parse_args()
    filepath = arguments.filepath
    k = arguments.k
    n = arguments.n

    if filepath:
        try:
            n, k = read_file(filepath)
        except ValueError as e:
            raise ValueError("Please check your file all lines must be an integer")
    else:
        if not n and not k:
            raise ValueError('Please informe a filepath or N and K values')

    result = run_question(n, k)
    print(result)


