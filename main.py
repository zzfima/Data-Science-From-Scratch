from collections import Counter
from functools import partial, reduce
from matplotlib import pyplot as plt
import math


# years = [1950, 1960, 1970, 1980, 1990, 2000, 2010]
# gdp = [300.2, 543.3, 1075.9, 2862.5, 5979.6, 10289.7, 14958.3]
#
# plt.plot(years, gdp, color='green', marker='*',
# =':')
# plt.title('GDP per years')
# plt.ylabel('x1.000.000.000$')
# plt.xlabel('years')
# plt.show()


# movies = ["Энни Холл", "Бен-Гур", "Касабланка", "Ганди", "Вестсайдская история"]
# num_oscars = [5, 11, 3, 8, 10]
#
# xs = [i for i, _ in enumerate(movies)]
#
# plt.bar(xs, num_oscars)
# plt.xticks([i for i, _ in enumerate(movies)], movies)
# plt.show()

# grades = [83, 95, 91, 87, 70, 0, 85, 82, 100, 67, 73, 77, 0]
# decile = lambda grade: grade // 10 * 10
# histogram = Counter(decile(grade) for grade in grades)
# plt.bar(x=[x for x in histogram.keys()], height=[x for x in histogram.values()], width=7)
# plt.title('Students score')
# plt.xlabel('Decile grade')
# plt.ylabel('Students amount')
# plt.axis([-10, 110, 0, 5])
# plt.show()

# variance = [1, 2, 4, 8, 16, 32, 64, 128, 256]  # dispersion
# bias_squared = [256, 128, 64, 32, 16, 8, 4, 2, 1]  # square of bias
# total_error = [x + y for x, y in zip(variance, bias_squared)]
# xs = [i for i, _ in enumerate(variance)]  # x axis
#
# plt.plot(xs, variance, 'g-', label='dispersion')  # show variance
# plt.plot(xs, bias_squared, 'r-', label='squared bias')  # show squared bias
# plt.plot(xs, total_error, 'b:', label='total error')  # show total error
# plt.legend(loc=9)  # labels location
# plt.xlabel('Model complexity')
# plt.show()

# friends = [70, 65, 72, 63, 71, 64, 60, 64, 67]
# minutes = [175, 170, 205, 120, 220, 130, 105, 145, 190]
# labels = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i']
#
# plt.scatter(friends, minutes, marker='o')
# plt.axis([0, 80, 0, 250])
# for f, m, l in zip(friends, minutes, labels):
#     plt.annotate(l, xy=(f + 0.2, m - 5))
# plt.title('Dependency of friends amount and time in FB')
# plt.xlabel('Friends')
# plt.ylabel('Time')
# plt.show()

def vectors_add(v, w):
    return [x_v + y_v for x_v, y_v in zip(v, w)]


def vectors_sub(v, w):
    return [x_v - x_w for x_v, x_w in zip(v, w)]


def multi_vectors_add(vectors):
    vec_sum = vectors[0]

    for v in vectors[1:]:
        vec_sum = vectors_add(vec_sum, v)
    return vec_sum


def scalar_mul(c, v):
    return [c * i for i in v]


def num_add(a, b):
    return a + b


def mean_vectors(vectors):
    return scalar_mul(1 / len(vectors), multi_vectors_add(vectors))


multi_vectors_add_1 = partial(reduce, vectors_add)

v1 = [1, 2]
v2 = [3, 4]
v3 = vectors_add(v1, v2)
v3_1 = multi_vectors_add([v1, v2, v3])
v3_2 = multi_vectors_add_1([v1, v2, v3])
v4 = vectors_sub(v3, v1)

print(v3, v3_1, v3_2, v4)

grades = [4, 2, 3, 8]
print(reduce(num_add, grades))
print(scalar_mul(4, v1))
print(mean_vectors([[1, 2], [2, 3], [5, 5], [8, 2]]))


def dot(v, w):
    return sum(i1 * i2 for i1, i2 in zip(v, w))


print(dot([5, 6], [3, 2]))


def magnitude(v):
    return math.sqrt(dot(v, v))


print(magnitude([4, 5]))

# matrix n * k => n = 2 k = 3
A = [[1, 2, 3],
     [5, 4, 3]]


def matrix_shape(matrix):
    rows = len(matrix)
    cols = len(matrix[0])
    return rows, cols


print(matrix_shape(A))


def get_raw(matrix, i):
    return matrix[i]


print(get_raw(A, 1))


def get_col(matrix, j):
    return [i[j] for i in matrix]


print(get_col(A, 1))


def show_matrix(matrix):
    for row in range(len(matrix)):
        print(matrix[row])


def make_matrix(num_rows, num_cols, f):
    return [[f(i, j)
             for i in range(num_cols)]
            for j in range(num_rows)]


show_matrix(make_matrix(4, 4, lambda i, j: i * j))

show_matrix(make_matrix(4, 4, lambda i, j: 1 if i == j else 0))

friendships = [(0, 1), (0, 2), (1, 2), (1, 3), (2, 3), (3, 4),
               (4, 5), (5, 6), (5, 7), (6, 8), (7, 8), (8, 9)]


def make_matrix_from_connections(connections):
    # find amount of rows and columns
    max_num = max(max(connections, key=lambda t: t[0] if t[0] > t[1] else t[1]))
    # build matrix of zeroes
    matrix = make_matrix(max_num + 1, max_num + 1, lambda i, j: 0)
    for t in range(len(connections)):
        con = connections[t]
        matrix[con[0]][con[1]] = 1
        matrix[con[1]][con[0]] = 1
    return matrix


show_matrix(make_matrix_from_connections(friendships))
