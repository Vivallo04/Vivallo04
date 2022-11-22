from mdutils.mdutils import MdUtils
import logging
import random
import json


def read_file(file):
    file = open(file)
    data = json.load(file)

    for challenge in data['challenges']:
        if challenge['challenge_name'] == "Two Sum":
            logging.debug(challenge['challenge_description'])

    file.close()


def get_upcoming(file) -> list:
    file = open(file)
    data = json.load(file)

    temp = list()
    logging.info('Upcoming: ')
    for i in data['upcoming']:
        temp.append(i)
        logging.debug(i)

    file.close()
    return temp


def get_old(file) -> list:
    file = open(file)
    data = json.load(file)

    temp = list()
    logging.info('Old:  ')
    for i in data['old']:
        temp.append(i)
        logging.debug(i)

    file.close()
    return temp


def get_challenge_of_the_day(file) -> str:
    pass


def write_challenge_of_the_day(challenge):
    pass


def get_solution(file):
    pass


def write_solution(solution, lang):
    pass


def select_daily_challenge(daily, upcoming, old) -> str:
    while daily in old:
        i = random.randint(0, len(upcoming))
        daily = upcoming[i]
    return daily


if __name__ == '__main__':
    logging.basicConfig(format='%(asctime)s - %(message)s',
                        datefmt='%d-%b-%y %H:%M:%S', level=logging.DEBUG)
    logging.info('Executing...')

    text_file = 'challenges.json'
    upcoming = get_upcoming(text_file)
    old = get_old(text_file)

    read_file(text_file)
    logging.info('Done!')
