public class Demo13 {
    public static void main(String[] args) {
        String day="saturday";
        switch(day){
            case "monday","tuesday","wednesday": System.out.println("first");
                    break;        
            case "friday","sunday","saturday": System.out.println("weekends");
                    break;
            default: System.out.println("Wrong day");
        } 
    }
}
