package d060;

import java.io.*;
import java.net.Socket;
import java.util.Scanner;

class ClientEx {
    public static void main(String[] args) {
        var sc = new Scanner(System.in);
        try {
            var socket = new Socket("localhost", 8888);
            var in = new BufferedReader(new InputStreamReader(socket.getInputStream()));
            var out = new BufferedWriter(new OutputStreamWriter(socket.getOutputStream()));
            while (true) {
                System.out.print("to send>>");
                var output = sc.nextLine();
                out.write(output + "\n");
                out.flush();
                if (output.equals("bye")) {
                    break;
                }
                System.out.println("Server: " + in.readLine());
            }
        } catch (IOException e) {
            e.printStackTrace();
        }
        sc.close();
    }
}
