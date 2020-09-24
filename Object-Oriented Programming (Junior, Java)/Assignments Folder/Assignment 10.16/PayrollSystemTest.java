//Franklin Nuth
//CSC316-A
//Assignment 10.16
//2 December 2018

public class PayrollSystemTest 
{
    public static void main(String args[])
    {
    SalariedEmployees salariedEmployees = new SalariedEmployees( "John", "Smith", "111-11-1111", 800.00);
    HourlyEmployee hourlyEmployee = new HourlyEmployee( "Karen", "Price", "222-22-2222", 16.75, 40 );
    CommissionEmployee commissionEmployee = new CommissionEmployee("Sue", "Jones", "333-33-3333", 10000, .06, 10 );
    BasePlusCommissionEmployee basePlusCommissionEmployee = new BasePlusCommissionEmployee("Bob", "Lewis", "444-44-4444",5000, .04, 300 );
    PieceworkerEmployee pieceWorker = new PieceworkerEmployee("Ralph", "Tang", "777-223-987", 213, 16);
    
    System.out.printf("********** (Printing for each object individually.)\n");
    System.out.printf( "%s\n%s: $%,.2f\n\n", salariedEmployees, "earned", salariedEmployees.getPaymentAmount());
    System.out.printf( "%s\n%s: $%,.2f\n\n", hourlyEmployee, "earned", hourlyEmployee.getPaymentAmount());
    System.out.printf( "%s\n%s: $%,.2f\n\n", commissionEmployee, "earned", commissionEmployee.getPaymentAmount());
    System.out.printf( "%s\n%s: $%,.2f\n\n", basePlusCommissionEmployee, "earned", basePlusCommissionEmployee.getPaymentAmount());
    System.out.printf( "%s\n%s: $%,.2f\n\n", pieceWorker, "earned", pieceWorker.getPaymentAmount());
    System.out.printf("********** (Printing for each object through array.)\n");
    
    Employee employees[] = new Employee[ 5 ];

    employees[0] = salariedEmployees;
    employees[1] = hourlyEmployee;
    employees[2] = commissionEmployee;
    employees[3] = basePlusCommissionEmployee;
    employees[4] = pieceWorker; 
    
    for(Employee currentEmployee : employees)
        {   
        if (currentEmployee instanceof SalariedEmployees)
        {
        System.out.printf( "%s\n%s: $%,.2f\n\n", salariedEmployees, "earned", salariedEmployees.getPaymentAmount());
        }
        else if (currentEmployee instanceof HourlyEmployee)
        {
        System.out.printf( "%s\n%s: $%,.2f\n\n", hourlyEmployee, "earned", hourlyEmployee.getPaymentAmount());
        }
        else if (currentEmployee instanceof CommissionEmployee)
        {
        System.out.printf( "%s\n%s: $%,.2f\n\n", commissionEmployee, "earned", commissionEmployee.getPaymentAmount());
        }
        else if (currentEmployee instanceof BasePlusCommissionEmployee)
        {
        System.out.printf( "%s\n%s: $%,.2f\n\n", basePlusCommissionEmployee, "earned", basePlusCommissionEmployee.getPaymentAmount());
        }
        else if (currentEmployee instanceof PieceworkerEmployee)
        {
        System.out.printf( "%s\n%s: $%,.2f\n\n", pieceWorker, "earned", pieceWorker.getPaymentAmount());
        }
        }
    }
    
}
