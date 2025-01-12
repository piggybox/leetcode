// Two Sum

package main

import "fmt"

func twoSum(nums []int, target int) []int {
	hash := make(map[int]int)
	// we don't populate full hash to avoid using the same number twice

	for i, num := range nums {
		part := target - num
		_, exist := hash[part]
		if exist {
			return []int{hash[part], i}
		} else {
			hash[num] = i
		}
	}

	return []int{}
}

func main() {
	list, target := []int{2, 7, 11, 15}, 9
	result := twoSum(list, target)
	fmt.Println(result)
}
