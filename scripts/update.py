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


def update_challenges_list(file, new_old: list):
    with open(file, "r+") as json_file:
        data = json.load(json_file)
        data['old'] = new_old

        json_file.seek(0)  # rewind
        json.dump(data, json_file)
        json_file.truncate()
        print("New list update: ⏬")
        print(new_old)


def select_daily_challenge(file: str, upcoming_list: list, old_list: list) -> str:
    daily = random.choice(upcoming_list)
    while is_in_old(daily, old_list):
        print("Oops! Already taken 🎯")
        daily = random.choice(upcoming_list)
    print("🌟 " + daily)
    old_list.append(daily)
    update_challenges_list(file, old_list)

    return daily


def is_in_old(i: str, old_list: list) -> bool:
    return i in old_list


def write_challenge_of_the_day(challenge):
    pass


def write_solution(solution, lang):
    pass


if __name__ == '__main__':
    # Set up logging
    logging.basicConfig(format='%(asctime)s - %(message)s',
                        datefmt='%d-%b-%y %H:%M:%S', level=logging.DEBUG)
    logging.info('Executing...')

    # Read and update the challenges so that they do not repeat
    text_file = 'challenges.json'
    upcoming = get_challenge_updates(text_file, 'upcoming')
    old = get_challenge_updates(text_file, 'old')

    todays_challenge = select_daily_challenge(text_file, upcoming, old)

    # Update the readme file


    logging.info('Done!')
