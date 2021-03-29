// Rotate Array

package main

import "fmt"

func rotate(nums []int, k int) {
	if k > len(nums) {
		k = k % len(nums)
	}

	for i := 0; i < k; i++ {
		temp := nums[len(nums)-k+i]

		// makr room at head
		for j := len(nums) - k + i; j > i; j-- {
			nums[j] = nums[j-1]
		}

		nums[i] = temp
	}
}

func main() {
	// list, k := []int{1, 2, 3, 4, 5, 6, 7}, 3
	// list, k := []int{-1}, 2
	list, k := []int{1, 2}, 3
	rotate(list, k)
	fmt.Println(list)
}
