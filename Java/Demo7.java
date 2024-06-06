import java.io.*;
import java.util.*;

public class Demo7 {
public static void main(String[] args) {
  String[] line = {"Hello", "My" ,"Name" ,"is" ,"darshil", "kumar"};
    try{
        File obj = new File("myFile.text");
        if (obj.createNewFile()) {
            System.out.println("File Created" + obj.getName());
        }
        else{
            System.out.println("File Already Exist");
        }
        FileWriter Writer = new FileWriter("myFile.text");
        for(int i =0; i<line.length; i++){
            Writer.write(line[i] + ' ');
        }
        Writer.close();
        Scanner Reader = new Scanner(obj);
        while (Reader.hasNextLine()) {
            String data = Reader.nextLine();
            System.out.println(data);
        }
        Reader.close();
    }
    catch( Exception e){
        System.out.println("An Error has accour");
        e.printStackTrace();
    }
}
    
}