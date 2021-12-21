package d052;

import javax.swing.*;
import java.awt.*;

class Quiz09_02 {
    public static void main(String[] args) {
        var frame = new JFrame("BorderLayout Practice");
        frame.setVisible(true);
        frame.setSize(400, 200);
        frame.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
        var pane = frame.getContentPane();
        pane.setLayout(new BorderLayout(5, 7));
        pane.add(new JButton("Center"), BorderLayout.CENTER);
        pane.add(new JButton("North"), BorderLayout.NORTH);
        pane.add(new JButton("West"), BorderLayout.WEST);
        pane.add(new JButton("East"), BorderLayout.EAST);
        pane.add(new JButton("South"), BorderLayout.SOUTH);
    }
}