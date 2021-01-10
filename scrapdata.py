import time
from selenium import webdriver
from bs4 import BeautifulSoup
import csv

# BeautifulSoup
driver = webdriver.Chrome('/Users/derek.calamari/PycharmProjects/ScrapPrac/chromedriver 2')
driver.get('https://www.baseball-reference.com/leagues/MLB/2020.shtml')
time.sleep(5)
html = driver.page_source
soup = BeautifulSoup(html, 'html.parser')
html_soup = soup.prettify()
war_data = soup.find('table', id='team_output').find('tbody')
fielding_data = soup.find('table', id='teams_standard_fielding').find('tbody')
batting_data = soup.find('table', id='teams_standard_batting').find('tbody')
pitching_data = soup.find('table', id='teams_standard_pitching').find('tbody')
batting_head = soup.find('table', id='teams_standard_batting').find('thead').tr
pitching_head = soup.find('table', id='teams_standard_pitching').find('thead').tr
war_head = soup.find('table', id='team_output').find('thead').tr
fielding_head = soup.find('table', id='teams_standard_fielding').find('thead').tr


# write CSV files with beautifulsoup data
def batting_csv():
    output_file = open('batting.csv', 'w')
    writer = csv.writer(output_file)
    top = []
    row = []
    for th in batting_head.findAll('th'):
        top.append(th.get_text())
    writer.writerow(top)
    for line in batting_data.findAll('tr'):
        for item in line:
            row.append(item.get_text())
        writer.writerow(row)
        row.clear()


def pitching_csv():
    output_file = open('pitching.csv', 'w')
    writer = csv.writer(output_file)
    top = []
    row = []
    for th in pitching_head.findAll('th'):
        top.append(th.get_text())
    writer.writerow(top)
    for line in pitching_data.findAll('tr'):
        for item in line:
            row.append(item.get_text())
        writer.writerow(row)
        row.clear()


def war_csv():
    output_file = open('war.csv', 'w')
    writer = csv.writer(output_file)
    top = []
    row = []
    for th in war_head.findAll('th'):
        top.append(th.get_text())
    writer.writerow(top)
    for line in war_data.findAll('tr'):
        row.append(line.find('th').get_text())
        for td in line.findAll('td'):
            left = td.find('div', class_='left').get_text()
            right = td.find('div', class_='right').get_text()
            row.append(left + ' ' + right)
        writer.writerow(row)
        row.clear()


def fielding_csv():
    output_file = open('fielding.csv', 'w')
    writer = csv.writer(output_file)
    top = []
    row = []
    for th in fielding_head.findAll('th'):
        top.append(th.get_text())
    writer.writerow(top)
    for line in fielding_data.findAll('tr'):
        for item in line:
            row.append(item.get_text())
        writer.writerow(row)
        row.clear()


time.sleep(5)
driver.quit()
