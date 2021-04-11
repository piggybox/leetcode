// Valid Anagram

package main

import "fmt"

func isAnagram(s string, t string) bool {
	// reduce string comparasion to hash comparasion
	hash1 := make(map[rune]int)
	hash2 := make(map[rune]int)

	for _, char := range s {
		_, exist := hash1[char]
		if exist {
			hash1[char] += 1
		} else {
			hash1[char] = 1
		}
	}

	for _, char := range t {
		_, exist := hash2[char]
		if exist {
			hash2[char] += 1
		} else {
			hash2[char] = 1
		}
	}

	// compare two hashes
	result := true
	for k1, v1 := range hash1 {
		v2, exist := hash2[k1]
		if exist {
			if v1 == v2 {
				continue
			} else {
				return false
			}
		} else {
			return false
		}
	}

	for k1, v1 := range hash2 {
		v2, exist := hash1[k1]
		if exist {
			if v1 == v2 {
				continue
			} else {
				return false
			}
		} else {
			return false
		}
	}

	return result
}

func main() {
	s := "ab"
	t := "a"

	result := isAnagram(s, t)
	fmt.Print(result)
}
