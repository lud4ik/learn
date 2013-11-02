package main

import (
    "encoding/gob"
    "fmt"
    "net"
    "time"
)

func server() {
    ln, err := net.Listen("tcp", ":9999")
    if err != nil {
        fmt.Println(err)
        return
    }
    for {
        c, err := ln.Accept()
        if err != nil {
            fmt.Println(err)
            continue
        }
        go handleServerConnection(c)
    }
}

func handleServerConnection(c net.Conn) {
    commands := map[string] string {
        "PING": "PONG",
    }
    var msg string
    for {
        err := gob.NewDecoder(c).Decode(&msg)
        if err != nil {
            fmt.Println(err)
            c.Close()
        } else {
            fmt.Println(commands[msg])
        }
    }
}

func client() {
    c, err := net.Dial("tcp", "127.0.0.1:9999")
    if err != nil {
        fmt.Println(err)
        return
    }
    for {
        msg := "PING"
        fmt.Println(msg)
        err = gob.NewEncoder(c).Encode(msg)
        if err != nil {
            fmt.Println(err)
            c.Close()
            break
        }
        time.Sleep(time.Second)
    }
}

func main() {
    go server()
    go client()
    var input string
    fmt.Scanln(&input)
}