// Reverse String

package main

import (
	"fmt"
	"math"
)

func myAtoi(s string) int {
	leadingSpace := 0
	signFlag := 1
	_ = signFlag // avoid defined but not used error
	var result int
	numSign := 0
	numFlag := 0
	spaceFlag := 0

	for i, char := range s {
		if i == leadingSpace && char == ' ' && spaceFlag == 0 {
			leadingSpace += 1
			continue
		} else if i == leadingSpace && char == '-' && numSign == 0 && numFlag == 0 {
			signFlag = -1
			leadingSpace += 1
			numSign += 1
			spaceFlag = 1
		} else if i == leadingSpace && char == '+' && numSign == 0 && numFlag == 0 {
			leadingSpace += 1
			numSign += 1
			spaceFlag = 1
		} else if i == leadingSpace && char >= '0' && char <= '9' {
			result = result*10 + int(char-'0')
			leadingSpace += 1
			numFlag = 1
			spaceFlag = 1

			// check boundry right away
			if result*signFlag > math.MaxInt32-1 {
				return math.MaxInt32
			} else if result*signFlag < -1*math.MaxInt32 {
				return -1*math.MaxInt32 - 1
			}
		} else {
			break
		}

	}

	return result * signFlag
}

func main() {
	str := "9223372036854775808"

	result := myAtoi(str)
	fmt.Println(result)
}
