from jar import Jar


def test_init():
    jar = Jar(100)
    assert isinstance(jar, Jar)
    try:
        jar1 = Jar(-2)
    except ValueError:
        pass


def test_str():
    jar = Jar()
    assert str(jar) == ""
    jar.deposit(1)
    assert str(jar) == "🍪"
    jar.deposit(11)
    assert str(jar) == "🍪🍪🍪🍪🍪🍪🍪🍪🍪🍪🍪🍪"


def test_deposit():
    jar = Jar()
    try:
        jar.deposit(13)
    except ValueError:
        pass
    jar1 = Jar()
    jar1.deposit(2)
    assert jar1.size == 2


def test_withdraw():
    jar = Jar()
    jar.deposit(2)
    try:
        jar.withdraw(3)
    except ValueError:
        pass
    jar1 = Jar()
    jar1.deposit(2)
    jar1.withdraw(2)
    assert jar1.size == 0
