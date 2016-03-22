# A-Word-Game-Python-

========> A Word Game <========

This game is similar to Scrabble or Words with Friends. The player can choose to play by himself/herself or let the computer play.

== Objective ==

The player receives a hand of random letters, then tries to create the longest valid word by using those letters to get the maximum score. A score is base on the length of the word and the letters in that word.

== Scoring ==

* The score is the sum of the scores for each word formed, multiplied by the length of the word. It will plus 50 points bonus if all letters are used on the first word created.

'a' is worth  1, 'b' is worth  3, 'c' is worth  3, 'd' is worth  2, 'e' is worth  1, 'f' is worth  4, 'g' is worth  2, 
'h' is worth  4, 'i' is worth  1, 'j' is worth  8, 'k' is worth  5, 'l' is worth  1, 'm' is worth  3, 'n' is worth  1, 
'o' is worth  1, 'p' is worth  3, 'q' is worth  10, 'r' is worth  1, 's' is worth  1, 't' is worth  1, 'u' is worth  1, 
'v' is worth  4, 'w' is worth  4, 'x' is worth  8, 'y' is worth  4, 'z' is worth  10

* Some letters may remain unused and they won't be scored.

* For example, the player receives “c h n i u i c z” on a hand, then create ’zucchini’ on the first try. It would be worth 242 points. ==> ((10+1+3+3+4+1+1+1)*8)+50
