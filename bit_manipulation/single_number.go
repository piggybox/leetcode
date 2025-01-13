// Single Number

package main

import "fmt"

func singleNumber(nums []int) int {
	hash := make(map[int]uint8)

	for _, num := range nums {
		hash[num] += 1
	}

	for k, v := range hash {
		if v == 1 {
			return k
		}
	}

	return -1
}

func main() {
	list := []int{4, 1, 2, 1, 2}
	result := singleNumber(list)
	fmt.Println(result)
}
