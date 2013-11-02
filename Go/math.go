package main

import (
    "fmt"
    "time"
    "math/rand"
)

func generate(channel chan int, max int){
    for i := 0; i < max; i++ {
        channel <- rand.Intn(100)
        time.Sleep(time.Second)
    }
}

func nsd(a, b int) int {
    if a > b {
        a, b = b, a
    }
    for b != 0 {
        a, b = b, a % b
    }
    return a
}

func main() {
    var a, b int
    left := make(chan int)
    right := make(chan int)
    go generate(left, 10)
    go generate(right, 10)
    for {
        select {
            case A := <- left:
                a = A
                if b != 0 {
                    fmt.Printf("NSD(%d, %d) = %d\n", a, b, nsd(a, b))
                    a, b = 0, 0
                }
            case B := <- right:
                b = B
                if a != 0 {
                    fmt.Printf("NSD(%d, %d) = %d\n", a, b, nsd(a, b))
                    a, b = 0, 0
                }
            case <- time.After(time.Second):
                fmt.Println("timeout")
                goto exit
        }
    }
    exit:
}