# WELCOME TO CRAIGLIST JOB SCRAPE Automation with Google Gmail Integration

> This project is intended to build an automation pipeline for anything posted in Craiglist and alerting people through sending email with gmail. 

## Installing / Getting started

1. Download the python file in the repo. 
1. Connect your google gmail api with credentials taken beforehand.
   1. Put the api token into your computer.
   1. Change the python code accordingly where you put your token.
   1. For more information about Google Api Authorization (https://developers.google.com/gmail/api/auth/web-server)
1. Create a new crontab entry for script.
  

```shell
0 * * * * sudo /anaconda3/bin/python craiglist.py
```

* First it gets the web page of wanted craiglist page and parses its html. 
	* Code looks for job title, post date and links.
	* Finds matching job titles with the string set. 
	* Puts all of matching job info into arrays. 
	* Creates an html document from these arays. 
* Prepares the email with html, sender and receiver email addresses. 
* Connects with google gmail api with credentials taken beforehand. 
** Before starting y ou should fix necessary permissions on gmail account like sending email, creating drafts or just reading emails.**
*  Sets gmail service up and makes connection.
* Sends email with matching findings in its body part. 

 Email sent via this project (https://github.com/aykseldi/CraiglistJobScrape/blob/master/Email.png)

```bash
Normally this code should be called from crontab entry on a pc working all the day. 
Since I do not have pc all day running, I found a side solution with rtcwake package which comes with most linux distributions. RTCWAKE  makes a system sleep state until specified wakeup time, so I will make a hourly crontab entry which runs the python code then invokes rtcwake for to sleep 1 hour. This circular process goes on all through day or you can fix it to just work on nights.
```

Licensing

"The code in this project is licensed under MIT license."
