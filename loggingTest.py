import logging
logging.basicConfig(level=logging.INFO,filename='mylog.log')
logging.info('Starting program')
logging.info('try to divide 1 by 0')
logging.info('try to divide 1 by 0')
print(1/0)
logging.info('division succeed')
logging.info('Ending program')
