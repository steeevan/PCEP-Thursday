### **Instruction Document for Rock-Paper-Scissors Game**

---

### **Rock-Paper-Scissors Game: Project Instructions**

---

### **Objective:**
Your goal is to create a Python command-line game where the user plays Rock-Paper-Scissors against the computer. The program should:
- Allow the user to input their choice.
- Randomly generate the computer’s choice.
- Compare the choices and determine the winner.
- Display results for each round and keep track of scores.

---

### **Steps to Complete the Project**

---

### **Step 1: Setup Your Environment**
1. Open your Python editor (IDLE, VS Code, PyCharm, etc.).
2. Create a new Python file named `rock_paper_scissors.py`.

---

### **Step 2: Plan the Game Logic**
Think about the structure of the game:
1. The user will choose one of three options: "Rock," "Paper," or "Scissors."
2. The computer will randomly select one of these options.
3. The game will compare the user’s choice and the computer’s choice to determine the winner:
   - Rock beats Scissors.
   - Scissors beats Paper.
   - Paper beats Rock.
   - If both choose the same option, it’s a tie.
4. Scores will be updated based on the winner.

---

### **Step 3: Define the Game Options**
- Use a **list** to store the three valid game options: "Rock," "Paper," and "Scissors."
- Think about how you’ll ensure the user selects a valid option. What happens if they type something invalid?

---

### **Step 4: Create Variables for Scores**
- Use variables to keep track of:
  1. The user’s score.
  2. The computer’s score.
- Decide how these scores will be updated after each round.

---

### **Step 5: Write Functions for Each Step**
Break the game into manageable pieces by writing separate functions. These are the main steps:

1. **User Input:**
   - Write a function to ask the user for their choice.
   - Ensure the input is valid. If it’s not valid, prompt the user to try again.

2. **Computer’s Choice:**
   - Write a function that randomly selects one option for the computer from the list of choices.

3. **Determine Winner:**
   - Write a function that compares the user’s choice and the computer’s choice.
   - This function should return whether the user wins, the computer wins, or if it’s a tie.

4. **Display Results:**
   - Write a function that shows:
     - The user’s choice.
     - The computer’s choice.
     - Who won the round.
   - It should also show the updated scores.

---

### **Step 6: Create the Main Game Loop**
- Write a loop to play the game repeatedly until the user decides to quit.
- Steps in the loop:
  1. Call the function to get the user’s choice.
  2. Call the function to generate the computer’s choice.
  3. Use the function to determine the winner.
  4. Update the scores based on the winner.
  5. Display the results for the round.
  6. Ask the user if they want to play again. End the loop if the user says “no.”

---

### **Step 7: Test the Game**
- Run your program and test each step:
  1. Can the user input their choice, and is it validated correctly?
  2. Does the computer generate a valid choice?
  3. Does the game correctly determine the winner?
  4. Are the results displayed properly, including the scores?
  5. Does the program exit cleanly when the user chooses to quit?

---

### **Step 8: Add Extra Features (Optional)**
Once your basic game works, try adding these features:
1. **Best-of-X Rounds:** Let the user play a set number of rounds (e.g., best of 3).
2. **Leaderboard:** Keep a record of scores across multiple games.
3. **Custom Names:** Allow the user to set their name at the start of the game.
4. **Additional Options:** Extend the game by adding more choices, such as "Lizard" and "Spock."
5. **Random Messages:** Add fun messages when the user wins or loses a round.

---

### **Tips for Success**
- Test your program after completing each step to ensure everything works correctly.
- Keep your code organized by using comments to explain what each part does.
- Use descriptive names for your variables and functions so your code is easy to understand.

---
