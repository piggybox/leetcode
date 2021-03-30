// Move zeros

package main

import "fmt"

func moveZeroes(nums []int) {
	// two pointers solution
	i, j := 0, 0
	for ; j < len(nums); j++ {
		// seek until finding a non-zero
		if nums[j] != 0 {
			// swap
			temp := nums[i]
			nums[i] = nums[j]
			nums[j] = temp

			i += 1
		}
	}
}

func main() {
	list := []int{0, 1, 0, 3, 12}
	// list := []int{0, 0, 1, 0, 0, 13, 0, 2}
	// list := []int{1}

	moveZeroes(list)
	fmt.Println(list)
}
