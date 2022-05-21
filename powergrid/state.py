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

class State:

    name = ""
    game_nearly_over = False
    game_over = False 

    number_of_houses = 0
    cash_reserves = 0
    total_number_of_houses = 0
    powerplants = []

    fuel_stocks = {
        "coal": 0,
        "oil": 0,
        "trash": 0,
        "nuclear": 0
    }

    def __init__(self):
        pass

    def compute_lead_auction(self, auction_pool): 
        
        powerplants = []

        for powerplant in auction_pool:
            consumption = weighting["consumption"] * powerplant["consumption"]
            production = weighting["production"] * [str(powerplant["production"])]
            base_cost = weighting["base_cost"] * powerplant["baseCost"]
            fuel_cost = weighting["fuel_cost"] * powerplant["fuelType"] 
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
        


        # value to others 
        # quantify value of powerplant to each opponents and make decision based in conjuction to valut to us 
        # look at fuel stocks of opponents, how much + can they power
        # there cash reserves 
        # powerplants owned 
        # value = percentage of fueltype owned 





