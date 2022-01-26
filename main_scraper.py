from bs4 import BeautifulSoup
import requests  # requests info from a specific website
import time

print('Filter out a skill')
unfamiliar_skill = input('> ')
print(f'Filtering out {unfamiliar_skill}')


def find_jobs():
    html_text = requests.get(
        'https://www.timesjobs.com/candidate/job-search.html?searchType=personalizedSearch&from=submit&txtKeywords=python&txtLocation=').text  # url goes here
    soup = BeautifulSoup(html_text, 'lxml')

    job_list = soup.find_all('li', class_='clearfix job-bx wht-shd-bx')
    for index, job in enumerate(job_list):
        publish_date = job.find('span', class_='sim-posted').span.text
        if 'month' in publish_date:
            pass
        else:
            company_name = job.find('h3', class_='joblist-comp-name').text.replace(' ', '')
            skill_requirements = job.find('span', class_='srp-skills').text.replace(' ', '')
            job_information = job.header.h2.a['href']
            if unfamiliar_skill not in skill_requirements:

                with open(f'posts/{index}.txt', 'w') as f:
                    f.write(f"Company Name: {company_name.strip()} \n")
                    f.write(f"Required Skills: {skill_requirements.strip()} \n")
                    f.write(f"Listing Date: {publish_date.strip()} \n")
                    f.write(f"Job information: {job_information}")
                print(f'File saved: {index}')


if __name__ == '__main__':
    while True:
        find_jobs()
        time_wait = 10
        print(f'Waiting {time_wait} minutes...')
        time.sleep(time_wait * 60)

