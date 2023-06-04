# Pokébox Backend / API

[Link to live API](https://project-5-backend.herokuapp.com/)

[Link to live Pokébox front-end](https://project-5-pokebox.herokuapp.com/)

[Link to Pokébox front-end repo](https://github.com/paulio11/project-5)

## Contents

## Introduction

## Project Planning

### GitHub Project

The GitHub project board feature was used to keep track of what I was working on and what still needed to be done. I created a user story for each feature, or an issue for each to do and bug, then moved them when necessary throughout the development of both front and back-end.

[Link to Project Board](https://github.com/users/paulio11/projects/4)

![GitHub Project Board](https://raw.githubusercontent.com/paulio11/project-5-backend/main/documentation/images/readme-projectboard.png)

### Database Schema

The models required for this project are:

- **Post** - for use diary entires.
- **Comment** - for replies to diary entries.
- **Like** - for user liking diary entries.
- **Profile** - for a user's profile information and Pokémon collection.

![Database Schema](https://raw.githubusercontent.com/paulio11/project-5-backend/main/documentation/images/readme-schema.png)

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

| Name     | Type              | Details                                                                                              | Notes                                                                                                                    |
| -------- | ----------------- | ---------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------ |
| id       | Primary Key       |                                                                                                      |                                                                                                                          |
| owner    | Foreign Key       | to User                                                                                              |                                                                                                                          |
| created  | DateTimeField     | auto_now_add=True                                                                                    | Date of creation, automatically added                                                                                    |
| about    | TextField         | max_length=400, blank=True, default="..."                                                            | Text field for a users description. Has the default text "Hello! I am a new trainer just starting my Pokémon adventure." |
| favorite | CharField         | max_length=30, blank=True                                                                            | Character field that will hold a users favorite Pokémon, assigned from a list of possibilities on the front end          |
| pokemon  | ArrayField        | Array of IntegerFields, default=list                                                                 | The array will hold pokemon collected by the user, each pokemon represented by their ID (an integer)                     |
| avatar   | ResizedImageField | upload_to="avatars/", size=[300, 300], crop=["middle", "center"], force_format="WEBP", default="..." | For the user's avatar, resized and cropped to a suitable size, has a default image                                       |

The profile object is automatically created for each new user using a `post_save` signal.

## Serializers

The django Rest Framework serializer component is used as an intermediary between the database models and the API views (see below). They provide fields in addition to those from the parent model, a method for creation, and can define which should be read only. Each model has it's own serializer:

### [Post Serializer](https://github.com/paulio11/project-5-backend/blob/main/posts/serializers.py)

The post serializer provides the following to the API view:

- **Owner** - This field uses the owner's username taken from the user model.
- **Created** - Provided by the function `get_created()` which returns a formatted date string.
- **Like ID** - Provided by the function `get_like_id()` which returns the ID of the Like object for the Post if the user has liked it. Used to show like status on the front end.
- **Profile ID** - Displays the post owner's profile ID. Used on the front end to link to the owner's profile when viewing the post.
- **Profile Avatar** - Displays the post owner's avatar. Used to represent the post owner on the front end.

### [Comment Serializer](https://github.com/paulio11/project-5-backend/blob/main/comments/serializers.py)

The comment serializer provides the following to the API view:

- **Owner** - This field uses the owner's username taken from the user model.
- **Created** - Provided by the function `get_created()` which returns a formatted date string.
- **Profile ID** - Displays the comment owner's profile ID. Used on the front end to link to the owner's profile when viewing the comment.
- **Profile Avatar** - Displays the comment owner's avatar. Used to represent the comment owner on the front end.

### [Like Serializer](https://github.com/paulio11/project-5-backend/blob/main/likes/serializers.py)

The like serializer provides the following to the API view:

- **Owner** - This field uses the owner's username taken from the user model.
- **`create()`** - This function handles the integrity error if a duplicate like object is found. This is to stop the same user liking a post more than once.

### [Profile Serializer](https://github.com/paulio11/project-5-backend/blob/main/profiles/serializers.py)

The profile serializer provides the following to the API view:

- **Owner** - This field uses the owner's username taken from the user model.
- **Created** - Provided by the function `get_created()` which returns a formatted date string.
- **Pokemon** - Defines this field as a list that can be empty.

### [CurrentUser Serializer](https://github.com/paulio11/project-5-backend/blob/main/pokebox/serializers.py)

Defined by `REST_AUTH_SERIALIZERS` variable in settings. The current user serializer extends DJ Rest Auth's UserDetailsSerializer to provide this additional information:

- **Profile ID** - Provides the current user's profile ID, used on the front-end to provide a link to their profile.

## Views

Each view provides a response to the front-end based on the request. They are responsible for generating the appropriate JSON output using the defined serializer and asigning correct permissions.

### [Post Views](https://github.com/paulio11/project-5-backend/blob/main/posts/views.py)

- **`PostList()` and `PostDetail()`**
  - Inherits from the `generics.ListCreateAPIView` class. It specifies the serializer class as `PostSerializer` and the permission classes as `permissions.IsAuthenticatedOrReadOnly`.
  - The `queryset` attribute is set to retrieve a list of Post objects from the database. The queryset is annotated with the counts of distinct likes and comments for each post and ordered by the creation date in descending order.
  - Specifies two filter backends: `filters.OrderingFilter` and `DjangoFilterBackend`. The `ordering_fields` attribute defines the fields that can be used for ordering the posts, which include like_count, comment_count, and created. The `filterset_class` attribute is set to PostFilter (see below).
  - The `perform_create()` method is overridden to set the owner of a newly created post to the authenticated user making the request.
- **`PostFilter()`**
  - Inherits from `rest_framework.FilterSet`. It is used to create a filters for the Post model.
  - Defines the `has_image` filter as a `rest_framework.BooleanFilter`. This filter is associated with the image field of the Post model.
  - Returns a filtered queryset that excludes posts with an empty image field. If the value is False or None, it returns the original queryset without applying any filtering.

### [Comment Views](https://github.com/paulio11/project-5-backend/blob/main/comments/views.py)

- **`CommentList()` and `CommentDetail()`**
  - Like the Post views these two views define the relevant serializer and permissions for the comment model and overrides comment creation to provide the logged in user as owner.
  - The `get_queryset()` method is overridden to provide a custom queryset for retrieving comments. It retrieves all comments using `Comment.objects.all()` and then checks if a post parameter is present in the request's query parameters. If the post parameter exists, it uses the `get_object_or_404()` function to retrieve the corresponding Post object. It then filters the comments queryset to only include comments associated with that particular post.

### [Like Views](https://github.com/paulio11/project-5-backend/blob/main/likes/views.py)

- **`LikeList()` and `LikeDetail()`**
  - As above these views define the relevant serializer and permissions for the Like model and overrides like creation to provided the logged in user as owner.

### [Profile Views](https://github.com/paulio11/project-5-backend/blob/main/profiles/views.py)

- **`ProfileList()` and `ProfileDetail()`**
  - Again defines the relevant serializer and permissions for the Profile model.
  - The `get_queryset()` method is overridden to provide a custom queryset for retrieving profiles. First, the `super().get_queryset()` is called to retrieve the initial queryset. Then, the method checks for optional query parameters in the request to sort or filter the profiles.
  - If the `owner` parameter is present in the request's query parameters, it uses the `get_object_or_404()` function to retrieve the corresponding User object and filters the queryset to only include profiles associated with that owner.
  - If `sort_by` is set to "pokemon", it changes it to "pokemon**len" to sort by the length of the Pokemon field. If `sort_by` is set to "owner", it changes it to "owner**username" to sort by the username of the owner.
  - If `sort_order` is set to "desc", it adds a "-" prefix to the `sort_by` parameter to indicate descending order.
  - Finally, the queryset is sorted using the `order_by` method based on the `sort_by` parameter and returned as the final result.

### [Other](https://github.com/paulio11/project-5-backend/blob/main/pokebox/views.py)

- **`root_route()`**
  - Overrides the home root of the API, displays a message.
- **`logout_route()`**
  - This view sends a response that sets the two cookies used for authentication as empty. This effectively logs out the user. This is a fix for the DJ Rest Auth logout view present in the version being used.

## Permissions

## Project Settings

The following are the non-default variables defined in [settings.py](https://github.com/paulio11/project-5-backend/blob/main/pokebox/settings.py):

### Cloudinary

- `CLOUDINARY_STORAGE`: Contains the Cloudinary URL.
- `DEFAULT_FILE_STORAGE`: Specifies the default file storage as Cloudinary.
- `MEDIA_URL`: Defines the URL path for media files.

### Django-Resized

- `DJANGORESIZED_DEFAULT_QUALITY`: Sets the default quality for resized images.
- `DJANGORESIZED_DEFAULT_KEEP_META`: Specifies whether to keep metadata for resized images.

### Allauth / dj-rest-auth

- `SITE_ID`: Identifies the Django site.
- `OLD_PASSWORD_FIELD_ENABLED`: Enables the use of the old password field.

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

## Testing

## Deployment

## Technologies

## Credits
