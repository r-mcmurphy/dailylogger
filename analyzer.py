"""Ok, let's face it - I suck at math, so it's likely that I messed
   up some widely known naming conventions and am doing stuff in a very
   naive childish way. I'm trying my best to avoid any kind of mistakes.
   At the end of the day, what I care for is the essence, not the form.

   I'm also aware that such things as numpy and scipy exist. I just wanna
   try to figure this stuff out on my own.

   P.S. This part is currently under construction."""


class Analyzer:
    @staticmethod
    def count_sum(array):
        return sum(array)

    @staticmethod
    def count_max_value(array):
        return max(array)

    @staticmethod
    def count_min_value(array):
        return min(array)

    @staticmethod
    def count_mean(array):
        return sum(array)/len(array)

    @staticmethod
    def count_median(array):
        arr = sorted(array)
        if len(arr) % 2 == 0:
            return (arr[int(len(arr)/2)-1] + arr[int(len(arr)/2)]) / 2
        else:
            return arr[len(arr)//2]

    @staticmethod
    def count_standard_deviation(samples):
        mean = sum(samples)/len(samples)
        variance = sum([(x-mean)**2 for x in samples])/len(samples)
        standard_deviation = variance**0.5
        return standard_deviation

    @staticmethod
    def count_covariance(array_1, array_2):
        raise NotImplementedError

    @staticmethod
    def count_pearsons_correlation(array_1, array_2):             # check it
        a = list(map(lambda x: x-sum(array_1)/len(array_1), array_1))
        b = list(map(lambda x: x-sum(array_2)/len(array_2), array_2))
        ab = list(map(lambda x, y: x*y, a, b))
        a2 = list(map(lambda x: x*x, a))
        b2 = list(map(lambda x: x*x, b))
        return sum(ab) / (sum(a2)*sum(b2))**0.5

    @staticmethod
    def count_spearmans_correlation(array_1, array_2):
        raise NotImplementedError
