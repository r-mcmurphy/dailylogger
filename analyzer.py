"""Ok, let's face it - I suck at math, so it's likely that I messed
   up some widely known naming conventions and am doing stuff in a very
   naive childish way. I'm trying my best to avoid any kind of mistakes.
   At the end of the day, what I care for is the essence, not the form.

   I'm also aware that such things as numpy and scipy exist. I just wanna
   try to figure this stuff out on my own.

   P.S. This part is currently under construction."""

class Analyzer():

	def count_sum(self, array):
		return sum(array)

	def count_max_value(self, array):
		return max(array)

	def count_min_value(self, array):
		return min(array)

	def count_mean(self, array):
		return sum(array)/len(array)

	def count_median(self, array):
		arr = sorted(array)
		if len(arr) % 2 == 0:
			return (arr[int(len(arr)/2)-1] + arr[int(len(arr)/2)]) / 2
		else:
			return arr[len(arr)//2]

	def count_standard_deviation(self, samples):
		mean = sum(samples)/len(samples)
		variance = sum([(x-mean)**2 for x in samples])/len(samples)
		standard_deviation = variance**0.5
		return standard_deviation

	def count_covariance(self, array_1, array_2):
		raise NotImplementedError

	def count_pearsons_correlation(self, array_1, array_2):				# check it
		a = list(map(lambda x: x-sum(array_1)/len(array_1), array_1))
		b = list(map(lambda x: x-sum(array_2)/len(array_2), array_2))
		ab = list(map(lambda x, y: x*y, a, b))
		a2 = list(map(lambda x: x*x, a))
		b2 = list(map(lambda x: x*x, b))
		return sum(ab) / (sum(a2)*sum(b2))**0.5

	def count_spearmans_correlation(self, array_1, array_2):
		raise NotImplementedError


# - Create analytical system 
# 	It should:
# 		- give raw numbers (raw, max, min, avg, median)
# 		- analyze each trackable's tendencies
# 		- search for relations in user's data (correlation / covariance)
# 		- search for any relation between data and time (part of day / week / month / year)
# 		- search for any other periodicality (see if there is a time pattern in data)
# 		- ...?