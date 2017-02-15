### My Event Demo API

#### Not Complete

**Current Project Status**

Not complete, outstanding tasks are marked with TODOs within code. A brief list is noted below

**Outstanding**

*   Personal Agenda
*   User Auth
*   Chat Application

**Project Description**

Please note that this part of the app was built on the 11/01/2016 between 17:00 & 22:00\. I have purposefully neglected some best practices due to time constraints, I have detailed below what changes I would make to ensure the product would be production ready.

My main goal for the app was to get the Express / JADE front end reading and writing from the API. I have achieved this, however I have been unable to add all the features I wanted to, you will see a wish list of features and improvements at the bottom of this page.

For speed and convince the API is running from a SQLite DB file, this allows it easy to run as a standalone app when you test it. To speed up the rest API production I made use of the Django Rest Framework and this has allowed me quickly develop a JSON rest API. I made use of class based views, however some views may need more tweaking or specific view methods. Authentication has been turned off for the API due to its test nature. In production however I would use oAuth or web token to authenticate the client against the API.

**Wishlist / Feature List**

*   Full User Authentication
*   Gamification, making use of realtime data (sockets, firebase, etc)
*   Cloud Notepad
*   Chat Application
*   Native APP interface
*   Event slides / file download