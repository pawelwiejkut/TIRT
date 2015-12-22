import org.apache.commons.io.IOUtils;

import javax.swing.*;
import java.io.*;
import java.net.Socket;

public class FileClient {

    public String GetResponse(Window window) {
        Socket sock = null;
        try {
            sock = new Socket("10.0.0.10", 5110);
        } catch (IOException e) {
            return "Connection to server error\n";
        }

        transferFile(sock);
        String resp = getMessage(sock,window);

        try {
            sock.close();
        } catch (IOException e) {
            e.printStackTrace();
        }
        return resp;
    }


    public static void transferFile(Socket sock) {
        byte[] mybytearray = new byte[1024];
        OutputStream os = null;
        try {
            os = sock.getOutputStream();
        } catch (IOException e) {
            e.printStackTrace();
        }
        FileInputStream fos = null;
        try {
            fos = new FileInputStream("sample.cap");
        } catch (FileNotFoundException e) {
            e.printStackTrace();
        }
        int count;
        try {
            while ((count = fos.read(mybytearray)) > 0) {
                os.write(mybytearray, 0, count);
            }
            sock.shutdownOutput();
            fos.close();
        } catch (IOException e) {
            e.printStackTrace();
        }


    }

    public String getMessage(Socket sock, final Window window) {
        final Main wind = new Main();
        InputStream is = null;
        try {
            is = sock.getInputStream();
        } catch (IOException e) {
            e.printStackTrace();
        }
        DataInputStream incomingMessage = new DataInputStream(is);
        try {
            String s;
            while ((s = incomingMessage.readLine()) != null) {
                final String finalS = s;
                SwingUtilities.invokeLater(new Runnable() {
                    public void run() {
                        window.textAreaString(finalS+"\n");
                    }
                });
                response(s);
            }
            is.close();

        } catch (IOException e) {
            return "Nie udało się pobrać odpowiedzi z serwera";
        }
    return null;
    }

    public String response(String resp){
        return resp;
    }

}
