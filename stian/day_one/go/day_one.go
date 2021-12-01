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
	prev := data[0]
	counter := 0
	for _, v := range data {
		if v > prev {
			counter++
		}
		prev = v
	}
	return counter
}

func partTwo(data []int) int {
	curr_sum := 0
	prev_sum := 0
	counter := 0
	for i, v := range data {
		curr_sum += v
		if i > 2 {
			if curr_sum > prev_sum {
				counter++
			}
			prev_sum = curr_sum
			curr_sum -= data[i-2]
		}
	}
	return counter
}
