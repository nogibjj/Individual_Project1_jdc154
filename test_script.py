from script import main


def test_main():
    done = main()
    assert done == 1


if __name__ == "__main__":
    test_main()
