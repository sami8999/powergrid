import logging
class Enemy:

    name = ""
    


    def __init__(self, name):
        self.name = name
        logging.info(f"Instantiated Enemy - {name}")
    
