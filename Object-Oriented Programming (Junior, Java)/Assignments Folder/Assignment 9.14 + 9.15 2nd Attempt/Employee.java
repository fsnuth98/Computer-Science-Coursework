//Franklin Nuth
//CSC316-A
//Assignment 9.14 + 9.15
//24 November 2018

//Error Note: Employee's public functions do not work in BasePlusCommissionEmployeeTest file.

public class Employee
{
   private String firstName;                              
   private String lastName;                               
   private String socialSecurityNumber;                   


   public Employee(String firstName, String lastName, 
      String socialSecurityNumber)
   {
      this.firstName = firstName;                                    
      this.lastName = lastName;                                    
      this.socialSecurityNumber = socialSecurityNumber;         
   }


   public String getFirstName()
   {
      return firstName;
   }

   public String getLastName()
   {
      return lastName;
   }

   public String getSocialSecurityNumber()
   {
      return socialSecurityNumber;
   } 
   
   @Override 
   public String toString()
   {
      return String.format("%s: %s %s%n%s: %s%n", 
         "employee", getFirstName(), getLastName(), 
         "social security number", getSocialSecurityNumber()); 
   }
} 