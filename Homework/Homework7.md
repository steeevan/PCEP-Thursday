### **Homework Assignment: Enhance Your Rock-Paper-Scissors Game**

---

### **Objective:**
Building upon your current Rock-Paper-Scissors game, you will extend its functionality by adding new features. This homework is designed to improve your understanding of Python concepts and encourage creativity.

---

### **Homework Tasks**

---

#### **1. Add a "Best-of-X Rounds" Feature**
- Modify your game so that the user and the computer play a fixed number of rounds, such as Best of 3 or Best of 5.
- At the end of all the rounds, display the overall winner based on who won the most rounds.
- Allow the user to choose the number of rounds before starting the game.

---

#### **2. Include a Dynamic Leaderboard**
- Track the user’s total wins and display a leaderboard at the end of the game.
- Save the leaderboard data (e.g., name and total wins) to a file so it persists across multiple plays.
- When the game starts, load the leaderboard and display the current rankings.

---

#### **3. Add a Help Menu**
- Create a help menu that explains:
  - The rules of the game (e.g., "Rock beats Scissors, Paper beats Rock").
  - The scoring system.
  - Any new features you’ve added.
- Make the help menu accessible by entering a special command, such as "Help."

---

#### **4. Expand the Game with New Choices**
- Add two new choices to the game: "Lizard" and "Spock."
- Update the logic to include the new rules:
  - Rock crushes Scissors.
  - Scissors cuts Paper.
  - Paper covers Rock.
  - Rock crushes Lizard.
  - Lizard poisons Spock.
  - Spock smashes Scissors.
  - Scissors decapitates Lizard.
  - Lizard eats Paper.
  - Paper disproves Spock.
  - Spock vaporizes Rock.
- Ensure the game still works correctly with the expanded choices.

---

#### **5. Randomized Messages**
- Add fun, randomized messages that display when the user or computer wins a round.
- Create separate lists of messages for:
  - Winning a round.
  - Losing a round.
  - A tie.
- Display a random message from the corresponding list after each round.

---

---

#### **7. Add Detailed Round Summaries**
- After each round, display:
  - The user's choice.
  - The computer's choice.
  - The result of the round (win, lose, or tie).
  - The updated score.

---

#### **8. Implement Error Logging**
- Add a feature to log errors to a list

---

#### **9. Allow Computer to Use Strategies**
- Implement different strategies for the computer:
  - **Random Mode**: The computer makes random choices.
  - **Predictive Mode**: The computer tries to counter the user’s most common choice.
- Let the user know which strategy the computer used after the game ends.

---

#### **10. Add a Replay Summary**
- When the game ends, show a summary of all rounds, including:
  - What the user and computer chose in each round.
  - Who won each round.
  - The overall winner.

---

### **Instructions:**
1. Carefully read each task and decide which features you will implement.
2. Begin with simpler tasks, like adding messages or a help menu, before moving on to more complex features, such as saving and loading files.
3. Test your game after each new feature to ensure it still works as expected.
4. Use comments in your code to explain what each new feature does.
5. Use descriptive variable names to keep your code organized and readable.

---

### **Submission Requirements:**
- Submit your updated game file as `rock_paper_scissors_enhanced.py`.
- Include comments at the top of your file listing:
  - Your name.
  - A brief description of the features you added.
  - Any challenges you faced while working on the assignment.
- Ensure your code is properly formatted and tested before submission.

---

### **Optional Challenges:**
If you finish early, try implementing these additional challenges:
1. **Graphical Output**: Use a library like `turtle` or `pygame` to create a simple graphical version of the game.
2. **Track Win Streaks**: Add functionality to track and display the user’s longest win streak.
3. **Custom Themes**: Allow users to change the names of the choices (e.g., "Dragon," "Knight," "Castle").

---

### **Due Date:**
- Submit your homework by **[11/21/2024]**.

---

