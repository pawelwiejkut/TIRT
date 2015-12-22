import javax.swing.*;

/**
 * Created by pawelwiejkut on 21.12.2015.
 */
public class Main {
    public static void main(String[] args) {

        Window window = new Window();
        window.textAreaString("Hi, le't try to find your subtitles...\n");
        window.textAreaString("Geting sample of your song in progress\n");
        GetPcap pcap = new GetPcap();
        window.textAreaString("Data uploaded successful, please wait ...\n");
        FileClient fileClient = new FileClient();
        window.textAreaString(fileClient.GetResponse(window));

    }
}
