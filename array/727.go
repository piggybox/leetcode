// Remove Duplicates from Sorted Array

package main

import "fmt"

func removeDuplicates(nums []int) int {
	if len(nums) == 0 {
		return 0
	}

	// two points to keep track of tidied data and raw data
	pa := 0

	for pb := 1; pb < len(nums); pb++ {
		if nums[pb] != nums[pa] {
			pa++
			nums[pa] = nums[pb]
		}
	}

	return pa + 1 // length
}

func main() {
	// list := []int{-3, -3, -2, -1, -1, 0, 0, 0, 0, 0 }
	// list := []int{0, 0, 1, 1, 1, 2, 2, 3, 3, 4, 4}
	// list := []int{1, 1, 2, 2, 3, 3}
	// list := []int{1, 1, 2, 2, 3}
	// list := []int{1, 1, 2}
	list := []int{1, 1}
	result := removeDuplicates(list)
	fmt.Println(result)
	for i := 0; i < result; i++ {
		fmt.Print(list[i], ",")
	}
}
