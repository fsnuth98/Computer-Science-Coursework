//Franklin Nuth
//CSC316 - A
//Craps Project
//25 November 2018

import java.security.SecureRandom;
import java.util.Scanner;

public class Craps
{
    SecureRandom randomNumbersCraps = new SecureRandom();
    Crowd crapsCrowdResponse = new Crowd();
        
    Player playerDice = new Player();
    Player playerRole = new Player();
    Dealer dealerRole = new Dealer();
    HouseBank housebankRole = new HouseBank();
    
    private enum Status{CONTINUE, WON, LOST};
    private Status gameStatus;
    
    private static final int SNAKE_EYES = 2;
    private static final int TREY = 3;
    private static final int SEVEN = 7;
    private static final int YO_LEVEN = 11;
    private static final int BOX_CARS = 12;
    
    private int myPoint;
        
    int PlayerBank = playerRole.getPlayerBank();
    int HouseBank = housebankRole.getHouseBank();
    int playerBet = playerRole.getBetAmount();
    
    public Craps()
    {
        this.myPoint = 0;
    }
    
    public void playCraps()
    {   
        int sumOfDice = playerDice.throwDice();
        dealerRole.announceThrowDiceResult();
        
        switch(sumOfDice)
        {
            case SEVEN:
            case YO_LEVEN:
                gameStatus = Status.WON;
                crapsCrowdResponse.getCrowdWinResponse();
                playerRole.playerWins(playerBet);
                housebankRole.houseLoses(playerBet);
                break;
            case SNAKE_EYES:
            case TREY:
            case BOX_CARS:
                gameStatus = Status.LOST;
                crapsCrowdResponse.getCrowdLoseResponse();
                playerRole.playerLoses(playerBet);
                housebankRole.houseWins(playerBet);
                break;
            default:
                gameStatus = Status.CONTINUE;
                crapsCrowdResponse.getCrowdPointResponse();
                myPoint = sumOfDice;
                System.out.printf("\nPoint is %d%n", myPoint);
        }
        
        while (gameStatus == Status.CONTINUE)
        {
            sumOfDice = playerDice.throwDice();
            dealerRole.announceThrowDiceResult();
            
            if (gameStatus == Status.WON)
            {
                System.out.println("Player wins!\n");
                playerRole.playerWins(playerBet);
                housebankRole.houseLoses(playerBet);
                crapsCrowdResponse.getCrowdWinResponse();
                break;
            }
            
            else
            {
                System.out.println("Player loses!\n");
                playerRole.playerLoses(playerBet);
                housebankRole.houseWins(playerBet);
                crapsCrowdResponse.getCrowdLoseResponse();
                break;
            }
        }
    }
}