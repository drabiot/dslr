# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    functions.py                                       :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: tchartie <tchartie@student.42.fr>          +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2026/06/25 15:53:19 by tchartie          #+#    #+#              #
#    Updated: 2026/06/25 16:09:38 by tchartie         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

from pandas import DataFrame


def ft_count(values: DataFrame) -> int:
	"""
	Compute the number of non-NaN rows in the given DataFrame.

	Args:
		values	(DataFrame): DataFrame to compute

	Returns:
		int: non-NaN rows in the given DataFrame
	"""
	return (len(values))


def ft_mean(values: DataFrame) -> float:
	"""
	Compute the number average of non-NaN values in the given DataFrame.

	Args:
		values	(DataFrame): DataFrame to compute

	Returns:
		float: average of the non-NaN values in the given DataFrame
	"""
	return (sum(values) / len(values))


def ft_std(values: DataFrame) -> float:
	"""
	Compute the standard deviation of non-NaN values in the given DataFrame.

	Args:
		values	(DataFrame): DataFrame to compute

	Returns:
		float: standard deviation of the non-NaN values in the given DataFrame
	"""
	m = ft_mean(values)
	return ((sum((v - m) ** 2 for v in values) / (len(values) - 1)) ** 0.5)


def ft_min(values: DataFrame) -> float:
	"""
	Find the minimum non-NaN value in the given DataFrame.

	Args:
		values	(DataFrame): DataFrame to compute

	Returns:
		float: minimun non-NaN values in the given DataFrame
	"""
	m = values[0]
	for v in values[1:]:
		if v < m:
			m = v
	return (m)


def ft_max(values: DataFrame) -> float:
	"""
	Find the maximum non-NaN value in the given DataFrame.

	Args:
		values	(DataFrame): DataFrame to compute

	Returns:
		float: maximum non-NaN values in the given DataFrame
	"""
	m = values[0]
	for v in values[1:]:
		if v > m:
			m = v
	return (m)


def ft_quantile(values: DataFrame, percent: float) -> float:
	"""
	Compute quantile of non-NaN value in the given DataFrame with the given percentile.

	Args:
		values	(DataFrame):	DataFrame to compute
		percent	(float):		Percentile as a decimal between 0 and 1

	Returns:
		float: The interpolated value at the given percentile
	"""
	sorted_vals = sorted(values)
	n = len(sorted_vals)
	index = percent * (n - 1)
	low = int(index)
	high = low + 1
	frac = index - low
	if high >= n:
		return (sorted_vals[low])
	return (sorted_vals[low] + frac * (sorted_vals[high] - sorted_vals[low]))
