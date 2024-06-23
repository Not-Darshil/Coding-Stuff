public class Demo14 {
    public static void main(String[] args) {
        Dog dog = new Dog();
        dog.eatSomething();
    }

    static void eatSomething() {
        System.out.println("Eating Foods");
    }

    static class Animal {
        void eatSomething() {
            System.out.println("Animal is eating");
        }
    }

    static class Dog extends Animal {
        @Override
        void eatSomething() {
            System.out.println("EATING SOMETHING");
        }
    }
}
