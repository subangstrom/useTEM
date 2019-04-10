# @Author: abinashkumar
# @Date:   2019-03-26T18:45:38-04:00
# @Last modified by:   abinashkumar
# @Last modified time: 2019-03-27T14:41:54-04:00



import xmlrpc.client
#from xmlrpc.client import MultiCall, Boolean

import pumpy

import logging
import numpy as np



if __name__ == "__main__":


    logging.basicConfig(level=logging.INFO)

    prox = xmlrpc.client.ServerProxy("http://10.154.7.25:8000/pump")

    prox.setFlowRate(100,'ul/min')
    prox.setVolume(1000,'ul')
    prox.time(10)
    prox.infuse()
    #prox.oppInfuse()

    #p1.setVolume(10,'ml')
