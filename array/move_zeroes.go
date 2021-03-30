// Move zeros

package main

import "fmt"

func moveZeroes(nums []int) {
	// two pointers solution
	i, j := 0, 0
	for ; j < len(nums); j++ {
		// seek until finding a non-zero
		if nums[j] != 0 {
			// shift items after 0 backward
			for k := 0; k < len(nums)-j; k++ {
				nums[i+k] = nums[j+k]
			}

			// fill zeros at the end
			for l := 0; l < j - i; l++ {
				nums[len(nums) -1 - l] = 0
			}

			// reset j to check items after pointer i
			j = i
			i += 1
		}

	}
}

func main() {
	// list := []int{0, 1, 0, 3, 12}
	// list := []int{0, 0, 1, 0, 0, 13, 0, 2}
	list := []int{1}

	moveZeroes(list)
	fmt.Println(list)
}
