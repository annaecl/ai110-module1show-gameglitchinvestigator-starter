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
  - The AI did make a small error in that is suggested to make a new CHANGES.md file (even though it had already made one in the previous session). This mistake was easy to correct/prevent, but still rather unexpected. 

---

## 3. Debugging and testing your fixes

- How did you decide whether a bug was really fixed?
  - Although the pytests helped confirm that some of the errors had been fixed (for example, that the guess vs. secret comparisons were being performed properly), I confirmed the fix by playing the game myself and monitoring the Developer Debug Info 
- Describe at least one test you ran (manual or using pytest)  
  and what it showed you about your code.
  - One test I ran involved making a couple guesses, and then trying to turn on and off the "Show Hint" feature. This test revealed very quickly that show hint checkbox did not always immediately trigger a response from the backend system, even though the UI changed. 
- Did AI help you design or understand any tests? How?
  - AI helped me build several tests targeted at my fixes, such as correcting for incorrect comparaisons and for updating scores. I also had it explain some of its tests and write accompanying comments, because I had a little trouble understanding the logic behind a couple of them without any explanation. I was very specific with what I asked the AI to test, having it construct tests based on the particular problem I wanted to target. 

---

## 4. What did you learn about Streamlit and state?

- How would you explain Streamlit "reruns" and session state to a friend who has never used Streamlit?
  - Honestly, I still don't feel like I learned much about Streamlit from this activity, as it was not the focus. However, when I asked Claude for an explanation, this is what it replied: 

> Imagine every time you click a button or type something on a webpage, the entire Python script runs again from top to bottom — like pressing "play" on a movie from the beginning. That's what Streamlit does. Every user interaction triggers a full rerun of your script. This is different from most web frameworks where only small pieces update. In Streamlit, the whole file re-executes, which keeps the code simple (no callbacks or event listeners), but it means variables reset to their initial values on every run. Because everything resets on each rerun, you need a way to "remember" things — like a score, a guess, or whether a game is in progress. That's what st.session_state is for. Think of it like a sticky notepad attached to the user's browser tab. Even though the script reruns, anything you write to st.session_state sticks around between reruns for that user's session. 

---

## 5. Looking ahead: your developer habits

- What is one habit or strategy from this project that you want to reuse in future labs or projects?
  - I want to reuse leveraging AI to write tests as I fix bugs.  
- What is one thing you would do differently next time you work with AI on a coding task?
  - I think I would try to be more diligent with documentation from the beginning. I completed this activity over multiple days, and it was hard to remember everything I had fixed previously and what was still broken without having to test everything all over again. 
- In one or two sentences, describe how this project changed the way you think about AI generated code.
  - It is teaching me to be cautious about implementing AI-generated code blindly, especially when it comes to writing effective tests. 
