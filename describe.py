# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    describe.py                                        :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: tchartie <tchartie@student.42.fr>          +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2026/06/24 14:22:11 by tchartie          #+#    #+#              #
#    Updated: 2026/06/24 14:38:33 by tchartie         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

from sys import argv
from pandas import read_csv, DataFrame

def main():
	try:
		assert len(argv) == 2
		data : DataFrame = read_csv(argv[1])
		print(data)
	except:
		return (1)
	return (0)

if __name__ == "__main__":
	main()
