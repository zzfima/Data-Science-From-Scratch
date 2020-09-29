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

daily_minutes = [1, 68.77, 51.25, 52.08, 38.36, 44.54, 57.13, 51.4, 41.42, 31.22,
                 34.76, 54.01, 38.79, 47.59, 49.1, 27.66, 41.03, 36.73, 48.65, 28.12,
                 46.62, 35.57, 32.98, 35, 26.07, 23.77, 39.73, 40.57, 31.65, 31.21,
                 36.32, 20.45, 21.93, 26.02, 27.34, 23.49, 46.94, 30.5, 33.8, 24.23,
                 21.4, 27.94, 32.24, 40.57, 25.07, 19.42, 22.39, 18.42, 46.96, 23.72,
                 26.41, 26.97, 36.76, 40.32, 35.02, 29.47, 30.2, 31, 38.11, 38.18,
                 36.31, 21.03, 30.86, 36.07, 28.66, 29.08, 37.28, 15.28, 24.17, 22.31,
                 30.17, 25.53, 19.85, 35.37, 44.6, 17.23, 13.47, 26.33, 35.02, 32.09,
                 24.81, 19.33, 28.77, 24.26, 31.98, 25.73, 24.86, 16.28, 34.51, 15.23,
                 39.72, 40.8, 26.06, 35.76, 34.76, 16.13, 44.04, 18.03, 19.65, 32.62,
                 35.59, 39.43, 14.18, 35.24, 40.13, 41.82, 35.45, 36.07, 43.67, 24.61,
                 20.9, 21.9, 18.79, 27.61, 27.21, 26.61, 29.77, 20.59, 27.53, 13.82,
                 33.2, 25, 33.1, 36.65, 18.63, 14.87, 22.2, 36.81, 25.53, 24.62,
                 26.25, 18.21, 28.08, 19.42, 29.79, 32.8, 35.99, 28.32, 27.79, 35.88,
                 29.06, 36.28, 14.1, 36.63, 37.49, 26.9, 18.58, 38.48, 24.48, 18.95,
                 33.55, 14.24, 29.04, 32.51, 25.63, 22.22, 19, 32.73, 15.16, 13.9,
                 27.2, 32.01, 29.27, 33, 13.74, 20.42, 27.32, 18.23, 35.35, 28.48,
                 9.08, 24.62, 20.12, 35.26, 19.92, 31.02, 16.49, 12.16, 30.7, 31.22,
                 34.65, 13.13, 27.51, 33.2, 31.57, 14.1, 33.42, 17.44, 10.12, 24.42,
                 9.82, 23.39, 30.93, 15.03, 21.67, 31.09, 33.29, 22.61, 26.89, 23.48,
                 8.38, 27.81, 32.35, 23.84]


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


print('Interquantile range:', interquantile_range(num_friends))
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
