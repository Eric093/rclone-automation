# myapp.py
import logging
import mylib
#from InquirerPy import inquirer  # Import the inquirer module
#from rclone_python import rclone  # Import the rclone module
logger = logging.getLogger(__name__)

def main():
    logging.basicConfig(filename='myapp.log', level=logging.INFO)
    logger.info('TOTO')
    #mylib.do_something()
    logger.info('Finished')

if __name__ == '__main__':
    main()