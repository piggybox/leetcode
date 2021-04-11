// Sign of the Product of an Array

package main

import "fmt"

func arraySign(nums []int) int {
	result := 1
	for _, i := range nums {
		if i < 0 {
			result *= -1
		} else if i == 0 {
			result = 0
			break
		}
	}

	return result
}

func main() {
	// list := []int{-1, -2, -3, -4, 3, 2, 1}

	// list := []int{1, 5, 0, 2, -3}

	list := []int{-1, 1, -1, 1, -1}

	result := arraySign(list)
	fmt.Println(result)
}
