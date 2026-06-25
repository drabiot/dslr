# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    describe.py                                        :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: tchartie <tchartie@student.42.fr>          +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2026/06/24 14:22:11 by tchartie          #+#    #+#              #
#    Updated: 2026/06/25 15:54:52 by tchartie         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

from sys import argv, path
path.append("..")
path.append(".")
path.append("./data_analysis")

from pandas import read_csv, DataFrame
from dslr_lib.functions import ft_count, ft_mean, ft_std, ft_min, ft_quantile, ft_max

def describe(data: DataFrame):
	numeric = data.select_dtypes(include='number').drop(columns=['Index'], errors='ignore')

	stats = {
		'count': {col: ft_count(numeric[col].dropna().values) 			for col in numeric.columns},
		'mean':  {col: ft_mean(numeric[col].dropna().values)			for col in numeric.columns},
		'std':   {col: ft_std(numeric[col].dropna().values)				for col in numeric.columns},
		'min':   {col: ft_min(numeric[col].dropna().values)				for col in numeric.columns},
		'25%':   {col: ft_quantile(numeric[col].dropna().values, 0.25)	for col in numeric.columns},
		'50%':   {col: ft_quantile(numeric[col].dropna().values, 0.50)	for col in numeric.columns},
		'75%':   {col: ft_quantile(numeric[col].dropna().values, 0.75)	for col in numeric.columns},
		'max':   {col: ft_max(numeric[col].dropna().values)				for col in numeric.columns},
	}
		
	result = DataFrame(stats).T
	print(result)
	return 0

def main():
	try:
		assert len(argv) == 2
		data : DataFrame = read_csv(argv[1])
		describe(data)
	except:
		return (1)
	return (0)

if __name__ == "__main__":
	main()
