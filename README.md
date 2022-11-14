# SEI Project 3 Django Djourneys

![Screenshot 2022-11-04 at 13 36 24](https://media.git.generalassemb.ly/user/44781/files/ac47f2d6-d2d4-4e8a-b70d-e2e896eedb71)

## Project Overview

The objective of this project was to create a web application with Python using the Django framework. The timeframe for this project was a week and it was completed in a group of three.

## Brief

Goals
- Create the application using at least 2 related models, one of which should be a user
- Manage team contributions and collaboration using a standard Git flow on GitHub
- Include all major CRUD functions for at least one of your models
- Add authentication AND authorization (page protection) to restrict access to appropriate users
-   User must be able to sign up or login
-   Signed in user must be able to change password and logout
-   Change password and logout must only be available to logged in users
- Layout and style your front-end with clean & well-formatted CSS, with or without a framework
- Deploy your application online so it's publicly accessible

Stretch Goals:

- Allow users to change website theme, Dark mode etc.
- Include Pagination
- Utilise 3rd party APIs
- Send verification email upon registration
- Allow users to upload image files
- Password reset using an email

## Deployment Link 
Visit Django Djourneys [with this link.](https://djangodjourney.herokuapp.com/)
Take the quiz to find your ideal holiday or freely browse 250 destinations!

## Code Installation
Django Djourney has no installation requirements, simply visit the Heroku app and create an account or take the quiz!

## Technologies Used 
- Python
- HTML5
- CSS3
- Django Framework
- PostgreSQL
- Multer
- Heroku

## Development Process

### Stage 1: Planning
The first stage consisted of brainstorming ideas for the project, setting up the Git repository and creating a Trello board to manage tasks. [Here is a link to the Trello board.](https://trello.com/b/OvjiXE35/project3-django-djourney)

As a group we decided on a holiday destination app. Taking inspiration from the Penhaligon website's fragrance quiz, we thought it would be a great idea to incorporate a quiz that would suggest holiday destinations based on the user's preferences. 

With the idea in mind, we created an ERD to establish the model relations of the app and wireframes to get a picture of how we wanted everything to look. These were created on Figma which you can view [here](https://www.figma.com/file/W85hBPu2LqPGj9Sj0xfmJD/Django-Djourney?node-id=0%3A1).

We then wrote out user stories to outline all the features we wanted to include in our app:
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

### Stage 2: Starting the build

With our functionalities in mind and our ERD and wireframes completed, we were ready to start building the app. We started by creating the templates, base.html being the base template for the site where we imported 3rd-party APIs, jQuery, fonts and Bootstrap. 
We all then created PostgreSQL databases in PGAdmin, for which the settings were configured in settings.py. 

### Stage 3: Features and functions

At this point, we split the workload between the three members of the team:
- I would work on the search function and APIs for displaying destinations.
- One teammate would work on user accounts and profiles, destination data and the quiz.
- One teammate would work on user reviews and ratings, styling and 3rd-party APIs.

A teammate found a spreadsheet of 250 destinations and edited it to include a 'Name' field, which I followed up on by adding the 'Country' and 'Keywords' for the individual destinations. 

![Screenshot 2022-11-08 at 16 15 03](https://media.git.generalassemb.ly/user/44781/files/b68386f6-8bda-490a-b160-9332774edbdd)

Once we had the necessary fields and information, the team leader exported the spreadsheet as a .csv file and imported it into our PostgreSQL database.

![image](https://media.git.generalassemb.ly/user/44781/files/36b5a76c-e040-4c37-b61f-04e0509b4abf)

Now that we had our database, I could start my work on the destinations index and search functionality. I first created the search box in index.html:
```
{% extends 'base.html' %}

{% block content %}


<div class="page">
    <h1 class="page-title">All Django Djourneys Destinations</h1>

<!-- SEARCH BOX -->
    <div class="search-div">
        <form method="POST" action="{% url 'search' %}" class="d-flex">
            {% csrf_token %}
            <input type="search" placeholder="Search by Country" class=" text-field" aria-label="Search" name="searched">
            <button type="submit" class="submit-button">Search </button>
        </form>
    </div><br>
    
<!-- END OF SEARCH BOX -->
```

I went on to create a separate template for the search filter results which contained a conditional to check for 'searched'. If this was fulfilled, the page would display the filtered results:
``` 
{% extends 'base.html' %}
{% load static %}
{% block content %}
{% if searched %}
<h1>You Searched For {{ searched }}</h1>
<br>
<div class="row card-group">
    {% for country in countries %}

```
I then created an API that would retrieve the input of the search box after the search button was pressed and compare it to the countries in the database. If there was a match, the cards for the destinations with that country would be displayed. I had to make sure to capitalize the input so that it would precisely match the country names we had in the database:
``` 
def search(request):
    if request.method == 'POST':
        searched = request.POST['searched']
        searched = searched.capitalize()
        countries = Destination.objects.filter(country__contains=searched)
        return render(request, 'search.html', {'searched': searched, 'countries': countries})
    else:
        return render(request, 'search.html')
```
Here's an example of the search filter in action:
![image](https://i.imgur.com/vHnFGXC.png)

I also worked on creating the 'add review' functionality, which was protected by @login_required to ensure that only signed up users could access the feature. This involved creating a review model, writing an API and then displaying the reviews on the destination detail template.
API:
```
@login_required
def add_review(request, destination_id, user_id):
    print("add_review")
    form = ReviewForm(request.POST)

    if form.is_valid():
        new_review = form.save(commit=False)
        new_review.destination_id = destination_id
        new_review.user_id = user_id
        new_review.save()
    return redirect('detail', destination_id = destination_id)
```
Model:
```
class Review(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    title = models.TextField(max_length=30, default="")
    rating = models.FloatField()
    destination = models.ForeignKey(Destination, on_delete=models.CASCADE)
    content = models.TextField(max_length=300)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.title} on {self.created_at}"

    class Meta:
        ordering = ['-created_at']
```
Outcome:
![image](https://i.imgur.com/S85tuki.png)

The next major step in the project was creating the quiz. My teammate worked using jQuery in the rango-query.js file to create the quiz animations and store the results, and I helped with fetching the suggested destinations based on the results of the quiz. Each selection in the quiz was stored in a list keywords, and I used the .filter Python method to return countries that had the same keywords stored in the database. In order for the quiz to always provide suggestions, I had to ensure that there was at least one instance of each possible combination of keywords in the database for the 250 destinations. 

```
def destinations_index(request):
if request.method == 'POST':
        results = request.POST['results']
        print(results)
        resultsList = results.split()
        query = ""
        print(query)
        countries = Destination.objects.filter(reduce(operator.and_, (Q(keywords__contains=x) for x in resultsList)))
        print(countries)
        return render(request, 'results.html', {'searched': results, 'countries': countries})
else:
    destinations = Destination.objects.all()
```
### Stage 4: Testing and styling

Throughout the creation of the application, everyone in the team was constantly testing the features to check that everything was operating as it should be. This allowed us to stay on top of our progress in getting the site to function. When we encountered bugs, we collectively approached the issues and used a lot of print / console.log to pinpoint which information was missing, pointing us to where we were making mistakes. 

In terms of styling, we wanted our site to look clean and for it to be fully mobile responsive. Our teammate that focused on the styling was frequently consulting us for feedback and did a fantastic job of making the site look great- especially on mobile. 

### Bonus features / stretch goals 

Two features that we were really happy with were both 3rd-party APIs that displayed the local weather of the destination and a map. Openweather was used for the weather API and Google Maps for the map API.
![image](https://i.imgur.com/mWLScEa.png)

## Challenges

The search functionality, while appearing concise in its final form, was definitely a huge task for me. Considering it was my first project using Python, I had to read a lot of documentation and work together with my teammates to find a solution through a lot of trial and error. 

## Wins 
Having a fully functioning quiz that actually tailors destinations to the combination of answers given by the user was a massive win. It took a lot of communication and cooperation between the whole team to get that working, and I'm very proud that we made it happen. 
Having a week to create an app with Python was a daunting task for me as I had been used to JavaScript at that time, and learning Python from scratch was frustrating at times. However, with practice and consistency my confidence with Python grew significantly in a short time, and I really appreciate the language's ease of comprehension and utility now that I have a better grasp of it. 

## Key Learnings
I was very pleased with how well my team worked together, from delegating roles evenly to providing feedback and cooperating with eachother on tasks where we needed eachother's help. It showed me that establishing a clear plan and engaging in meaningful communication is key to a successful team. 

This project was a great introduction to Python for me and massively improved my understanding of the language. From this I learned that getting stuck in and creating applications, even if you initially feel out of your depth, is the best way to learn a new language and framework. 

## Bugs
Heroku deletes images after a certain period of time, meaning that profile pictures in the app aren't currently displayed. This could be solved by using a different platform for deployment or another tool for image upload such as Cloudinary.

## Future Improvements
For each destination, I would like to add a feature that redirects users to another website where they can check flights / travel such as Google Flights or Skyscanner.
