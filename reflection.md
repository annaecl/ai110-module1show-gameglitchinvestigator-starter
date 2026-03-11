# 💭 Reflection: Game Glitch Investigator

Answer each question in 3 to 5 sentences. Be specific and honest about what actually happened while you worked. This is about your process, not trying to sound perfect.

## 1. What was broken when you started?

- What did the game look like the first time you ran it?
- List at least two concrete bugs you noticed at the start  
  (for example: "the hints were backwards").

--- 
### Bugs 
- Firstly, when I guessed a number, it said "GO LOWER," except the number I picked was one! Since the number was supposed to be between 1 and 100, this seemed incorrect. Furthermore, during that same game, when I guessed 90, it suddenly said to "GO HIGHER." If the game says go lower for 1, then it should also say go lower for 90! It should not flip-flop.
- Secondly, when I tried to start a new game (by pressing the "New Game" button) after having turned off the "Show hint" feature, I wasn't able to submit any new guesses --- the game simply froze. I also could not turn back on the hint feature after turning it off.
- Also, when I switch the difficulty of the game, there is an incongruency between what the main screen says and what the side bar says: for hard mode, the main screen says that you can guess numbers between 1 and 100, while the sidebar claims that the number could actually be between 1 and 50. These should be consistent. 
---

## 2. How did you use AI as a teammate?

- Which AI tools did you use on this project (for example: ChatGPT, Gemini, Copilot)?
  - Claude and Copilot 
- Give one example of an AI suggestion that was correct (including what the AI suggested and how you verified the result).
  - I was confused about the following logic, as it seemed very arbitrary: 
  ```
    if outcome == "Too High":
        if attempt_number % 2 == 0:
            return current_score + 5
        return current_score - 5

    if outcome == "Too Low":
        return current_score - 5
  ```
  - So I consulted Claude to confirm whether or not there seemed to be any reason that the parity of the attempt number should influence the player's score. Claude agreed with my assessment, which I verified with a more thorough dissection of the code. 
- Give one example of an AI suggestion that was incorrect or misleading (including what the AI suggested and how you verified the result).

---

## 3. Debugging and testing your fixes

- How did you decide whether a bug was really fixed?
- Describe at least one test you ran (manual or using pytest)  
  and what it showed you about your code.
- Did AI help you design or understand any tests? How?

---

## 4. What did you learn about Streamlit and state?

- How would you explain Streamlit "reruns" and session state to a friend who has never used Streamlit?

---

## 5. Looking ahead: your developer habits

- What is one habit or strategy from this project that you want to reuse in future labs or projects?
  - This could be a testing habit, a prompting strategy, or a way you used Git.
- What is one thing you would do differently next time you work with AI on a coding task?
- In one or two sentences, describe how this project changed the way you think about AI generated code.
