package d060;

import java.io.*;
import java.net.ServerSocket;
import java.util.Scanner;

class ServerEx {
    public static void main(String[] args) {
        var sc = new Scanner(System.in);
        try {
            System.out.println("waiting for connect...");
            var socket = new ServerSocket(9999).accept();
            System.out.println("connected");
            var in = new BufferedReader(new InputStreamReader(socket.getInputStream()));
            var out = new BufferedWriter(new OutputStreamWriter(socket.getOutputStream()));
            while (true) {
                var input = in.readLine();
                if (input.equals("bye")) {
                    System.out.println("client entered bye");
                    break;
                }
                System.out.println("Client: " + input);
                System.out.print("to send>>");
                out.write(sc.nextLine() + "\n");
                out.flush();
            }
        } catch (IOException e) {
            e.printStackTrace();
        }
        sc.close();
    }
}
