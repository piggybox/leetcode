// Best Time to Buy and Sell Stock II

package main

import "fmt"

func maxProfit(prices []int) int {
	i, j := 0, 1
	total := 0
	for j < len(prices) {
		if prices[j] > prices[i] {
			total += prices[j] - prices[i]
		}
		i += 1
		j += 1
	}

	return total
}

func main() {
	list := []int{7, 1, 5, 3, 6, 4}
	// list := []int{1, 2, 3, 4, 5}
	// list := []int{7, 6, 4, 3, 1}
	result := maxProfit(list)
	fmt.Println(result)
}
