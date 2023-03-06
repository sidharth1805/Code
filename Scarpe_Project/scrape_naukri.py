import requests
from bs4 import BeautifulSoup

# Set the URL to scrape
url = "https://www.naukri.com/data-engineer-jobs?k=data%20engineer&expMin=1"

print("started")
# Send a GET request to the URL and get the response
response = requests.get(url)
# print(response.text)

# Create a BeautifulSoup object from the response text
soup = BeautifulSoup(response.text, "html.parser")
print(soup)
# Find all the job postings on the page
job_postings = soup.find_all("div", {"class": "jobTupleHeader"})
print(job_postings)
# Loop through each job posting and extract the relevant information
for job_posting in job_postings:
    # Check if the experience requirement is 1 year
    experience_required = job_posting.find(
        "li", {"class": "fleft grey-text br2 placeHolderLi experience"}
    )
    if experience_required and "1-3" in experience_required.text:
        # Extract the job title and company name
        job_title = job_posting.find(
            "a", {"class": "title fw500 ellipsis"}
        ).text.strip()
        company_name = job_posting.find(
            "a", {"class": "subTitle ellipsis fleft"}
        ).text.strip()

        # Extract the job location and apply URL
        job_location = job_posting.find(
            "li", {"class": "fleft grey-text br2 placeHolderLi location"}
        ).text.strip()
        apply_url = job_posting.find("a", {"class": "title fw500 ellipsis"})["href"]

        # Print the job information
        print(
            f"{job_title} at {company_name} in {job_location}\nApply at: {apply_url}\n"
        )
