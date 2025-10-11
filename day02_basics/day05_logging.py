import logging

# Configure logging
logging.basicConfig(
    filename="app.log",
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] %(message)s"
)

logging.info("App started")
logging.warning("This is a warning")
logging.error("This is an error message")

try:
    x = 10 / 0
except Exception as e:
    logging.exception("An exception occurred")

logging.info("App finished")
