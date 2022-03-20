import hashlib
import datetime

class Blockchain():
	def __init__(self):
		self.chain = list()
		self.chain.append(Block(index=0, prev_hash="0x0", data="Genesis block"))

	def get_previous_block(self):
		return self.chain[-1]

	def mine_block(self, data):
		new_block = Block(
			index = len(self.chain) + 1,
			data = data,
			prev_hash = self.get_previous_block().hash_block()
		)
		
		self.chain.append(new_block)

		return str(new_block)

	def is_blockchain_valid(self):
		prev_hash = "0x0"
		for block in self.chain:
			if block.prev_hash != prev_hash:
				return False
			
			if not block.is_block_valid():
				return False

			prev_hash = block.hash_block()

		return True

	def dictify(self):
		return { block.index:block.dictify() for block in self.chain }

	def test_fill(self):
		self.mine_block("Data 1")
		self.mine_block("Data 2")
		self.mine_block("Data 3")
		self.mine_block("Data 4")



class Block():
	MINE_DIFFICULTY = 4 # number of 0-s required at the beginning

	def __init__(self, index, data, prev_hash):
			self.index = index
			self.timestamp = str(datetime.datetime.now())
			
			self.block_data = data

			self.prev_hash = prev_hash

			self.proof = 1
			self.calculate_proof_of_work()

	def __str__(self):
		return "-".join((
			str(self.index),
			self.timestamp,
			self.block_data,
			str(self.proof),
			self.prev_hash
		))

	def hash_block(self):
		return hashlib.sha256(str(self).encode()).hexdigest()

	@staticmethod
	def zero_count(tx_hash, n):
		return tx_hash[0:n] == "0" * n

	def calculate_proof_of_work(self):
		while not self.zero_count(self.hash_block(), Block.MINE_DIFFICULTY):
			self.proof += 1

		return self.proof

	def is_block_valid(self):
		return self.zero_count(self.hash_block(), Block.MINE_DIFFICULTY) # proof of work is valid

	def dictify(self):
		return {
			"index": self.index,
			"timestamp": self.timestamp,
			"data": self.block_data,
			"prev_hash": self.prev_hash,
			"proof": self.proof,
			"hash" : self.hash_block()
		}

def main():
	bc = BlockChain()
	bc.test_fill()

	for block in bc.chain:
		print(f"""
			Data: {block.block_data},
			prev_hash: {block.prev_hash},
			hash: {block.hash_block()}
			""".replace("\t", ""), end="\n\n")

	print(bc.is_blockchain_valid())
	


if __name__ == "__main__":
	main()
