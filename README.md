 # PokerAI
PokerAI is part of a school project.
The aim is to create an artificial intelligence, wich should be able to beat bots playing based on statistics at the game of Texas Hold’em Poker.

# Documentation

## The Idea
We both like playing Poker and we are both interested in AI. So one evening when we were playing Poker, we talked about school and that we need a project idea. Soon we came up with the idea of an AI playing Poker.

## V. 0.1 The Game of Poker
The first step towards our goal is to create an enviroment where we can simulate Poker games. This enviroment should be able to use different Player models such as a random Player as well as our AI.

The first Version of this implemented on Jan 18,2024 with commit 34856b560c3025587b6dbc4992bdae6f23ba3a5d

## V. 0.2 Hand Detection
We dedicated the next three days to determining Poker hands, like pairs, straights, or flushes. But there was a piece of code we found handeling this: https://dev.to/mattryanmtl/identify-a-hand-in-poker-with-python-4b93.

This exeact code was implemented with commit ce494331c19ffbe8f112c11767ce04a3c8e67973. 

However this code was made for a set of 5 cards, not for the needed 7. 

So overwrote some of it and got it to work in commit 560dc25987bd9035701d4f189a9014697902f4de

One still missing feature with hand detection is to distiguish between a good and a bad set of equal value. 
This is adressed is issue #5

## V. 0.3 The AI
We collected training data https://allenfrostline.com/blog/texas-holdem-series-2/. With this we were able to create the first version of the AI, wich is right about 35% of the time. 

This is implemented in commit 9190ebbc64736b03060dd749dfc72a74152baca0.

That is better than guessing, but not that much better, so there is a lot to improve. This version evealuates flop situations, by lookng at cards only. This will be changed in future versions.

