//Franklin Nuth
//CSC316 - A
//Craps Project
//6 December 2018

public class Dealer
{   
    Player dealerSeePlayerDice = new Player();
    
    public Dealer()
    {
        this.dealerSeePlayerDice = dealerSeePlayerDice;
    }
    
    public void announceThrowDiceResult()
    {
        System.out.printf("The player has thrown a " + dealerSeePlayerDice.getRolledDice() + "!\n");
    }
}