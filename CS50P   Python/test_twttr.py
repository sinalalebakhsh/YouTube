from twttr import shorten


def test_shorten():
    """Shorten should remove all vowels in a string."""
    assert shorten("aeiou") == ""
    assert shorten("AEIOU") == ""
    assert shorten("Shorten") == "Shrtn"
    assert shorten("The rain in spain.") == "Th rn n spn."
    assert shorten("1a2b3c4f5e") == "12b3c4f5"
# from twttr import vowels

# def test_siinaa_to_sn():
#     assert vowels('siinaa') == 'sn'
