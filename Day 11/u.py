def draw(player, cpu):
    for _ in cards:
        deck = cards[random.randint(0, len(cards)-1)]
        draw_card = deck
        if len(player) == 2:
            break
        else:
            player.append(draw_card)

    for _ in cards:
        deck = cards[random.randint(0, len(cards)-1)]
        draw_card = deck
        if len(cpu) == 2:
            break
        else:
            cpu.append(draw_card)
    
    player_score = sum(player_hand)
    cpu_score = sum(cpu_hand)

cpu_first = cpu_hand[0]



# def initial_check(pscore, cscore):
#     if pscore == 21:
#         startGame = False
#         clearConsole()
#         print(logo)
#         print(f"Your final hand: {player_hand}, final score: {player_score}")
#         print(f"Computer's final cards: {cpu_hand}, score: {cpu_score}")
#         print("You win 😃")
#         menu = input(
#     "Do you want to play a game of Blackjack? Type 'y' or 'n': ").lower()

#     elif cscore == 21:
#         startGame = False
#         clearConsole()
#         print(logo)
#         print(f"Your final hand: {player_hand}, final score: {player_score}")
#         print(f"Computer's final hand: {cpu_hand}, final score: {cpu_score}")

def player_turn(player_hand,player_score,):
    """Initiate player's turn"""
    deck = cards[random.randint(0, len(cards)-1)]
    draw_card = deck
    player_hand.append(draw_card)
    player_score = sum(player_hand)


menu = input(
    "Do you want to play a game of Blackjack? Type 'y' or 'n': ").lower()

if menu == "y":
    clearConsole()
    # blackjack()
    startGame = True

elif menu == "n":
    startGame = False

draw(player_hand, cpu_hand)



while startGame:
    print(logo)

    print(f"Your cards: {player_hand}, current score: {player_score}")
    print(f"Computer's first hand: {cpu_first}")
    choice = input("Type 'y' to get another card, type 'n' to pass: ")
    if choice = ye
    player_turn(player_hand = player_hand,player_score = player_score)
    # initial_check(player_score,player_score)

    if (player_score > 21 and 11 in player_hand):
        for i in range(len(player_hand)):
            if player_hand[i] == 11:
                player_hand[i] = 1
    elif (cpu_score > 21 and 11 in cpu_hand):
        for i in range(len(cpu_hand)):
            if cpu_hand[i] == 11:
                cpu_hand[i] = 1