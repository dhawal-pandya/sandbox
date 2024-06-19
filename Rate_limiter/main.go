package main

import (
	"fmt"
	"time"
)

func main() {
	rateLimiter := createRateLimiter(Limit(1.0 / 200.0)) // limit is 1 call within 200 milliseconds
	rateLimitedReturnPi := rateLimiter(returnPi)

	// Testing
	// i use userID, but ideally it should be IP address
	fmt.Println("testing call within rate limit")
	fmt.Println(rateLimitedReturnPi("user1")) // 3.141592653589793

	fmt.Println("testing call after exceeding rate limit")
	for i := 0; i < 5; i++ {
		fmt.Println(rateLimitedReturnPi("user2")) // Rate limit exceeded. Please try again later.
	}

	fmt.Println("testing multiple calls within rate limit")
	for i := 0; i < 5; i++ {
		time.Sleep(250 * time.Millisecond)
		fmt.Println(rateLimitedReturnPi("user3")) // 3.141592653589793
	}
}
