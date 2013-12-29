from card_deck import CardDeck
from card import Card
from go_to_space_card import GoToSpaceCard
from money_card import MoneyCard

class CommunityChestCardDeck(CardDeck):

    cards = [
        MoneyCard("Life insurance matures. Collect $100",100),
        MoneyCard("Income Tax Refund. Collect $20.",20),
        MoneyCard("Bank Error in your Favor. Collect $200.",200),
        MoneyCard("You have won second prize in a beauty contest. Collect $10",10),
        Card("Go to Jail. Go directly to Jail. Do not pass Go. Do not collect $200."),
        Card("It is your birthday. Collect $10 from every player"),
        MoneyCard("Doctor's Fees. Pay $50",-50),
        MoneyCard("Pay hospital fees of $100",-100),
        Card("You are assessed for street repairs. $40 per house, $115 per hotel"),
        MoneyCard("Receive $25 consulting fee",25),
        Card("Get out of Jail free. This card may be kept until needed or traded."),
        MoneyCard("You inherit $100.",100),
        GoToSpaceCard("Advance to Go. Collect $200","Go"),
        MoneyCard("From sale of stock you get $50",50),
        MoneyCard("Holiday fund matures. Receive $100",100),
        MoneyCard("Pay school fees of $50",-50)
    ]
