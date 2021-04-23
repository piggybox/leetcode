// Count and Say

package main

import "fmt"

func countAndSay(n int) string {
	if n == 1 {
		return "1"
	} else {
		


		return countAndSay(n-1)
	}
}

func main() {
	n := 1

	result := countAndSay(n)
	fmt.Println(result)
}
