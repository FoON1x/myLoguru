from loguru import logger

def main():
    print("Hello from loguru-study!")


if __name__ == "__main__":


    logger.trace('trace msg')
    logger.debug('debug msg')
    logger.info('info msg')
    logger.success('success msg')
    logger.warning('warning msg')
    logger.error('error msg')
    logger.critical('critical msg')

    child = logger.bind(foo='bar')
    child.info('info msg')
    with logger.contextualize(programmer="want"):
        logger.trace('trace msg')
        logger.debug('debug msg')
        logger.info('info msg')
        logger.success('success msg')
        logger.warning('warning msg')
        logger.error('error msg')
        logger.critical('critical msg')
