// Find the Winner of the Circular Game
// medium

package main

import (
	"fmt"
)

type node struct {
	data int
	next *node
	prev *node
}

func initializeRing(n int) *node {
	if n <= 0 {
		return nil
	}

	head := &node{data: 1}
	p := head

	for i := 2; i <= n; i++ {
		p.next = &node{data: i, prev: p}
		p = p.next
	}

	// complete the circle
	p.next = head
	head.prev = p

	return head
}

func removeNode(p *node) *node {
	prev := p.prev
	next := p.next
	prev.next = next
	next.prev = prev

	return next
}

func findTheWinner(n int, k int) int {
	p := initializeRing(n)
	numNode := n

	for numNode > 1 {
		// move k-1 steps
		for j := 0; j < k-1; j++ {
			p = p.next
		}

		// fmt.Printf("removed: %d\n", p.data)
		p = removeNode(p)

		// debugRing(p)

		numNode -= 1
	}

	return p.data

}

func debugRing(p *node) {
	head := p
	p2 := p
	for p2.next != head {
		fmt.Println(p2.prev.data, p2.data, p2.next.data)
		p2 = p2.next
	}

	fmt.Println(p2.prev.data, p2.data, p2.next.data)
}

func main() {
	n := 6
	k := 5
	// expect 1

	result := findTheWinner(n, k)
	fmt.Println(result)
}
