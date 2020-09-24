//Franklin Nuth
//CSC316 - A
//Craps Project
//25 November 2018

public class Dice
{
    Die Die1 = new Die();
    Die Die2 = new Die();
    
    private int diceTotal;
    private int rolledDie1 = Die1.getRollingDie();
    private int rolledDie2 = Die2.getRollingDie();
    
    public Dice()
    {
        this.diceTotal = rolledDie1 + rolledDie2;
    }
    
    public int getTotalOfDice()
    {
        return diceTotal;
    }
    
    private void setTotalOfDie(int diceTotal)
    {
        this.diceTotal = diceTotal;
    }
}