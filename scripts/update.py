from mdutils.mdutils import MdUtils
import logging
import random
import json

"""
1. Update to see new and old
2. Select a random challenge from upcoming
3. Write the upcoming and its solution to the file
"""


def get_challenge_updates(file: str, to_update: str) -> list:
    file = open(file)
    data = json.load(file)

    temp = list()
    logging.info(to_update + " ⬇")
    for i in data[to_update]:
        temp.append(i)
        logging.debug(i)

    file.close()
    return temp


def select_daily_challenge(upcoming_list: list, old_list: list) -> str:
    daily = random.choice(upcoming_list)
    while is_in_old(daily, old_list):
        print("Oops! Already taken 🎯")
        daily = random.choice(upcoming_list)
    print("🌟 " + daily)
    return daily


def is_in_old(i: str, old_list: list) -> bool:
    return i in old_list


def write_challenge_of_the_day(challenge):
    pass


def get_solution(file):
    pass


def write_solution(solution, lang):
    pass


if __name__ == '__main__':
    logging.basicConfig(format='%(asctime)s - %(message)s',
                        datefmt='%d-%b-%y %H:%M:%S', level=logging.DEBUG)
    logging.info('Executing...')

    # Read and update the challenges so that they do not repeat
    text_file = 'challenges.json'
    upcoming = get_challenge_updates(text_file, 'upcoming')
    old = get_challenge_updates(text_file, 'old')

    todays_challenge = select_daily_challenge(upcoming, old)

    # Update the readme file

    logging.info('Done!')
