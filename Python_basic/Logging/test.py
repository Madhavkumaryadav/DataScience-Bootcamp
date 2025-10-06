from log import get_logger

logger = get_logger(__name__)

def add(a, b):
    logger.debug("The addition operation is taking place: %s + %s", a, b)
    return a + b


if __name__ == '__main__':
    logger.debug("The addition function is called from main")
    result = add(10, 34)
    logger.info("Result of add(10,34) = %s", result)

