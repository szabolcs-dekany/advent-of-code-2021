package main

import (
	"bufio"
	"log"
	"os"
	"strconv"
)

func ReadMeasurements(fileName string) []int64 {
	measurementsFile, err := os.Open(fileName)
	measurements := make([]int64, 0)

	if err != nil {
		log.Fatal(err)
	}

	defer measurementsFile.Close()

	scanner := bufio.NewScanner(measurementsFile)

	for scanner.Scan() {
		depth, err := strconv.ParseInt(scanner.Text(), 10, 64)
		if err != nil {
			log.Fatal(err)
		}
		measurements = append(measurements, depth)
	}

	if err := scanner.Err(); err != nil {
		log.Fatal(err)
	}
	return measurements
}
