import numpy as np
from .base_distribution import BaseDistribution
class Dist_ks938(BaseDistribution):
	def __init__(self):
		self.x_min = 0
		self.x_max = 2.
		self.f_max = 1.5


	def pdf(self, x):
		"""This is your PDF"""
		return (3./8.)*(x**2.)

	def mean(self):
		"""This is the mean of the PDF"""
		return 0.5

	def std(self):
		"""This is the standard deviation of the pdf"""
		return np.sqrt(3./20.)
