package main

import (
	"errors"
	"time"
)

type CircuitBreaker struct {
	noOfFailuresAllowed int           // after how many errors should the circuit break
	noOfFailures        int           // number of failures
	recoveryTime        time.Duration // after how long to check
	state               string        // open or closed
	lastFailureTime     time.Time     // last failure time
}

func (cb *CircuitBreaker) Execute(operation func() error) error {
	// if state is open , but enough time has passed since last failure, then set to half-open
	// it means it is open for testing
	if cb.state == "open" && time.Since(cb.lastFailureTime) > cb.recoveryTime {
		cb.state = "half-open"
	}

	if cb.state == "closed" {
		err := operation()
		if err != nil {
			cb.recordFailure()
		} else {
			cb.reset()
		}
		return err
	} else if cb.state == "half-open" {
		// allow only limited requests to test if system has recovered
		// rate limiterc can be added to the operation here, to limit the api calls
		err := operation() // add rate limiter here
		if err != nil {
			cb.recordFailure()
			return err
		} else {
			cb.state = "closed" // if it starts working then we close it again
			cb.reset()
			return nil
		}
	}
	return errors.New("circuit breaker is open")
}

func (cb *CircuitBreaker) recordFailure() {
	cb.lastFailureTime = time.Now()
	cb.noOfFailures++
	if cb.noOfFailures > cb.noOfFailuresAllowed/2 { // after half of the failures, it will be half-open
		cb.state = "half-open"
	}
	if cb.noOfFailures > cb.noOfFailuresAllowed { // after reaching the failure threshold, it will be open
		cb.state = "open"
	}
}

func (cb *CircuitBreaker) reset() {
	cb.noOfFailures = 0
}

func NewCircuitBreaker(noOfFailuresAllowed int, recoveryTime time.Duration) *CircuitBreaker {
	return &CircuitBreaker{
		noOfFailuresAllowed: noOfFailuresAllowed,
		noOfFailures:        0,
		recoveryTime:        recoveryTime,
		state:               "closed",
	}
}
