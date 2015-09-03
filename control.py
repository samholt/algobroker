#!/usr/bin/python3
import algobroker
algobroker.send_control("ticker_yahoo",
                       {	
    "cmd" : "set",     
    "assets" : ["3888.HK", "0700.HK", "0388.HK"]
    })

algobroker.send_control("strategy_alert",
                        {	
    "cmd" : "set",
    "limits" : {
    "3888.HK" : [ 14.8, 15.5],	
    "0700.HK" : [ 125.0, 130.0],
    "0388.HK" : [ 180.0, 185.0]
    }
    })