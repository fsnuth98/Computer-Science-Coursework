//Franklin Nuth
//CSC316-A
//Assignment 9.14 + 9.15
//24 November 2018

public class SalariedEmployees extends Employee
{
    private double hours;
    private double wage;
    
    public SalariedEmployees(String firstName, String lastName, String socialSecurityNumber, double hours, double wage)
    {
        super(firstName, lastName, socialSecurityNumber);
        
        this.hours = hours;
        this.wage = wage;
    }
    
   public void setWage(double wage)
   {
       this.wage = wage;
   }
   
   public double getWage()
   {
    if (wage < 0.0)
    throw new IllegalArgumentException("Base salary must be >= 0.0");
        return wage;
   }
   
   public void setHours(double hours)
   {
       if(hours >= 0 | hours <= 168)
       {
       this.hours = hours;
       }
       
       else
       {
           System.out.println("Invalid hours; cannot work less than 0 or more than 168.");
       }
       
   }
   
   public double getHours()
   {
       return hours;
   }
   
   public double earnings()              
   {                                     
      return wage * hours;
   } 
   
   @Override
   public String toString()                                             
   {                                                                    
      return String.format("%n%s: %.2f%n%s: %.2f",                    
         "hours", hours,                                     
         "wage", wage, super.toString());                           
   } 
   
}