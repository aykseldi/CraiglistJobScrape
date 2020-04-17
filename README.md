# CraiglistJobScrape
**Step by step what code makes...
1. It is written for scraping job postings of craiglist. 
2. First it gets the web page of wanted craiglist page and parses its html. Then looks for job title, post date and links.
3. Finds matching job titles with the string set. 
4. Puts all of matching job info into arrays. 
5. Creates an html document from these arays. 
6. Prepares the email with html, sender and receiver email addresses. 
7. Connects with google gmail api with credentials taken beforehand. 
---You should fix necessary permissions on gmail account like sending email, creating drafts or just reading emails.
8. Sets gmail service up and makes connection.
9. Sends email with matching findings in its body part. 

