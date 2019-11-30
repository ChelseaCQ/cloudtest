#!/usr/bin/env python
# coding: utf-8

import sys
import hashlib
import json
from time import time


class Blockchain(object):
    def __init__(self):
        self.current_transactions = []
        self.chain = []

        # Create the genesis block
        self.new_block(previous_hash=1, proof='COMSM0010cloud')

    def new_block(self, proof, previous_hash=None):
        """
        生成新块
        :param proof: <int> The proof given by the Proof of Work algorithm
        :param previous_hash: (Optional) <str> Hash of previous Block
        :return: <dict> New Block
        """

        block = {
            'index': len(self.chain) + 1,
            'timestamp': time(),
            'transactions': self.current_transactions,
            'proof': proof,
            'previous_hash': previous_hash or self.hash(self.chain[-1]),
        }

        # Reset the current list of transactions
        self.current_transactions = []

        self.chain.append(block)
        return block

    @property
    def last_block(self):
        return self.chain[-1]

    @staticmethod
    def hash(block):
        """
        生成块的 SHA-256 hash值
        :param block: <dict> Block
        :return: <str>
        """

        # We must make sure that the Dictionary is Ordered, or we'll have inconsistent hashes
        block_string = json.dumps(block, sort_keys=True).encode()
        return hashlib.sha256(block_string).hexdigest()
    def proof_of_work(self, last_proof,dif):
        """
        简单的工作量证明:
         - 查找一个 p' 使得 hash(pp') 以4个0开头
         - p 是上一个块的证明,  p' 是当前的证明
        :param last_proof: <int>
        :return: <int>
        """
        nonce=0
        dif=dif
        print(last_proof)
        print("this is last_proof")
        while self.valid_proof(last_proof, nonce,dif) is False:
            nonce += 1

        return nonce

    @staticmethod
    def valid_proof(last_proof, nonce,dif):
        """
        验证证明: 是否hash(last_proof, proof)以4个0开头?
        :param last_proof: <int> Previous Proof
        :param proof: <int> Current Proof
        :return: <bool> True if correct, False if not.
        """
        guess1=str(last_proof)+""+str(nonce)
        guess=guess1.encode('utf-8')
        # guess = f'{last_proof}{nonce}'.encode('utf-8')
        print(guess)
        guess_hash = hashlib.sha256(guess).hexdigest()
        print(guess_hash)
        return guess_hash[:dif] == str(0).zfill(dif)
    

blockchain= Blockchain()
# if __name__ == "__main__":
#
#     diff_level=int(sys.argv[1])
this_block = blockchain.chain[-1]
proof = this_block['proof']
nonce = blockchain.proof_of_work(proof,4)
nonce







