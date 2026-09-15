import logging
import os
from datetime import datetime

Log_FILE=f"{datetime.now().strftime('%Y-%m-%d_%H-%M-%S')}.log"
log_path = os.path.join(os.getcwd(), "logs", Log_FILE)
# os.makedirs(os.path.dirname(log_path), exist_ok=True)
os.makedirs(log_path, exist_ok=True)


LOG_FILEPATH=os.path.join(log_path,Log_FILE)



logging.basicConfig(
    level=logging.INFO,
    filename=LOG_FILEPATH,
    format="[%(asctime)s] %(lineno)d %(name)s - %(levelname)s %(message)s"

)
logging.info("Logging started")