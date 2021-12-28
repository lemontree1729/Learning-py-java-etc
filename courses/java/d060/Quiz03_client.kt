package d060

import java.io.BufferedWriter
import java.io.OutputStreamWriter
import java.net.Socket
import java.util.*

fun main() {
    println("connecting with server...")
    val socket = Socket("localhost", 9999)
    println("server connected")
    val sc = Scanner(System.`in`)
    val input = Scanner(socket.getInputStream())
    val output = BufferedWriter(OutputStreamWriter(socket.getOutputStream()))
    while (true) {
        val cal = sc.nextLine()
        output.write("$cal\n")
        output.flush()
        println(input.nextLine())
    }
}