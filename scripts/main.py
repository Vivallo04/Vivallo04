from bs4 import BeautifulSoup
import fileinput
import html2text
import json
import logging
import markdown
import random
import requests
import shutil
import sys

"""
1. Choose a new challenge
2. Write it down in the README.md
2.5 Write its solution
3. Update the last challenge in the json file
"""


# Load json in memory
def get_challenge_updates(file_path: str, update_field: str) -> list:
    # open with utf 8 encoding

    with open(file_path, 'r') as file:
        data = json.load(file)

    temp = list()
    for i in data[update_field]:
        temp.append(i)

    file.close()
    print("⚙Updating challenges...")
    return temp


# Choose a random challenge
def select_daily_challenge(file: str, upcoming_list: list, old_list: list) -> str:
    daily_challenge = random.choice(upcoming_list)
    if len(upcoming_list) == len(old_list):
        old_list = []
        update_challenges_list(file, old_list)
        return daily_challenge

    while is_in_old(daily_challenge, old_list):
        print("Oops! Already taken 🎯")
        daily_challenge = random.choice(upcoming_list)

    old_list.append(daily_challenge)
    update_challenges_list(file, old_list)
    print("🌟 " + daily_challenge)
    return daily_challenge


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
                content = i['content']
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


def set_last_challenge_content(file: str, todays_challenge_content: str):
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
    for line in fileinput.input(readme_file, inplace=True, encoding="utf-8"):
        if placeholder in line:
            line = line.replace(placeholder, new_text)
        sys.stdout.write(line)


def write_solution(solution, lang):
    pass


def main():
    # Make a GET request to the problem page
    URL = "https://leetcode.com/problems/all/"
    page = requests.get(URL)

    # Parse the HTML of the page
    soup = BeautifulSoup(page.content, "html.parser")

    # Find the title and description elements
    title_element = soup.find("h4", class_="title")
    description_element = soup.find("div", class_="question-content")

    # Extract the text from the elements
    title = title_element
    description = description_element

    # Save the information to a JSON file
    data = {
        "title": title,
        "description": description
    }
    with open("problem.json", "w") as f:
        json.dump(data, f)


# -------------
def read_file(file_name: str):
    logging.info("📰Reading file...")
    with open(file_name, "r+", encoding="utf-8") as file:
        text = file.read()
        return str(text)


def save_text_to_html(text):
    html = markdown.markdown(text)
    with open("readme.html", "w", encoding="utf-8") as file:
        file.write(html)


def replace_text_in_html(class_name: str, tag: str, new_text: str):
    with open("readme.html", "r+", encoding="utf-8") as file:
        html_text = file.read()
        soup = BeautifulSoup(html_text, features="html.parser")
        element = soup.find(tag, {"class": class_name})
        print("🔎 Tag found")
        print(element.string)
        element.string = new_text

        file.seek(0)
        file.write(soup.prettify())
        file.truncate()
        print("✅ Text replaced in html")


def convert_html_to_markdown(html):
    markdown_text = html2text.html2text(html)
    with open("readme.md", "w", encoding="utf-8") as file:
        file.write(markdown_text)


def copyfile(file_to_copy, new_path):
    shutil.copyfile(file_to_copy, new_path)


if __name__ == '__main__':
    # Variables
    challenges_json = "challenges.json"
    readme_temp = read_file("../README.md")

    # Load lists in memory
    upcoming = get_challenge_updates(challenges_json, "upcoming")
    old = get_challenge_updates(challenges_json, "old")

    # Choose a random challenge ⬇
    # Challenge Name
    daily = select_daily_challenge(challenges_json, upcoming, old)

    # Challenge Content
    daily_content = get_challenge_content(challenges_json, daily)

    # Pull the HTML temp file and replace the text
    replace_text_in_html("problem-title", "h3", daily)
    replace_text_in_html("problem-content", "p", daily_content)
    replace_text_in_html("problem-solution", "p", "🤓")

    # Convert it back to markdown
    convert_html_to_markdown(read_file("readme.html"))

    # Copy the README to the root folder to replace it
    copyfile("readme.md", "../README.md")

    logging.info('Done!')
