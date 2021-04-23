// 1813. Sentence Similarity III

package main

import (
	"fmt"
	"strings"
)

func areSentencesSimilar(sentence1 string, sentence2 string) bool {
	s1Array := strings.Split(sentence1, " ")
	s2Array := strings.Split(sentence2, " ")

	pa, pb := 0

	for 
	
}

func main() {
	// sentence1 := "My name is Haley"
	// sentence2 := "My Haley"

	// sentence1 := "of"
	// sentence2 := "A lot of words"

	// sentence1 := "Eating right now"
	// sentence2 := "Eating"

	sentence1 := "d T d ED uXW L U J n klIe"
	sentence2 := "d T d ED uXW L U J klIe"

	result := areSentencesSimilar(sentence1, sentence2)
	fmt.Print(result)
}
