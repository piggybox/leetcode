// Contains Duplicate

package main

import "fmt"

func containsDuplicate(nums []int) bool {
	hash := make(map[int]bool)

	for i := 0; i < len(nums); i++ {
		_, exists := hash[nums[i]]
		if exists {
			return true
		} else {
			hash[nums[i]] = true
		}
	}

	return false
}

func main() {
	// list := []int{1, 2, 3, 1}
	list := []int{1, 2, 3, 4}
	// list := []int{7, 6, 4, 3, 1}
	result := containsDuplicate(list)
	fmt.Println(result)
}
