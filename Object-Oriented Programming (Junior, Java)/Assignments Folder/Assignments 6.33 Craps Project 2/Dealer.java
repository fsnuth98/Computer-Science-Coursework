//Franklin Nuth
//CSC316 - A
//Craps Project
//25 November 2018

public class Dealer
{   
    Player dealerSeePlayerDice = new Player();
    
    public Dealer()
    {
    }
    
    public void announceThrowDiceResult()
    {
        System.out.print("The player has thrown a " + dealerSeePlayerDice.throwDice() + "!\n");
    }
}