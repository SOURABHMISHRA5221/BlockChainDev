import datetime
import hashlib
import json
from flask import Flask, jsonify

class Blockchain:

    #initialisation of genesis block
    def __init__(self):
        self.chain = []
        self.create_block(proof=1,prev_hash='0')

    #creation of new block
    def create_block(self,proof,prev_hash):
        block = {'index' : len(self.chain)+1,
                 'proof' : proof,
                 'timestamp' : str(datetime.datetime.now),
                 'prev_hash' : prev_hash,
                 'transaction' : []
                 }
        self.chain.append(block)
        return block

    #
    def consensus (self, prev_proof):
        a=1
        b= False
        while b is False :
            hash= hashlib.sha256(str((a+1)**2 - (prev_proof)**2).encode()).hexdigest()
            if hash[:2]=="00":
                b=True
            else:
                a+=1
        return a
                
    #
    def prev_block(self):
        return self.chain[-1] 
    
    def hashing (self,block):
        encoding = json.dumps(block, sort_keys=True)
        return hashlib.sha256(encoding).hexdigest()


    
    def validate (self,chain):
        start = chain[0]

        for i in range(1,len(chain)):
            block=chain[i]
            if block[prev_hash] != self.hash(start):
                return False

            prev_proof=start['proof']
            proof = block ['proof']
            hash= hashlib.sha256(str((a+1)**2 - (prev_proof)**2).encode()).hexdigest()
            if hash[:2] !="00":
                return True
            start = block
        return True

    
               

blockchain = Blockchain()
def mining():
    prev_block= Blockchain.prev_block()
    prev_hash=Blockchain.hashing(prev_block)
    prev_proof=previous_block['proof']
    proof=Blockchain.consensus(prev_proof)
    block=Blockchain.create_block(proof,prev_hash)
    response = {'message': 'A block is MINED',
                'index': block['index'],
                'timestamp': block['timestamp'],
                'proof': block['proof'],
                'prev_hash': block['prev_hash']}
      
    return jsonify(response), 200

def print_chain():
     global blockchain
     response = {'chain': blockchain.chain,
                'length': len(blockchain.chain)}
     return jsonify(response), 200

def valid():
    valid = Blockchain.validate(Blockchain.chain)
      
    if valid:
        response = {'message': 'The Blockchain is valid.'}
    else:
        response = {'message': 'The Blockchain is not valid.'}
    return jsonify(response), 200

while(1>0):
    print ("press 1 to continue and 0 to exit")
    a= int(input())
    if (a == 0):
        break
    else:
        print ("Press 1 to mine the block")
        #print ("Press 1 to create new block")
        print ("Press 2 to validate the blockchain")
        print ("Press 3 to print the blockchain")
        b=int(input())
        if b == 1 :
            print (mining())
        if b==2 :
            print (valid())
        if b == 3 :
            print (print_chain())









            
           
        
