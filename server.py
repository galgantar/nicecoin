import fastapi

from NiceCoin import Blockchain

blockchain = Blockchain()
blockchain.test_fill()

app = fastapi.FastAPI()

@app.post("/mine_block")
def mine_block(block_data):
	if not blockchain.is_blockchain_valid():
		return fastapi.HTTPexception(
			status_code=400,
			detail="Blockchain is invalid"
		)

	block = blockchain.mine_block(data)

	return block.dictify()


@app.get("/blockchain")
def get_blockchain():
	if not blockchain.is_blockchain_valid():
		return fastapi.HTTPexception(
			status_code=400, detail="Blockchain is invalid"
		)

	return blockchain.dictify()