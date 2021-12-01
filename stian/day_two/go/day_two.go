package main

import (
	"fmt"
	"os"
)

func main() {
	file, err := os.Open("day_one.txt")
	if err != nil {
		panic(err)
	}

	defer file.Close()
	var line int
	data := make([]int, 0)
	_, err = fmt.Fscanf(file, "%d", &line)

	for err == nil {
		data = append(data, line)
		_, err = fmt.Fscanf(file, "%d\n", &line)
	}

	fmt.Println("Part 1:", partOne(data))
	fmt.Println("Part 2:", partTwo(data))
}

func partOne(data []int) int {
	return 0
}

func partTwo(data []int) int {
	return 0
}
