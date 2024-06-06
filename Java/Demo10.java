import java.util.*;

public class Demo10 {

    public static void main(String[] args) {
        String Sample = "India will won the T20 world cup";
        System.out.println("Sample String is : " + Sample);
        String Basicformat = Base64.getEncoder().encodeToString(Sample.getBytes());
        System.out.println("Encoding Sample is : " + Basicformat);
        byte[] actualByte = Base64.getDecoder().decode(Basicformat);
        String actualcode = new String(actualByte);
        System.out.println("Decoding string is : " + actualcode);
    }
}