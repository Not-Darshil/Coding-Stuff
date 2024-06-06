interface Sayable {
    void say();
}
public class MethodReference {
    public static void saySomething() {
        System.out.println("It is static method.");
    }
    public static void main(String[] args) {
        Sayable sayable = MethodReference::saySomething;
        sayable.say();
    }
}