//Franklin Nuth
//CSC316 - A
//Craps Project
//25 November 2018

import java.util.Scanner;

public class CrapsDriver
{
            
    public static void main(String args[])
    {
    Scanner playerInput = new Scanner(System.in);   
    HouseBank houseBankObject = new HouseBank();
    Player playerObject = new Player();
    Craps crapsObject = new Craps();
    Scanner inputBet = new Scanner(System.in); 
    
    int houseBank = houseBankObject.getHouseBank();
    int playerBank = playerObject.getPlayerBank();    
            
    System.out.printf("\nPlayer's money: " + playerBank + "\n"+ "The house's money: "+ houseBank + "\n\n" + "Please enter an integer to access a function below!\n[1]: Play a game of Craps.\n[2]: Go over the rules for Craps.\n[3]: Exit the program.\n");
    int input = playerInput.nextInt();
    
    while (input != 3)
    {
        switch (input) 
        {
            case 1:
                System.out.println("Please enter the amount you are going to bet: ");
                int betAmount = inputBet.nextInt();
                playerObject.setBetAmount(betAmount);
                crapsObject.playCraps();
                houseBank = houseBankObject.getHouseBank();
                playerBank = playerObject.getPlayerBank();
                System.out.printf("\nPlayer's money: " + playerBank + "\n"+ "The house's money: "+ houseBank + "\n\n" + "Please enter an integer to access a function below!\n[1]: Play a game of Craps.\n[2]: Go over the rules for Craps.\n[3]: Exit the program.\n");
                input = playerInput.nextInt();
                break;
            case 2:
                System.out.printf("\nThe game of Craps is played just by rolling a dice after betting.\nIf the number comes up as a 7 or an eleven, you win!\nIf you roll a 2, 3, or 12, you lose! If you roll any other number, you will enter a Point Round,\nwhere you will continue to roll until you roll the winning number to win, or roll a losing number to lose.\n\n");
                houseBank = houseBankObject.getHouseBank();
                playerBank = playerObject.getPlayerBank();
                System.out.printf("\nPlayer's money: " + playerBank + "\n"+ "The house's money: "+ houseBank + "\n\n" + "Please enter an integer to access a function below!\n[1]: Play a game of Craps.\n[2]: Go over the rules for Craps.\n[3]: Exit the program.\n");
                input = playerInput.nextInt();
                break;
            case 3:
                System.out.printf("\nOkay then. See you later!\n");
                break;
            default:
                System.out.printf("\nReturning to main menu due to invalid input error.\n\n");
                houseBank = houseBankObject.getHouseBank();
                playerBank = playerObject.getPlayerBank();
                System.out.printf("\nPlayer's money: " + playerBank + "\n"+ "The house's money: "+ houseBank + "\n\n" + "Please enter an integer to access a function below!\n[1]: Play a game of Craps.\n[2]: Go over the rules for Craps.\n[3]: Exit the program.\n");
                input = playerInput.nextInt();
                break;
        }
    }
    }
}