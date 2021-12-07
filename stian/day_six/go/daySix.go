package main

import (
	"bufio"
	"fmt"
	"os"
	"runtime"
	"strconv"
	"strings"
	"time"
)

func main() {
	file, err := os.Open("day_six.txt")
	if err != nil {
		panic(err)
	}

	defer file.Close()
	scanner := bufio.NewScanner(file)
	var data []string

	for scanner.Scan() {
		data = append(data, scanner.Text())
	}

	s := strings.Split(data[0], ",")

	start := time.Now()
	fmt.Println("Ans", partOne(s))
	elapsed := time.Since(start)
	fmt.Printf("Runtime %s \n", elapsed)

	start = time.Now()
	fmt.Println("Ans", naiveSolution(s))
	elapsed = time.Since(start)
	fmt.Printf("Runtime %s \n", elapsed)
}

func partOne(s []string) int64 {
	var counts [9]int64
	// populate the inital list
	for _, v := range s {
		new_v := string(v)
		val, _ := strconv.ParseInt(new_v, 10, 64)
		counts[val]++
	}

	for i := 0; i < 175; i++ {
		tmp := counts[0]
		for j := 0; j < len(counts)-1; j++ {
			counts[j] = counts[j+1]
		}
		counts[6] += tmp
		counts[8] = tmp
	}
	var sum int64
	for _, val := range counts {
		sum += val
	}
	PrintMemUsage()
	return sum
}

func naiveSolution(s []string) int {
	fish := make([]int, 0)
	for _, v := range s {
		new_v := string(v)
		val, _ := strconv.Atoi(new_v)
		fish = append(fish, val)
	}

	i := 0

	for i < 175 {
		new_fish := 0
		for j := 0; j < len(fish); j++ {
			if fish[j] == 0 {
				new_fish += 1
				fish[j] = 6
			} else {
				fish[j]--
			}
		}
		for j := 0; j < new_fish; j++ {
			fish = append(fish, 8)
		}
		i += 1
	}

	PrintMemUsage()
	return len(fish)
}

func PrintMemUsage() {
	var m runtime.MemStats
	runtime.ReadMemStats(&m)
	// For info on each, see: https://golang.org/pkg/runtime/#MemStats
	fmt.Printf("Alloc = %v MiB", bToMb(m.Alloc))
	fmt.Printf("\tTotalAlloc = %v MiB", bToMb(m.TotalAlloc))
	fmt.Printf("\tSys = %v MiB", bToMb(m.Sys))
	fmt.Printf("\tNumGC = %v\n", m.NumGC)
}

func bToMb(b uint64) uint64 {
	return b / 1024 / 1024
}
