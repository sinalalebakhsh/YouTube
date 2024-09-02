from seasons import check_birthday


def main():
    test_check_birthday()


def test_check_birthday():
    assert check_birthday('1993-01-21') == ('1993', '01', '21')
    assert check_birthday('1993-1-21') == None
    assert check_birthday('February 21, 1993') == None

if __name__ == "__main__":
    main()
