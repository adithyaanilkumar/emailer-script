# Setup:

## Windows

1. go to system(control Pannel) on windows > advanced system settings > environment variable >  Add system variable(not user)
2. add variable name as iedc_email and the value as  <your gmail>
3. add another variable iedc_pass and value as  <your password>
4. click on save
5. close all powershell windows and restart

## For linux:

just export the variables in the command line as EXPORT iedc_email="<your gmail>" 

 EXPORT iedc_pass="<your password>"

# MAILER SCRIPT: 

1. clone the repo
2. cd into the html email folder
3. add the emails in the list.csv file on different lines
4. go to the mailer.py file 
5. change the subject of email on line 14
6. paste the content for the email as plain text,( just the written part of the content) in the text = """ Hi how are you """ section, line 19
7. paste the html obtained from the website in the html variable after """\   . on line 25
8. be careful to  not clear the \ 
9. after verifying everything, run " python mailer.py" to run the script
10. the list of emails that are not sent are shown in the error.csv file
11. Have given a delay of 7 seconds so that the server is not overloaded