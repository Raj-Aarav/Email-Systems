Email-System
Using Socket programming we are trying to create an email system based on client-server model. We are using Python for the implementation. 
It is using TCP for the working. 
In the project, there are going to be 3 Primary files : 
  1. Server.py : Is the main server file which needs to be executed first, and it must remain ON until the connections are closed.
  2. Client.py : Here, the client will choose whether to send a mail, or read the inbox.
  3. Users.py : This is where the new users details will be entered and stored in database. It won't allow any duplicate user email, if the email already exists.
  4. Users.db : Database where the mails which are sent are stored alongwith users details.

