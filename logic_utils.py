def get_range_for_difficulty(difficulty: str):
    """Return (low, high) inclusive range for a given difficulty."""
    if difficulty == "Easy":
        return 1, 20
    if difficulty == "Normal":
        return 1, 100
    if difficulty == "Hard":
        return 1, 50
    return 1, 100 #this should be eliminated and an exception should be raided


def parse_guess(raw: str):
    """
    Parse user input into an int guess.

    Returns: (ok: bool, guess_int: int | None, error_message: str | None)
    """
    if raw is None:
        return False, None, "Enter a guess."

    if raw == "":
        return False, None, "Enter a guess."

    try:
        if "." in raw:
            value = int(float(raw)) #this could be risky -- raw may not be a float
        else:
            value = int(raw)
    except Exception:
        return False, None, "That is not a number." #this should account for it, but I should check

    return True, value, None #default case


#FIX: Fixed guess vs. secret comparison — corrected direction of "Too High"/"Too Low" messages and added type-safe fallback for string/int mismatches
def check_guess(guess, secret):
    """
    Compare guess to secret and return (outcome, message).

    outcome examples: "Win", "Too High", "Too Low"
    """
    if guess == secret:
        return "Win", "🎉 Correct!"

    try:
        if guess > secret:
            return "Too High", "📉 Go LOWER!"  # guess is above secret, so player should go lower
        else:
            return "Too Low", "📈 Go HIGHER!"  # guess is below secret, so player should go higher
    except TypeError: #assumes that parse_guess has already run...
        g = str(guess)
        if g == secret:
            return "Win", "🎉 Correct!"
        if g > secret:
            return "Too High", "📈 Go HIGHER!"
        return "Too Low", "📉 Go LOWER!"


#FIX: Fixed arbitrary point deductions — "Too High" no longer adds points on even-numbered attempts; both wrong outcomes now consistently subtract 5 points
def update_score(current_score: int, outcome: str, attempt_number: int):
    """Update score based on outcome and attempt number."""
    # Award points for a correct guess; reward fewer attempts with higher points.
    # Points decrease by 10 for each attempt made, with a floor of 10 so the
    # player always gains something for an eventual correct guess.
    if outcome == "Win":
        points = 100 - 10 * (attempt_number + 1)
        if points < 10:
            points = 10
        return current_score + points

    # Any incorrect guess (too high or too low) costs 5 points equally.
    # Previously, "Too High" had inconsistent logic that sometimes added points
    # on even-numbered attempts — that bug has been fixed here.
    if outcome == "Too High" or outcome == "Too Low":
        return current_score - 5

    # Unknown outcome — score is unchanged
    return current_score
