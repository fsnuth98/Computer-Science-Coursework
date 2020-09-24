//Franklin Nuth
//CSC316-A
//Assignment 10.16
//2 December 2018

public class PayableInterfaceTest 
{
   public static void main(String[] args)
   {
      // create four-element Payable array
      Payable[] payableObjects = new Payable[7];
      
      // populate array with objects that implement Payable
      payableObjects[0] = new Invoice("01234", "seat", 2, 375.00);
      payableObjects[1] = new Invoice("56789", "tire", 4, 79.95);
      payableObjects[2] = new SalariedEmployees("John", "Smith", "111-11-1111", 800.00);
      payableObjects[3] = new SalariedEmployees("Lisa", "Barnes", "888-88-8888", 1200.00);
      payableObjects[4] = new HourlyEmployee("Monolisa", "Barnes", "888-88-8888", 1200.00, 40.0);
      payableObjects[5] = new CommissionEmployee("Nino", "Barnes", "888-88-8888", 10000, 0.5, 0.5);
      payableObjects[6] = new BasePlusCommissionEmployee("James", "Barnes", "888-88-8888", 10, 0.5, 100);

      System.out.println("Invoices and Employees processed polymorphically:"); 

      // generically process each element in array payableObjects
      for (Payable currentPayable : payableObjects)
      {
          if(currentPayable instanceof BasePlusCommissionEmployee)
          {
            ((BasePlusCommissionEmployee) currentPayable).getModifiedSalary();
            System.out.printf("%n%s %n%s: $%,.2f%n", 
            currentPayable.toString(), // coduld invoke implicitly
            "payment due", currentPayable.getPaymentAmount()); 
          }
          
          else
          {    
         // output currentPayable and its appropriate payment amount
         System.out.printf("%n%s %n%s: $%,.2f%n", 
            currentPayable.toString(), // could invoke implicitly
            "payment due", currentPayable.getPaymentAmount()); 
          }
      } 
   } // end main
} 