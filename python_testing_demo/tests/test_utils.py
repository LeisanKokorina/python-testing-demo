import pytest
from app.utils import is_strong_password, mean, fibonacci

@pytest.mark.parametrize(
    "text, expected",
    [
        ("Hello World!", "hello-world"),
        ("  multiple   spaces  ", "multiple-spaces"),
        ("Ünicode & Symbols", "ünicode-symbols"),  # lowercasing kept; non-ascii not stripped
        ("foo_bar+baz", "foo-bar-baz"),
        ("--edge--", "edge"),
    ],
)

@pytest.mark.parametrize(
    "password, ok",
    [
        ("Abcdef1!", True),
        ("short1!", False),              # too short
        ("alllowercase1!", False),       # no uppercase
        ("ALLUPPERCASE1!", False),       # no lowercase
        ("NoNumber!", False),            # no digit
        ("NoSpecial1", False),           # no special
    ],
)
def test_is_strong_password(password, ok):
    assert is_strong_password(password) is ok

def test_mean_happy_path():
    assert mean([2, 4, 6]) == 4

def test_mean_raises_on_empty():
    with pytest.raises(ValueError):
        mean([])

@pytest.mark.parametrize("n, expected", [(0,0), (1,1), (2,1), (5,5), (8,21)])
def test_fibonacci(n, expected):
    assert fibonacci(n) == expected

@pytest.mark.parametrize("bad", [-1, 1.5, "x"])
def test_fibonacci_bad_inputs(bad):
    with pytest.raises((TypeError, ValueError)):
        # some inputs raise TypeError, some ValueError
        fibonacci(bad)  # type: ignore[arg-type]
