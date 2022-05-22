weighting = {

    "consumption": -2,
    "production": 1,
    "fuel_cost":-1,
    "cost":-1
}

fuel_cost = {

    "Oil": 3,
    "Coal": 1,
    "Nuclear": 14,
    "Trash": 6,
}

class State:

    name = ""
    game_nearly_over = False
    game_over = False 

    number_of_houses = 0
    cash_reserves = 0
    total_number_of_houses = 0
    powerplants = []

    fuel_reserves = {
        "Coal": 0,
        "Oil": 0,
        "Trash": 0,
        "Nuclear": 0
    }

    def __init__(self):
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

        # strategic score
        fuel_ratio = self.fuel_reserves[str(auction["auctionedPowerPlant"]["fuelType"])] / sum(self.fuel_reserves.values())



        # strategic_score = 
        


        # value to others 
        # quantify value of powerplant to each opponents and make decision based in conjuction to valut to us 
        # look at fuel stocks of opponents, how much + can they power
        # there cash reserves 
        # powerplants owned 
        # value = percentage of fueltype owned 





