import java.util.*;
import java.util.stream.Collectors;
// import java.util.stream.Collector;
public class Demo1{
    public static void main(String[] args){
        List<Integer> number = Arrays.asList(2,3,4);
        List<Integer> square = number.stream().map(x->x*x).collect(Collectors.toList());
        System.out.println(square);
        System.out.println(number);
        List <String> names =Arrays.asList("Dhruv","Darshil","Chirag");
        List <String> result = names.stream().filter(s->s.startsWith("D")).collect(Collectors.toList());
        System.out.println(result);
        }
}