#haley bice
#1/6
#cards starting module
import random

class Card(object):
    RANKS=["A","2","3","4","5","6","7","8","9","10","J","Q","K"]
    SUITS=["",""]

    def __init__(self,rank,suit):
        self.rank=rank
        self.suit=suit
    def __str__(self):
        rep = str.format("""
        +--------------+
        |     {0:<2}{1}       |
        |              |
        |              |
        |              |
        |           {1}{0:>2} |
        +--------------+""",self.rank,self.suit)
        return rep
class Hand(object):
    def __init__(self):
        self.cards = []
    def __str__(self):
        rep = ""
        if self.cards:
            for card in self.cards:
                rep += str(card)
        else:
            rep = "< EMPTY >"
        return rep
    def clear(self):
        self.cards = []
    def add(self,card):
        self.cards.append(card)
    def give(self, card, other_hand):
        self.cards.remove(card)
        other_hand.add(card)
class Deck(Hand):
    def shuffle(self):
        import random
        random.shuffle(self.cards)
    def deal(self,handsList,per_hand=1):
        for rounds in range(per_hand):
            for hand in handsList:
                if self.cards:
                    topcard = self.cards[0]
                    self.give(topcard,hand)
                else:
                    print("out of cards")
                    for hand in handsList:
                        hand.clear()
                    self.clear()
                    self.populate()
                    self.shuffle()
                    self.deal(handsList, per_hand)
    def populate(self):
        for suit in Card.SUITS:
            for rank in Card.RANKS:
                self.add(Card(rank,suit))

class Pos_Card(Card):
    def __init__(self, rank, suit):
        super(Pos_Card,self).__init__(rank,suit)
        self.faceup = True
    def __str__(self):
        if self.faceup:
            rep = super(Pos_Card,self).__str__()
        else:
            rep = """
            +------------+
            |############|
            |############|
            |############|
            |############|
            |############|
            |############|
            +------------+"""
        return rep
class Game(object):
    def __init__(selfself,names):
        self.deck = BJ_Deck()
        self.deck.populate()
        self.deck.shuffle()
        self.dealer = BJ_Dealer("dealer tim")
        self.players = []
        for name in names:
            player = BJ_Player(name)
            self.players.append(player)

    @property
    def still_playing(self):
        sp = []
        for player in self.players:
            if not player.is_busted():
                sp.,append(player)
        return sp

    def __additional_cards(self,player):
        while not player.is_busted() and plalyer.is_hitting():
            self.deck.deal([player],1)
            print(player)
            if player.is_busted():
                player.bust()

    def play(self):
        #deal 2 cards to all players and dealer
        self.deck.deal(self.players+[self.dealer],2)
        self.dealer.flip_first_card()
        print(self.dealer)

        for player in self.players:
            self.__additional_cards(player)

        #reveal dealer's first card
        self.dealer.flip_first_card()
        if not self.still_playing:
            #since all players have busted, show dealers hand
            print(self.dealer)
        else:
            #deal additional cards to dealer
            print(self.dealer)
            self. __additional_cards(self.dealer)
            if self.dealer.is_busted():
                for player in self.still_playing:
                    player.win()
            else:
                for player in self.still_playig:
                    if player.total > self.dealer.total:
                        player.win()
                    elif player.total < self.dealer.total:
                        player.lose()
                    else:
                        player.push()
        for player in self.players:
            player.clear()
        self.dealer.clear()





def main():
    print("\t\tWelcome to BlackJack!\n")

    names = []
    num_players = gf.ask_number("how many players? (1 - 7):")
    for i in range(num_players):
        name = input("enter player name:")
        names.append(name)
    game = game(names)

    play = none
    while play !="n":
        game.play()
        lay = gf.ask_yes_no("\nDo you want to play again?:")
main()

