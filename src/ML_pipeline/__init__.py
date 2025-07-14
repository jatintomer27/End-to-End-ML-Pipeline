import os
import sys
import logging

logging_str = "[%(asctime)s: %(levelname)s: %(module)s: %(asctime)s]" 

log_dir = "logs"
log_filepath = os.path.join(log_dir,"running_logs.log")
os.makedirs(log_dir,exist_ok=True)

logging.basicConfig(
    level=logging.INFO,
    format=logging_str,
    
    handlers=[
        logging.FileHandler(log_filepath),
        logging.StreamHandler(sys.stdout)
    ]
)

logger = logging.getLogger("MLProjectLogger") 

# It defines a specific logger instance with the name "MLProjectLogger" 
# that you can use throughout your ML project for structured and controlled logging.


# sys.stdout is a built-in Python object that represents the standard output stream
# typically the console or terminal where your program runs.
