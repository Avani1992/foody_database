import logging

class Logging1:


        logging.basicConfig(filename="Logging.log", format='%(asctime)s %(filename)s  %(levelname)s  %(message)s', filemode="w")
        logging.NullHandler



log=Logging1()
