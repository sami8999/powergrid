from flask import Flask, request
import state as State
import pdb

app = Flask(__name__)

@app.route("/")
def heartbeat():
    return "Alive"


@app.route("/pg/startGame", methods=['POST'])
def start_game():
    data = request.json
    state.name = data.get("name")
    return "Success"

@app.route("/pg/gameNearlyOver", methods=['POST'])
def game_nearly_over():
    data = request.json
    state.game_nearly_over = True
    return "Hello, World!"


@app.route("/pg/gameOver", methods=['POST'])
def game_over():
    data = request.json
    state.game_over = True
    return "Hello, World!"


@app.route("/pg/leadAuction", methods=['POST'])
def lead_auction():
    data = request.json
    auction_pool = data.get("auctionPool") 
    body = state.compute_lead_auction(auction_pool)
    return body


@app.route("/pg/bidAuction", methods=['POST'])
def bid_auction():
    data = request.json
    auction = data
    body = state.compute_bid(auction)
    return body 


@app.route("/pg/wonAuction", methods=['POST'])
def won_auction():
    data = request.json
    return "Hello, World!"


@app.route("/pg/purchaseFuel", methods=['POST'])
def purchase_fuel():
    data = request.json
    return "Hello, World!"


@app.route("/pg/purchasedFuel", methods=['POST'])
def purchased_fuel():
    data = request.json
    return "Hello, World!"


@app.route("/pg/purchaseHouses", methods=['POST'])
def purchase_houses():
    data = request.json
    return "Hello, World!"


@app.route("/pg/purchasedHouses", methods=['POST'])
def purchased_houses():
    data = request.json
    return "Hello, World!"


@app.route("/pg/powerHouses", methods=['POST'])
def power_houses():
    data = request.json
    return "Hello, World!"


if __name__ == "__main__":
    app.run(debug=True)
    state = State()