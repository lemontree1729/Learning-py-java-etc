package d060

import java.io.BufferedWriter
import java.io.OutputStreamWriter
import java.net.ServerSocket

class TimerThread(val output: BufferedWriter) : Thread() {
    override fun run() {
        val tick = 20
        var cnt = 0
        while (cnt < tick) {
            output.write("${cnt++}\n")
            output.flush()
            Thread.sleep(500)
        }
    }
}

fun main() {
    val server = ServerSocket(9999)
    println("It's time server")
    println("connecting to client...")
    val socket = server.accept()
    println("connected with client")
    val output = BufferedWriter(OutputStreamWriter(socket.getOutputStream()))
    val timer = TimerThread(output)
    timer.start()
    println("server closed")
}