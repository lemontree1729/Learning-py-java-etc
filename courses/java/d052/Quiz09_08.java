package d052;

import javax.swing.*;
import java.awt.*;

class Quiz09_08 {
    public static void main(String[] args) {
        var frame = new JFrame("frame");
        frame.setVisible(true);
        frame.setSize(300, 300);
        frame.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
        var pane = frame.getContentPane();
        pane.setLayout(new BorderLayout());
        var panel1 = new JPanel();
        panel1.add(new JButton("open"));
        panel1.add(new JButton("close"));
        panel1.add(new JButton("exit"));
        panel1.setBackground(Color.GRAY);
        pane.add(panel1, BorderLayout.NORTH);
        var panel2 = new JPanel(null);
        for (int i = 0; i < 20; i++) {
            var label = new JLabel();
            label.setSize(10, 10);
            label.setBackground(Color.BLUE);
            label.setLocation((int) (Math.random() * 200 + 50), (int) (Math.random() * 160));
            label.setOpaque(true);
            panel2.add(label);
        }
        pane.add(panel2, BorderLayout.CENTER);
        var panel3 = new JPanel();
        panel3.add(new JButton("Word Input"));
        panel3.add(new JTextField(15));
        panel3.setBackground(Color.YELLOW);
        pane.add(panel3, BorderLayout.SOUTH);
    }
}
