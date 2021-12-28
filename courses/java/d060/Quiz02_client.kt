package d060

import java.net.Socket
import java.util.*

fun main() {
    val socket = Socket("localhost", 9999)
    println("connected with server")
    val input = Scanner(socket.getInputStream())
    while (input.hasNext()) {
        print("${input.nextLine()}  ")
    }
    println("\ndisconnected")
}