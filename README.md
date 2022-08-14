# Graphic Me

Graphic Me is a graphic design service. This website is allows user to search previous work done by the graphic design company, create a user profile account and order custom graphic for their needs. 



Live website: https://

![Image of responsive design](assets/images/readme-images/responsive.PNG)

## Table of Content
1. [User Experience](#user-experience)
    1. [Target Audience](#target-audience)
    2. [User Stories](#user-stories)
        1. [Site Owner](#site-owner)
        2. [User](#user)
3. [Design](#design) 
    1. [Design Choices](#design-choices)
    2. [Colour](#colours)
    3. [Fonts](#fonts)
    4. [Structure](#structure)
4. [Technologies Used](#technologies-used)
    1. [Languages](#languages)
    2. [Frameworks & Tools](#frameworks-&-tools)
5. [Features](#features)
    1. [Username submission section](#username_submission_section)
    2. [Scoring section](#scoring_section)
    3. [Quiz Instructions](#quiz_instructions)
    4. [Quiz section](#quiz_section)
    5. [Quiz Rating section](#quiz_rating_section)
6. [Testing](#testing)
    1. [HTML Validation](#HTML-validation)
    2. [CSS Validation](#CSS-validation)
    3. [Accessibility](#accessibility)
    4. [Performance](#performance)
8. [Bugs](#Bugs)
9. [Deployment](#deployment)
10. [Credits](#credits)
    1. [Quiz Images](#quiz-images)
11. [Acknowledgements](#acknowledgements)

## User Experience

### Target Audience
- People looking for a grahic design service
- People who want to know the graphic designers history in the industry.

### User Stories
#### Site Owner
- As a Site Owner  I can view customers orders so that I can track their progress and trends
- As a Site Owner  I can add, edit and delete items in the portfolio so that manage the site gallery
- As a Site Owner I can upload completed work so that I can complete a customers order
- As a Site Owner, I want to receive feedback from the user.

#### User 
- As a User I can create an account so that make purchases and track orders
- As a User I can easily login and logout so that access my information
- As a User I can recover my password so that I don’t get locked out of my account
- As a User I can receive a confirmation email when I register an account so that I am certain of the creation of my account
- As a User I can create a custom order so that I can buy a graphic
- As a User I can easily enter payment details so that checkout quickly
- As a User I can view my orders so that I can see the order progress and download my completed products
- As a User I can access my shopping cart so that view my current order
- As a User I can easily see the est cost of my order so that I can track my spending
- As a User I can search keywords so that navigate the site easily
- As a User I can I can sort items in the portfolio so that narrow down my search
- As a User I can see the search results title and the number of results so that to quickly see what items and how many are there
- As a User I can leave a review so that I can tell the site owner what I thought of the service
- As a User I can view products details in the portfolio so that a better understanding of the skillset


## Design
### Colour
- Website background: black
- Navigation button: border gold (#FFC300), background colour blue (#0080FF) and white text
- Users score: background colour gold (#FFC300) and text colour black
- Quiz answer option buttons: border gold (#FFC300), background colour blue (#0080FF) and white text
- Rating section: border gold (#FFC300), background colour blue (#0080FF) and white text

### Fonts
- The font used for this website is Outfit, sourced from Google Fonts

### Structure
The website is structured to make an intuitive experience for the user. 
- The Landing page prompts the user to input their username.
- The next page the user is brought to is the instructions page.
- The last page is the geography quiz.
- Once the quiz has finished the user is prompted to play again which will bring them back to the beginning of the quiz.


## Features

### Username submission section
- This section allows the user to enter their user before the quiz begins

![Image of username submission section](assets/images/readme-images/username-input.PNG)

### Quiz Instructions 
- This section explains to the User what they must to to play the quiz.

![Image of quiz instructions section](assets/images/readme-images/quiz_instructions.PNG)

### Scoring section
- The scoring section keeps track of the users score based on the answers they have submitted

![Image of scoring system](assets/images/readme-images/scoringsystem.PNG)

### Quiz section
- The quiz section holds the main quiz which consists of the image and answer options
- The image will change every time the user clicks the next button and moves on to the next question
- The answers section holds four different answer options to choose from. If the user clicks the correct answer the selection button will turn green and a point will be added to their overall score, if incorrect the button will turn red and the user will not gain a point.

![Image of quiz section](assets/images/readme-images/main-quiz-section.PNG)

### Quiz Rating section
- The rating section allows users to rate the quiz from 1-5 based on their experience. This feedback will also help on improving the quiz in the future.

![Image of rating section](assets/images/readme-images/rating-section.PNG)

## Technologies Used

### Languages
- HTML
- CSS
- JavaScript

### Frameworks & Tools
- Git
- GitHub
- Gitpod
- Google Fonts

## Testing 
### Performance
### HTML

- No errors returned when checking site through W3C Validator
![Image of HTML validation](assets/images/readme-images/html-val.PNG)


### CSS
- No errors found when stie was run through W3C CSS Validator
![Image of CSS validator](assets/images/readme-images/css-val.PNG)

### Javascript
- No errors found when passing site through Jshint validator
    - There are 7 functions in this file.
    - Function with the largest signature take 1 arguments, while the median is 0.
    - Largest function has 9 statements in it, while the median is 4.
    - The most complex function has a cyclomatic complexity value of 2 while the median is 1.

### Lighthouse
![Image of lighthouse report](assets/images/readme-images/lighthouse.PNG)

- The site was deployed to GitHub pages. The steps to deploy are as follows:
    - In the GitHub repository, navigate to the Settings tab
    - From the source section drop-down menu, select the Master Branch
    - Once the master branch has been selected, the page will be automatically refreshed with a detailed ribbon display to indicate the successful deployment.

## Bugs
| **Feature / Function** | **Expected Result** | **Actual Result** | **Action** |
|-------------|------------|---------------------|-------------------|
| Click chosen answer | Clicking an answer changes the colour to either green or red depending on the result, one point is added to the score if the user answered correctly. | Colour of the users answer changes appropriately. If the user keeps clicking the correct answer the score will continue to be incremented. Also The user can keep selecting answers until they find the correct answer | Create functions to disable quiz buttons once an answer has been selected |
| Play Again button | The quiz ends and the user can click the button to start a new game | The quiz ends and until the user gives feedback the game can't continue | Created a function to restet the game after the Plat Again button has been clicked |

## Credits
### Quiz Images
- Paris - Image by pexels.com
- London - Image by Chris Schippers, sourced from pexels.com
- Barcelona - Image by Aleksandar Pasaric, sourced from pexels.com
- Singapore - Image by Robert Stokoe, sourced from pexels.com
- Phnom Penh - Image by allPhoto Bangkok, sourced from pexels.com