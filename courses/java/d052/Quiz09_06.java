package d052;

import java.awt.Color;

import javax.swing.*;

class Quiz09_06 {
    public static void main(String[] args) {
        var frame = new JFrame("Random Labels");
        frame.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
        frame.setVisible(true);
        frame.setSize(300, 300);
        var pane = frame.getContentPane();
        pane.setLayout(null);
        for (int i = 0; i < 20; i++) {
            var label = new JLabel();
            label.setSize(10, 10);
            label.setBackground(Color.BLUE);
            label.setLocation((int) (Math.random() * 300), (int) (Math.random() * 300));
            label.setOpaque(true);
            pane.add(label);
        }
    }
}
