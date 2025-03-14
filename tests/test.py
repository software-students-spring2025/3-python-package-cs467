import pytest
from DemoPackage.furtune_cookie import dev_fortune_cookie
from DemoPackage.generate_emoji import dev_generate_emoji


def test_dev_fortune_cookie_valid_category():
    """Test that valid categories return a correctly formatted string."""
    for category in ["general", "bug", "debug", "success"]:
        result = dev_fortune_cookie(category)
        assert isinstance(result, str)  # return type must be string type
        assert "🔮 Developer Fortune:" in result  # have prefix
        assert len(result.strip()) > 20  # effective return result

def test_dev_fortune_cookie_invalid_category():
    """Test that an invalid category defaults to 'general'."""
    result = dev_fortune_cookie("invalid_category")
    assert isinstance(result, str)
    assert "🔮 Developer Fortune:" in result
    assert len(result.strip()) > 20

def test_dev_fortune_cookie_empty_string():
    """Test that an empty string defaults to 'general'."""
    result = dev_fortune_cookie("")
    assert isinstance(result, str)
    assert "🔮 Developer Fortune:" in result
    assert len(result.strip()) > 20

def test_dev_fortune_cookie_none_input():
    """Test that passing None defaults to 'general'."""
    result = dev_fortune_cookie(None)  # None
    assert isinstance(result, str)
    assert "🔮 Developer Fortune:" in result
    assert len(result.strip()) > 20

def test_generate_emoji_valid():
    valid_emojis = ["😂", "🤣", "😆", "😁"]
    result = generate_emoji("laugh")
    assert result in valid_emojis, f"Expected one of {valid_emojis}, got {result}"

def test_generate_emoji_invalid():
    result = generate_emoji("unknown")
    assert result == "🤔", f"Expected default emoji '🤔', got {result}"

def test_generate_emoji_case_insensitive():
    valid_emojis = ["😂", "🤣", "😆", "😁"]
    result = generate_emoji("LAUGH")
    assert result in valid_emojis, f"Expected one of {valid_emojis} for case-insensitive input, got {result}"

def test_generate_emoji_output_type():
    result = generate_emoji("cry")
    assert isinstance(result, str), f"Expected output type str, got {type(result)}"