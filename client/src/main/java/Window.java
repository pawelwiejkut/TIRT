import javax.swing.*;
import java.awt.event.ActionListener;

/**
 * Created by pawelwiejkut on 21.12.2015.
 */
public class Window extends JFrame {

    private JButton startButton;
    private JTextArea textArea1;
    private JPanel rootPanel;

    public Window() {
        super("Lirycs for everyone");
        setContentPane(rootPanel);
        pack();
        setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
        setVisible(true);


    }


    public void textAreaString(String a){
        textArea1.append(a);
    }

}