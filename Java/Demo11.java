import java.util.*;

public class Demo11 {
public static void main(String[] args) {
    List <String> gamesList = new ArrayList<String>();
    gamesList.add("Hockey");    
    gamesList.add("Football");    
    gamesList.add("Cricket");
    gamesList.forEach(games-> System.out.println(games));    
}    
}