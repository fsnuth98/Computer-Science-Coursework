//Franklin Nuth
//CSC316 - A
//Craps Project
//25 November 2018

import java.util.Scanner;

public class Player
{
    Dice playerThrowDice = new Dice();
    Scanner inputBet = new Scanner(System.in);        
    
    private int playerBank;
    private int betAmount;      
    
    public Player()
    {
        this.playerBank = 1000;
        this.betAmount = getBetAmount();
    }
    
    public int getPlayerBank()
    {
        return playerBank;
    }
    
    private void setPlayerBank(int playerBank)
    {
        this.playerBank = playerBank;
    }
    
    /*
    public void queryBetAmount()
    {
        System.out.println("Please enter the amount you are going to bet: ");
        this.betAmount = inputBet.nextInt();
    }
    */

    public int getBetAmount()
    {
        return betAmount;
    }
    
    public void setBetAmount(int betAmount)
    {
        this.betAmount = betAmount;
    }
    
    public int throwDice()
    {
        return playerThrowDice.getTotalOfDice();
    }
    
    public void playerWins(int betAmount)
    {
       this.playerBank = playerBank + betAmount;
    }
    
    public void playerLoses(int betAmount)
    {
       this.playerBank = playerBank - betAmount;
    }
}