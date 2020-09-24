//Franklin Nuth
//CSC316-A
//Assignment 9.14 + 9.15
//24 November 2018

public class HourlyEmployeeTest 
{
   public static void main(String[] args) 
   {
      // instantiate CommissionEmployee object
      HourlyEmployee employee = new HourlyEmployee(
         "Sue", "Jones", "222-22-2222", 10000, .06);      
      
      // get commission employee data
      System.out.println(
         "Employee information obtained by get methods:");
      System.out.printf("%n%s %s%n", "First name is",
         employee.getFirstName());
      System.out.printf("%s %s%n", "Last name is", 
         employee.getLastName());
      System.out.printf("%s %s%n", "Social security number is", 
         employee.getSocialSecurityNumber());
      System.out.printf("%s %.2f%n", "Wage is", 
         employee.getWage());
      System.out.printf("%s %.2f%n", "Hours is",
         employee.getHours());

      //employee.setGrossSales(5000); 
      //employee.setCommissionRate(.1); 
      
      System.out.printf("%n%s:%n%n%s%n",                                
         "Updated employee information obtained by toString", employee);
   } // end main
} // end class CommissionEmployeeTest