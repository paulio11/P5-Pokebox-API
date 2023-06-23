# Pokébox Backend / API

[Link to live API](https://project-5-backend.herokuapp.com/)

[Link to live Pokébox front-end](https://project-5-pokebox.herokuapp.com/)

[Link to Pokébox front-end repo](https://github.com/paulio11/P5-Pokebox)

## Contents

1. [Introduction](#introduction)
2. [Project Planning](#project-planning)
3. [GitHub Project](#github-project)
4. [Database Schema](#database-schema)
5. [Serializers](#serializers)
6. [Views](#views)
7. [Permissions](#permissions)
8. [Project Settings](#project-settings)
9. [Bugs and Fixes](#bugs-and-fixes)
10. [Testing](#testing)
11. [Deployment](#deployment)
12. [Technologies](#technologies)
13. [Credits](#credits)

## Introduction

This is the back-end API for [Pokébox](https://project-5-pokebox.herokuapp.com/). Created using Django and the Rest Framework. Visit my [front-end repo](https://github.com/paulio11/P5-Pokebox) for more information.

[Back to top 🔺](#pokébox-backend--api)

## Project Planning

### GitHub Project

The GitHub project board feature was used to keep track of what I was working on and what still needed to be done. I created a user story for each feature, or an issue for each to do and bug, then moved them when necessary throughout the development of both front and back-end.

[Link to Project Board](https://github.com/users/paulio11/projects/4)

**Project Board:**

![GitHub Project Board](https://raw.githubusercontent.com/paulio11/P5-Pokebox-API/main/documentation/images/readme-projectboard.png)

### Database Schema

The models required for this project are:

- **Post** - for user diary entries.
- **Comment** - for replies to diary entries.
- **Like** - for user likes on diary entries.
- **Profile** - for a user's profile information and Pokémon collection.
- **Announcement** - for admin user's to post website announcements.
- **News** - for admin user's to news items.

**Entity-Relationship Diagram:**

![Entity-Relationship Diagram](https://raw.githubusercontent.com/paulio11/P5-Pokebox-API/main/documentation/images/readme-schema.png)

#### Post Model

| Name    | Type              | Details                                                                | Notes                                                                      |
| ------- | ----------------- | ---------------------------------------------------------------------- | -------------------------------------------------------------------------- |
| id      | Primary Key       | unique                                                                 |                                                                            |
| owner   | Foreign Key       | to User                                                                | The author of the post                                                     |
| created | DateTimeField     | auto_now_add=True                                                      | Date of post, automatically added on creation                              |
| body    | TextField         | max_length=400                                                         | The text content of the post                                               |
| image   | ResizedImageField | blank=True, upload_to="images/", size=[600, None], force_format="WEBP" | Optional image for post. Cropped to a width of 600px and converted to WEBP |

#### Comment Model

| Name    | Type          | Details           | Notes                                            |
| ------- | ------------- | ----------------- | ------------------------------------------------ |
| id      | Primary Key   |                   |                                                  |
| owner   | Foreign Key   | to User           |                                                  |
| created | DateTimeField | auto_now_add=True | Date of comment, automatically added on creation |
| body    | TextField     | max_length=400    | The text content of the comment                  |

#### Like Model

| Name  | Type        | Details | Notes |
| ----- | ----------- | ------- | ----- |
| id    | Primary Key |         |       |
| owner | Foreign Key | to User |       |
| post  | Foreign Key | to Post |       |

#### Profile Model

| Name     | Type              | Details                                                                                              | Notes                                                                                                                     |
| -------- | ----------------- | ---------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------- |
| id       | Primary Key       |                                                                                                      |                                                                                                                           |
| owner    | Foreign Key       | to User                                                                                              |                                                                                                                           |
| created  | DateTimeField     | auto_now_add=True                                                                                    | Date of creation, automatically added                                                                                     |
| about    | TextField         | max_length=400, blank=True, default="..."                                                            | Text field for a user's description. Has the default text "Hello! I am a new trainer just starting my Pokémon adventure." |
| favorite | CharField         | max_length=30, blank=True                                                                            | Character field that will hold a users favorite Pokémon, assigned from a list of possibilities on the front end           |
| pokemon  | ArrayField        | Array of IntegerFields, default=list                                                                 | The array will hold pokemon collected by the user, each pokemon represented by their ID (an integer)                      |
| avatar   | ResizedImageField | upload_to="avatars/", size=[300, 300], crop=["middle", "center"], force_format="WEBP", default="..." | For the user's avatar, resized and cropped to a suitable size, has a default image                                        |

The profile object is automatically created for each new user using a `post_save` signal.

#### Announcement Model

| Name    | Type          | Details           | Notes                                 |
| ------- | ------------- | ----------------- | ------------------------------------- |
| id      | Primary Key   |                   |                                       |
| created | DateTimeField | auto_now_add=True | Date of creation, automatically added |
| body    | CharField     | max_length=1000   | The body of the announcement.         |

#### News Model

| Name     | Type              | Details                                                              | Notes                                                               |
| -------- | ----------------- | -------------------------------------------------------------------- | ------------------------------------------------------------------- |
| id       | Primary Key       |                                                                      |                                                                     |
| created  | DateTimeField     | auto_now_add=True                                                    | Date of creation, automatically added                               |
| title    | TextField         | max_length=100                                                       | The title of the news item                                          |
| body     | CharField         | max_length=1000                                                      | The body of the news item                                           |
| image    | ResizedImageField | blank=True, upload_to="news/", size=[666, None], force_format="WEBP" | Optional image for the news item, resized and the format is changed |
| category | CharField         | max_length=5, choices = (Anime, TCG, Games, Other)                   | Category of the news item, with a selectable list of options        |

[Back to top 🔺](#pokébox-backend--api)

## Serializers

The django Rest Framework serializer component is used as an intermediary between the database models and the API views (see below). They provide fields in addition to those from the parent model, can define which should be read only and a method for creation. Each model has it's own serializer:

### [Post Serializer](https://github.com/paulio11/P5-Pokebox-API/blob/main/posts/serializers.py)

The post serializer provides the following to the API view:

- **Owner** - This field uses the owner's username taken from the user model.
- **Created** - Provided by the function `get_created()` which returns a formatted date string.
- **Like ID** - Provided by the function `get_like_id()` which returns the ID of the Like object for the Post if the user has liked it. Used to show like status on the front end.
- **Profile ID** - Displays the post owner's profile ID. Used on the front end to link to the owner's profile when viewing the post.
- **Profile Avatar** - Displays the post owner's avatar. Used to represent the post owner on the front end.

### [Comment Serializer](https://github.com/paulio11/P5-Pokebox-API/blob/main/comments/serializers.py)

The comment serializer provides the following to the API view:

- **Owner** - This field uses the owner's username taken from the user model.
- **Created** - Provided by the function `get_created()` which returns a formatted date string.
- **Profile ID** - Displays the comment owner's profile ID. Used on the front end to link to the owner's profile when viewing the comment.
- **Profile Avatar** - Displays the comment owner's avatar. Used to represent the comment owner on the front end.

### [Like Serializer](https://github.com/paulio11/P5-Pokebox-API/blob/main/likes/serializers.py)

The like serializer provides the following to the API view:

- **Owner** - This field uses the owner's username taken from the user model.
- **`create()`** - This function handles the integrity error if a duplicate like object is found. This is to stop the same user liking a post more than once.

### [Profile Serializer](https://github.com/paulio11/P5-Pokebox-API/blob/main/profiles/serializers.py)

The profile serializer provides the following to the API view:

- **Owner** - This field uses the owner's username taken from the user model.
- **Created** - Provided by the function `get_created()` which returns a formatted date string.
- **Pokemon** - Defines this field as a list that can be empty.
- **col_size** - Collection Size, defined as a read only field.

### [Announcement Serializer](https://github.com/paulio11/P5-Pokebox-API/blob/main/news/serializers.py)

The announcement serializer provides the following to the API view:

- **Created** - Provided by the function `get_created()` which returns a formatted date string.

### [News Serializer](https://github.com/paulio11/P5-Pokebox-API/blob/main/news/serializers.py)

The news serializer provides the following to the API view:

- **Created** - Provided by the function `get_created()` which returns a formatted date string.

### [CurrentUser Serializer](https://github.com/paulio11/P5-Pokebox-API/blob/main/pokebox/serializers.py)

Defined by `REST_AUTH_SERIALIZERS` variable in settings. The current user serializer extends DJ Rest Auth's UserDetailsSerializer to provide this additional information:

- **Profile ID** - Provides the current user's profile ID, used on the front-end to provide a link to their profile.
- **Profile Avatar** - Provides the current user's profile avatar, used on the front-end to display the logged in user's avatar.
- **Is Staff** - A boolean value that allows the front-end website to conditionally render specific elements if the logged in user is an admin.

[Back to top 🔺](#pokébox-backend--api)

## Views

Each view provides a response to the front-end based on the request. They are responsible for generating the appropriate JSON output using the defined serializer and assigning correct permissions.

### [Post Views](https://github.com/paulio11/P5-Pokebox-API/blob/main/posts/views.py)

- **`PostList()` and `PostDetail()`**
  - Inherits from the `generics.ListCreateAPIView` and `generics.RetrieveUpdateDestroyAPIView` class respectively. It specifies the serializer class as `PostSerializer` and the permission classes as `permissions.IsAuthenticatedOrReadOnly`.
  - The `queryset` attribute is set to retrieve a list of Post objects from the database. The queryset is annotated with the counts of distinct likes and comments for each post and ordered by the creation date in descending order.
  - Specifies three filter backends: `filters.SearchFilter`, `filters.OrderingFilter` and `DjangoFilterBackend`.
  - The `ordering_fields` attribute defines the fields that can be used for ordering the posts, which include like_count, comment_count, and created.
  - The `filterset_class` attribute is set to PostFilter (see below).
  - The `search_fields` are set to `body` and `owner__username` so a user can search for a post by either the owner of the post or by words in the body text.
  - The `perform_create()` method is overridden to set the owner of a newly created post to the authenticated user making the request.
- **`PostFilter()`**
  - Inherits from `rest_framework.FilterSet`. It is used to define filters for the Post model.
  - Defines the `has_image` filter as a `rest_framework.BooleanFilter`. This filter is associated with the image field of the Post model.
  - Returns a filtered queryset that excludes posts with an empty image field. If the value is False or None, it returns the original queryset without applying any filtering.

### [Comment Views](https://github.com/paulio11/P5-Pokebox-API/blob/main/comments/views.py)

- **`CommentList()` and `CommentDetail()`**
  - Like the Post views, these two views define the relevant serializer and permissions for the comment model and overrides comment creation to provide the logged in user as owner.
  - The `get_queryset()` method is overridden to provide a custom queryset for retrieving comments. It retrieves all comments using `Comment.objects.all()` and then checks if a post parameter is present in the request's query parameters. If the post parameter exists, it uses the `get_object_or_404()` function to retrieve the corresponding Post object. It then filters the comments queryset to only include comments associated with that particular post.

### [Like Views](https://github.com/paulio11/P5-Pokebox-API/blob/main/likes/views.py)

- **`LikeList()` and `LikeDetail()`**
  - As above these views define the relevant serializer and permissions for the Like model and overrides like creation to provide the logged in user as owner.

### [News & Announcement Views](https://github.com/paulio11/P5-Pokebox-API/blob/main/news/views.py)

- **`NewsFilter()`**
  - Inherits from `rest_framework.FilterSet`. It is used to define filters for the News model.
  - Defines `category` as a multiple choice filter. This filter is assciated with the category field and uses the same variable for choices.
  - Returns a filtered queryset that will only show news items that match the category defined in the url parameters.
  - Also allows the use of a news item's ID field as the filter, so a specific item can be loaded and displayed.
- **`NewsList()`, `NewsDetail()`, `AnnouncementList()` and `AnnouncementDetail()`**
  - As is the norm, these two views define the relevant serializer for the news and announcement model.
  - There is no perform create function this time as owner is not a required field for these models.
  - `IsAdminOrReadOnly` is defined as the permission class in order to allow only admin users full access.

### [Profile Views](https://github.com/paulio11/P5-Pokebox-API/blob/main/profiles/views.py)

- **`ProfileList()` and `ProfileDetail()`**
  - Again defines the relevant serializer and permissions for the Profile model.
  - The `queryset` attribute is set to retrieve a list of Profile objects from the database. The queryset is annotated with an `ExpressionWrapper()` which uses a built in Postgresql function called `array_length` to count the length of the `pokemon` array field and return it as a new field.
  - Specifies three filter backends: `filters.SearchFilter`, `filters.OrderingFilter` and `DjangoFilterBackend`.
  - The `ordering_fields` attribute defines the fields that can be used for ordering the profile, which include `owner__username`, `col_size`, and `created`.
  - The `filterset_fields` is set to `owner__username` so a specific user's profile can easily be found.
  - The `search_fields` is set to `owner__username` so a user can search for a trainer by their username.

### [Other](https://github.com/paulio11/P5-Pokebox-API/blob/main/pokebox/views.py)

- **`root_route()`**
  - Overrides the home root of the API, displays a message.
- **`logout_route()`**
  - This view sends a response that sets the two cookies used for authentication as empty. This effectively logs out the user. This is a fix for the DJ Rest Auth logout view present in the version being used.

[Back to top 🔺](#pokébox-backend--api)

## Permissions

This project uses two custom permissions `IsOwnerOrReadOnly` and `IsAdminOrReadOnly`. The first is used in the PostDetail, CommentDetail, ProfileDetail and LikeDetail views. This permission grants full CRUD access to the owner of the object and read-only access to others. The second is used on views relating to the News and Announcement models. Granting full access to admin users, and read-only access to a normal user.

[Back to top 🔺](#pokébox-backend--api)

## Project Settings

The following are the non-default variables defined in [settings.py](https://github.com/paulio11/P5-Pokebox-API/blob/main/pokebox/settings.py) essential for this project:

### Cloudinary

- `CLOUDINARY_STORAGE`: Contains the Cloudinary URL.
- `DEFAULT_FILE_STORAGE`: Specifies the default file storage as Cloudinary.
- `MEDIA_URL`: Defines the URL path for media files.

### Django-Resized

- `DJANGORESIZED_DEFAULT_QUALITY`: Sets the default quality for resized images.
- `DJANGORESIZED_DEFAULT_KEEP_META`: Specifies whether to keep metadata for resized images.

### Allauth / dj-rest-auth

- `SITE_ID`: Identifies the Django site.
- `OLD_PASSWORD_FIELD_ENABLED`: Enables the use of the old password field when attempting to change password.

### Rest Framework

- `DEFAULT_AUTHENTICATION_CLASSES`: Defines the authentication classes for the API. Uses session authentication in development (`DEV`) and JWT cookie authentication in other environments.
- `DEFAULT_PAGINATION_CLASS` and `PAGE_SIZE`: Set pagination settings.

### JWT

- `JWT_AUTH_SECURE`: Specifies whether JWT authentication should use a secure connection.
- `JWT_AUTH_COOKIE`: Defines the cookie name for JWT authentication.
- `JWT_AUTH_REFRESH_COOKIE`: Sets the cookie name for JWT token refresh.
- `JWT_AUTH_SAMESITE`: Specifies the SameSite attribute for JWT cookies.

### CORS

- `CORS_ALLOW_CREDENTIALS`: Enables sending credentials (e.g., cookies) in cross-origin requests.
- `CORS_ALLOWED_ORIGINS`: Lists the allowed origins for cross-origin requests.

[Back to top 🔺](#pokébox-backend--api)

## Bugs and Fixes

There are no known bugs in the project at the time of project submission. I made it a priority to quickly address and resolve any issues that came up during development. To see the fixes I implemented, you can check my [commit history](https://github.com/paulio11/P5-Pokebox-API/commits/main) for commits labeled with the "Fix" prefix. The project is in a solid and dependable state for evaluation and the end-user.

[Back to top 🔺](#pokébox-backend--api)

## Testing

Testing information can be found [here](https://github.com/paulio11/P5-Pokebox-API/blob/main/TESTING.md).

[Back to top 🔺](#pokébox-backend--api)

## Deployment

Deployment steps can be found [here](https://github.com/paulio11/P5-Pokebox-API/blob/main/DEPLOYMENT.md).

[Back to top 🔺](#pokébox-backend--api)

## Technologies

### Main Languages Used

- [Python](<https://en.wikipedia.org/wiki/Python_(programming_language)>)

### Frameworks

- [Django](https://www.djangoproject.com/) - A high-level Python web framework.
- [Django Rest Framework](https://www.django-rest-framework.org/) - A powerful and flexible toolkit for building Web APIs.

### Libraries

- [dj-database-url](https://pypi.org/project/dj-database-url/) - Enables the use of database URLs in Django. ElephantSQL provides an easy to use database URL which makes using this library essential.
- [django-cloudinary-storage](https://pypi.org/project/django-cloudinary-storage/) - A Django package that provides Cloudinary storage for both media and static files as well as management commands for removing unnecessary files. Images added to posts, user avatars and default avatars along with other static files are stored in Cloudinary.
- [django-resized](https://pypi.org/project/django-resized/) - Used to resize images uploaded by the user. This keeps the file size manageable, and crops avatars to a square so they display correctly on my front-end.
- [gunicorn](https://pypi.org/project/gunicorn/) - Gunicorn ‘Green Unicorn’ is a Python WSGI HTTP Server for UNIX.
- [Pillow](https://pypi.org/project/Pillow/) - A Python Imaging Library that adds image processing capabilities to the Python interpreter.
- [psycopg2](https://pypi.org/project/psycopg2/) - Psycopg is the most popular PostgreSQL database adapter for the Python programming language. Using a Postgres database was essential for this project as my profile model contains an ArrayField which is incompatible with the default sqlite database used by django.
- [Coverage](https://pypi.org/project/coverage/) - To check for 100% automated test coverage.
- [dj-rest-auth](https://dj-rest-auth.readthedocs.io/en/latest/) - Provides a set of API endpoints that handle user registration and authentication.
- [django-allauth](https://django-allauth.readthedocs.io/en/latest/) - An integrated set of Django applications addressing authentication, registration, account management as well as 3rd party (social) account authentication.
- [django-cors-headers](https://pypi.org/project/django-cors-headers/) - Adds Cross-Origin Resource Sharing (CORS) headers to responses. This allows in-browser requests to the Django application from other origins.
- [django-filter](https://django-filter.readthedocs.io/en/stable/) - Allows users to filter down a queryset based on a model’s fields, displayed as a form.
- [djangorestframework-simplejwt](https://pypi.org/project/djangorestframework-simplejwt/) - A JSON Web Token authentication plugin for the Django REST Framework.

### Other

- [ElephantSQL](https://www.elephantsql.com/) - Hosting of the PostgreSQL database used by squigl.
- [GitHub](https://github.com/) - Repository hosting, commit history and project management with user stories.
- [Heroku](https://heroku.com/) - Pokébox back-end API is deployed to Heroku.
- [Cloudinary](https://cloudinary.com/) - Hosting of images and other static files.
- [CI Python Linter](https://pep8ci.herokuapp.com/) - Used to validate my Python code.

[Back to top 🔺](#pokébox-backend--api)

## Credits

### Code

- This project was loosely based on Moments by [Code Institute](https://codeinstitute.net/), a project designed to teach Django Rest Framework and React. There are some code similarities, in particular:
  - [Logout Route View](https://github.com/paulio11/P5-Pokebox-API/blob/main/pokebox/views.py#L16) - This code acts as a fix for the DJ Rest Auth logout view present in the version being used.
  - [Get Like ID Function](https://github.com/paulio11/P5-Pokebox-API/blob/main/posts/serializers.py) - This returns the like object ID for the requested post if a user has liked it.
- The `IsOwnerOrReadOnly` permission class used for detail views is an example of a custom permission from the Rest Framework documentation. It can be found [here](https://www.django-rest-framework.org/api-guide/permissions/#examples).

[Back to top 🔺](#pokébox-backend--api)
