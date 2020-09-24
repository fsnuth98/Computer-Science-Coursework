//Franklin Nuth
//CSC316 - A
//Assignment 8.1
//11 November 2018

// Fig. 8.17: MyLine.java
// MyLine class represents a line.
import java.awt.Color;
import java.awt.Graphics;

public class MyLine
{
   private int x1; // x-coordinate of first endpoint
   private int y1; // y-coordinate of first endpoint
   private int x2; // x-coordinate of second endpoint
   private int y2; // y-coordinate of second endpoint
   private Color color; // color of this line

   // constructor with input values
   public MyLine(int x1, int y1, int x2, int y2, Color color)
   {
      this.x1 = x1; 
      this.y1 = y1; 
      this.x2 = x2; 
      this.y2 = y2; 
      this.color = color;
   } 
   
   public MyLine()
   {
      this.x1 = 0;
      this.y1 = 0; 
      this.x2 = 0; 
      this.y2 = 0; 
      this.color = Color.BLACK;
   }
   
   public int getLineX1()
   {
       return x1;   
   }
   
   public void setLineX1(int x1)
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
   
   public int getLineX2()
   {
       return x2;   
   }
   
   public void setLineX2(int x2)
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
      
   public int getLineY1()
   {
       return y1;   
   }
   
   public void setLineY1(int y1)
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
   
   public int getLineY2()
   {
       return y2;   
   }
   
   public void setLineY2(int y2)
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
      g.drawLine(getLineX1(),getLineY1(), getLineX2(), getLineY2());
   } 
} // end class MyLine