package d060

import java.io.BufferedWriter
import java.io.OutputStreamWriter
import java.net.Socket
import java.util.*

fun main() {
    val sc = Scanner(System.`in`)
    print("enter server ip to connect>>")
    val serverip = sc.nextLine()
    val socket = Socket(serverip, 9999)
    println("connected with server $serverip")
    val output = BufferedWriter(OutputStreamWriter(socket.getOutputStream()))
    while (true) {
        val outputMessage = sc.nextLine()
        output.write("$outputMessage\n")
        output.flush()
        if (outputMessage == "stop")
            break
    }
}