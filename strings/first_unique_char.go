// First Unique Character in a String

package main

import (
	"fmt"
)

func firstUniqChar(s string) int {
	hash := make(map[byte]uint)
	charArray := []byte(s)

	for _, char := range charArray {
		_, exist := hash[char]
		if exist {
			hash[char] += 1 
		} else {
			hash[char] = 1
		}
	}

	for i, char := range charArray {
		if hash[char] == 1 {
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
