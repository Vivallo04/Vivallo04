import fileinput
import logging
import random
import json
import sys

"""
1. Choose a new challenge
2. Write it down in the README.md
2.5 Write its solution
3. Update the last challenge in the json file
"""


# Load json in memory
def get_challenge_updates(file: str, to_update: str) -> list:

    # open with utf 8 encoding

    file = open(file, "r+", encoding="utf-8")
    data = json.load(file)

    temp = list()
    for i in data[to_update]:
        temp.append(i)

    file.close()
    print("⚙Updating challenges...")
    return temp


# Choose a random challenge
def select_daily_challenge(file: str, upcoming_list: list, old_list: list) -> str:
    daily = random.choice(upcoming_list)
    if len(upcoming_list) == len(old_list):
        old_list = []
        update_challenges_list(file, old_list)
        return daily

    while is_in_old(daily, old_list):
        print("Oops! Already taken 🎯")
        daily = random.choice(upcoming_list)

    old_list.append(daily)
    update_challenges_list(file, old_list)
    print("🌟 " + daily)
    return daily


def is_in_old(i: str, old_list: list) -> bool:
    return i in old_list


# === Complementary method
def update_challenges_list(file, new_old: list):
    with open(file, "r+", encoding="utf-8") as json_file:
        data = json.load(json_file)
        data['old'] = new_old

        json_file.seek(0)  # rewind
        json.dump(data, json_file)
        json_file.truncate()
        print("Old list update: ⏬")
        print(new_old)


# Get today's challenge title and content
def get_challenge_content(file: str, challenge: str) -> str:
    with open(file, "r+") as json_file:
        data = json.load(json_file)

        for i in data['challenges']:
            name = i['title']
            if name == challenge:
                content = "⭐" + i['content']
                print("👀 " + content)
                return content


# Get last challenge
def get_last_challenge(file: str) -> str:
    file = open(file, "rb")
    data = json.load(file)
    last = data['last_problem_title']
    print("👴 Latest challenge: " + last)
    file.close()
    return last


def set_last_challenge(file, challenge):
    with open(file, "r+") as json_file:
        data = json.load(json_file)
        data['last_problem_title'] = challenge
        json_file.seek(0)
        json.dump(data, json_file)
        json_file.truncate()
        print("✅ Last challenge updated: " + challenge)
    json_file.close()


def set_last_challenge_content(file, todays_challenge_content: str):
    with open(file, "r+", encoding="utf-8") as json_file:
        data = json.load(json_file)
        data['last_problem_content'] = todays_challenge_content
        json_file.seek(0)
        json.dump(data, json_file)
        json_file.truncate()
        print("✅ Last challenge content updated: " + str(todays_challenge_content))
    json_file.close()


# Write today's challenge and solution
def write_challenge_of_the_day(readme_file: str, new_text: str, placeholder):
    # write to markdown
    for line in fileinput.input(readme_file, inplace=1, encoding="utf-8"):
        if placeholder in line:
            line = line.replace(placeholder, new_text)
        sys.stdout.write(line)


def write_solution(solution, lang):
    pass


if __name__ == '__main__':
    # Set up logging
    logging.basicConfig(format='%(asctime)s - %(message)s',
                        datefmt='%d-%b-%y %H:%M:%S', level=logging.DEBUG)
    logging.info('Executing...')

    # Global variables
    text_file = 'challenges.json'
    readme = '../README.md'

    # Read and update the challenges so that they do not repeat
    upcoming = get_challenge_updates(text_file, "upcoming")
    old = get_challenge_updates(text_file, "old")

    # Current variables
    last_challenge = get_last_challenge(text_file)
    todays_challenge_name = select_daily_challenge(text_file, upcoming, old)
    todays_challenge_content = get_challenge_content(text_file, todays_challenge_name)

    # Update the readme file and params
    write_challenge_of_the_day(readme, todays_challenge_name, "⭐")
    write_challenge_of_the_day(readme, todays_challenge_content, "👀")
    set_last_challenge(text_file, todays_challenge_name)
    set_last_challenge_content(text_file, todays_challenge_content)

    logging.info('Done!')
