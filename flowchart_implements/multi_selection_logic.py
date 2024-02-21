import random as r

player_choice = input("Rock, paper or scissors: ").lower()


def get_ai_choice():
    int = r.randrange(1, 4)
    match int:
        case 1:
            return "rock"
        case 2:
            return "paper"
        case 3:
            return "scissor"


match player_choice:
    case "rock":
        match get_ai_choice():
            case "rock":
                print("Draw")
            case "scissor":
                print("Player wins")
            case "paper":
                print("AI wins")
    case "paper":
        match get_ai_choice():
            case "rock":
                print("Player wins")
            case "scissor":
                print("AI wins")
            case "paper":
                print("Draw")
    case "scissor":
        match get_ai_choice():
            case "rock":
                print("AI wins")
            case "scissor":
                print("Draw")
            case "paper":
                print("Player wins")
