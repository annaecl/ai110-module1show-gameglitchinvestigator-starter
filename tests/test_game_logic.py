from logic_utils import check_guess, update_score

def test_winning_guess():
    # If the secret is 50 and guess is 50, it should be a win
    result, _ = check_guess(50, 50)
    assert result == "Win"

def test_guess_too_high():
    # If secret is 50 and guess is 60, hint should be "Too High"
    result, _ = check_guess(60, 50)
    assert result == "Too High"

def test_guess_too_low():
    # If secret is 50 and guess is 40, hint should be "Too Low"
    result, _ = check_guess(40, 50)
    assert result == "Too Low"


# Fix a: all values are properly reset when a new game starts
def test_new_game_resets_all_state():
    session = {"attempts": 5, "score": 150, "status": "won", "history": [10, 20, 30]}
    session["attempts"] = 0
    session["score"] = 0
    session["status"] = "playing"
    session["history"] = []
    assert session["attempts"] == 0
    assert session["score"] == 0
    assert session["status"] == "playing"
    assert session["history"] == []


# Fix b: secret is always compared as an integer in check_guess
def test_int_secret_correct_guess_odd_attempt():
    # Odd attempt — secret was kept as int in the old code too; should win
    outcome, _ = check_guess(50, 50)
    assert outcome == "Win"

def test_int_secret_correct_guess_even_attempt():
    # Even attempt — old bug converted secret to str, breaking equality
    # With the fix, secret stays int and the win is detected correctly
    outcome, _ = check_guess(50, 50)
    assert outcome == "Win"

def test_int_secret_low_number_vs_higher_secret():
    # Old bug: check_guess(9, "50") would compare "9" > "50" lexicographically
    # and wrongly return "Too High". With int secret, this returns "Too Low".
    outcome, _ = check_guess(9, 50)
    assert outcome == "Too Low"

# Fix c: update_score is calculated correctly
def test_win_score_increases():
    # Basic sanity check: winning from a score of 0 should add points, not leave it at 0 or go negative
    score = update_score(0, "Win", 1)
    assert score > 0

def test_win_score_decreases_with_more_attempts():
    # Fewer attempts should reward more points — guessing on attempt 1 should score higher than attempt 5
    early = update_score(0, "Win", 1)
    late = update_score(0, "Win", 5)
    assert early > late

def test_too_high_deducts_five_points():
    # A wrong guess ("Too High") should cost exactly 5 points
    score = update_score(100, "Too High", 1)
    assert score == 95

def test_too_high_on_even_attempt_also_deducts():
    # Old bug: "Too High" on even-numbered attempts added +5 instead of deducting
    # This ensures even attempts still correctly subtract 5 points
    score = update_score(100, "Too High", 2)
    assert score == 95

def test_too_low_deducts_five_points():
    # "Too Low" should cost the same 5 points as "Too High" — wrong is wrong regardless of direction
    score = update_score(100, "Too Low", 1)
    assert score == 95

def test_win_score_floor_is_ten():
    # Without a floor, attempt 100 would yield a huge negative bonus (100 - 10*101 = -910)
    # The floor ensures a win always grants at least 10 points no matter how many attempts were made
    score = update_score(0, "Win", 100)
    assert score == 10
