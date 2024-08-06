package main

import (
	"fmt"
)

func main() {
	
	var x, y = 2, 3
	ptr := &x
	ptr2 := &y
	arr := [2]*int{ptr, ptr2}
	for i := range arr {
		fmt.Println(*arr[i])
	}
}
