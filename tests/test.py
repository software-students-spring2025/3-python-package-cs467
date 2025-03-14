import pytest
from DemoPackage.furtune_cookie import dev_fortune_cookie
from DemoPackage.generate_emoji import generate_emoji
from DemoPackage.owl_banner import gl_banner

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
