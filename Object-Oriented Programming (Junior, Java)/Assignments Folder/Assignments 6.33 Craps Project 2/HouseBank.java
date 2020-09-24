//Franklin Nuth
//CSC316 - A
//Craps Project
//25 November 2018

public class HouseBank
{
    private int houseBank = 10000;
    Player playerObjectForBank = new Player();
    
    private int playerWager = playerObjectForBank.getBetAmount();
    
    public HouseBank()
    {
    }
    
    public int getHouseBank()
    {
        return houseBank;
    }
    
    private void setHouseBank(int houseBank)
    {
        this.houseBank = houseBank;
    }
    
    public void houseWins(int playerWager)
    {
       this.houseBank = houseBank + playerWager;
    }
    
    public void houseLoses(int playerWager)
    {
       this.houseBank = houseBank - playerWager;
    }
}