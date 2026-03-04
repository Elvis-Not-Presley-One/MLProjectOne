# D1

**X1** represents whether x_player occupies the center square of the board, while **X2** represents whether o_player occupies the center square. Both features have values of 0 or 1, where 0 means the player does not occupy the center and 1 means the player does. The intuition behind this is that the center square is the most valuable position on the board since it is part of 4 of the 8 possible winning lines, more than any other square.

**X3** represents the number of corner squares occupied by x_player, while **X4** represents the number of corner squares occupied by o_player. The intuition here is that corners are the next most valuable positions after the center since each corner is part of 3 of the 8 possible winning lines. Tracking how many corners each player holds gives insight into their overall board control.

**X5** represents the number of lines containing two X pieces and one empty square. The intuition is that these are immediate winning opportunities for the learner, since placing a piece in the empty square would complete three in a row.

**X6** represents the number of lines containing two O pieces and one empty square. The intuition is that these represent immediate threats from the opponent. The learner needs to recognize and block these to avoid losing.

**X7** represents the number of lines containing one X piece and two empty squares. The intuition is that these lines represent developing opportunities for the learner. Building toward two in a row sets up future winning chances.

**X8** represents the number of lines containing one O piece and two empty squares. The intuition is that these represent early-stage threats from the opponent. While not as urgent as X6, they show where the opponent could build toward a win if left unchecked.

The weights for the fixed evaluation function were chosen by hand based on strategic reasoning about tic tac toe. Features that are more important to winning were given higher magnitude weights. For example, X5 (two X's in a line) was given a high positive weight since it represents a near-win, and X6 (two O's in a line) was given a strong negative weight since failing to block a threat leads to a loss. Center and corner features were given moderate weights reflecting their positional value. The weights were then adjusted slightly through trial and error to produce an opponent that plays reasonably but not perfectly, giving the learner room to improve during training.

---

# D4

**What was easy about this assignment?**

The game logic was pretty simple to implement since tic tac toe is only a 3x3 grid. Checking for wins and draws was straightforward. The overall concept made sense because we had already gone over it in class with the checkers example, so translating that to tic tac toe wasn't too bad.

**What was challenging about this assignment, or parts that you couldn't get working correctly?**

Getting the learner to actually improve was tough. We spent a lot of time debugging the weight updates and tuning the learning rate. Designing the opponent's fixed evaluation function was also tricky because we had to balance it so the learner had something meaningful to learn against. When something wasn't working it was hard to pinpoint whether the problem was in the features, the weights, or the training loop.

**What did you like about this assignment?**

It was cool to watch the win percentage go up over time in the plots. Building everything from scratch instead of using a library made the concepts from class click a lot more. It felt like we actually understood what was going on under the hood.

**What did you dislike about this assignment?**

Debugging was frustrating because a small mistake in one part could quietly break the whole learning process without throwing an error. There were a lot of pieces that all had to work together correctly.

**How did your team function?**

Our team functioned well. We created a group chat to coordinate a time to meet. Mina wrote out a high-level outline of the project and questions to be answered. They also brainstormed the board features and opponent evaluation function. Colin created the project roadmap and architecture for the team to follow. Elvis, Mimi, and Joey Joey all created their own implementation of the project themselves so they can learn the concepts in their own way. We stayed in contact through the group chat and met up a few times to go over code and test everything together.

**What did you learn from this assignment?**

We learned how a system can learn a strategy just through repeated play without being told how to play. We also saw firsthand how much feature selection matters and how the LMS update rule works in practice. Working as a team on a coding project was a good experience too.
