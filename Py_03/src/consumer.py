import sys
import json
import redis
import logging
from typing import List


def read_out(bad_accounts: List[str]) -> None:
    """
    Reads messages from Redis pubsub channel and swaps sender and receiver
    information if the receiver is in the `bad_accounts` list and the amount is
    greater than 0.

    Args:
        bad_accounts (List[str]): List of bad accounts.
    """
    # Redis client
    r = redis.Redis(host='localhost', port=6379, db=0, decode_responses=True)
    # Redis pubsub
    p = r.pubsub()
    # Subscribe to channel_1
    p.subscribe("channel_1")

    while True:
        # Get message from pubsub
        message = p.get_message()
        # Check if message is valid
        if message and 'data' in message:
            try:
                # Get payload and decode if it's a string
                payload = message['data']
                if isinstance(payload, str):
                    data = json.loads(payload)
                    # Check if receiver is in bad accounts and amount is
                    # positive
                    if (data.get('metadata').get('to') in bad_accounts and
                            int(data['amount']) > 0):
                        # Swap sender and receiver
                        data['metadata']['to'], data['metadata']['from'] = (
                            data['metadata']['from'], data['metadata']['to'])
                        # Log the modified data
                        logging.info(json.dumps(data))
                    else:
                        # Log the original data
                        logging.info(payload)
            except json.JSONDecodeError:
                pass


if __name__ == "__main__":
    # Check if the script is called with the correct arguments
    if len(sys.argv) < 3 or sys.argv[1] != "-e":
        logging.error("Usage: need args: -e, accounts")
        sys.exit(1)
    # Configure logging
    logging.basicConfig(level=logging.INFO)
    # Get the list of bad accounts
    bad_accounts = sys.argv[2].split(",")
    # Read messages from Redis pubsub
    read_out(bad_accounts)
