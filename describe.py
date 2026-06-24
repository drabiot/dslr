# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    describe.py                                        :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: tchartie <tchartie@student.42.fr>          +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2026/06/24 14:22:11 by tchartie          #+#    #+#              #
#    Updated: 2026/06/24 16:10:57 by tchartie         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

from sys import argv
from pandas import read_csv, DataFrame
from dslr_lib.functions import ft_count, ft_mean, ft_std, ft_min, ft_quantile, ft_max

def describe(data : DataFrame):
	numeric = data.select_dtypes(include='number').drop(columns=['Index'], errors='ignore')

	stats = {
		'count': ft_count(numeric),
		'mean':  ft_mean(numeric),
		'std':   ft_std(numeric),
		'min':   ft_min(numeric),
		'25%':   ft_quantile(numeric,0.25),
		'50%':   ft_quantile(numeric, 0.50),
		'75%':   ft_quantile(numeric, 0.75),
		'max':   ft_max(numeric),
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
