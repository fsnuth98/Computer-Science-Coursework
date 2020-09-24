//Franklin Nuth
//CSC316-A
//Assignment 10.16
//2 December 2018

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

   public double getModifiedSalary()
   {
      return baseSalary * 1.10;
   } 
   
   // calculate earnings
   @Override 
   public double getPaymentAmount()
   {
      return getBaseSalary() * 1.10;
   }

   // return String representation of BasePlusCommissionEmployee
   @Override
   public String toString()
   {
      return String.format("%s %s%n%s: %.2f", "base-salaried",
         super.toString(), "base salary", getBaseSalary());   
   } 
} 
