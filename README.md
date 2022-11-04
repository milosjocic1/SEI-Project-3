# Project 3 - Django Djourneys

## Description

This project was assigned at the end of the eighth week of General Assembly’s 3-month SEI (Software Engineering Immersive) course, which teaches people who don't how to code the basics of software engineering with a view to launching a career in the tech sector. The aim of this project was to design an app in Python using the Django framework over the course of one week. This project was a group project together with two other students on the course.

## Deployment link

[You can find Django Djourneys deployed on this link](https://https://djangodjourney.herokuapp.com/). Take the quiz and see where your next journey should take you!

## Getting Started/Code Installation

### Instructions

#### Deployed app

There are no specific installation requirements for this app since Django Djourneys runs in the browser. Simply create an account or take our four-part quiz to get started!

## Timeframe & Working Team

We worked as a team of three over the course of a week to deliver this project. We split tasks equally to ensure we were all contributing to the project at the same level. We were an especially effective team on this project! I took the lead to manage the project and track tasks to ensure we remain on target for delivery.

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

- Allow user to change website theme, Dark mode etc.
- Include Pagination
- Utilise 3rd party APIs
- Send verification email upon registeration
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

We agreed as a team that I would take the role of team leader, so I made sure from the outset that we followed a clear development and task tracking process in order to ensure we could hit our goals to deliver the minimum viable product on deadline, and give ourselves additional time to focus on styling touches, stretch goals and presentation day. I took an active role in managing team members and tasks, maintaining ongoing communication with my teammates via Slack and Zoom to ensure we all stayed on target with tasks and could resolve any issues or bugs constructively and in a timely manner.

### Task management  

In order to create, assign and manage tasks, I created a public Trello board which all of the members of our group could access. This made working on our project much easier and allowed us to work more effectively as a group. We reviewed the Trello board each day to assign tasks, mark them as completed and create any additional tasks as required to keep track of these. You can find the link to our Trello board [here](https://trello.com/b/BjeZaJ0E/rate-my-cat).

![Screenshot 2022-09-09 at 12 46 53](https://media.git.generalassemb.ly/user/44781/files/518d6b93-92a0-493b-8d0a-33add6ebed95)

## Build/Code Process

Documented below are the stages we went through in order to build the code for our project.  

### Stage 1: Brainstorming  

We started by brainstorming ideas for our app. Initial ideas included a World Cup 2022 match fixture tracker, a sports venue booking system and one or two other ideas related to sporting events. After some initial research, we decided to rule these out and went with our final, very appealing idea.

### Stage 2: Pick an idea  

My team were all quite ready for a holiday and yaking inspiration from the perfume brand Penhaligon's website, where users can take a test to build a "fragrance profile" and be matched to the best fragrances for them, we thought: "Wouldn't it be great if you could have an app that tells you what your next holiday destination should be?". The idea struck a chord with all of us and we decided to build a quiz that users can take to be matched to a list of potential holiday destinations.

### Stage 3: Wireframe, ERD and user stories  

#### ERD

We began with an ERD to map the relations between our models.![ERD](https://media.git.generalassemb.ly/user/44781/files/55fa7e93-19d9-4dfb-b55b-47b5267fdbeb)

#### Wireframes

We then began working on wireframes to visualise how our site would look page by page.
![image](https://media.git.generalassemb.ly/user/44781/files/b74fb9d7-4015-44e2-a1ff-7e5db2c2a89b)
![image (1)](https://media.git.generalassemb.ly/user/44781/files/f34d814c-8202-4982-a4c3-3d3be94fb3e6)
![image (2)](https://media.git.generalassemb.ly/user/44781/files/4d5d79f6-4512-4ffa-bba8-0dcdb1788710)
![image (3)](https://media.git.generalassemb.ly/user/44781/files/c1177570-61e3-47c5-be71-fbfad99c0b06)

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

### Stage 4: Creating Git repo and starting files  

As team leader, I took charge of initial file and folder setup, first creating a repo on Git for our project, then laying out the basic file and folder structure for our models, controllers, routes and views. I also created the database which would store our information on mongoDB.

### Stage 5: Requirements  

We got together as a team to define the basic requirements for our site. We wanted the user to:

- be able to create an account where they could upload an image of their cat and then
- submit this to be rated by other users
- have a leaderboard of the most popular cats
- with an average rating taken from the sum of all of their previous ratings
- show cats by location
- have the functionality to delete a cat
- or add a cat/change their cat

### Stage 6: Basic layout  

After we established the main functionalities we wanted from our app, we began working on the basic layout. We wanted the user to be greeted by a welcome page, with links to an About Us page, a joke Disclaimer page, and a page with a little bit more info about us and the project.

![Screenshot 2022-11-04 at 13 36 24](https://media.git.generalassemb.ly/user/44781/files/ac47f2d6-d2d4-4e8a-b70d-e2e896eedb71)

### Stage 7: Structuring logic and working on functions  

I worked specifically on creating and adding cats to users who had been signed up to the site. I created the model, controllers and routes for this, and made sure to populate each instance of a cat with the appropriate user information so we could see who the cat belongs to! I then hooked this up to the leaderboard functionality, which I built by creating a list of cats displayed by average rating.

### Stage 8: Testing functions  

We tested functions repeatedly as we went along and got each other to test these to ensure we weren't missing any bugs. We iterated through functions a few times to get them just right before implementing them in the master branch.

### Stage 9: Styling  

We went through several iterations of our website, building on the style as we went, before we settled on the final version. We decided to go for a look that was fun and friendly - we're talking about rating cat pictures after all! - that would be welcoming to the user. We experienced a lot of issues with conflicting CSS rules in order to get the website mobile responsive, and managed to resolve all of our conflicts here just in time for presentation. Future iterations would make more use of media queries in order to avoid any conflicts when swtiching between computer and mobile.

![Screenshot 2022-11-04 at 13 40 17](https://media.git.generalassemb.ly/user/44781/files/c61d0b1e-8965-401e-b3af-7a8081f9cd3e)

### Stage 10: Testing the site  

With our site finished, we made sure to through each page and function to make sure everything worked well. We had enough time before delivery toi be able to do this, and it meant we were able to fix slight issues in e.g. the way elements displayed or functions affected elements on the page.

![Screenshot 2022-11-04 at 13 41 37](https://media.git.generalassemb.ly/user/44781/files/148b7553-02d5-4f75-b102-8b532450e3be)

### Stage 11: Bonus features  

We achieved a few of our bonus items by adding an About Us page which gave details on our team as wella s links to our personal Github repos, as well as our Ailurophiles link, which displays a list of other users to users who are logged into the site. 

## Challenges

We originally wanted to include a location functionality that would let users see cats in other areas, displayed on a map. We realised that we didn't have enough time in the process to allow us to include this, so we decided to leave this functionality out entirely and focus on getitng our core functionalities up and runnign perectly. Creating the leaderboard was also a big challenge since I had a difficult time getting the cats to display properly in descending order of average rating.

### Problem-solving  

When it came to solving issues, I was proactive in identifying and helping with issues as they arose. I made sure to keep a list of all current bugs and issues so we could keep track and address these one by one as time allowed. If a team member was having an issue or encountering a bug, I made sure we communicated and addressed this together with a "two heads are better than one" approach, and appropriate console.logs to pinpoint the issue precisely. I made sure we didn't each spend too long trying to fix errors, and instead got teammates to share their screen so we could talk through the code together. On several occasions, we identified the issue almost immediately after sharing screens and were able to fix the issue quickly, e.g. a delete button that wasn't working, which I saw was due to the fact that the text within the button had been set to trigger the function instead of the button itself.

## Wins

The fact that our project is fully responsive is a big win:

<img src="https://media.git.generalassemb.ly/user/44781/files/6269cc84-9ca8-4fc3-b93f-f0207ac7f148" width="300" height="600" />
<img src="https://media.git.generalassemb.ly/user/44781/files/f5e03ae1-bb6e-45d5-8db9-f10430cc78b1" width="300" height="600" />
<img src="https://media.git.generalassemb.ly/user/44781/files/443edb29-3c53-4cc2-a6cc-ba4c7c88c4eb" width="300" height="600" />

### Favourite functions

#### Destination Quiz (rango-query.js)

My favourite function above all has to be the quiz function - the main element of our site - which I wrote using jQuery. The quiz is actually structured as a form with a hidden input tag that contains an empty value attribute. The quiz itself is composed of a series of four questions. The user has three options per round, one of which is entirely neutral. With each answer they click, a specific keyword is pushed to this empty value attribute, or no keyword if their answer is neutral. When the user then clicks on the "Find my holiday!" button at the end of the quiz, the string stored in the value attribute is then used as a "profile" to search the database of destinations and return a list of destinations. Each destination in our database has a specific combination of keywords, meaning that only those destinations containing these keywords will be returned and made visible to the user, i.e. destinations matching their profile. jQuery is used to update the value attribute with each question answered, to make use of delay times and fade-out functionalities, thus providing a great experience for the person taking the quiz!

![Screenshot 2022-11-04 at 13 46 00](https://media.git.generalassemb.ly/user/44781/files/7906422e-ec6f-46a0-bbbf-a999d47e2280)

![Screenshot 2022-11-04 at 13 42 33](https://media.git.generalassemb.ly/user/44781/files/653ab9e4-b22c-44b5-97b7-38b16dcfc5c5)

#### Destination Quiz (rango-query.js)

#### Leaderboard sorting

This code sorts the cats in descending order of average rating. Since this was early on in my development as an engineer, it felt like a hard task at the time, but now seems so easy by comparison!

![Screenshot 2022-11-02 at 16 36 13](https://media.git.generalassemb.ly/user/44781/files/79e6328c-5a12-4321-9f92-9cbe5f5e14cb)

## Key Learnings & Takeaways

This project taught me that communication between team members really is key to the success of a group project. In order to resolve issues promptly, it is essential to keep talking to the others on the team about what you're doing, when you're doing it, the issues you encounter along the way, and most importantly - to ask for help! It's also extremely important to ensure that if you're working in the same files, you tell each other what you're doing, and if necessary, create a separate branch on your local repo to work on individual updates and functionalities/features, then merge this into your development branch before pushing and opening a pull request. This avoids conflicts in the main development branch and potential merge issues, something we dealt with a lot in the early stages.

I also learned that I actually enjoy managing a (smnall) team of devs and handling management of a project! It was strange at first, but having been my own boss for a decade and having to manage translation projects - some of them quite large and working with up to 10 other translators - I found my skills readily transferred across to software engineering and the development process went well as a result.

## Bugs

At present the only bug is that our user information table does not fit neatly in the main body on mobile, but spills over.

## Future Improvements

In future iterations of Rate My Cat, I would want to add the location functionality so users can view cats in their area or another location, along with the average rating for the cats. This would be displayed on a map which users can search.
