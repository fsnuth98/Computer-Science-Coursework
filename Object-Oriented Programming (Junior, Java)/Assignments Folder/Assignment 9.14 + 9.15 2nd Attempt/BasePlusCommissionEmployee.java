//Franklin Nuth
//CSC316-A
//Assignment 9.14 + 9.15
//24 November 2018

public class BasePlusCommissionEmployee extends CommissionEmployee
{
    private double baseSalary;
    
   // six-argument constructor
   public BasePlusCommissionEmployee(String firstName, String lastName, 
      String socialSecurityNumber, int grossSales, 
      double commissionRate, double baseSalary)
   {
      super(firstName, lastName, socialSecurityNumber, 
         grossSales, commissionRate, baseSalary);                      
      // if baseSalary is invalid throw exception
      this.baseSalary = baseSalary;
   }
   
   // set base salary
   public void setBaseSalary(double baseSalary)
   {
      if (baseSalary < 0.0)                   
         throw new IllegalArgumentException(
            "Base salary must be >= 0.0");  

      this.baseSalary = baseSalary;                
   } 

   // return base salary
   public double getBaseSalary()
   {
      return baseSalary;
   } 

   // calculate earnings
   @Override 
   public double earnings()
   {
      return getBaseSalary() + super.earnings();
   }

   // return String representation of BasePlusCommissionEmployee
   @Override
   public String toString()
   {
      return String.format("%s %s%n%s: %.2f", "base-salaried",
         super.toString(), "base salary", getBaseSalary());   
   } 
} // end class BasePlusCommissionEmployee


/**************************************************************************
 * (C) Copyright 1992-2014 by Deitel & Associates, Inc. and               *
 * Pearson Education, Inc. All Rights Reserved.                           *
 *                                                                        *
 * DISCLAIMER: The authors and publisher of this book have used their     *
 * best efforts in preparing the book. These efforts include the          *
 * development, research, and testing of the theories and programs        *
 * to determine their effectiveness. The authors and publisher make       *
 * no warranty of any kind, expressed or implied, with regard to these    *
 * programs or to the documentation contained in these books. The authors *
 * and publisher shall not be liable in any event for incidental or       *
 * consequential damages in connection with, or arising out of, the       *
 * furnishing, performance, or use of these programs.                     *
 *************************************************************************/
