package d052;

import javax.swing.*;
import java.awt.*;

class Quiz09_07 {
    public static void main(String[] args) {
        var frame = new JFrame("Ten Color Buttons Frame");
        frame.setVisible(true);
        frame.setSize(300, 300);
        frame.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
        var pane = frame.getContentPane();
        pane.setLayout(new BorderLayout());
        var panel1 = new JPanel();
        panel1.add(new JLabel("enter text"));
        panel1.add(new JTextField(15));
        pane.add(panel1, BorderLayout.NORTH);
        var panel2 = new JPanel(new GridLayout(4, 4));
        for (int i = 0; i < 10; i++)
            panel2.add(new JButton(Integer.toString(i)));
        String[] ops = { "CE", "CAL", "+", "-", "x", "/" };
        for (var op : ops)
            panel2.add(new JButton(op));
        pane.add(panel2, BorderLayout.CENTER);
        var panel3 = new JPanel();
        panel3.add(new JLabel("op result"));
        panel3.add(new JTextField(15));
        pane.add(panel3, BorderLayout.SOUTH);
    }
}
