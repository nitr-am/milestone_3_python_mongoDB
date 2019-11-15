# My online reading History

## [Project Demo, my online reading history](https://my-online-book-reading-history.herokuapp.com/).

This is my online books reading history. Here I can add all the books I am reading, and that I am going to read. I can add some details about the books, like the genre, date of puclication, how much did I liked it and some comments about it.
This will be very usefull because many times we forget the books we read, and as they are precious for me I want to have them somewhere and being able to consult them anytime.
This is good also because I can keep count of the books I read. 

## UX

This project is intended to people who have interest for the world of books and are interested on keep a record of the books they read and their perception of the the book in matter at the moment. 
I opted for a single page document to visualize the books in a list because I am only intersted on watching the book title and its author at a first glance, and then my review about it. I think the users will need the same if they want to keep a record of the books they read. 
In the main page the users will see the books as a list in a simple way because is the only thing that matters. The simpler the better. 
There is a navigation bar at the top in which we can find all the functionality of the appliation. Add a new book, update an existant one, look the different generes, modify them, and add some new ones. 

As a User I would want:

- To easily view all the books in a list. 
- To see the most relevant information of the book as a first glance. 
- To easily add a new book I recenly read. 
- To easily modify any book.
- To easily have access to the review I make of a book. 
- To easily delete any book. 

I took the structure of my project from a project done prior to this one in the Code Institute topic related on how How Python Talks to Data from the "*Interactive Frontend Development*" unit. It was a very good inspiration for me because it had all what I wanted for my project. 
The use of python language in a combination with databases usage coming from MongoDB. 
It was a challenge for me, but at the end it was highly rewarding as well because I feel I complitely understood wverything I did and for me that is the most imporant thing. 

#### Wireframes:

The wireframes for the application were done using Balsamiq:

- [Main page](/wireframes/main_page.png/)
- [Add Book](/wireframes/add_book.png/)

## Features

This application is simple. That is what is needed. Plane, easy to read and to use. 

### Existing Features
The application was done with the intention to use the CRUD Operations learned with Code Institute which are essential when working with data.

* **Navigation bar:** This is the menu and the center of operations for the app. From here, it is possible to add a new book, to go and see all the books I have read, to see the generes of the books I have read, to add more generes. 
* **Add a new book:** This allow the user to create a register. To add a new book to the list. 
* **See the currently read books:** This is the main page in which the user see all the books in the form of a list. 
* **Delete button:** It allows the user to delete an existan register (book).
* **Edit button:** If the user want to change the information of an existant book he/she can do it by clicking on the "edit" button. It will redirect the ser to a page in which changes can be done. 
* **Adding/modifying Genre:** In books genere is important and most of them can be clasified in a short list of generes. There is a predefined list but it can be modified as the taste of the user. 
* **Adding a score:** For ease of use there is a list of predefined numbers to demonstrate how the user liked a book. List rnges from 1 to 5. 
* **Write a review:** There is the possibility to write a review of the book as well as edit it. 

#### Features Left to Implement

There is still to be done a filter by genre books search. 

## Technologies Used

The technologies used for the development of the project so far are: 
- HTML: to edit the content.
- Python: to create my back-end application which connects with the server. It "GET" and "POST" the needed data.
- Javascript: To give interactivity to the project. 
- Jquery: As a Javascript library to help with the interactivity. 
- [Materialize](https://materializecss.com/about.html): This is a Google created tool to give shape to the application. From it I took icons, the navbar and the general structure of the pages. It was also use to get the mutability among the diffferent screen sizes. 
- [gitpod](https://www.gitpod.io/): As an online IDE to integrate all the resources and facilitate the development of the project. 
- [GitHub](https://github.com/): As online repository and for version control. 

## Testing

The process of develpment of this web page has passed through a series of test of its funcitonality. 

The use of Materialize has facilitated things. All the content has been developed with the intention to fit all the screens sizes available, since mobile phones to computer screens. 

The site has been viewed in different browsers such as Safari, Chrome, Firefox, Edge and Explorer and screen sizes proper of tablets and mobile phones. 

#### Client stories testing:

 - A user will immediately know what the web page is about.
 - The user will immediately get the list of the books read as that is the only intention of the application.
 - The user will immediately know how to use the app. Add books, modify them and delete them. 

#### Testing of functionality:

The project has been tested in different screen sizes, like mobile phone, tablet and desktop size.

- The application needed to be as simple as possible and as easy to use as possible as is not for sharing, is only for personal use of highly motivated readers. 
- It needed to have a "edit" and "delete" buttons next to each book and both buttons was decided to look as flat as possible because the only thing that matters in the page are the titles of the books. Both buttons were tested on receib¿ving the desired outcome of each.
- "Delete" button works fine, it deletes an existant book taking it out of the lists.
- "Edit" button takes the user to a differet page in which predefined values appear but can be modified. 
- An exapand for more button needed Javascipt to work, was properly tested. It shows the review of the book in a drop-down manner. 
- The add new book page was tested and it allows the user to fill all the blank spaces and then when the "Add Book" button is triggered it takes the user to the main page showing the recently added record. 
- The book genres page shows the exitant genres and allows the user to also, edit, delete and add new genres. 

## Deployment

This project was developed firstly based of a [Code Institute](https://codeinstitute.net/) [template](https://github.com/Code-Institute-Org/gitpod-full-template) to be able to work with data using the [Gitpod](https://www.gitpod.io/) IDE, committed to git and pushed to [GitHub](https://github.com/) online repository throughout a built in Gitpod function so everybody get access to it.

To find the repository for the project on GitHub, please follow this link: https://github.com/nitr-am/milestone_3_python_mongoDB

### Heroku 

My project is deployed on [Heroku](https://www.heroku.com/) platform and can be viewed at the following link: https://my-online-book-reading-history.herokuapp.com/

To deploy this project to Heroku, the following steps were taken:

1. Go to the Heroku Website and create new app
2. Create requirements.txt to tell Heroku what dependencies need to be installed.
3. Create a Procfile to tell Heroku what type of app is it.
4. Scale Dynos to help Heroku run the application.
5. Login into Heroku Account via command line and push the project from there. 
6. Go back to Heroku Website and in the settings option click Reveal Config Vars and manage IP and PORT vars. In my case IP = 0.0.0.0 and PORT = 3000. 
7. Go to and click on "Open App" button. 

## Credits

#### Aknowledgements

Thank you to Code Institute, they thaught me to work with Python, to use MongoDB and to mix them together. Thanks to the instructions videos from thheir Ful Stack Web Developer course that allowed me to learn all this, hence allowed me to develop this project from which I am very satisfied for. 
