import math

import matplotlib.pyplot as plt
from collections import Counter

num_friends = [100, 49, 41, 40, 25, 21, 21, 19, 19, 18,
               18, 16, 15, 15, 15, 15, 14, 14, 13, 13,
               13, 13, 12, 12, 11, 10, 10, 10, 10, 10,
               10, 10, 10, 10, 10, 10, 10, 10, 10, 10,
               9, 9, 9, 9, 9, 9, 9, 9, 9, 9,
               9, 9, 9, 9, 9, 9, 9, 9, 8, 8,
               8, 8, 8, 8, 8, 8, 8, 8, 8, 8,
               8, 7, 7, 7, 7, 7, 7, 7, 7, 7,
               7, 7, 7, 7, 7, 7, 6, 6, 6, 6,
               6, 6, 6, 6, 6, 6, 6, 6, 6, 6,
               6, 6, 6, 6, 6, 6, 6, 6, 5, 5,
               5, 5, 5, 5, 5, 5, 5, 5, 5, 5,
               5, 5, 5, 5, 5, 4, 4, 4, 4, 4,
               4, 4, 4, 4, 4, 4, 4, 4, 4, 4,
               4, 4, 4, 4, 4, 3, 3, 3, 3, 3,
               3, 3, 3, 3, 3, 3, 3, 3, 3, 3,
               3, 3, 3, 3, 3, 2, 2, 2, 2, 2,
               2, 2, 2, 2, 2, 2, 2, 2, 2, 2,
               2, 2, 1, 1, 1, 1, 1, 1, 1, 1,
               1, 1, 1, 1, 1, 1, 1, 1, 1, 1,
               1, 1, 1, 1]


def median(arr):
    arr = sorted(arr)
    length = len(arr)
    if length % 2 == 0:
        middle = int(length / 2)
    else:
        middle = int(length // 2)
    return arr[middle]


def quantile(arr, percent):
    place = int(len(arr) * percent)
    return sorted(arr)[place]


def data_range(arr):
    return max(arr) - min(arr)


def mean_deviation(arr):
    my_median = median(arr)
    return [i - my_median for i in arr]


def variance(arr):
    deviations = mean_deviation(arr)
    return sum([k ** 2 for k in deviations]) / (len(deviations) - 1)


def standard_deviation(arr):
    return math.sqrt(variance(arr))


def interquantile_range(arr):
    return quantile(arr, 0.75) - quantile(arr, 0.25)


print('Variance:', variance(num_friends))
print('Data range:', data_range(num_friends))
print('Quantile 10%:', quantile(num_friends, 0.10))
print('Quantile 25%:', quantile(num_friends, 0.25))
print('Quantile 75%:', quantile(num_friends, 0.75))
print('Quantile 90%:', quantile(num_friends, 0.90))
print('Num of points:', len(num_friends))
print('Minimum of friends:', min(num_friends))
print('Maximum of friends:', max(num_friends))
mean_of_friends = sum(num_friends) / len(num_friends)
print('Number of friends mean', mean_of_friends)
friends_count = Counter(num_friends)
xs = range(max(friends_count) + 1)
ys = [friends_count[f] for f in xs]
plt.axis([0, max(xs) + 1, 0, max(ys) + 1])
plt.bar(xs, ys, color='red', label='friends count')

friends_count_md = Counter(mean_deviation(num_friends))
ys_md = [friends_count_md[f] for f in xs]
plt.bar(xs, ys_md, color='magenta', label='friends count mean_dispersion')
plt.hlines(mean_of_friends, xmin=0, xmax=max(xs) + 1, colors='green', label='mean')
plt.vlines(median(num_friends), ymin=0, ymax=max(ys), colors='orange', label='median')

plt.vlines(quantile(num_friends, 0.10), ymin=0, ymax=max(ys), colors='red', label='quantile 10%')
plt.vlines(quantile(num_friends, 0.25), ymin=0, ymax=max(ys), colors='pink', label='quantile 25%')
plt.vlines(quantile(num_friends, 0.75), ymin=0, ymax=max(ys), colors='yellow', label='quantile 75%')
plt.vlines(quantile(num_friends, 0.90), ymin=0, ymax=max(ys), colors='brown', label='quantile 90%')
plt.xlabel('friends amount')
plt.ylabel('frequency')
plt.legend(loc='lower right')
plt.show()

median(num_friends)
