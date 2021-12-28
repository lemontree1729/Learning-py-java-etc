package d060

import java.io.*
import java.net.ServerSocket
import java.util.*

fun main() {
    val sc = Scanner(System.`in`)
    try {
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
    } catch (e: IOException) {
        e.printStackTrace()
    }
    sc.close()
}