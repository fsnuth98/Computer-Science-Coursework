//Franklin Nuth
//CSC316-A
//Assignment 9.14 + 9.15
//24 November 2018

public class CommissionEmployee extends Employee
{           
   private double grossSales; // gross weekly sales       
   private double commissionRate; // commission percentage
   private double baseSalary;
   
   public CommissionEmployee(String firstName, String lastName, String socialSecurityNumber, int grossSales, 
      double commissionRate, double baseSalary)
   {                
      super(firstName, lastName, socialSecurityNumber);
       
      if (grossSales < 0.0) 
         throw new IllegalArgumentException(
            "Gross sales must be >= 0.0");
      
      if (commissionRate <= 0.0 || commissionRate >= 1.0)
         throw new IllegalArgumentException(
            "Commission rate must be > 0.0 and < 1.0");
      
      this.grossSales = grossSales;
      this.commissionRate = commissionRate;
      this.baseSalary = baseSalary;
   }

   public void setGrossSales(double grossSales)
   {
      if (grossSales < 0.0) 
         throw new IllegalArgumentException(
            "Gross sales must be >= 0.0");

      this.grossSales = grossSales;
   } 

   public double getGrossSales()
   {
      return grossSales;
   } 

   public void setCommissionRate(double commissionRate)
   {
      if (commissionRate <= 0.0 || commissionRate >= 1.0)
         throw new IllegalArgumentException(
            "Commission rate must be > 0.0 and < 1.0");

      this.commissionRate = commissionRate;
   } 

   public double getCommissionRate()
   {
      return commissionRate;
   } 
               
   public double earnings()              
   {                                     
      return commissionRate * grossSales;
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
   
   @Override
   public String toString()                                             
   {                                                                    
      return String.format("%n%s: %.2f%n%s: %.2f",                    
         "gross sales", grossSales,                                     
         "commission rate", commissionRate, super.toString());                           
   } 
}