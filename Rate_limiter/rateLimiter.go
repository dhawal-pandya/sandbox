package main

import (
	"fmt"
	"math"
	"time"
)

type ID string
type TimeInMillis float64
type Limit float64
type DecoratedFunc func(ID) float64
type Decorator func(DecoratedFunc) DecoratedFunc

func createRateLimiter(limit Limit) Decorator {
	lastCalled := make(map[ID]TimeInMillis)

	return func(f DecoratedFunc) DecoratedFunc {
		return func(id ID) float64 {
			currentTime := TimeInMillis(time.Now().UnixMilli())

			// if the ID has not been called before
			if _, ok := lastCalled[id]; !ok {
				lastCalled[id] = currentTime
				return f(id)
			}

			// if the ID has been called before
			timeSinceLastCall := currentTime - lastCalled[id]
			if timeSinceLastCall < TimeInMillis(1/limit) {
				fmt.Println("Rate limit exceeded.")
				return 0.0 // assuming float64 return type
			}
			lastCalled[id] = currentTime
			return f(id)
		}
	}
}

func returnPi(id ID) float64 {
	return math.Pi
}
