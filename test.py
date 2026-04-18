import os
from datetime import datetime
import sys
import time
import logging
import argparser

@dataclass 
class User:
	name: str
	age: int


@timeclass

logging.basicConfig(level=logging.INFO)
logging.info("this is a big message")

parser = argparser.ArgumentParser()
parser.add_argument("--name", help="your name")
args = parser.parse_args()

print(f"hello {args.name}")
