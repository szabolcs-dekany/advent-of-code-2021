package main

import "fmt"

func RunPartTwo() {
	fmt.Println("--------------------------------")
	fmt.Println("Advent of Code 2021 - 1 - Part 2")
	measurements := ReadMeasurements("input.txt")
	var previousSum int64 = 0
	var numberOfIncreasedMeasurements int64 = 0

	for i := 0; i < len(measurements); i++ {
		if i == 0 {
			previousSum = measurements[i] + measurements[i+1] + measurements[i+2]
			continue
		}

		if i+3 > len(measurements) {
			continue
		}

		sum := measurements[i] + measurements[i+1] + measurements[i+2]
		if sum > previousSum {
			numberOfIncreasedMeasurements++
		}
		previousSum = sum
	}

	fmt.Printf("Increased measurements: %d \n", numberOfIncreasedMeasurements)
}
