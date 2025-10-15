# Minopus Web App
## Project Description
The project will be a web aplication where students can collaborate to help each other with studying. The main use of the site will be for studying purposes with a heavy focus on study orientated features such as the ability to share questions in text, image and video form. People will be able to use the site for general uses as well but that will be a separate part of the app and will not impact the other part of the site. There will be public servers, private servers and one on one chats which will allow people to share their queries on different levels. They can choose to share their question with the public giving the question the most exposure and the bese chance at being solved or you can share it to a private group chat to get answers from your friends who might be working on similar questions or you can talk to one friend who might be working on the same project as you to collaborate.

## Functional Requirements
- User must be able to sign up and log in through email
- Users can edit their profile, including name, profile picture, and interests
- Users can create public and private servers to talk on
- Users can talk to friends one on one to help collaborate on a project
- Users can upload questions via text, image or video

## Non-Functional Requirements
- The application should be able to load the dashboard within 2 seconds under normal conditions
- All user data in transit and at rest must be encrypted using industry-standard protocols
- The UI should be intuitive and consistent across different modules, facilitating ease of navigation
- The system should have an uptime of 99.9%, minimising downtime during critical study periods
- The codebase should follow standardised coding practices and include comprehensive documentation to facilitate future maintenance and updates

## Visual Choices
| Colour Palette                                                                                                                                                                                                                 | Typography                                                                                                                                                                        | Image and Icon Choice                                                                                                                                                                                |
|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| I chose the colour scheme "mechanical and floaty" which contained shades of blue as well as grey and black because I thought it would look good with the layout of the site. It didn't look too bad, but it wasn't that great. | I chose to use Sans Serif fonts for my small text and body text I according to "A guide to typography" website suggested that these kinds of fonts are best for this application. | I haven't chosen any images to go onto the website yet other than the company logo that was generated last year. I have decided to keep that as it is a good logo that does match the sites purpose. |
|                                                                                                                                                                                                                                | For my Sans Serif font I chose "Rleud Demo" as I thought it looked good and matched the site.                                                                                      |                                                                                                                                                                                                      |
|                                                                                                                                                                                                                                | From the article "A guide to typography" I also found that Serif fonts are best for headings and large text however I couldn't find anything that would work on the site.         |                                                                                                                                                                                                      |

## Annotated Pages
![Page 1](/Flask/working_documents/1st%20design%20login.png)
This is the first page that users will see where they have to login in. There are three signin options users can choose from giving them flexibility. These will function as buttons that redirect users to other dedicated pages where they can actually signin. There is a bit of information on the page at the bottom telling the user a little about the website. There are three more buttons on the top of the page which allow you to download as an app go to a support page and login using email.

![Page 2](/Flask/working_documents/1st%20design%20main1.png)
This is the main page that users see and is the page they arrive on after loging in. This page displays important information such as friends you have and their online/offline status as well as having sidebars that display more information such as dms that you have. You can click on the dms to full screen them as a chat and can add friends by clicking the add friend button. There is a menubar at the top where you can enter more menus when you click on the buttons and finally there is another side menu on the far left with houses the different groups which you can click on to enter the group chat.

![Page 3](/Computing-Web-App//Flask/working_documents/1st%20design%20chat.png)
This page is representative of a dm chat but can also be used to illustrate what a group chat looks like where you can chat to others about your work. The sidebars and top menubar remain in place which is a feature of the website allowing for easy navigation around the website.


## Best Practice Approaches
I have used multiple best practice approaches to ensure that the site is developed efficiently and properly. I used a website which gave some preset colour schemes that ensured I was using colours that worked well together and looked nice overall. I used another website to conduct research on typography to assess what font will look and work the best on the website in certain places.


## Alternate Design
I changed the colour scheme to better match the website and the logo of the website. The logo had a pink to orange gradient and I used a similar style that I got from the website 'Visme' which had pre set colour scheme that I could use that would work well together and look good. I changed the way the login paged looked and functioned to make it more streamlined and easier to login. I also changed the main page of the website quite a bit to make it easier to navigate with larger icons and a better colour scheme that with colours that compliment each other. 

| Colour Palette                                                                                                                                                                                                                                                                                                                                                                                                                           | Typography                                                                                                                                                                                                                                    | Image and Icon Choice                                                                                                                                                                      |
|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| I chose the colour scheme "Gradient Pop", which contained a pink to orange gradient that matched the company logo, so I thought it would be a better colour scheme than the last one. This colour scheme also had contrasting colours like blue and black. I also chose this scheme because I thought it would look good with the layout of the site and in the end after the rearrangement of the site it did match the site quite well | I chose to keep Sans Serif fonts for my small text and body text as according to "A guide to typography" website suggested that these kinds of fonts are best for this application.                                                           | I have places where images can go, and I have also kept the company logo that was generated last year. I have decided to keep that as it is a good logo that does match the sites purpose. |
|                                                                                                                                                                                                                                                                                                                                                                                                                                          | For my Sans Serif font I chose "Rleud Demo" as I thought it looked good and matched the site.                                                                                                                                                 |                                                                                                                                                                                            |
|                                                                                                                                                                                                                                                                                                                                                                                                                                          | From the article "A guide to typography" I also found that Serif fonts are best for headings and large text however, I couldn't find anything that would work on the site. I kept this the same but might change it  if I find a better font. |                                                                                                                                                                                            |


## Test Cases
Test case ID: TC01. 

Test case name: Successful login. 

Preconditions: User must have a registered account. 

Test steps:  
1. Open application. 
2. Prompt user to enter valid username and password. 
3. Click the login button. 
Expected result: The user is able to login and is redirected to the main page of the website. 

Test case ID: TC02. 

Test case name: Unsuccessful Sign up. 

Precondtions: None. 

Test steps:  
1. Open application. 
2. Prompt user to click sign up button. 
3. Prompt user to enter a new username and password that meets all requirements. 
4. Click sign up button. 
5. If user enters invalid username or password display error message. 
6. Prompt user to reenter whichever item is wrong. 
7. Click sign up button. 
8. If username and password are valid. 
Expected result: The user is able to sign up and now has a registered username and password to login in next time. 

## Week 11
14/10/2025
Added sign up functionality that sends the information to the database/backend which can be recalled later when sigining in again after the user has logged out.

Got the chat functionality working where it writes the chat message history into the database so it saves and can be retireved even when you log out.
