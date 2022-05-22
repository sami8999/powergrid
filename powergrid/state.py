weighting = {

    "consumption": -2,
    "production": 1,
    "fuel_cost":-1,
    "cost":-1
}

fuel_cost = {

    "oil": 3,
    "coal": 1,
    "nuclear": 14,
    "trash": 6,
}

import jsonify
class State:

    name = ""
    game_nearly_over = False
    game_over = False

    cash_balance = 0 # How much cash we have

    number_of_houses = 0
    
    total_number_of_houses = 0
    owned_powerplants = [] # list of dictionaries
    owned_houses = [] # list of dictionaries

    fuel_stocks = {
        "coal": 0,
        "oil": 0,
        "trash": 0,
        "nuclear": 0
    }

    enemies = [] # List of Enemy Objects

    def __init__(self):
        pass
    

    @staticmethod
    def successful_response(self):
        resp = jsonify(success=True)
        return resp
    
    def return_enemy_object(self, name):
        # Find Enemy Object Based on Name
        for enemy in self.enemies:
            if enemy.name == name:
                return enemy

    def update_enemy_state(self, enemy_object, payload):
        # Update Enemy Attributes based on most recent payload
        pass

    def compute_lead_auction(self, auction_pool): 
        
        powerplants = []

        for powerplant in auction_pool:
            consumption = weighting["consumption"] * powerplant["consumption"]
            production = weighting["production"] * powerplant["production"]
            base_cost = weighting["base_cost"] * powerplant["baseCost"]
            fuel_cost = weighting["fuel_cost"] *  fuel_cost[str(powerplant["fuelType"])] 
            total_score = consumption + production + base_cost + fuel_cost
            powerplants.append({
                "name":powerplant["id"],
                "score":total_score
                })

        powerplants.sort(key = lambda powerplant:powerplant["score"])

        body = {
            "powerPlantId" : powerplants[1]["name"],
            "bid" : 1,
            "pass" : False,
        }

        return body

    def compute_fuel_cost(self, fuel_market_state):

        weighting['fuel']["oil"] = 1+ ((24-fuel_market_state["Oil"])/3) 
        weighting['fuel']["coal"] = 1+ ((24-fuel_market_state["Coal"])/3) 
        weighting['fuel']["trash"] = 1+ ((24-fuel_market_state["Trash"])/3) 
        weighting['fuel']["nuclear"] = 13 - fuel_market_state["Nuclear"] if fuel_market_state["Nuclear"]>4 else 18 - (fuel_market_state["Nuclear"] * 2)


    def compute_bid(self,auction): 

        # bidding is a function of value to us and value to opponents 
        # at a score defined by our weigthing determine whether to bid or pass 

        # value to us
        consumption = weighting["consumption"][str(auction["auctionedPowerPlant"]["consumption"])]
        production = weighting["production"][str(auction["auctionedPowerPlant"]["production"])]
        cost =  weighting["cost"] * auction["highestBid"] if auction["highestBid"] !=0 else weighting["cost"] * auction["auctionedPowerPlant"]["baseCost"]
        self.compute_fuel_cost(auction['gameState']['fuelMarketState'])
        fuel = weighting["fuel"]

        absolute_score = consumption + production + cost + fuel #cost wrong

        strategic_score = 
        
    def checking_balance(self, expense):
        # Makes sure we never go into debt
        if expense > self.cash_balance:
            return True
        else:
            return False
    
    def add_powerplant_to_owned(self, response):
        if response["winner"]["name"] == self.name:
            self.owned_powerplants.append(response["winner"]["auctionedPowerPlant"])
        
        # value to others 
        # quantify value of powerplant to each opponents and make decision based in conjuction to valut to us 
        # look at fuel stocks of opponents, how much + can they power
        # there cash reserves 
        # powerplants owned 
        # value = percentage of fueltype owned 
    



