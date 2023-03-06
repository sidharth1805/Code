import requests
from bs4 import BeautifulSoup

# Set the URL to scrape
url = "https://www.linkedin.com/jobs/search/?f_E=1%2C2&keywords=data%20engineer&sortBy=R&f_TP=1&redirect=false&position=1&pageNum=0"

# Send a GET request to the URL and get the response
response = requests.get(url)
print(response.text)
# Create a BeautifulSoup object from the response text
soup = BeautifulSoup(response.text, "html.parser")
# print(soup)

# Find all the job postings on the page
job_postings = soup.find_all(
    "li", {"class": "result-card job-result-card result-card--with-hover-state"}
)

# Loop through each job posting and extract the relevant information
for job_posting in job_postings:
    # Check if the experience requirement is 1 year
    experience_required = job_posting.find(
        "span", {"class": "job-result-card__experience-badge"}
    )
    if experience_required and "1 year" in experience_required.text:
        # Extract the job title and company name
        job_title = job_posting.find("h3", {"class": "result-card__title"}).text.strip()
        company_name = job_posting.find(
            "a", {"class": "result-card__subtitle-link"}
        ).text.strip()

        # Extract the job location and apply URL
        job_location = job_posting.find(
            "span", {"class": "job-result-card__location"}
        ).text.strip()
        apply_url = job_posting.find("a", {"class": "result-card__full-card-link"})[
            "href"
        ]

        # Print the job information
        print(
            f"{job_title} at {company_name} in {job_location}\nApply at: {apply_url}\n"
        )
