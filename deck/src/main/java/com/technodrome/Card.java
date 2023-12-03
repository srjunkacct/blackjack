package com.technodrome;

public class Card {

private final Rank rank;
private final Suit suit;

public Card( Rank rank, Suit suit)
{
    this.rank = rank;
    this.suit = suit;
}

public Rank getRank( ) { return rank;}
    public Suit getSuit() { return suit;}

    public static enum Rank {
        TWO,
        THREE,
        FOUR,
        FIVE,
        SIX,
        SEVEN,
        EIGHT,
        NINE,
        TEN,
        JACK,
        QUEEN,
        KING,
         ACE
    }

    public static enum Suit {
        CLUBS,
        DIAMONDS,
        HEARTS,
        SPADES
    }
}
