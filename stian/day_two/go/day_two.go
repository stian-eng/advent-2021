package main

import (
	"bufio"
	"fmt"
	"os"
	"strconv"
	"strings"
)

func main() {
	file, err := os.Open("day_two.txt")
	if err != nil {
		panic(err)
	}

	defer file.Close()
	scanner := bufio.NewScanner(file)
	var data []string

	for scanner.Scan() {
		data = append(data, scanner.Text())
	}
	// var line int
	// data := make([]int, 0)
	// _, err = fmt.Fscanf(file, "%d", &line)

	// for err == nil {
	// 	data = append(data, line)
	// 	_, err = fmt.Fscanf(file, "%d\n", &line)
	// }

	fmt.Println("Part 1:", partOne(data))
	fmt.Println("Part 2:", partTwo(data))
}

func partOne(data []string) int {
	horizontal := 0
	depth := 0
	for _, v := range data {
		fields := strings.Fields(v)
		dir := fields[0]
		num, _ := strconv.Atoi(fields[1])
		if dir == "forward" {
			horizontal += num
		} else if dir == "down" {
			depth += num
		} else {
			depth -= num
		}
	}
	// 2147104
	return horizontal * depth
}

func partTwo(data []string) int {
	horizontal := 0
	depth := 0
	aim := 0
	for _, v := range data {
		fields := strings.Fields(v)
		dir := fields[0]
		num, _ := strconv.Atoi(fields[1])
		if dir == "forward" {
			horizontal += num
			depth += (aim * num)
		} else if dir == "down" {
			aim += num
		} else {
			aim -= num
		}
	}
	// 2044620088
	return horizontal * depth
}
