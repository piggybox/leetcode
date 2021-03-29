// Intersection of Two Arrays II

package main

import (
	"fmt"
)

func intersect(nums1 []int, nums2 []int) []int {
	hash1 := make(map[int]int)
	hash2 := make(map[int]int)

	for _, num1 := range nums1 {
		hash1[num1] += 1
	}

	for _, num2 := range nums2 {
		hash2[num2] += 1
	}

	result := []int{}

	for k1, v1 := range hash1 {
		v2, exist := hash2[k1]
		if exist {
			count := 0
			if v1 < v2 {
				count = v1
			} else {
				count = v2
			}

			for i := 0; i < count; i++ {
				result = append(result, k1)
			}

		}
	}

	return result
}

func main() {
	list1 := []int{4, 9, 5}
	list2 := []int{9, 4, 9, 8, 4}

	result := intersect(list1, list2)
	fmt.Println(result)
}
