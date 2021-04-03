// Reverse Integer

package main

import (
	"fmt"
	"math"
	"strconv"
)

func reverse(x int) int {
	var sign bool
	if x < 0 {
		sign = false
		x = x * -1
	} else {
		sign = true
	}

	xStr := []byte(strconv.Itoa(x))
	reverseString(xStr)
	result, _ := strconv.Atoi(string(xStr))

	if result > math.MaxInt32 {
		return 0
	}

	if sign {
		return result
	} else {
		return result * -1
	}
}

func reverseString(s []byte) {
	for i := 0; i < len(s)/2; i++ {
		temp := s[i]
		s[i] = s[len(s)-i-1]
		s[len(s)-i-1] = temp
	}
}

func main() {
	// x := -123
	// x := 120
	x := 1534236469

	result := reverse(x)
	fmt.Print(result)
}
