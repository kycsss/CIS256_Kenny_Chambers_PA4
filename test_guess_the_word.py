# Kenny Chambers
# CIS256 FALL 2026
# Programming Assignment 4

import pytest
import guess_the_word

@pytest.fixture
def play(monkeypatch, capsys):
    def _play(word, guesses):
        it = iter(guesses)
        monkeypatch.setattr(guess_the_word.random, "choice", lambda _words: word)
        monkeypatch.setattr("builtins.input", lambda _prompt="": next(it))
        guess_the_word.play_game()
        return capsys.readouterr().out
    return _play