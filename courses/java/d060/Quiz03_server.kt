package d060

import java.io.BufferedWriter
import java.io.OutputStreamWriter
import java.net.ServerSocket
import java.util.*

class Calculator(val serverSocket: ServerSocket) : Thread() {
    override fun run() {
        val socket = serverSocket.accept()
        println("client ${socket.inetAddress} connected at ${this.name}")
        val input = Scanner(socket.getInputStream())
        val output = BufferedWriter(OutputStreamWriter(socket.getOutputStream()))
        while (true) {
            val cal = input.nextLine().split(" ")
            val first = cal[0].toInt()
            val op = cal[1]
            val second = cal[2].toInt()
            val result = when (op) {
                "+" -> first + second
                "-" -> first - second
                "*" -> first * second
                "/" -> first.toFloat() / second.toFloat()
                else -> "wrong"
            }
            println("${cal.joinToString("")}=${result}")
            output.write("${result}\n")
            output.flush()
        }
    }
}

fun main() {
    println("starting calculate server")
    val server = ServerSocket(9999)
    println("connecting with client...")
    for (i in 1..4)
        Calculator(server).start()
}