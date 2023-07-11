<h1 align="center">Babylicious Blog, a blog to share your recipies that you made with love for your baby</h1>

<p align="center"><img src="static/extras/amIresposive.png"
        alt="Babylicious Blog webpage on multiple devices"></p>

[Live Project Here](https://project-portofolio4-babyfood.herokuapp.com/)

# Babylicious Blog - Introduction

This project is a Full Stack website built using the Django framework. Babylicious Blog is a blogwith baby recipes where users can look, search or post a recipe for their baby. When the user is logged in they can also like/unlike a post and comment on a post. They can also share their favourite baby recipies by adding a post and upload or update their user image and details.

README Table Content

- [Babylicious Blog - Introduction](#babylicious-blog---introduction)
  - [User Experience - UX](#user-experience---ux)
    - [User Stories](#user-stories)
    - [Agile Methodology](#agile-methodology)
    - [The Scope](#the-scope)
      - [Main Site Goals](#main-site-goals)
  - [Database Diagram](#database-diagram)
  - [Design](#design)
      - [Colours](#colours)
      - [Typography](#typography)
    - [Wireframes](#wireframes)
  - [Features](#features)
    - [Home Page](#home-page)
    - [About Page](#about-page)
    - [Post Detail Page - Top](#post-detail-page---top)
    - [Post Detail Page - Steps](#post-detail-page---steps)
    - [Post Detail Page - Comments](#post-detail-page---comments)
    - [Edit Comments Page](#edit-comments-page)
    - [Categories Page](#categories-page)
    - [Books Page](#books-page)
    - [Add/Edit Recipie Page](#addedit-recipie-page)
    - [Search Box](#search-box)
    - [Search Results Page](#search-results-page)
    - [Search Results - Input Empty](#search-results---input-empty)
    - [Search Results - No Results Found](#search-results---no-results-found)
    - [Signup Page](#signup-page)
    - [Login Page](#login-page)
    - [Logout Page](#logout-page)
    - [User Profile Page](#user-profile-page)
    - [Navbar](#navbar)
    - [Herosection](#herosection)
    - [Footer](#footer)
  - [Messages and Interaction With Users](#messages-and-interaction-with-users)
    - [Sign up](#sign-up)
    - [Login](#login)
    - [Logout](#logout)
    - [Profile Update](#profile-update)
    - [Like Post](#like-post)
    - [Unlike Post](#unlike-post)
    - [Comment Post](#comment-post)
    - [Comment Post - 2](#comment-post---2)
    - [Delete/Edit Comment](#deleteedit-comment)
    - [Delete Comment - 1](#delete-comment---1)
    - [Delete Comment - 2](#delete-comment---2)
    - [Edit Comment](#edit-comment)
    - [Email Sent - Success](#email-sent---success)
    - [Email Sent - Failed](#email-sent---failed)
    - [Add Book](#add-book)
    - [Edit Book](#edit-book)
    - [Delete Book 1](#delete-book-1)
    - [Delete Book 2](#delete-book-2)
    - [Empty Search](#empty-search)
    - [No Search Found](#no-search-found)
  - [Admin Panel/Superuser](#admin-panelsuperuser)
  - [Technologies Used](#technologies-used)
    - [Languages Used](#languages-used)
      - [Django Packages](#django-packages)
    - [Frameworks - Libraries - Programs Used](#frameworks---libraries---programs-used)
    - [Testing](#testing)
  - [Creating the Django app](#creating-the-django-app)
  - [Deployment of This Project](#deployment-of-this-project)
  - [Final Deployment](#final-deployment)
  - [Forking This Project](#forking-this-project)
  - [Cloning This Project](#cloning-this-project)
  - [Credits](#credits)
    - [Content](#content)
    - [Information Sources / Resources](#information-sources--resources)
  - [Special Thanks](#special-thanks)

  ## User Experience - UX

### User Stories

* As a website user, I can:

1. Navigate around the site and easily view the desired content.
2. View a list of recipes for babies and choose accordingly.
3. Search recipes to find specific recipes.
4. Click on post to read the recipe details.
5. Register for an account to avail of the services offered to members.
6. View the number of likes on a recipe.

* As logged in website user, I can:

1. Like/unlike recipes I enjoyed.
2. Comment/reply on recipes and give my opinion about the posts.
3. Delete my previous comments.
4. Manage my profile by updating my details and user image.
5. Share my favourites recipies by posting them on the Page.
6. Edit my favourite baby recipies posted previously.
7. Delete my favourite recipies posted previously.
8. Logout from the website.

* As a website superuser, I can:

1. Create and publish a new recipe.
2. Create a new user, recipes and categories.
3. Delete user, recipes, categories and comments.
4. Edit user's favourite recipies that was posted previously.
5. Delete user's favourite recipies that was posted previously.

### Agile Methodology

All functionality and development of this project were managed using GitHub which Projects can be found
[here](https://github.com/ionelaSabinaMacovei/ProjectPortofolio4-Babyfood/issues)

### The Scope

#### Main Site Goals

 * A simple, straightforward, intuitive UX experience;
 * Explicit content;
 * An easy navigation for the user through all the pages and features;
 * A site that is visually appealing on all screen sizes.

## Database Diagram

![Database Diagrama](static/extras/Database.png)<br>

## Design

#### Colours

![Colours Palete](static/extras/colors-pallete.png)<br>

* The colour scheme that inspired me to develop this layout for the website.

#### Typography

* The Comic Neue font is used as the main font for the whole project.

### Wireframes

Wireframes for this project can be located [here](WIREFRAMES.md)


## Features

### Home Page

![Home Page](static/extras/features/home-page.png)

* On the home page the  users can see a selection of 6 recipes, the navbar and 7 dropdown images which give to the user informations about each categorie .<br>

### About Page

![About Page](static/extras/features/about-page.png)

* The About Page gives, users information about the Babylicious Blog website. It introduces the users to the
website.<br>


### Post Detail Page - Top

![Post Detail Page - Top](static/extras/features/postdetail-top.png)

* At the top of the Post Details Page, users can see the post's main
image and they can also have access to information about the post. The
post information includes recipe name, author name, image and when was posted.<br>

### Post Detail Page - Steps

![Post Detail Page - Steps](static/extras/features/postdetail-mid.png)

* In this page section, users can read the ingredients and follow the steps to complete the recipe. Also at the buttom of this the user can se the number of likes, category, the number of comments and the option to like/unlike the post. <br>

### Post Detail Page - Comments

![Post Detail Page - Comments](static/extras/features/postdetail-comment.png)

* At the bottom of this page, If the user is logged can post and read comments posted by other users. If the user is logged in or is a 
superuser they have access to the buttons for deleting or updating comments. Also the user can reply to other users comments.

### Edit Comments Page

![Edit Comments Page](static/extras/features/edit-comment.png)

* On this page, users are allowed to comment, delete and edit their own post comments.

### Categories Page

![Categories Page ](static/extras/features/category-page.png)<br><br>

* On the Categories Page, users can access the post filtered by the chosen category.

### Add/Edit Recipie Page

![Add Recipie Page](static/extras/features/add-post.png)

![Edit Recipie Page](static/extras/features/edit-post.png)

On this page, registered users can fill out the form to add or edit a post with their favourite recipie.

### Search Box

![Search Box](static/extras/features/search-box.png)

* In this box, the users can search by inputting a keyword in the search tool. This allows the user to try and find 
  the recipe they are looking for.

### Search Results Page

![Search Results Page](static/extras/features/search-result.png)

* On the Search Results Page, users can see the recipes found by their search.  When their recipe is located, the user can go to the 
  Post Details Page by clicking on the card result.

### Search Results - Input Empty

![Search Results - Input Empty](static/extras/features/search-empty.png)

* On the Search Results Page - Input Empty, users will see this message if their search returns with an empty input.

### Search Results - No Results Found

![Search Results - No Results Found](static/extras/features/search-null.png)

* On the Search Results Page - No Results Found, users will see this message if there is nothing found for the search.

### Signup Page

![Signup Page](static/extras/features/signup-page.png)

* On the Signup Page, a new user can sign up for the Babylicious Blog website by filling out and then submitting the form.

### Login Page

![Login Page](static/extras/features/signin-page.png)

* On the Login Page, users can log in to the website by inputting the username and password and have access 
  to website services for a user registered.

### Logout Page

![Logout Page](static/extras/features/signout-page.png)

* On the Logout Page, users can confirm that they wish to exit the website.

### User Profile Page

![User Profile Page](static/extras/features/profile-info.png)

![User Profile Page](static/extras/features/profile-info1.png)

* On the Profile Page, users have access to their own information and can update their user name, email and profile image. Also they can see all their posts and they delete theit profile

### Navbar

![Navbar](static/extras/features/navbar.png)

* The navigation bar is present at the top of every page and houses all links to the various other pages.
* The options to Register or Log in will change to the option to log out once a user has logged in.
* Once a user has signed in, more options such as add post, profile page and user image will be available in the navbar.
* A search box is nested in the navbar.
* The navbar is fully responsive, collapsing into a hamburger menu when the screen size becomes smaller.

### Herosection

![Herosection](static/extras/features/herosection.png)

![Herosection](static/extras/features/category-dropdown.png)
* In the herosection users can access the categories list by clicking on the dropdown menu. Also the dropdown images will display informations about each category

### Footer

![Footer](static/extras/features/footer.png)
* On the website footer, users can see basic information about the blog such as social media, 
  copyright, and a quote about baby diversification.

## Messages and Interaction With Users

* Some interactive messages were added to the project to make the navigation on the website easier and to improve the
user's experience.

### Sign up

![Sign up](static/extras/features/signup-message.png)

* When users sign up to the website they will see a message at the top of the page saying "Successfully signed in as
(username)".<br>

### Login

![Login](static/extras/features/signin-message.png)

* When users sign in to the website they will see a message at the top of the page saying "Successfully signed in as
(username)".<br>

### Logout

![Logout](static/extras/features/signout-message.png)

* When users log out of the website they will see a message at the top of the page saying "You have signed out".<br>
  
### Profile Update

![Profile Update](static/extras/features/profile-update-message.png)

* When users update their profile they will see a message at the top of the page saying that their account has been updated.<br>

### Like Post

![Like Post](static/extras/features/like-message.png)
* *When users are logged in to the website they can like a post and they will see a message at the top of the page 
  saying "You have liked this post".<br>

### Unlike Post

![Unlike Post](static/extras/features/unlike-message.png)

* When users are logged in to the website they can unlike a post that has been liked by the user and they will see a message 
  at the top of the page saying "You have unliked this post".<br>

### Delete/Edit Comment

![Delete Comment](./assets/readme/features/interactive_messages/tasty_blog_user_interaction_comment_delete_1.jpg)

* When users are logged in to the website and they have previously posted a comment or if the user is a superuser they will see the 
Delete and Edit buttons at the bottom of comments.<br>

### Delete Comment - 1

![Delete Comment - 2](./assets/readme/features/interactive_messages/tasty_blog_user_interaction_comment_delete_2.jpg)

* If they wish to delete their comment, they can press the button Delete and a Bootstrap box model will pop up with the message 
  "Are you sure you want to delete your comment?".<br>

### Delete Comment - 2

![Delete Comment - 3](./assets/readme/features/interactive_messages/tasty_blog_user_interaction_comment_delete_3.jpg)

* After pressing the Delete button again inside the Bootstrap box model they will see a message on the 
  top of the page, "Your comment was deleted successfully".<br>

### Edit Comment

![Edit Comment](./assets/readme/features/interactive_messages/tasty_blog_user_interaction_comment_edit.jpg)

* After pressing the Update, users will see a message on the top of the page, "The comment was successfully updated".<br>

### Email Sent - Success

![Email Sent - Success](./assets/readme/features/interactive_messages/tasty_blog_user_interaction_email_sent_2.jpg)

* After users submit the form to info@tastyblog successfully, they will see the message, "Thanks for your email! 
  We will contact you as soon as possible".<br>

### Email Sent - Failed

![Email Sent - Failed](./assets/readme/features/interactive_messages/tasty_blog_user_interaction_email_sent.jpg)

* If the email was not submitted successfully, users will see the message, "Sorry, something went wrong! 
  Try to submit the email again".<br>

### Add Book

![Add Book](./assets/readme/features/interactive_messages/tasty_blog_user_interaction_add_book.jpg)  

* When users are logged in to the website they can publish a post with a favourite cookbook and after they submit the 
post they will see a message at the top of the page saying "Your post was sent successfully and is awaiting approval".<br>

### Edit Book

![Edit Book](./assets/readme/features/interactive_messages/tasty_blog_user_interaction_book_edit.jpg)  
* When users are logged in to the website they can edit their own previously published posts and they will see the message 
  "The post was successfully updated" after pressing the Submit button.<br>

### Delete Book 1 

![Delete Book 1](./assets/readme/features/interactive_messages/tasty_blog_user_interaction_book_delete_2.jpg)
When users are logged in to the website and they wish to delete their posts, they can press the button Delete and a 
Bootstrap box model will pop up with the message "Are you sure you want to delete your post?".<br>  

### Delete Book 2

![Delete Book 2](./assets/readme/features/interactive_messages/tasty_blog_user_interaction_book_delete.jpg)  

* After pressing the Delete button again inside the Bootstrap box model they will see a message on the 
  top of the page, "Your post was deleted successfully".<br>

### Empty Search

![Empty Search](./assets/readme/features/interactive_messages/tasty_blog_user_interaction_profile_empty_search.jpg)

* Any user can search for a keyword using the input search and if the search is done with an empty input they will see a
  message saying, "You forgot to search a recipe. Please try searching again.".<br>

### No Search Found

![No Search Found](./assets/readme/features/interactive_messages/tasty_blog_user_interaction_profile_no_search_found.jpg)

* And if there are no results matching or similar to the keyword, the user will see the following message, "We are sorry. 
  There are no searches for (keyword) on the website. Try the search again".<br>

## Admin Panel/Superuser
![No Search Found](./assets/readme/extras/tasty_blog_superuser.jpg)

* On the Admin Panel, as an admin/superuser I have full access to CRUD functionality so I can view, create, edit and
delete the following ones:
1. Posts
2. Comments
3. Author
4. Categories
5. Profiles
6. Books

