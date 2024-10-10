import json
import sys
import threading
import time
import logging
from multiprocessing import Process
from mitmproxy import http
from mitmproxy.tools.main import mitmdump
from mitmproxy.http import HTTPFlow

# Set up logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

subprocess_instance = None

def receive_answer(answers_list):
    # Placeholder function to handle answers
    logging.info(f"Received answers: {answers_list}")

def request(flow: http.HTTPFlow) -> None:
    # Handle HTTP request here
    pass

def response(flow: http.HTTPFlow) -> None:
    # Handle HTTP response

    if "https://xyks.yuanfudao.com/leo-math/android/exams?" in flow.request.url:
        answer = json.loads(flow.response.text)
        logging.info(f"Exam answer received: {json.dumps(answer, indent=4)}")

    elif "https://xyks.yuanfudao.com/leo-game-pk/android/math/pk/match?" in flow.request.url:
        answer = json.loads(flow.response.text)
        answers_list = [question['answer'] for question in answer.get('examVO', {}).get('questions', [])]

        if answers_list:
            subprocess_instance = Process(target=receive_answer, args=(answers_list,))
            subprocess_instance.start()
            logging.info(f"Answers list for PK match received: {answers_list}")

if __name__ == "__main__":
    sys.argv = ["mitmdump", "-s", __file__, "--listen-host", "0.0.0.0", "--listen-port", "7532"]
    mitmdump()
