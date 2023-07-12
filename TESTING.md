# Testing
Back to the [README](README.md)

* Testing has taken place continuously throughout the development of the project. Each view was tested regularly. 
  When the outcome was not as expected, debugging took place at that point.  

### Python Validation - PEP8
* Python testing was done using the PEP8 Online to ensure there were no syntax errors in the project. All python files
were entered into the online checker.

#### Blog
* [admin.py](static/extras/test/admin-blog.png)
* [apps.py](static/extras/test/apps-blog.png)
* [models.py](static/extras/test/models-blog.png)
* [forms.py](static/extras/test/forms-blog.png)
* [signals.py](static/extras/test/signals-blog.png)
* [urls.py](static/extras/test/urls-blog.png)
* [views.py](static/extras/test/views-blog1.png)
* A error were raised in the blog/views.py file, however these were related to default django authorisation
code and could not be changed to remove the errors(line to long).


#### Babyfood
* [asgi.py](static/extras/test/asgi-babyfood.png)
* [urls.py](static/extras/test/urls-babyfood.png)
* [wsgi.py](static/extras/test/wsgi-babyfood.png)
* [settings.py](static/extras/test/setings-babyfood.png)
* A few errors were raised in the babyfood/settings.py file, however these were related to default django authorisation
code and could not be changed to remove the errors(line to long).
* [views.py](static/extras/test/views-babyfood.png)

### Lighthouse
Lighthouse was used to test Performance, Best Practices, Accessibility and SEO on Desktop.

##### Desktop Results:
![Lighthouse Mobile Result](static/extras/test/light-house-desktop.png).

###### Mobile Results:
![Lighthouse Desktop Result](static/extras/test/lighthouse-mobile.png).

### HTML Validation
![HTML Validation Result](static/extras/test/html-validator.png).

### CSS Validation

![CSS Validation Result](static/extras/test/css-validator.png).
![CSS Validation Result](static/extras/test/css-warnings.png).
* Custom CSS was validated using W3C Jigsaw validation service. Twenty-three warnings were displayed, however, 
  these are related to vendor extension prefixes which will not affect the CSS performance.

## Manual Testing

The original Google sheet file for the manual testing report can be found [here](https://docs.google.com/spreadsheets/d/1jyXqMLt8xYcv7T4iBDfvAt6MWkkNOb9O3zaiBT0-dek/edit#gid=0)

![Manual Test](static/extras/test/manual-test1.png)
![Manual Test](static/extras/test/manual-test2.png)
![Manual Test](static/extras/test/manual-test3.png)
![Manual Test](static/extras/test/manual-test4.png)
![Manual Test](static/extras/test/manual-test5.png)

### Backend/Admin Panel Testing

As a Site owner<br>I want to be able to review all posts, categories, users, likes, etc.	So that I can maintain the site and remove any offensive content. 
<br>Given that I'm a Site owner<br>When I navigate to the admin<br>Then I should see all posts, categories, users, likes, etc.
<br>As a Site owner<br>I want to be able to edit/update/delete a post.	So that I can maintain the site and remove any offensive content. 
 <br>Given that I'm a Site owner<br>When I navigate to the admin<br>Then I should see be able to control all content on the website 
<br>As a Site owner<br>I want to be able to ensure<br>all areas of the site to function correctly and have no bugs. So that I can ensure an enjoyable browsing experience for all newcomers. 
<br>Given that I'm a Site owner<br>When I check all site functionality<br>Then I should see that everything works as expected, there are no bugs and all links and forms work as expected 

## Bugs