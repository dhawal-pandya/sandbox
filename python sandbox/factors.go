package main

import (
	"fmt"
	"math"
	"sort"
	"time"
)

// i wrote this in Golang, just for the speed in execution, prototyping was done in python itself.

func findFactors(number int) []int {
	factors := []int{}
	sqrtNum := int(math.Sqrt(float64(number)))

	for i := 1; i <= sqrtNum; i++ {
		if number%i == 0 {
			factors = append(factors, i)
			otherFactor := number / i
			if otherFactor != i {
				factors = append(factors, otherFactor)
			}
		}
	}
	return factors
}

func main() {
	num := 999999999999999999
	startTime := time.Now()

	result := findFactors(num)
	sort.Ints(result)

	elapsedTime := time.Since(startTime)
	fmt.Printf("Factors of %d: %v\n", num, result)
	fmt.Printf("Elapsed time: %v\n", elapsedTime)
}
