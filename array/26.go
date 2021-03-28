package main

import "fmt"

// Remove Duplicates from Sorted Array

func removeDuplicates(nums []int) int {
	if len(nums) == 0 {
		return 0
	}

	// two points to keep track of tidied data and raw data
	pa, pb := 0, 0

	for pb < len(nums)-1 {
		// check duplicates
		for nums[pa] == nums[pb] {
			pb++

			// check if hitting the end
			// tricky part: the last part is duplicated or not
			if pb == len(nums)-1 && nums[pa] != nums[pb] {
				pa += 1
				nums[pa] = nums[pb]
				return pa + 1
			} else if pb == len(nums) {
				return pa + 1
			}
		}

		// move first non-duplicate to the next position after pa
		pa += 1
		nums[pa] = nums[pb]
	}

	return pa + 1 // length
}

func main() {
	// list := []int{-3, -3, -2, -1, -1, 0, 0, 0, 0, 0 }
	// list := []int{0, 0, 1, 1, 1, 2, 2, 3, 3, 4, 4}
	// list := []int{1, 1, 2, 2, 3, 3}
	// list := []int{1, 1, 2, 2, 3}
	// list := []int{1, 1, 2}
	list := []int{1, 2}
	result := removeDuplicates(list)
	fmt.Println(result)
	for i := 0; i < result; i++ {
		fmt.Print(list[i], ",")
	}
}
