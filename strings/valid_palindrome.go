// Reverse String

package main

import (
	"fmt"
	"regexp"
	"strings"
)

func isPalindrome(s string) bool {
	// preprocessing
	r, _ := regexp.Compile("[a-zA-Z0-9]+")
	result := r.FindAllString(s, -1)

	lower := []string{}

	for _, s := range result {
		lower = append(lower, strings.ToLower(s))
	}

	processed := strings.Join(lower, "")

	// check palindrome
	for i := 0; i < len(processed)/2; i++ {
		if processed[i] == processed[len(processed)-i-1] {
			continue
		} else {
			return false
		}
	}
	return true
}

func main() {
	// str := "A man, a plan, a canal: Panama"
	str := "race a car"

	result := isPalindrome(str)
	fmt.Println(result)
}
