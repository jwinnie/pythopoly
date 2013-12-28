
from card_deck import CardDeck
from card import Card
from go_to_space_card import GoToSpaceCard
from money_card import MoneyCard

class ChanceCardDeck(CardDeck):

    cards = [
        GoToSpaceCard("Advance to Boardwalk","Boardwalk"),
        GoToSpaceCard("Advance to Go. Collect $200","Go"),
        Card("You have been elected chairman of the Board. Pay each player $50"),
        MoneyCard("Speeding Fine: $15",-15),
        Card("Go back 3 spaces"),
        MoneyCard("Bank pays you dividend of $50",50),
        Card("Advance to the nearest railroad. If unowned, you may buy it from the bank. If owned, pay owner twice the rental to which they are otherwise entitled"),
        Card("Go to Jail. Go directly to Jail. Do not pass Go. Do not collect $200."),
        Card("Get out of Jail free. This card may be kept until needed or traded."),
        Card("Advance to the nearest railroad. If unowned, you may buy it from the bank. If owned, pay owner twice the rental to which they are otherwise entitled"),
        Card("Advance to the nearest utility. If unowned, you may buy it from the bank. If owned, throw dice and pay owner a total 10 times amount thrown."),
        GoToSpaceCard("Take a trip to Reading Railroad. If you pass Go, collect $200.","Reading Railroad"),
        MoneyCard("Your building loan matures. Collect $100",100),
        GoToSpaceCard("Advance to Illinois Avenue. If you pass Go, collect $200","Illinois Avenue"),
        GoToSpaceCard("Advance to St. Charles Place. If you pass Go, collect $200","St. Charles Place"),
        Card("Make general repairs to all your property. For each house, pay $25. For each hotel, pay $100.")
            ]
