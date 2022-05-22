weighting = {

    "consumption": -2,
    "production": 2,
    "fuel_cost":-1,
    "cost":-1,
    "fuel_usefulness":30,
    "price_appeal":30,
    "houses_to_power": 0.5
}

fuel_cost = {

    "Oil": 3,
    "Coal": 1,
    "Nuclear": 14,
    "Trash": 6,
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

    fuel_reserves = {
        "Coal": 0,
        "Oil": 0,
        "Trash": 0,
        "Nuclear": 0
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

        fuel_cost["Oil"] = 1+ ((24-fuel_market_state["Oil"])/3) 
        fuel_cost["Coal"] = 1+ ((24-fuel_market_state["Coal"])/3) 
        fuel_cost["Trash"] = 1+ ((24-fuel_market_state["Trash"])/3) 
        fuel_cost["Nuclear"] = 13 - fuel_market_state["Nuclear"] if fuel_market_state["Nuclear"]>4 else 18 - (fuel_market_state["Nuclear"] * 2)

    def compute_bid(self,auction): 

        # bidding is a function of value to us and value to opponents 
        # at a score defined by our weigthing determine whether to bid or pass 

        # absolute score
        consumption = weighting["consumption"] * auction["auctionedPowerPlant"]["consumption"]
        production = weighting["production"] * auction["auctionedPowerPlant"]["production"]
        cost =  weighting["cost"] * auction["highestBid"] if auction["highestBid"] !=0 else weighting["cost"] * auction["auctionedPowerPlant"]["baseCost"]
        self.compute_fuel_cost(auction['gameState']['fuelMarketState'])
        fuel = weighting["fuel_cost"] *  fuel_cost[str(auction["auctionedPowerPlant"]["fuelType"])]
        absolute_score = consumption + production + cost + fuel

        # strategic score to us 
        fuel_usefulness = (self.fuel_reserves[str(auction["auctionedPowerPlant"]["fuelType"])] / sum(self.fuel_reserves.values())) * weighting["fuel_usefulness"]
        price_appeal = ((auction["highestBid"] if auction["highestBid"] !=0 else auction["auctionedPowerPlant"]["baseCost"]) / self.cash_reserves) * weighting["price_appeal"]  
        houses_now_able_to_power = auction["auctionedPowerPlant"]["production"] * weighting["houses_to_power"] if auction["auctionedPowerPlant"]["consumption"] <= self.fuel_reserves[str(auction["auctionedPowerPlant"]["fuelType"])] else 0
        strategic_score_to_us = fuel_usefulness + price_appeal

        # value to others 

        # strategic score to others 
        op_fuel_usefulness = 0
        op_price_appeal = 0
        op_able_to_power = 0

        # quantify value of powerplant to each opponents and make decision based in conjuction to valut to us 
        # look at fuel stocks of opponents, 
        # how much they can power given assuming they win the auction 
        # there cash reserves 
        # powerplants owned 
        # value = percentage of fueltype owned 
    
        
    def checking_balance(self, expense):
        # Makes sure we never go into debt
        if expense > self.cash_balance:
            return True
        else:
            return False
    
    def add_powerplant_to_owned(self, response):
        if response["winner"]["name"] == self.name:
            self.owned_powerplants.append(response["winner"]["auctionedPowerPlant"])
    



