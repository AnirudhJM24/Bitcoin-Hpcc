from collections import defaultdict
from address import parse_script_pubkey
import json

def dataholder(dataobj):
    Transactiondat = {
                
                "txvn": "transaction_id",
                "input count" : 0,
                "fee":0,
                "inputs": [
                
            ],
            "outputs": [
                
            ]
        }

    Txinput = {
            "address": "address",
            "value":0
            }
        
    Txoutput = {
            "value": 10.5,
            "address": "address"
            }
    
    if dataobj == 'Transactiondat':
        return Transactiondat
    elif dataobj == 'Txinput':
        return Txinput
    elif dataobj == 'Txoutput':
        return Txoutput




def creatFinalTxJson(transactionHashMap):
    txdatafinal = []
    for txid, txdata in transactionHashMap.items():

        Transactiondat = dataholder('Transactiondat')
        Transactiondat["txvn"] = txdata['txvn']
        Transactiondat["input count"] = txdata['input count']

        for input_tx_data in txdata['inputs']:

            txinput = dataholder('Txinput')
            input_txid = input_tx_data['txid'].lower()
            if input_txid not in transactionHashMap.keys():
                txinput['address'] = 'unknown'
                txinput['value'] = 'unknown'
            
            else:
                vout = input_tx_data['vout']
                if vout!='FFFFFFFF':
                    vout = int(vout,16)
                    txinput['address'] = parse_script_pubkey(transactionHashMap[input_txid]['outputs'][vout]['script_pubkey'].lower())
                    txinput['value'] = transactionHashMap[input_txid]['outputs'][vout]['value']
                else:
                    txinput['address'] = 'reward'
                    txinput['value'] = '0'
            Transactiondat['inputs'].append(txinput)
        
        
        for output_data in txdata['outputs']:
            Txoutput = dataholder('Txoutput')
            Txoutput['address'] = parse_script_pubkey(output_data['script_pubkey'])
            Txoutput['value'] = output_data['value']
            Transactiondat['outputs'].append(Txoutput)
        txdatafinal.append(Transactiondat)
    
    return txdatafinal


        
