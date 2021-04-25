// Sum of Digits in Base K
// easy

package main

import (
	"fmt"
	"math/big"
	"strconv"
)

func sumBase(n int, k int) int {
	converted := big.NewInt(int64(n)).Text(k)

	result := 0
	for _, char := range converted {
		num, _ := strconv.Atoi(string(char))
		result += num
	}

	return result
}

func main() {
	n := 10
	k := 10
	result := sumBase(n, k)
	fmt.Println(result)
}
