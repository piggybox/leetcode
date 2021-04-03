// Reverse String

package main

import "fmt"

func reverseString(s []byte) {
	for i := 0; i < len(s)/2; i++ {
		temp := s[i]
		s[i] = s[len(s)-i-1]
		s[len(s)-i-1] = temp
	}
}

func main() {
	str := []byte{'H', 'a', 'n', 'n', 'a', 'h'}

	reverseString(str)
	fmt.Printf(string(str))
}
