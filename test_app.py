import app as banking


def setup_function():
    banking.balance = 1000.0


def test_home_page():
    response = banking.app.test_client().get("/")
    assert response.status_code == 200
    assert b"Simple Banking Application" in response.data


def test_health_endpoint():
    response = banking.app.test_client().get("/health")
    assert response.status_code == 200
    assert response.json["status"] == "healthy"


def test_balance_check():
    response = banking.app.test_client().post("/", data={"action": "balance"})
    assert response.status_code == 200
    assert b"Balance checked: 1000.00" in response.data


def test_deposit():
    response = banking.app.test_client().post(
        "/", data={"action": "deposit", "amount": "250"}
    )
    assert response.status_code == 200
    assert b"Deposit successful. Current balance: 1250.00" in response.data
    assert banking.balance == 1250.0


