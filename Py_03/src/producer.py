import json
import logging
import random
import string
import time
import redis


def generate_transaction() -> dict:
    """
    Generate a random transaction.

    Returns:
        dict: The transaction data, with 'metadata' and 'amount' keys.
    """
    from_account = ''.join(str(random.randint(1, 9)) * 10)
    to_account = ''.join(str(random.randint(1, 9)) * 10)
    amount = str(random.randint(-100000, 100000))
    return {
        'metadata': {
            'from': from_account,
            'to': to_account},
        'amount': amount}


def main() -> None:
    """
    Main program.

    Publishes a random transaction to a Redis pubsub channel every 5 seconds.
    """
    # Connect to Redis
    redis_client = redis.Redis(
        host='localhost',
        port=6379,
        db=0,
        decode_responses=True
    )

    # Subscribe to pubsub channel
    pubsub = redis_client.pubsub()
    pubsub.psubscribe("channel_*")

    # Publish transactions
    while True:
        transaction = generate_transaction()
        json_data = json.dumps(transaction)
        redis_client.publish("channel_1", json_data)
        logging.info(json_data)
        time.sleep(5)  # Publish transactions every 5 seconds


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    main()
