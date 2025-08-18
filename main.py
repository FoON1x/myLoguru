from loguru import logger

def main():
    print("Hello from loguru-study!")


if __name__ == "__main__":
    # logger.remove()
    logger.add('msg.log', level='ERROR')
    # logger.remove(handler)

    logger.trace('trace msg')
    logger.debug('debug msg')
    logger.info('info msg')
    logger.success('success msg')
    logger.warning('warning msg')
    logger.error('error msg')
    logger.critical('critical msg')
