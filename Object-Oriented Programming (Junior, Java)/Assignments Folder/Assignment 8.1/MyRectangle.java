//Franklin Nuth
//CSC316 - A
//Assignment 8.1
//11 November 2018

// Fig. 8.17: MyLine.java
// MyLine class represents a line.
import java.awt.Color;
import java.awt.Graphics;
//import java.security.SecureRandom;

public class MyRectangle
{   
   private int x1; // x-coordinate of first endpoint
   private int y1; // y-coordinate of first endpoint
   private int x2; // x-coordinate of second endpoint
   private int y2; // y-coordinate of second endpoint
   private Color color; // color of this line
   private boolean filled;


   // constructor with input values
   public MyRectangle(int x1, int y1, int x2, int y2, Color color)
   {
      this.x1 = x1; 
      this.y1 = y1; 
      this.x2 = x2; 
      this.y2 = y2; 
      this.color = color; 
      this.filled = true;
   } 
   
   public MyRectangle()
   {
      this.x1 = 0;
      this.y1 = 0; 
      this.x2 = 0; 
      this.y2 = 0; 
      this.color = Color.BLACK;
      this.filled = false;
   }
   
   public int getUpperLeftX()
   {
      /* SecureRandom randomX1rectangle = new SecureRandom();
       SecureRandom randomX2rectangle = new SecureRandom();
       
       this.x1 = randomX1rectangle.nextInt(300);
       this.x2 = randomX2rectangle.nextInt(300);*/
       
       if (this.x1 > this.x2)
       {
           return x1;
       }
       
       else
       {
           return x2;
       }
   }
   
   public int getUpperLeftY()
   {
       /*SecureRandom randomY1rectangle = new SecureRandom();
       SecureRandom randomY2rectangle = new SecureRandom();
       
       this.y1 = randomY1rectangle.nextInt(300);
       this.y2 = randomY2rectangle.nextInt(300);*/
       
       if (this.y1 > this.y2)
       {
           return y1;
       }
       
       else
       {
           return y2;
       }
   }
      
   public int getWidth()
   {
       if (x1 > x2)
       {
           return Math.abs(x1) - Math.abs(x2);
       }
       
       else
       {
           return Math.abs(x2) - Math.abs(x1);
       }
   }
   
   public int getHeight()
   {
       if (y1 > y2)
       {
           return Math.abs(y1) - Math.abs(y2);
       }
       
       else
       {
           return Math.abs(y2) - Math.abs(y1);
       }
   }
   
   public int getRectangleX1()
   {
       return x1;   
   }
   
   public void setRectangleX1(int x1)
   {
       if (this.x1 >= 0)
       {
           this.x1 = x1;
       }
       
       else
       {
           this.x1 = 0;
       }
   }
   
   public int getRectangleX2()
   {
       return x2;   
   }
   
   public void setRectangleX2(int x2)
   {
       if (this.x2 >= 0)
       {
           this.x2 = x2;
       }
       
       else
       {
           this.x2 = 0;
       }
   }
      
   public int getRectangleY1()
   {
       return y1;   
   }
   
   public void setRectangleY1(int y1)
   {
       if (this.y1 >= 0)
       {
           this.y1 = y1;
       }
       
       else
       {
           this.y1 = 0;
       }
   }
   
   public int getRectangleY2()
   {
       return y2;   
   }
   
   public void setRectangleY2(int y2)
   {
       if (this.y2 >= 0)
       {
           this.y2 = y2;
       }
       
       else
       {
           this.y2 = 0;
       }
      
   // Actually draws the line
   public void draw(Graphics g)
   {
      g.setColor(color);
      g.fillRect(getRectangleX1(), getRectangleY1(), getRectangleX2(), getRectangleY2());
   } 
} // end class MyLine