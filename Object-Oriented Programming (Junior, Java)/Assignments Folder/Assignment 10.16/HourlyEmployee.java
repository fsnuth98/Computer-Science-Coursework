//Franklin Nuth
//CSC316-A
//Assignment 10.16
//2 December 2018

public class HourlyEmployee extends Employee
{
   private double hours;
   private double wage;
    
   public HourlyEmployee(String firstName, String lastName, String socialSecurityNumber, double wage, double hours)
   {
       super(firstName, lastName, socialSecurityNumber);
       
       this.wage = wage;
       this.hours = hours;
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
   
   @Override
   public double getPaymentAmount()              
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