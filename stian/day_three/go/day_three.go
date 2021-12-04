package main

import (
	"bufio"
	"fmt"
	"os"
	"strconv"
)

func main() {
	file, err := os.Open("day_three.txt")
	if err != nil {
		panic(err)
	}

	defer file.Close()
	scanner := bufio.NewScanner(file)
	var data []string

	for scanner.Scan() {
		data = append(data, scanner.Text())
	}

	fmt.Println("Part 1:", partOne(data))
	fmt.Println("Part 2:", partTwo(data))
}

func partOne(data []string) int64 {
	count_ones := make([]int, len(data[0]))
	count_zero := make([]int, len(data[0]))
	for _, val := range data {
		for i, v := range val {
			if string(v) == "0" {
				count_zero[i]++
			} else if string(v) == "1" {
				count_ones[i]++
			}
		}
	}
	num1 := ""
	num2 := ""
	for i := 0; i < len(count_ones); i++ {
		if count_ones[i] > count_zero[i] {
			num1 += "1"
			num2 += "0"
		} else {
			num1 += "0"
			num2 += "1"
		}
	}
	gamma, _ := strconv.ParseInt(num1, 2, 64)
	epsilon, _ := strconv.ParseInt(num2, 2, 64)

	return gamma * epsilon
}

func findCommon(data []string, keyword string, index int) []string {
	tmp := make([]string, 0)
	for _, val := range data {
		if val[index] == keyword[index] {
			tmp = append(tmp, val)
		}
	}
	return tmp
}

func findGammaEpisolon(data []string) (string, string) {
	count_ones := make([]int, len(data[0]))
	count_zero := make([]int, len(data[0]))
	for _, val := range data {
		for i, v := range val {
			if string(v) == "0" {
				count_zero[i]++
			} else if string(v) == "1" {
				count_ones[i]++
			}
		}
	}
	gamma := ""
	epsilon := ""
	for i := 0; i < len(count_ones); i++ {
		if count_ones[i] > count_zero[i] {
			gamma += "1"
			epsilon += "0"
		} else if count_ones[i] < count_zero[i] {
			gamma += "0"
			epsilon += "1"
		} else {
			// the counts are equal
			gamma += "1"
			epsilon += "0"
		}
	}
	return gamma, epsilon
}

func partTwo(data []string) int64 {
	nums := data
	i := 0
	for len(nums) > 1 {
		gamma, _ := findGammaEpisolon(nums)
		nums = findCommon(nums, gamma, i)
		i++
	}
	oxygen, _ := strconv.ParseInt(nums[0], 2, 64)
	nums = data
	i = 0
	for len(nums) > 1 {
		_, epsilon := findGammaEpisolon(nums)
		nums = findCommon(nums, epsilon, i)
		i++
	}
	carbon, _ := strconv.ParseInt(nums[0], 2, 64)
	return oxygen * carbon
}
