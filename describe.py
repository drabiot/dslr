# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    describe.py                                        :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: tchartie <tchartie@student.42.fr>          +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2026/06/24 14:22:11 by tchartie          #+#    #+#              #
#    Updated: 2026/06/24 15:45:10 by tchartie         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

from sys import argv
from pandas import read_csv, DataFrame
import numpy as np

def describe(data : DataFrame):
	numeric = data.select_dtypes(include='number').drop(columns=['Index'], errors='ignore')

	stats = {
		'count': numeric.count(),
		'mean':  numeric.mean(),
		'std':   numeric.std(),
		'min':   numeric.min(),
		'25%':   numeric.quantile(0.25),
		'50%':   numeric.quantile(0.50),
		'75%':   numeric.quantile(0.75),
		'max':   numeric.max(),
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
