//Franklin Nuth
//CSC316-A
//Assignment 9.14 + 9.15
//24 November 2018

public class PieceworkerEmployee extends Employee
{
    private double pieces;
    private double wage;
    
    public PieceworkerEmployee(String firstName, String lastName, String socialSecurityNumber, double pieces, double wage)
    {
        super(firstName, lastName, socialSecurityNumber);
        
        this.pieces = pieces;
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
   
   public void setPieces(double hours)
   {
       this.pieces = pieces;
   }
   
   public double getPieces()
   {
       return pieces;
   }
   
   public double earnings()              
   {                                     
      return wage * pieces;
   } 
   
   @Override
   public String toString()                                             
   {                                                                    
      return String.format("%n%s: %.2f%n%s: %.2f",                    
         "pieces", pieces,                                     
         "wage", wage, super.toString());                           
   } 
}
   