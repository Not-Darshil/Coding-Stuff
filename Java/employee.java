import java.io.Serializable;

class Employee implements Serializable {
    int empid;
    String empname;

    public Employee(int empid, String empname) {
        this.empid = empid;
        this.empname = empname;
    }
}
