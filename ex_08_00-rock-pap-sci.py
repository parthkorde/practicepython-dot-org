#Rock Paper Scissors | PARTH KORDE
def rps(option_A,option_B,condition):
    while True:
        if condition=='rs' or condition=='sr':
            if option_A=='r' and option_B=='s':
                print(f'Rocks beats Scissors.{player1} WINS! ')
            else:
                print(f'Rock beats Scissors. {player2} WINS! ')
        if condition=='rp' or condition=='pr':
            if option_A=='r' and option_B=='p':
                print(f'Paper beats Rock.{player2} WINS! ')
            else:
                print(f'Paper beats Rock. {player1} WINS! ')
        if condition=='ps' or condition=='sp':
            if option_A=='p' and option_B=='s':
                print(f'Scissors beat Paper.{player2} WINS! ')
            else:
                print(f'Scissors beat Paper. {player1} WINS! ')
        break
while True:
    player1=input('\nEnter player 1 name: ')
    if player1.lower=='stop':
        break
    player2=input('Enter player 2 name: ')
    A=input(f'Enter your choice {player1}: ')
    B=input(f'Enter your choice {player2}: ')
    try:
        int(A)
        print('Invlaid input. Please enter valid choices.')
        int(B)
        print('Invlaid input. Please enter valid choices.')
        continue
    except:
        if A.lower() in ['r','p','s'] and B.lower() in ['r','p','s']:
            inp_sum=A.lower()+ B.lower()
            ls_common=['rr','ss','pp']
            ls_comb=['rs','rp','ps']
            CHECK=inp_sum in ls_common
            # print(inp_sum)
            if CHECK==True:
                print(f"This is a tie. You're both good at reading minds! {A} and {B}")
            else:
                for check in ls_comb:
                    if check==inp_sum or check[::-1]==inp_sum:
# 'check' lines for any error!
                        # print(A)
                        # print(B)
                        # print(inp_sum)
                        rps(A.lower(),B.lower(),inp_sum)
                        break
                    # print(f'Check is {check}')
                    # print(f'input was {A} and {B}')
        else:
                print('Invalid Input. Please enter valid choices.')
                continue
