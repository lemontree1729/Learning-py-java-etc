package d052;

import javax.swing.*;
import java.awt.*;

class Quiz09_03 {
    public static void main(String[] args) {
        var frame = new JFrame("Ten Color Buttons Frame");
        frame.setVisible(true);
        frame.setSize(500, 200);
        frame.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
        var pane = frame.getContentPane();
        pane.setLayout(new GridLayout(4, 4));
        for (int i = 0; i < 16; i++) {
            var buttom = new JButton(Integer.toString(i));
            buttom.setBackground(new Color((float) Math.random(), (float) Math.random(), (float) Math.random()));
            pane.add(buttom);
        }
    }
}
