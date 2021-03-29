// Plus one

package main

import "fmt"

func plusOne(digits []int) []int {
	digits[len(digits)-1] += 1

	// shift 10 to 1,0
	for i := len(digits) - 1; i > 0; i-- {
		if digits[i] == 10 {
			digits[i-1] += 1
			digits[i] = 0
		}
	}

	// expand the top if needed
	if digits[0] == 10 {
		digits2 := make([]int, len(digits)+1)
		for i := 2; i < len(digits2); i++ {
			digits2[i] = digits[i-1]
		}
		digits2[0] = 1
		digits2[1] = 0

		return digits2
	}

	return digits
}

func main() {
	// list := []int{9}
	list := []int{9, 9}

	result := plusOne(list)
	fmt.Println(result)
}
