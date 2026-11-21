# Kenny Chambers
# CIS256 FALL 2026
# Programming Assignment 4

import guess_the_word

def run(monkeypatch, capsys, word, guesses):
    it = iter(guesses)
    monkeypatch.setattr(guess_the_word.random, "choice", lambda _words: word)
    monkeypatch.setattr("builtins.input", lambda _prompts="": next(it))
    guess_the_word.play_game()
    return capsys.readouterr().out

