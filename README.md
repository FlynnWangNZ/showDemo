README
===========================

This project was built from my previous work experience.  
As a way to record what I have learned and done.  
See the demo [Online](http://104.128.91.5). Database will reset daily.  

  - username: demo
  - password: 2wsx#EDC

****
*I write the code from my memory and no details nor commercial info related to my previous employer*

## Functions
  - Email: As a QA, we always send emails of the release versions to many groups of members.  It is quite annoying to fill in the form by hand especially the version numbers from SVN server.  
  - Decode: Another useful tool for a company which develops customized protocol based on TCP and UDP. This helps to get human-readable format out of the data captured with TCPDUMP  
  - Jobs: This is the app I am using to record which jobs I have applied and all the following context like interviews and emails.

## Skills
  - Python (back end language)
  - Django (full-stack framework)
  - SQLite (could be altered with MYSQL or any others)
  - BootStrap (I am not very much into front end skills)
  - Jquery/Javascript/CSS 
  - Linux & Shell script (This project is deployed on my server runs CentOS)
  - Git & Github

## Features
  + Email page
      + Email title and Send to will auto change while components and database file changes
      + GetVersion button will send ajax request and react with the server
      + Jira Issues are connected to Jira Server using related library
      + There is a regex check with the test report
      + Attention content relates to 'is urgent' and 'component'
  + Decode page
      + Jsonviewer library is used to show data in a json format
      + Factory design method is used on the server side for different type of projects
  + Jobs page
      + Multi database tables are designed and used to store the valuable data
      + Admin configuration to control how data displayed
      
