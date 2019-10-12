from random import randint


def game():
    print('Welcome! You\'re Playing:')
    print(
    """
   _____      ________                                _____  ________  .__              
  /  _  \    /  _____/_____    _____   ____     _____/ ____\ \______ \ |__| ____  ____  
 /  /_\  \  /   \  ___\__  \  /     \_/ __ \   /  _ \   __\   |    |  \|  |/ ___\/ __ \ 
/    |    \ \    \_\  \/ __ \|        \  ___/  (  <_> )  |     |    `   \  \  \__\  ___/ 
\____|__  /  \______  (____  /__|_|  /\___  >  \____/|__|    /_______  /__|\___  >___  >
        \/          \/     \/      \/     \/                         \/        \/    \/ 
    """
    )

    human_bank = 1000
    while True:
        you = float(input("How much money do you want to wager? "
                        "Your bank has ${} ".format(human_bank)))
        if you > 0 <= human_bank:
            print("You're betting ${}".format(you))
            dice_roll = randint(1, 6)
            human_guess = float(input('What number you think the dice will roll on? '
                                        'Select numbers: 1-6 '))
            if human_guess == dice_roll:
                human_bank += you
                print('Dice landed on {}'.format(dice_roll))
                print("Congrats! You now have ${}".format(human_bank))
            else:
                human_bank -= you
                print("Bummers! Dice landed on {}! Money gone...".format(dice_roll))
                print("You have ${}".format(human_bank))
            if human_bank == 0.0:
                print("Game over! You're out of cash")
                break
            play_again = input("Enter 'y' to play again or 'n' to stop ").lower()
            if play_again == 'y':
                continue
            elif play_again == 'n':
                print("Game Over...")
                if human_bank > 1000:
                    print("You're lucky! You won ${} ".format(human_bank - 1000))
                    break
                elif human_bank < 1000:
                    print("Better luck next time! You loss ${} ".format(1000 - human_bank))
                    break
                else:
                    print("You didn't win nor you didn't lose!")
                    break
        else:
            print('Enter a valid amount. You have ${} to bet'.format(human_bank))
game()



