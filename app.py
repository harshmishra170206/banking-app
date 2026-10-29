import math
from flask import Flask, jsonify, render_template_string, request

app = Flask(__name__)
balance = 1000.0

PAGE = """
<!doctype html>
<html lang="en">
<head>
    <meta charset="utf-8">
    <title>Simple Banking Application</title>
</head>
<body>
    <h1>Simple Banking Application</h1>
    <p>Current balance: {{ "%.2f"|format(balance) }}</p>
    <form method="post">
        <label for="action">Choose operation</label>
        <select name="action" id="action">
            <option value="balance">Check balance</option>
            <option value="deposit">Deposit money</option>
        </select>
        <label for="amount">Amount</label>
        <input type="number" name="amount" id="amount" min="0.01" step="0.01">
        <button type="submit">Submit</button>
    </form>
    <p>{{ message }}</p>
</body>
</html>
"""

@app.route("/", methods=["GET", "POST"])
def home():
    global balance
    message = ""
    if request.method == "POST":
        action = request.form.get("action", "")
        if action == "balance":
            message = f"Balance checked: {balance:.2f}"
        elif action == "deposit":
            try:
                amount = float(request.form.get("amount", "0"))
            except ValueError:
                amount = 0
            if not math.isfinite(amount) or amount <= 0:
                message = "Enter a deposit amount greater than zero."
            else:
                balance += amount
                message = f"Deposit successful. Current balance: {balance:.2f}"
        else:
            message = "Invalid option."
    return render_template_string(PAGE, balance=balance, message=message)


@app.route("/health")
def health():
    return jsonify(status="healthy"), 200


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)