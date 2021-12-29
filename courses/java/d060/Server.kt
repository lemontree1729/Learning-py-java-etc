package d060

import java.io.*
import java.net.ServerSocket
import java.net.SocketTimeoutException
import java.util.*

fun main() {
    val sc = Scanner(System.`in`)
    try {
        while (true) {
            println("waiting for connect...")
            val socket = ServerSocket(9999).accept()
            println("connected")
            val input = BufferedReader(InputStreamReader(socket.getInputStream()))
            val output = BufferedWriter(OutputStreamWriter(socket.getOutputStream()))
            while (true) {
                val inputMessage = input.readLine()
                if (inputMessage == "bye") {
                    println("client entered bye")
                    break
                }
                println("Client: $inputMessage")
                print("to send>>")
                output.write("${sc.nextLine()}\n")
                output.flush()
            }
            println("disconnected")
        }
    } catch (e: IOException) {
        e.printStackTrace()
    }
    sc.close()
}