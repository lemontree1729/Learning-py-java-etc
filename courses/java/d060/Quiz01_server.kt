package d060

import java.io.IOException
import java.io.InputStreamReader
import java.net.ServerSocket
import java.util.*
import kotlin.Exception

fun main() {
    val server = ServerSocket(9999)
    while (true) {
        println("waiting for connect...")
        val socket = server.accept()
        println("connected with client ${socket.inetAddress}")
        val input = Scanner(InputStreamReader(socket.getInputStream()))
        while (true) {
            val inputMessage = input.nextLine()
            if (inputMessage == "stop")
                break
            println(inputMessage)
        }
        println("disconnected")
    }
}