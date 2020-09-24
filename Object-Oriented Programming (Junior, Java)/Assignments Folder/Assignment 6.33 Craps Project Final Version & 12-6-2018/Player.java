//Franklin Nuth
//CSC316 - A
//Craps Project
//6 December 2018

import java.util.Scanner;

public class Player
{
    Scanner inputBet = new Scanner(System.in);      
    Dice playerThrowDice;
    private int playerBank = 1000;
    private int betAmount;    
    public int rolledAmount;
    public int thrownDice;
    
    public Player()
    {
        playerThrowDice = new Dice();
        this.playerBank = 1000;
        this.betAmount = getBetAmount();
        this.rolledAmount = throwDice();
    }
    
    public int getPlayerBank()
    {
        return playerBank;
    }
    
    private void setPlayerBank(int playerBank)
    {
        this.playerBank = playerBank;
    }

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
        int thrownDice = playerThrowDice.getTotalOfDice();
        return thrownDice;
    }
    
    public int getRolledDice()
    {
        return rolledAmount;
    }
    
    public void playerWins(int betAmount)
    {
       playerBank = playerBank + betAmount;
    }
    
    public void playerLoses(int betAmount)
    {
       playerBank = playerBank - betAmount;
    }
}