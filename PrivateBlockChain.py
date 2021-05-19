#PrivateBlockChain.py
"""By Sourabh Mishra"""
from hashlib import sha256
import json

#dumy_block
dumyBlock = {"Index":0,"transactions":[],"previousHash":None,"proofOfWork":0}

#BlockChain
blockChain = [dumyBlock]

#Global Sender for our BlockChain
globalSender = "Sourabh"

#Global Transaction
globalTransaction = []

#For transaction
def transect():
    recipent = input("Recipent Name:\n")
    amount   = input("Amount:\n")
    return recipent,amount

#For creating Transaction
def createTransaction(recipent,amount):
    return {'sender':globalSender,'recipent':reci,'amount':amou}

#Conversion of blockToString
def blockToString(block):
    stringPreviousBlock = ""
    for key in block:
        stringPreviousBlock = stringPreviousBlock+str(block[key])
    return stringPreviousBlock

#For generating hash
def generateHash(block):
    stringPreviousBlock = ""
    for key in block:
        stringPreviousBlock = stringPreviousBlock+str(block[key])
    return sha256(json.dumps(stringPreviousBlock).encode('utf-8')).hexdigest()
     
    
#For generating PoW
def generateProofOfWork(block):
    block['proofOfWork'] = 0
    stringPreviousBlock = blockToString(block)
    hashOfBlock = sha256(json.dumps(stringPreviousBlock).encode('utf-8')).hexdigest()
    while ( hashOfBlock[0:2]!='00'):
           block['proofOfWork'] +=1
           stringPreviousBlock = blockToString(block)
           hashOfBlock = sha256(json.dumps(stringPreviousBlock).encode('utf-8')).hexdigest()
    return block['proofOfWork']


#For Mining A Block
def mine(transaction):
    global blockChain
    global globalTransaction
    lastBlock = blockChain[-1]
    hashOfBlock = generateHash(lastBlock)
    globalTransaction+=[transaction]
    block = {"Index":len(blockChain),"transactions":globalTransaction,"previousHash":hashOfBlock,"proofOfWork":0}
    generateProofOfWork(block)
    blockChain +=[block]
    print(blockChain[-1])
    return

#for validating
def validate():
    global blockChain
    everythingCorrect = True
    for blockNo in range(1,len(blockChain)):
        previousHash = generateHash(blockChain[blockNo-1])
        if previousHash != blockChain[blockNo]['previousHash']:
            everthingCorrect = False
            break
    if everythingCorrect:
        print("blockChain is correct")
    else:
        print("blocChain is currupted")
           
        
    
while __name__ == "__main__":
    if (input("Do you want to do transaction?\n")=='yes'):
        reci,amou = transect()
        transaction = createTransaction(reci,amou)
        mine(transaction)
        validate()
    else:
        break
    
