import pytest
from ..main.app import sentiment_analysis

def toArray(string):
    sentence = []
    sentence.append(string)
    return sentence

def test_sentiment_positive():
    assert "positive" == sentiment_analysis(toArray("I love donuts"))

def test_sentiment_negative():
    assert "negative" == sentiment_analysis(toArray("I hate donuts"))

def test_sentiment_neutral():
    assert "neutral" == sentiment_analysis(toArray("This article is ok"))