# Game Glitch Investigator — Change Log

## Fix: `new_game` handler fully resets game state

**File:** `app.py`, lines 136–148

### What was wrong

The original `new_game` button handler only reset two variables:

```python
if new_game:
    st.session_state.attempts = 0
    st.session_state.secret = random.randint(1, 100)
    st.success("New game started.")
    st.rerun()
```

This left several issues:

| Problem | Effect |
|---|---|
| `score` was not reset | Score carried over from the previous game, making it meaningless |
| `status` was not reset | If the previous game ended in a win or loss, `status` stayed `"won"` or `"lost"`, immediately blocking the new game on the next rerun |
| `history` was not reset | Old guesses from the previous game remained visible in the debug panel |
| Secret used hardcoded `1, 100` range | Ignored the selected difficulty — Easy and Hard ranges were never used when starting a new game |

### What was changed

```python
if new_game:
    # Reset attempt counter so the player starts fresh
    st.session_state.attempts = 0
    # Generate a new secret using the current difficulty's range (not hardcoded 1–100)
    st.session_state.secret = random.randint(low, high)
    # Reset score so it doesn't carry over from the previous game
    st.session_state.score = 0
    # Reset status to "playing" so the game loop is active again
    st.session_state.status = "playing"
    # Clear guess history from the previous game
    st.session_state.history = []
    st.success("New game started.")
    # Rerun the app to reflect the fresh state immediately
    st.rerun()
```

### Summary of variables reset

| Variable | Before fix | After fix |
|---|---|---|
| `attempts` | Reset to `0` | Reset to `0` |
| `secret` | Re-randomized, but always `1–100` | Re-randomized within difficulty range (`low`–`high`) |
| `score` | **Not reset** | Reset to `0` |
| `status` | **Not reset** | Reset to `"playing"` |
| `history` | **Not reset** | Reset to `[]` |

---

## Fix: `update_score` applies consistent −5 penalty for incorrect guesses

**File:** `app.py`, lines 49–66

### What was wrong

The original scoring logic had separate branches for `"Too High"` and `"Too Low"` with inconsistent behavior:

- `"Too Low"` always deducted 5 points (correct intent).
- `"Too High"` used `attempt_number % 2 == 0` to decide the penalty:
  - On even-numbered attempts: **added** 5 points (a reward for a wrong guess).
  - On odd-numbered attempts: deducted 5 points.

This meant a player could gain points by guessing too high on the right attempt, which was unintended and noted in the original code as arbitrary.

### What was changed

Both `"Too High"` and `"Too Low"` now unconditionally deduct 5 points:

```python
# Any incorrect guess (too high or too low) costs 5 points equally.
if outcome == "Too High" or outcome == "Too Low":
    return current_score - 5
```

### Summary

| Outcome | Before fix | After fix |
|---|---|---|
| `"Too Low"` | −5 points | −5 points |
| `"Too High"` (even attempt) | **+5 points** | −5 points |
| `"Too High"` (odd attempt) | −5 points | −5 points |
