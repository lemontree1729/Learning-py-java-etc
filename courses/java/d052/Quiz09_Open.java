package d052;

import javax.swing.*;
import java.awt.*;

class Quiz09_Open {
    public static void main(String[] args) {
        var frame = new JFrame("frame");
        frame.setVisible(true);
        frame.setSize(300, 300);
        frame.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
        var pane = frame.getContentPane();
        pane.setLayout(new BorderLayout());
        var panel1 = new JPanel();
        String[] strs = { "Open", "Read", "Close" };
        for (var str : strs)
            panel1.add(new JButton(str));
        panel1.setBackground(Color.GRAY);
        pane.add(panel1, BorderLayout.NORTH);
        var panel2 = new JPanel(null);
        panel2.setBackground(Color.YELLOW);
        String[] word = { "Hello", "Java", "Love" };
        for (int i = 0; i < 3; i++) {
            var label = new JLabel(word[i]);
            label.setSize(50, 50);
            label.setLocation(50 + 20 * i, 50 + 20 * i);
            panel2.add(label);
        }
        pane.add(panel2, BorderLayout.CENTER);
    }
}
