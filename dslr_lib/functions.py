# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    functions.py                                       :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: tchartie <tchartie@student.42.fr>          +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2026/06/24 15:53:29 by tchartie          #+#    #+#              #
#    Updated: 2026/06/24 17:15:24 by tchartie         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

from pandas import DataFrame

def ft_count(data: DataFrame):
	result = {}
	for col in data.columns:
		count = 0
		for val in data[col]:
			if val == val:
				count += 1
		result[col] = count
	return (result)

def ft_mean(data: DataFrame):
	result = {}
	for col in data.columns:
		total = 0
		count = 0
		for val in data[col]:
			if val == val:
				total += val
				count += 1
		result[col] = total / count
	return (result)

def ft_std(data: DataFrame):
	result = {}
	mean = ft_mean(data)
	for col in data.columns:
		total = 0
		count = 0
		for val in data[col]:
			if val == val:
				total += (val - mean[col]) ** 2
				count += 1
		result[col] = (total / (count - 1)) ** 0.5
	return (result)

def ft_min(data: DataFrame):
	result = {}
	for col in data.columns:
		min_val = None
		for val in data[col]:
			if val == val:
				if min_val is None or val < min_val:
					min_val = val
		result[col] = min_val
	return (result)

def ft_max(data: DataFrame):
	result = {}
	for col in data.columns:
		max_val = None
		for val in data[col]:
			if val == val:
				if max_val is None or val > max_val:
					max_val = val
		result[col] = max_val
	return (result)

def ft_quantile(data: DataFrame, percent: float):
	result = {}
	for col in data.columns:
		values = sorted([val for val in data[col] if val == val])
		n = len(values)
		index = percent * (n - 1)
		low = int(index)
		high = low + 1
		frac = index - low
		if high >= n:
			result[col] = values[low]
		else:
			result[col] = values[low] + frac * (values[high] - values[low])
	return (result)
