// First Unique Character in a String

package main

import (
	"fmt"
)

func firstUniqChar(s string) int {
	hash := make(map[rune]bool)

	for _, char := range s {
		_, exist := hash[char]
		if exist {
			hash[char] = false
		} else {
			hash[char] = true
		}
	}

	for i, char := range s {
		if hash[char] {
			return i
		}
	}

	return -1
}

func main() {
	x := "loveleetcode"
	// x := "aabb"

	result := firstUniqChar(x)
	fmt.Print(result)
}
