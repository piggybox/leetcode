// Rotate Image

package main

import "fmt"

func rotate(matrix [][]int) {
	n := len(matrix[0])

	for i := 0; i < n/2; i++ {
		for j := i; j < (n - i - 1); j++ {
			temp := matrix[i][j]
			matrix[i][j] = matrix[n-j-1][i]
			matrix[n-j-1][i] = matrix[n-i-1][n-j-1]
			matrix[n-i-1][n-j-1] = matrix[j][n-i-1]
			matrix[j][n-i-1] = temp
		}
	}
}

func main() {
	// matrix := [][]int{{1, 2, 3}, {4, 5, 6}, {7, 8, 9}}
	matrix := [][]int{{5, 1, 9, 11}, {2, 4, 8, 10}, {13, 3, 6, 7}, {15, 14, 12, 16}}
	rotate(matrix)
	fmt.Println(matrix)
}
