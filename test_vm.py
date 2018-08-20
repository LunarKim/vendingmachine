from vm import VendingMachine

def test_initial_change_should_be_zero():
    m = VendingMachine()
    assert "잔액은 0원입니다" == m.run("잔액")

def test_check_coin():
    m = VendingMachine()
    assert "100원을 넣었습니다" == m.run("동전 100")

def test_accumulation_of_change():
    m = VendingMachine()
    m.run("동전 100")
    m.run("동전 100")
    assert "잔액은 200원입니다" == m.run("잔액")

def test_unknown_message():
    m = VendingMachine()
    assert "알 수 없는 명령입니다." == m.run("치즈케이크")

def get_coffee():
    m = VendingMachine()
    m.run("동전 200")
    assert "잔액은 50원입니다" == m.run("잔액")
    assert "커피가 나왔습니다." == m.run("음료 커피")
