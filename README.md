# Project 3 - Django Djourneys

## Description

This project was assigned at the end of the eighth week of General Assembly’s 3-month SEI (Software Engineering Immersive) course, which teaches people who don't know how to code the basics of software engineering with a view to launching a career in the tech sector. The aim of this project was to design an app in Python using the Django framework over the course of one week. This project was a group project together with two other students on the course.

## Deployment link

[You can find Django Djourneys deployed on this link](https://djangodjourney.herokuapp.com/). Take the quiz and see where your next journey should take you!

![Screenshot 2022-11-04 at 13 36 24](https://media.git.generalassemb.ly/user/44781/files/ac47f2d6-d2d4-4e8a-b70d-e2e896eedb71)

## Getting Started/Code Installation

### Instructions

#### Deployed app

There are no specific installation requirements for this app since Django Djourneys runs in the browser. Simply create an account or take our four-part quiz to get started!

## Timeframe & Working Team

We worked as a team of three over the course of a week to deliver this project. We split tasks equally to ensure we were all contributing to the project at the same level. We were an especially effective team on this project! I took the lead to manage the project and track tasks to ensure we remained on target for delivery.

## Technologies Used

We built this project in Python and HTML within the Django framework, with CSS for the styling. We used Multer for image upload and deployed our app on Heroku.

## Brief

Our brief for this project was to build an app from scratch in Python as a team using the Django framework, and then to deploy this on Heroku. Our criteria were as follows:

- Create the application using at least 2 related models, one of which should be a user
- Manage team contributions and collaboration using a standard Git flow on GitHub
- Include all major CRUD functions for at least one of your models
- Add authentication AND authorization (page protection) to restrict access to appropriate users
-   User must be able to sign up or login
-   Signed in user must be able to change password and logout
-   change password and logout must only be available to logged in users
- Layout and style your front-end with clean & well-formatted CSS, with or without a framework
- Deploy your application online so it's publicly accessible

Some of the possible stretch goals we could achieved included:

- Allow users to change website theme, Dark mode etc.
- Include Pagination
- Utilise 3rd party APIs
- Send verification email upon registration
- Allow users to upload image files
- Password reset using an email

At the end of the project we had to present our project while covering the points below:

- What is the app about?
- How does your app work?
- What bits of code are you most proud of?
- What was your favourite part to work on?
- What issues did you encounter?
- What would you add next?

## Planning  

### Development Overview  

As team leader, I worked with my teammates to come up with a clear development process that we could follow and track our progress over the course of project:

1. Brainstorm
2. Pick an idea
3. Wireframe, ERDs and user stories
4. Create repo and starting files (.js, .css., .html)
5. Break the process down by requirements
6. Basic layout
7. Structure logic and begin working on functions
8. Test functions
9. Touch up styling
10. Test site
11. BONUS: Add extras

### Team leadership  

Speaking to the team, we agreed that I would be team leader and handle management of the project and development flow. As in previous projects, we collaborated to set out a clear development overview that would allow us to remain accountable, on target and achieve our goals for this app. We established minimum deliverable functionalities as well as stretch goals, and as the project progressed, I ensured that we all stuck to these as a team. Wherever issues arose, we worked together to resolve these and I periodically checked in with my teammates to see if they needed help, feedback or support with bugs. We used Zoom and Slack to stay in constant communication throughout the project.

### Task management  

I created a public Trello board which all of our team could access in order to track, assign and manage tasks. This really helped us work collaboratively and we reviewed the Trello board on a daily basis each day to make sure we stayed up to date on what had been done, what needed to be assigned, and what hadn't been started yet. You can find the link to our Trello board [here](https://trello.com/b/OvjiXE35/project3-django-djourney).

![Screenshot 2022-11-04 at 14 44 05](https://media.git.generalassemb.ly/user/44781/files/30dd4f83-d60d-4f03-9d8c-c330f6087327)

## Build/Code Process

Documented below are the stages we went through in order to build the code for our project.  

### Stage 1: Brainstorming  

We started by brainstorming ideas for our app. Initial ideas included a World Cup 2022 match fixture tracker, a sports venue booking system and one or two other ideas related to sporting events. After some initial research, we decided to rule these out and went with our final, very appealing idea.

### Stage 2: Pick an idea  

My team were all quite ready for a holiday and taking inspiration from the perfume brand Penhaligon's website, where users can take a test to build a "fragrance profile" and be matched to the best fragrances for them, we thought: "Wouldn't it be great if you could have an app that tells you what your next holiday destination should be?". The idea struck a chord with all of us and we decided to build a quiz that users can take to be matched to a list of potential holiday destinations.

### Stage 3: Wireframe, ERD and user stories  

#### ERD

We started by drawing up an ERD to map out the relations between all of our models and functionalities.

![ERD](https://media.git.generalassemb.ly/user/44781/files/69120fdf-0cc4-4d7c-a748-4e32f7fdea1c)

#### Wireframes

We then got to work on wireframing our site page by page:  
<img src="https://media.git.generalassemb.ly/user/44781/files/b74fb9d7-4015-44e2-a1ff-7e5db2c2a89b" width="500" height="350">
<img src="https://media.git.generalassemb.ly/user/44781/files/f34d814c-8202-4982-a4c3-3d3be94fb3e6" width="500" height="350">
<img src="https://media.git.generalassemb.ly/user/44781/files/4d5d79f6-4512-4ffa-bba8-0dcdb1788710" width="500" height="550">
<img src="https://media.git.generalassemb.ly/user/44781/files/c1177570-61e3-47c5-be71-fbfad99c0b06" width="500" height="550">

#### User Stories

We took time to think about the features and functionalities we wanted our users to have, and set out the following user stories:

- As an unregistered user, I want a function to sign up to the site  
- As an unregistered user, I want to know what the site is about  
- As a registered user, I want to be able to create a profile  
- As a user of the site, I want to be able to see a list of destinations  
- As a user, I want to be able to see details about those destinations
- As a user, I want to be able to edit my profile  
- As a user, I want to be able to take the quiz 
- As a user, I want to be able to see my quiz results and the destinations they match up with
- BONUS: As a registered user, I want to be able to leave reviews   
- BONUS: As a user, I want to learn about the creators of the site  
- BONUS: As a user, I want to add my own destinations    

### Stage 4: Creating GitHub repo and starting files  

Since I was the team leader on this project, I created a repo on GitHub and set up the initial file structure so that we could begin working. I communicated constantly with my team to make sure that we were always working in the dev branch, and helping them to resolve any issues with migrations, merges, etc. We experienced relatively few issues with conflicts during merges as a result and development ran more or less smoothly.

### Stage 5: Requirements  

We defined our basic requirements at the outset:

- Users should be greeted by a welcome page explaining the site and the quiz
- Users should have the option to take the quiz, or skip straight to a list of all destinations
- Users should be able to create an account
- Users should be able to see details on individual destinations
- Users should be able to leave reviews on destinations they have visited

### Stage 6: Basic layout  

Once we had set out our basic requirements, we got started on the basic layout of the site in line with our wireframes. I created a **templates** folder in our main app directory where all of our html files would be located. We started with **base.html**, which is the file that serves as the base template for our site, with imported 3rd-party APIs, jQuery library, fonts, Bootstrap, CSS. The header contains our links to navigate the site, with additional links in the footer, while the **main** element uses backend code to allow us to insert other html files as the user navigates the site: 

![Screenshot 2022-11-08 at 16 49 29](https://media.git.generalassemb.ly/user/44781/files/3107161d-3e90-4733-ae1e-d39209bc8d69)
  
The first page users see is **home.html**:

![Screenshot 2022-11-08 at 16 55 25](https://media.git.generalassemb.ly/user/44781/files/a1bd7cca-990c-4d42-8e89-86388596e2ae)

The HTML in this file between **{% block content %}** and **{% endblock %}** is taken as a whole block of code and slotted into the **base.html** because we have added **{% extends 'base.html' %}** at the top of the file. In this way we began building the different pages for our site, with separate HTML files for the users' profile, user registration, and destinations both collectively as well as individually. We would later add separate files for our quiz, quiz results, and search functionality: 

![Screenshot 2022-11-08 at 17 04 15](https://media.git.generalassemb.ly/user/44781/files/ce434032-2000-449d-ae7a-a72a2c82973b)

### Stage 7: Structuring logic and working on functions  

We delegated functions by feature to each of the members of our team:

- I would work on creating user accounts, user profiles, the list of destinations and the main quiz function 
- One teammate would work on our search function and APIs for displaying destinations
- One teammate would work on user review functionality, ratings, site styling/pagination and 3rd party APIs

I started by looking for a suitable list of destinations to use for our databse. I settled on a list of 250 destinations collated by Nghia Nhuyen and offered for use on her GitHub [here](https://github.com/nghia-t-nguyen/travel-bot-project/blob/main/Travel-Destinations.csv). I edited the spreadsheet to include the **Name** of the destination, my teammates entered the **Location** and updated the **Country**for each one, and I also added the **Currency**. Later, I would also add a list of specific **Keywords** to each destination, which would be use later on in our quiz function:

![Screenshot 2022-11-08 at 16 15 03](https://media.git.generalassemb.ly/user/44781/files/b68386f6-8bda-490a-b160-9332774edbdd)

With our basic list of destinations completed, I exported this as a .csv file and imported it into our database in PostgreSQL, taking care to deselect the ID tag when specifying the columns to import:

![image](https://media.git.generalassemb.ly/user/44781/files/36b5a76c-e040-4c37-b61f-04e0509b4abf)
![Screenshot 2022-10-02 at 15 07 33](https://media.git.generalassemb.ly/user/44781/files/69702af8-401c-4fc8-8100-885940647d60)

This allowed my teammate to begin working on creating the APIs to retrieve all destinations via our search function or when the user clicks on 'View All Destinations': 

![Screenshot 2022-11-08 at 19 47 43](https://media.git.generalassemb.ly/user/44781/files/89e0f050-4273-44af-b4ba-69919883231b)

as well as rendering details for individual destinations:

![Screenshot 2022-11-08 at 19 49 21](https://media.git.generalassemb.ly/user/44781/files/63557125-58c5-47da-aca5-4ef51813bee9)
  
Next, I worked on the user creation functionality. Creating the user account was simple enough with the use of a **signup** API. I wrote this to capture the information the user enters during sign-up as a POST request, validate this and then save the information as a new instance of User. With their user account now created, the user is then redirected to the index page:

![Screenshot 2022-11-04 at 15 58 41](https://media.git.generalassemb.ly/user/44781/files/8f1d03f5-a926-4e14-b4a1-92428c30cfb7)

The file **forms.py** contains a model for a form that allows the user to update their profile information: 

<img width="714" alt="Screenshot 2022-11-08 at 19 17 41" src="https://media.git.generalassemb.ly/user/44781/files/8397f0b3-d898-461c-9863-09e949eed517">
  
This is mirrored on the frontend with the following form:

![Screenshot 2022-11-08 at 19 24 36](https://media.git.generalassemb.ly/user/44781/files/76f6e361-0fab-4f98-97d4-1e1ea8bf3b99)

The form is populated with their existing information, and once they click on the submit button, the **profile_update** API is triggered. The information entered in the frontend form is sent as a request to the backend, validated against the structure of the user and profile update forms, and if valid, both the user and profile objects are updated in the database:

![Screenshot 2022-11-08 at 19 26 52](https://media.git.generalassemb.ly/user/44781/files/55f3a8d6-ac9b-4ec5-bb89-a70539f39da6)

### Favourite functions

#### User signup & profile creation

The trick on this project was to allow the user to sign up and simultaneously create a profile for the user in the background. 

With the sign up API already written, I created a **signals.py** file. This contains two signals that would cause two additional functions to be triggered on the creation of an instance of User, and when they update their information. This creates an instance of Profile, which stores information about the user. This is then displayed when they log into the website, and is based on the instance of User that has just been created. It was tricky to get working at first, but by using console.log on each line of my code, I was able to pinpoint my error, which was an incorrect import statement.

![Screenshot 2022-11-04 at 16 02 35](https://media.git.generalassemb.ly/user/44781/files/24ee6053-5e0c-46b9-88b9-0cde729c38ca)

#### Destination Quiz (rango-query.js)

I wrote the quiz function - the main element of our site - using jQuery. The quiz is actually structured as a form with a hidden input tag that contains an empty value attribute. The quiz itself is composed of a series of four questions. The user has three options per round, one of which is entirely neutral. With each answer they click, a specific keyword is pushed to this empty value attribute, or no keyword if their answer is neutral. When the user then clicks on the "Find my holiday!" button at the end of the quiz, the string stored in the value attribute is then used as a "profile" to search the database of destinations and return a list of destinations. Each destination in our database has a specific combination of keywords, meaning that only those destinations containing these keywords will be returned and made visible to the user, i.e. destinations matching their profile. jQuery is used to update the value attribute with each question answered, to make use of delay times and fade-out functionalities, thus providing a great experience for the person taking the quiz!

![Screenshot 2022-11-04 at 13 46 00](https://media.git.generalassemb.ly/user/44781/files/7906422e-ec6f-46a0-bbbf-a999d47e2280)

![Screenshot 2022-11-04 at 13 42 33](https://media.git.generalassemb.ly/user/44781/files/653ab9e4-b22c-44b5-97b7-38b16dcfc5c5)

### Stage 8: Testing functions  

Testing functions along the way is how we managed to stay on track for delivery and ensure we minimised the risk of bugs. We used a lot of console.logs to capture the information we were generating and see what extra code was needed to achieve the functionality we wanted. We also got the other members of our team to test our code and look through it to make sure we didn't miss anything critical.

### Stage 9: Styling  

We knew from the start that we wanted our site to be responsive, simple, clean and easy on the eyes. We drew inspiration from Skyscanner, Trip Advisor and other sites to style our website, with destinations presented as cards: 

![Screenshot 2022-11-04 at 13 40 17](https://media.git.generalassemb.ly/user/44781/files/c61d0b1e-8965-401e-b3af-7a8081f9cd3e)

When all destinations are displayed on the **destinations/index.html**, we first start with a div that has the classes of **"row card-group"**. A separate **card** div is then created for each destination, containing the destination image, name, review, and other details:

![Screenshot 2022-11-09 at 10 30 31](https://media.git.generalassemb.ly/user/44781/files/6300fc11-9b16-470b-ab9c-8c5d082c7d86)

Providing feedback as a team, our teammate who focused on styling the site to make it fully mobile responsive when the width of 428px is reached:

<p float="left">
<img width="335" alt="Screenshot 2022-11-08 at 20 52 01" src="https://media.git.generalassemb.ly/user/44781/files/f232c29e-7e8c-428d-8be2-ef22c06059c7">
<img width="337" alt="Screenshot 2022-11-08 at 20 51 35" src="https://media.git.generalassemb.ly/user/44781/files/7a329af5-598f-402f-9375-c2e39e6420cb">
</p>

This means e.g. that the two divs that make up our quiz are displayed one above the other instead of side-by-side on a computer, and the font size is reduced to fit within the respective divs throughout the site:

<img src="https://media.git.generalassemb.ly/user/44781/files/e58aca6a-cf6f-47ed-8ed9-ee749e87e259" height="500" width="250">

### Stage 10: Testing the site  

We tested our quiz repeatedly to adjust timings and fadeouts, and tested the destination list, user signup, profile creation and API calls to make sure these were all working the way we wanted.

![Screenshot 2022-11-04 at 13 41 37](https://media.git.generalassemb.ly/user/44781/files/148b7553-02d5-4f75-b102-8b532450e3be)

### Stage 11: Bonus features  

The development of our project went so well that we were able to add additional functionality, such as the option for users to leave a review on destinations they have visited before. A form is shown to users on the detail page for the individual destination. Here users canleave a review on a destination:

![Screenshot 2022-11-08 at 19 24 36](https://media.git.generalassemb.ly/user/44781/files/d9e89c66-d0a4-44e7-a914-a8479bf03c97)

When they click submit, the **add_review** API is triggered and information in the form is captured and validated against the review form model:

![Screenshot 2022-11-08 at 19 51 14](https://media.git.generalassemb.ly/user/44781/files/fc8ec83f-7857-4be2-9edf-c35e10751ec9)
![Screenshot 2022-11-08 at 20 28 34](https://media.git.generalassemb.ly/user/44781/files/b8cc8724-44d0-4ae9-8e6e-6cc0e6f31d1e)

If the content is valid according to the structure of the Review model, this is saved in the database as a new review and then listed on the individual destination.

## Challenges

We had a hard time with the search functionality of our app, but were able to get this working after extensive trial and error. We also found adding star ratings to be quite a challenge, and after testing several different methods to no success, came up with a solution that worked for us. We were also hampered by the number of API calls we could make to our 3rd party weather API, with just 50 calls permitted a day.

### Problem-solving  

We worked well as a team at investigating and resolving bugs as they came up. We maintained constant communication to resolve errors, and if teammates were currently too busy working on a specific functionality, I took the initiative as team leader to do additional research to resolve the bugs we were encountering. We went through each line of code one at a time to identify where issues were occurring and exactly what information we were getting back. I kept a log of all errors as they occurred so we could track issues and resolve them in a timely manner.

## Wins

The fact that our project is fully responsive is a big win:

<p float="left">
<img src="https://media.git.generalassemb.ly/user/44781/files/22f223c0-eda3-4bea-86b6-9c34ac12366a" width="300" height="600" >
<img src="https://media.git.generalassemb.ly/user/44781/files/443edb29-3c53-4cc2-a6cc-ba4c7c88c4eb" width="300" height="600" >
<img src="https://media.git.generalassemb.ly/user/44781/files/6269cc84-9ca8-4fc3-b93f-f0207ac7f148" width="300" height="600" >
</p>
                                                                                                                            
I'm also very happy that with just a week or so of Python under our belts, we were able to produce an app of this caliber. I personally struggled with adjusting from JavaScript to Python in the beginning stages, but working with my team to build an app we could be proud of and resolving issues along the way, my confidence in the language grew and I am very proud of the product we were able to deliver.
                                                                                                                            
## Key Learnings & Takeaways

This project taught me that working in a team can be fun and seamless when you establish your criteria and process clearly from the outset. We worked so well as a team that our communication was always effortless, productive and led to us resolving issues collaboratively in a very short time. Although I personally prefer JavaScript, I learned that I can do a lot with Python, and this project gave me a much better understanding of the language. I feel more confident using Python after implementing it on this project.

## Bugs

Heroku periodically deletes images, so some images such as profile photos will not display properly. This could be rectified by using Cloudinary for image storage rather than using Multer.

## Future Improvements

In future versions of Django Djourneys, I want to allow users to be able to add destinations - subject to approval by an administrator. These would require checking to ensure multiple versions of the same destination do not get added to the database. I would also add in forwarding to e.g. Skyscanner to allow users to check and book flights to the destination of their choice.
