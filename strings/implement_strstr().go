// Implement strStr()

package main

import "fmt"

func strStr(haystack string, needle string) int {
	if len(needle) == 0 {
		return 0
	}

	for pa := 0; pa < len(haystack); pa++ {
		for pb := 0; pb < len(needle); pb++ {
			if pa+pb < len(haystack) {
				if haystack[pa+pb] == needle[pb] && pb == len(needle)-1 {
					return pa
				}
				if haystack[pa+pb] == needle[pb] {
					continue
				} else {
					break
				}
			}
		}
	}

	return -1
}

func main() {
	haystack := "aaa"
	needle := "aaaa"

	result := strStr(haystack, needle)
	fmt.Println(result)
}
