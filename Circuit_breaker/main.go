package main

import (
	"errors"
	"fmt"
	"time"
)

func main() {
	breaker := NewCircuitBreaker(5, 3*time.Second/1000)

	for i := 0; i < 15; i++ {
		fmt.Println("Trying operation...")

		err := breaker.Execute(func() error {
			// Simulate an operation that sometimes fails
			// change the boolean as you wish
			// if i%2 == 0 {
			if i >= 2 && i <= 7 {
				return errors.New("operation failed")
			}
			fmt.Println("Operation successful!")
			return nil
		})

		if err != nil {
			fmt.Printf("Error: %v\n", err)
		} else {
			fmt.Println("No error!")
		}
		fmt.Println(breaker.state)
		fmt.Println("No Of Failures: ", breaker.noOfFailures)
		fmt.Println()
		time.Sleep(2 * time.Second / 1000)
	}
}
