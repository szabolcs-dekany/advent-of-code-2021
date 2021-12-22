package main

import (
	"fmt"
)

func RunPartOne() {
	fmt.Println("--------------------------------")
	fmt.Println("Advent of Code 2021 - 1 - Part 1")
	measurements := ReadMeasurements("input.txt")
	increased := getNumberOfIncreasedMeasurements(measurements)
	fmt.Printf("Increased measurements: %d \n", increased)
}

func getNumberOfIncreasedMeasurements(measurements []int64) int64 {
	var numberOfIncreasetMeasurements int64 = 0
	var previousMeasurement int64 = 0

	for i := 0; i < len(measurements); i++ {
		if i == 0 {
			continue
		}

		if measurements[i] > previousMeasurement {
			numberOfIncreasetMeasurements++
		}

		previousMeasurement = measurements[i]
	}

	return numberOfIncreasetMeasurements
}
