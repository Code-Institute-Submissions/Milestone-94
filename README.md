# Books

 On this site users can upload and review books they have read, which will show up on their profile page.

## Live demo on Heroku pages [HERE](https://milestone-3-project-daniella-m.herokuapp.com/)

## UX

### User Stories


- As a user, I want to easily register to the site.
- As a user, I want to easily log in to my account.
- As a user, I want to easily log out of my account.
- As a user, I want to easily edit or delete the books I uploaded.
- As a user, I want to easily upload and review books.
- As a user, I want to easily navigate around the site. 


### Wireframes

The wireframes were made using [Balsamiq](https://balsamiq.com/).

[Wireframes](https://github.com/DaniellaMinyo/Milestone-3/blob/master/static/milestone3.pdf)


## 2. Features

### 2.1. Existing features

1.  Navbar

- with a brand and home link that both take you to the home page.
- with a category dropdown menu where you can browse books by category.
- with a profile page, which shows all the books uploaded by the user.
- with a new book link, where users can upload a new book.
- with a logout page, when clicked logs out and takes you to the login page.
- with a login and register link visible when the user is loged out.

2.  Home page.

- Displayes the newest 3 uploaded books from each category.


3. Single_book page

- displays the book clicked on.

4.  Categories page

- displays the books from the category chosen in the dropdown menu.

5.  Profile

- displays all the books uploaded by the user.

6.  New book

- upload a new book.

7.  Login

- login to your account.

8.  Register

- register to site.

9. Edit and Delete buttons

- buttons on books uploaded by the user.


### 2.2. Features to implement

- Wishlist
- Review and add to profile books uploaded by others
- Admin being able to edit and take down books uploaded by other users
- Admin being able to add new categories.


## Technologies Used

- [GitHub](https://github.com/) - was used to host the project.
- [Gitpod](https://www.gitpod.io/) - IDE used.
- [Vscode](https://code.visualstudio.com/) - was used to develop the website.
- [Balsamiq](https://balsamiq.com/) - was used to create the project's wireframes.
- [HTML5](https://en.wikipedia.org/wiki/HTML5) - provides the structure and content for the site.
- [CSS3](https://en.wikipedia.org/wiki/Cascading_Style_Sheets) - provides the styling for the site.
- [Balsamiq](https://balsamiq.com/wireframes/) - Wireframes.
- [Js](https://en.wikipedia.org/wiki/JavaScript) - was used to add functionality.
- [Bootstrap](https://getbootstrap.com/) - was used to create the layout for the site.
- [Python](<https://en.wikipedia.org/wiki/Python_(programming_language)>)
- [jQuery](https://jquery.com/) - JS library.
- [MongoDB](https://www.mongodb.com/) - Database program.
- [Heroku](https://www.heroku.com/) - for deployment and running of apps.
- [Flask](https://flask.palletsprojects.com/en/1.1.x/) - Python web framework.


## Testing

## Code Validators

#### [HTML validator](https://validator.w3.org/)
-  When checked with validating by url no errors popped up.

#### [CSS validator](https://jigsaw.w3.org/css-validator/)
- One error found : 'Value Error : color none is not a color value : none', easily fixed by deleting value.

#### [JS validator](https://jshint.com/)
- No js used.

### [Python validator](http://pep8online.com/)
- a single error : continuation line with same indent as next logical line, rearranged code to solve issue.

### Responsiveness
- Galaxy S5 - Good
- iPhone 5/6/7/8 - Good
- iPad - Good
- iPad Pro - Good
- Desktop 1024px - Good
- Desktop >1200px - Good

### Browser compatibility
- Chrome: Responsiveness, Appearance and Functionality- Good
- Safari: Responsiveness and Appearance and Functionality- The appearance and responsiveness is good but it does not function properly.

### Bugs

- Issue: footer jumps up the page on some pages in certain sizes. Fix: add a min-height with calc to the main container.
- Issue: search bar doesn't work. Fix : Created a new search.html page where search results will be shown and changed the return template in app.py.


## Deployment

###  Create Project
- To create this project the [Gitpod Full Template](https://github.com/Code-Institute-Org/gitpod-full-template) was used to create a new repository.
- Then in my new repository on GitHub, I clicked the Gitpod button which built my workspace.

### Deployment to Heroku
This project is deployed and hosted on [Heroku](https://www.heroku.com/).
- Go [Heroku](https://www.heroku.com/) and login.
- Click on the 'New' button and select 'Create new app'.
- Enter the app name and select a region.
- IN'Settings' tab, click on 'Config Vars' to add Configuration Variables from the env.py file.
- In the menu select Deploy.
- In 'Deployment method' select GitHub to connect to your repository. Select your GitHub username and repository.
- Select Automatic deploys from the main branch.
- Click deploy branch.

Running the project locally

- First you must clone this project.
- Under the menu click on the Code dropdown menu.
- In the https section, copy the url.
- In your local terminal open Git Bash.
- Change your working directory to the one where you want to clone the directory.
- Type in git clone and then paste in the url you copied.
- Then just press enter.

## Credits
### Media
- The images, decriptions, and reviews all taken from [Goodreads](https://www.goodreads.com/)

### Code
- Code used from mini project- putting it all together, to which I made modifications according to the users needs.
- I took a lot of inspiration from https://www.w3schools.com/.

## Acknowledgments
- Thanks to all Code Institute staff.
- Thanks to Slack Community.