import pytest
import app as banking

def setup_balance():
    banking.balance = 1000.0

def client():
    return banking.app.test_client()

def test_health_endpoint(client = banking.app.test_client()):
    response = client.get("/health")
    assert response.status_code == 200
    assert response.json["status"] == "healthy"

def test_deposit(client = banking.app.test_client()):
    response = client.post("/", data={"action": "deposit", "amount": "250"})
    assert b"Deposit successful. Current balance: 1250.00" in response.data
    assert banking.balance == 1250.0

def test_withdrawal(client = banking.app.test_client()):
    response = client.post("/", data={"action": "withdraw", "amount": "200"})
    assert b"Withdrawal successful." in response.data
    assert banking.balance == 1050.0


