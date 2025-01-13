// Valid Sudoku
// medium

package main

import "fmt"

func isValidSudoku(board [][]byte) bool {
	// check rows
	for _, row := range board {
		if !checkDuplicates(row) {
			return false
		}
	}

	// check columns
	for i := 0; i < 9; i++ {
		currentCol := []byte{}
		for j := 0; j < 9; j++ {
			currentCol = append(currentCol, board[j][i])
		}
		if !checkDuplicates(currentCol) {
			return false
		}
	}

	// check blocks
	index := []int{0, 3, 6}
	index2 := []int{0, 1, 2}
	for _, row := range index {
		for _, col := range index {
			block := []byte{}

			for _, i := range index2 {
				for _, j := range index2 {
					block = append(block, board[row+i][col+j])
				}
			}

			if !checkDuplicates(block) {
				return false
			}
		}
	}

	return true
}

func checkDuplicates(list []byte) bool {
	hash := make(map[byte]bool)

	for _, item := range list {
		if item != '.' {
			_, exist := hash[item]
			if exist {
				return false
			} else {
				hash[item] = true
			}
		}
	}
	return true
}

func main() {
	// board := [][]byte{
	// 	{'5', '3', '.', '.', '7', '.', '.', '.', '.'},
	// 	{'6', '.', '.', '1', '9', '5', '.', '.', '.'},
	// 	{'.', '9', '8', '.', '.', '.', '.', '6', '.'},
	// 	{'8', '.', '.', '.', '6', '.', '.', '.', '3'},
	// 	{'4', '.', '.', '8', '.', '3', '.', '.', '1'},
	// 	{'7', '.', '.', '.', '2', '.', '.', '.', '6'},
	// 	{'.', '6', '.', '.', '.', '.', '2', '8', '.'},
	// 	{'.', '.', '.', '4', '1', '9', '.', '.', '5'},
	// 	{'.', '.', '.', '.', '8', '.', '.', '7', '9'}}

	// board := [][]byte{
	// 	{'8', '3', '.', '.', '7', '.', '.', '.', '.'},
	// 	{'6', '.', '.', '1', '9', '5', '.', '.', '.'},
	// 	{'.', '9', '8', '.', '.', '.', '.', '6', '.'},
	// 	{'8', '.', '.', '.', '6', '.', '.', '.', '3'},
	// 	{'4', '.', '.', '8', '.', '3', '.', '.', '1'},
	// 	{'7', '.', '.', '.', '2', '.', '.', '.', '6'},
	// 	{'.', '6', '.', '.', '.', '.', '2', '8', '.'},
	// 	{'.', '.', '.', '4', '1', '9', '.', '.', '5'},
	// 	{'.', '.', '.', '.', '8', '.', '.', '7', '9'}}

	board := [][]byte{
		{'.', '.', '4', '.', '.', '.', '6', '3', '.'},
		{'.', '.', '.', '.', '.', '.', '.', '.', '.'},
		{'5', '.', '.', '.', '.', '.', '.', '9', '.'},
		{'.', '.', '.', '5', '6', '.', '.', '.', '.'},
		{'4', '.', '3', '.', '.', '.', '.', '.', '1'},
		{'.', '.', '.', '7', '.', '.', '.', '.', '.'},
		{'.', '.', '.', '5', '.', '.', '.', '.', '.'},
		{'.', '.', '.', '.', '.', '.', '.', '.', '.'},
		{'.', '.', '.', '.', '.', '.', '.', '.', '.'}}
	result := isValidSudoku(board)
	fmt.Println(result)
}
