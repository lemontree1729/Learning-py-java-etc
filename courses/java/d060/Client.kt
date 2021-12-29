package d060

import java.io.*
import java.net.Socket
import java.util.*

fun main() {
    val sc = Scanner(System.`in`)
    try {
        val socket = Socket("localhost", 9999)
        val input = BufferedReader(InputStreamReader(socket.getInputStream()))
        val output = BufferedWriter(OutputStreamWriter(socket.getOutputStream()))
        while (true) {
            print("to send>>")
            val outputMessage = sc.nextLine()
            output.write("$outputMessage\n")
            output.flush()
            if (outputMessage == "bye")
                break
            println("Server: " + input.readLine())
        }
    } catch (e: IOException) {
        e.printStackTrace()
    }
    sc.close()
}
