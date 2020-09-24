//Franklin Nuth
//CSC316 - A
//Craps Project
//25 November 2018

import java.security.SecureRandom;

public class Die
{
    private SecureRandom randomNumbersDie = new SecureRandom();
    private int dieFaces; //= 1 + randomNumbersDie.nextInt(6); // = 1 + randomNumbersDie.nextInt(6);
    
    public Die()
    {
        this.dieFaces = 1 + randomNumbersDie.nextInt(6);
    }
    
    public int getRollingDie()
    {
        return dieFaces;
    }
    
    private void simulateAndSetRollingDie(int dieFaces)
    {
        this.dieFaces = 1 + randomNumbersDie.nextInt(6);
    }
}