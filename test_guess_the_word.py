# Kenny Chambers
# CIS256 FALL 2026
# Programming Assignment 4

import pytest
import guess_the_word

# Plays game with the fixed word and scripted guesses while returning printed output.
def run(monkeypatch, capsys, word, guesses):
    it = iter(guesses)
    monkeypatch.setattr(guess_the_word.random, "choice", lambda _words: word)
    monkeypatch.setattr("builtins.input", lambda _prompts="": next(it))
    guess_the_word.play_game()
    return capsys.readouterr().out

# Selected word from the predefined list test.
def test_word_from_list(monkeypatch):
    received = []
    monkeypatch.setattr(guess_the_word.random, "choice", lambda seq: received.append(seq) or seq[0])
    letters = iter("abcdefghijklmnopqrstuvwxyz")
    monkeypatch.setattr("builtins.input", lambda _prompt="": next(letters))
    guess_the_word.play_game()
    assert received == [guess_the_word.WORDS]

# Incorrect guess being flagged and counted test.
def test_incorrect_guess(monkeypatch, capsys):
    out = run(monkeypatch, capsys, "retro", ["z", "t", "r", "o", "e"])
    assert "INCORRECT!" in out
    assert "Wrong guesses: 1/7" in out