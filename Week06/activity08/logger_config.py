import logging


def setup_app_logging():
    # Initializing the global logging configuration
    logging.basicConfig(
        level=logging.DEBUG,
        format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
        handlers=[
            logging.FileHandler("app_debug.log")
        ]
    )
