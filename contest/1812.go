// 1812. Determine Color of a Chessboard Square

package main

import (
	"fmt"
	"strconv"
)

func squareIsWhite(coordinates string) bool {
	hash := map[rune]int{
		'a': 1,
		'b': 2,
		'c': 3,
		'd': 4,
		'e': 5,
		'f': 6,
		'g': 7,
		'h': 8,
	}

	var rank int
	for i, char := range coordinates {
		if i == 0 {
			rank = hash[char]
		} else {
			digit, _ := strconv.Atoi(string(char))
			rank += digit
		}
	}

	if rank%2 != 1 {
		return false
	} else {
		return true
	}
}

func main() {
	coordinates := "c7"

	result := squareIsWhite(coordinates)
	fmt.Print(result)
}
