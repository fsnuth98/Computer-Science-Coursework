//Franklin Nuth
//CSC316 - A
//Assignment 8.1
//11 November 2018

/*Error Note: The constructors in MyLine, My Rectangle, and MyOval keep arguing with my setter functions,
so all instance variables are not set by the setter functions. */

// Fig. 8.18: DrawPanel.java
// Program that uses class MyLine
// to draw random lines.
import java.awt.Color;
import java.awt.Graphics;
import java.security.SecureRandom;
import javax.swing.JPanel;

public class DrawPanel extends JPanel
{
   private SecureRandom randomNumbers = new SecureRandom();   
   private MyLine[] lines; // array on lines
   private MyRectangle[] rectangles;
   private MyOval[] ovals;

   // constructor, creates a panel with random shapes
   public DrawPanel()
   {
      setBackground(Color.WHITE);
      
      lines = new MyLine[5 + randomNumbers.nextInt(5)];
      rectangles = new MyRectangle[5 + randomNumbers.nextInt(5)];
      ovals = new MyOval[5 + randomNumbers.nextInt(5)];

      // create lines
      for (int count = 0; count < lines.length; count++)
      {
         // generate random coordinates
         int x1 = randomNumbers.nextInt(300);
         int y1 = randomNumbers.nextInt(300);
         int x2 = randomNumbers.nextInt(300);
         int y2 = randomNumbers.nextInt(300);
         
         // generate a random color
         Color color = new Color(randomNumbers.nextInt(256), 
            randomNumbers.nextInt(256), randomNumbers.nextInt(256));
         
         lines[count] = new MyLine(x1, y1, x2, y2, color);
      } 
      
      for (int count = 0; count < rectangles.length; count++)
      {
         // generate random coordinates
         int x1 = randomNumbers.nextInt(300);
         int y1 = randomNumbers.nextInt(300);
         int x2 = randomNumbers.nextInt(300);
         int y2 = randomNumbers.nextInt(300);
         
         // generate a random color
         Color color = new Color(randomNumbers.nextInt(256), 
            randomNumbers.nextInt(256), randomNumbers.nextInt(256));
         
         rectangles[count] = new MyRectangle(x1, y1, x2, y2, color);
      } 
      
      for (int count = 0; count < ovals.length; count++)
      {
         // generate random coordinates
         int x1 = randomNumbers.nextInt(300);
         int y1 = randomNumbers.nextInt(300);
         int x2 = randomNumbers.nextInt(300);
         int y2 = randomNumbers.nextInt(300);
         
         // generate a random color
         Color color = new Color(randomNumbers.nextInt(256), 
            randomNumbers.nextInt(256), randomNumbers.nextInt(256));
         
         ovals[count] = new MyOval(x1, y1, x2, y2, color);
      } 
   }
   
   // for each shape array, draw the individual shapes
   public void paintComponent(Graphics g)
   {
      super.paintComponent(g);

      // draw the lines
      for (MyLine line : lines)
         line.draw(g);
      
      for (MyRectangle rectangle : rectangles)
         rectangle.draw(g);
      
      for (MyOval oval : ovals)
         oval.draw(g);
   } 
} // end class DrawPanel