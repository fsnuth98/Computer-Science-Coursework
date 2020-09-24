//Franklin Nuth
//CSC316 - A
//Craps Project
//25 November 2018

import java.security.SecureRandom;
import java.util.Arrays;

public class Crowd
{
    /*
    public String[] winResponses = {"Amazing roll!\n",
                                           "Looks like its your lucky day!\n",
                                           "Can I please get some of that luck, too?\n"};
    
    public String[] loseResponses = {"Aww, you lost the roll. Let's try again!\n",
                                            "It's a lose. Better luck next time!\n",
                                            "It's a no this time, Chief. We should get a better roll next time!\n"};
    
    public String[] pointResponses = {"The suspense is killing me!\n",
                                             "Things are getting hype aroud here!\n",
                                             "This is intense!\n"};
    */
    
    SecureRandom randomNumbersForCrowd = new SecureRandom();
    
    private int randomNumber = randomNumbersForCrowd.nextInt(3);
    
    public Crowd()
    {
       
    }
    
    public void getCrowdWinResponse()
    {
        if(randomNumber == 1)
        {
        System.out.printf("Amazing roll!\n");
        }
        
        else if(randomNumber == 2)
        {
        System.out.printf("Looks like it's your lucky day!\n");
        }
        
        else if(randomNumber == 3)
        {
        System.out.printf("Can I please some of that luck too?!\n");
        }
    }
    
    public void getCrowdLoseResponse()
    {
        if(randomNumber == 1)
        {
        System.out.printf("Aww, you lost the roll. Let's try again!\n");
        }
        
        else if(randomNumber == 2)
        {
        System.out.printf("It's a lose. Better luck next time!\n");
        }
        
        else if(randomNumber == 3)
        {
        System.out.printf("It's a no this time, chief. Maybe you'll do better next time.");
        }
    }
        
    public void getCrowdPointResponse()
    {
        if(randomNumber == 1)
        {
        System.out.printf("The suspense is killing me!");
        }
        
        else if(randomNumber == 2)
        {
        System.out.printf("Things are getting interesting around here!");
        }
        
        else if(randomNumber == 3)
        {
        System.out.printf("Well this is intriguing.");
        }
    }
    
}