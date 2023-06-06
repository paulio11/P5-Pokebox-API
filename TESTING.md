# Testing

## Contents

1. [Validation](#validation)
2. [Automated Testing](#automated-testing)
3. [Manual Testing](#manual-testing)
4. [User Stories](#user-stories)

## Validation

### Python Code ([CI Python Linter](https://pep8ci.herokuapp.com/))

All python files with code written by myself were run through the CI Python Linter. These are the results:

| File                        | Result | Notes                      | Screenshot                                                                                                                            |
| --------------------------- | ------ | -------------------------- | ------------------------------------------------------------------------------------------------------------------------------------- |
| [comments/admin.py]()       | ✓      | All clear, no errors found | [Screenshot](https://raw.githubusercontent.com/paulio11/project-5-backend/main/documentation/images/testing-comments-admin.png)       |
| [comments/models.py]()      | ✓      | All clear, no errors found | [Screenshot](https://raw.githubusercontent.com/paulio11/project-5-backend/main/documentation/images/testing-comments-models.png)      |
| [comments/serializers.py]() | ✓      | All clear, no errors found | [Screenshot](https://raw.githubusercontent.com/paulio11/project-5-backend/main/documentation/images/testing-comments-serializers.png) |
| [comments/tests.py]()       | ✓      | All clear, no errors found | [Screenshot](https://raw.githubusercontent.com/paulio11/project-5-backend/main/documentation/images/testing-comments-tests.png)       |
| [comments/urls.py]()        | ✓      | All clear, no errors found | [Screenshot](https://raw.githubusercontent.com/paulio11/project-5-backend/main/documentation/images/testing-comments-urls.png)        |
| [comments/views.py]()       | ✓      | All clear, no errors found | [Screenshot](https://raw.githubusercontent.com/paulio11/project-5-backend/main/documentation/images/testing-comments-views.png)       |
| [likes/admin.py]()          | ✓      | All clear, no errors found | [Screenshot](https://raw.githubusercontent.com/paulio11/project-5-backend/main/documentation/images/testing-likes-admin.png)          |
| [likes/models.py]()         | ✓      | All clear, no errors found | [Screenshot](https://raw.githubusercontent.com/paulio11/project-5-backend/main/documentation/images/testing-likes-models.png)         |
| [likes/serializers.py]()    | ✓      | All clear, no errors found | [Screenshot](https://raw.githubusercontent.com/paulio11/project-5-backend/main/documentation/images/testing-likes-serializers.png)    |
| [likes/tests.py]()          | ✓      | All clear, no errors found | [Screenshot](https://raw.githubusercontent.com/paulio11/project-5-backend/main/documentation/images/testing-likes-tests.png)          |
| [likes/urls.py]()           | ✓      | All clear, no errors found | [Screenshot](https://raw.githubusercontent.com/paulio11/project-5-backend/main/documentation/images/testing-likes-urls.png)           |
| [likes/views.py]()          | ✓      | All clear, no errors found | [Screenshot](https://raw.githubusercontent.com/paulio11/project-5-backend/main/documentation/images/testing-likes-views.png)          |
| [pokebox/permissions.py]()  | ✓      | All clear, no errors found | [Screenshot](https://raw.githubusercontent.com/paulio11/project-5-backend/main/documentation/images/testing-pokebox-permissions.png)  |
| [pokebox/serializers.py]()  | ✓      | All clear, no errors found | [Screenshot](https://raw.githubusercontent.com/paulio11/project-5-backend/main/documentation/images/testing-pokebox-serializers.png)  |
| [pokebox/tests.py]()        | ✓      | All clear, no errors found | [Screenshot](https://raw.githubusercontent.com/paulio11/project-5-backend/main/documentation/images/testing-pokebox-tests.png)        |
| [pokebox/urls.py]()         | ✓      | All clear, no errors found | [Screenshot](https://raw.githubusercontent.com/paulio11/project-5-backend/main/documentation/images/testing-pokebox-urls.png)         |
| [pokebox/views.py]()        | ✓      | All clear, no errors found | [Screenshot](https://raw.githubusercontent.com/paulio11/project-5-backend/main/documentation/images/testing-pokebox-views.png)        |
| [posts/admin.py]()          | ✓      | All clear, no errors found | [Screenshot](https://raw.githubusercontent.com/paulio11/project-5-backend/main/documentation/images/testing-posts-admin.png)          |
| [posts/models.py]()         | ✓      | All clear, no errors found | [Screenshot](https://raw.githubusercontent.com/paulio11/project-5-backend/main/documentation/images/testing-posts-models.png)         |
| [posts/serializers.py]()    | ✓      | All clear, no errors found | [Screenshot](https://raw.githubusercontent.com/paulio11/project-5-backend/main/documentation/images/testing-posts-serializers.png)    |
| [posts/tests.py]()          | ✓      | All clear, no errors found | [Screenshot](https://raw.githubusercontent.com/paulio11/project-5-backend/main/documentation/images/testing-posts-tests.png)          |
| [posts/urls.py]()           | ✓      | All clear, no errors found | [Screenshot](https://raw.githubusercontent.com/paulio11/project-5-backend/main/documentation/images/testing-posts-urls.png)           |
| [posts/views.py]()          | ✓      | All clear, no errors found | [Screenshot](https://raw.githubusercontent.com/paulio11/project-5-backend/main/documentation/images/testing-posts-views.png)          |
| [profiles/admin.py]()       | ✓      | All clear, no errors found | [Screenshot](https://raw.githubusercontent.com/paulio11/project-5-backend/main/documentation/images/testing-profiles-admin.png)       |
| [profiles/models.py]()      | ✓      | All clear, no errors found | [Screenshot](https://raw.githubusercontent.com/paulio11/project-5-backend/main/documentation/images/testing-profiles-models.png)      |
| [profiles/serializers.py]() | ✓      | All clear, no errors found | [Screenshot](https://raw.githubusercontent.com/paulio11/project-5-backend/main/documentation/images/testing-profiles-serializers.png) |
| [profiles/tests.py]()       | ✓      | All clear, no errors found | [Screenshot](https://raw.githubusercontent.com/paulio11/project-5-backend/main/documentation/images/testing-profiles-tests.png)       |
| [profiles/urls.py]()        | ✓      | All clear, no errors found | [Screenshot](https://raw.githubusercontent.com/paulio11/project-5-backend/main/documentation/images/testing-profiles-urls.png)        |
| [profiles/views.py]()       | ✓      | All clear, no errors found | [Screenshot](https://raw.githubusercontent.com/paulio11/project-5-backend/main/documentation/images/testing-profiles-views.png)       |

## Automated Testing

My goal for automated testing was to reach 100% coverage using the Python library [Coverage](https://pypi.org/project/coverage/). 100% coverage was achieved excluding `manage.py` and `settings.py` as this is built in django code. I further developed each test to cover things usc has testing for login requirements and changes to the database. **See each test file for the full list of things tested for**.

Note - due to my profile model having an ArrayField which is incompatible with the default testing database engine (sqlite3), I had to temporarily remove all references to this field in order to make the tests run. The ArrayField was manually tested instead.

### Terminal Test Output

![Terminal test output](https://raw.githubusercontent.com/paulio11/project-5-backend/main/documentation/images/testing-terminaltestresults.png)

### Coverage Report

![Coverage report](https://raw.githubusercontent.com/paulio11/project-5-backend/main/documentation/images/testing-coveragereport.png)

**The following tests were carried out:**

### [comments.tests.py](https://github.com/paulio11/project-5-backend/blob/main/comments/tests.py)

| Name                                        | Testing For                                                      | Result |
| ------------------------------------------- | ---------------------------------------------------------------- | ------ |
| **CommentListTests**                        |
| test_get_comment_list                       | Endpoint returns successfully with correct data                  | ✓      |
| test_get_comment_list_for_post              | Endpoint with post parameter returns only comments for that post | ✓      |
| test_perform_create_without_user            | Logged out users can't create a comment                          | ✓      |
| test_perform_create_with_user               | Logged in users can create a comment                             | ✓      |
| **CommentDetailTests**                      |
| test_invalid_comment_id                     | Invalid comment ID parameter returns a 404 response              | ✓      |
| test_valid_comment_id                       | Valid comment ID parameter returns a 200 reponse                 | ✓      |
| test_user_can_edit_comment                  | A logged in user can edit their own comments                     | ✓      |
| test_user_cant_edit_someone_elses_comment   | A user can't edit a comment they don't own                       | ✓      |
| test_logged_out_user_cant_edit              | A logged out user can't edit a comment                           | ✓      |
| test_user_can_delete_comment                | A logged in user can delete their comments                       | ✓      |
| test_user_cant_delete_someone_elses_comment | A user can't delete a comment they don't own                     | ✓      |
| test_logged_out_user_cant_delete            | A logged out user can't delete a comment                         | ✓      |
| **CommentModelTests**                       |
| test_str_method                             | A created comment is represented by the correct string           | ✓      |

### [likes.tests.py](https://github.com/paulio11/project-5-backend/blob/main/likes/tests.py)

| Name                                     | Testing For                                               | Result |
| ---------------------------------------- | --------------------------------------------------------- | ------ |
| **LikeListTests**                        |
| test_get_like_list                       | Endpoint returns successfully with correct data           | ✓      |
| test_perform_create_without_user         | Logged out users can't create a like                      | ✓      |
| test_perform_create_with_user            | Logged in users can create a like                         | ✓      |
| **LikeDetailTests**                      |
| test_invalid_like_id                     | Invalid like ID parameter returns a 404 response          | ✓      |
| test_valid_like_id                       | Valid like ID parameter returns a 200 reponse             | ✓      |
| test_user_can_delete_like                | A logged in user can delete their likes                   | ✓      |
| test_user_cant_delete_someone_elses_like | A user can't delete a like they don't own                 | ✓      |
| test_logged_out_user_cant_delete_like    | A logged out user can't delete a comment                  | ✓      |
| **LikeModelTests**                       |
| test_str_method                          | A created like is represented by the correct string       | ✓      |
| **LikeSerializerTests**                  |
| test_create_duplicate_like               | User can't create duplicate likes, returns a 400 response | ✓      |

### [pokebox.tests.py](https://github.com/paulio11/project-5-backend/blob/main/pokebox/tests.py)

| Name                 | Testing For                                                   | Result |
| -------------------- | ------------------------------------------------------------- | ------ |
| **RootRouteTests**   |
| test_root_route      | Root route shows message                                      | ✓      |
| **LogoutRouteTests** |
| test_logout_route    | Correct response and cookies and their attributes are cleared | ✓      |

### [posts.tests.py](https://github.com/paulio11/project-5-backend/blob/main/posts/tests.py)

| Name                                            | Testing For                                                                       | Result |
| ----------------------------------------------- | --------------------------------------------------------------------------------- | ------ |
| **PostListTests**                               |
| test_get_post_list                              | Endpoint returns successfully with correct data                                   | ✓      |
| test_perform_create_without_user                | Logged out users can't create a post                                              | ✓      |
| test_perform_create_with_user                   | Logged in users can create a post                                                 | ✓      |
| **PostDetailTests**                             |
| test_invalid_post_id                            | Invalid post ID parameter returns a 404 response                                  | ✓      |
| test_valid_post_id                              | Valid post ID parameter returns a 200 response                                    | ✓      |
| test_user_can_edit_post                         | A logged in user can edit their posts                                             | ✓      |
| test_user_cant_edit_someone_elses_post          | A user can't edit posts they don't own                                            | ✓      |
| test_logged_out_user_cant_edit                  | A logged out user can't edit a post                                               | ✓      |
| test_user_can_delete_post                       | A logged in user can delete their posts                                           | ✓      |
| test_user_cant_delete_someone_elses_post        | A user can't delete posts they don't own                                          | ✓      |
| test_logged_out_user_cant_delete                | A logged out user can't delete a post                                             | ✓      |
| **PostFilterTests**                             |
| test_filter_off                                 | Response returns all post instances                                               | ✓      |
| test_filter_has_image                           | Response returns only posts with an image                                         | ✓      |
| test_filter_owner                               | Response returns only posts by specified owner                                    | ✓      |
| test_liked_filter                               | Response returns only posts liked by specified user                               | ✓      |
| test_filter_returned_queryset_if_value_is_true  | Filtered queryset only contains posts with images                                 | ✓      |
| test_filter_returned_queryset_if_value_is_false | Filtered queryset is unchanged                                                    | ✓      |
| **PostModelTests**                              |
| test_str_method                                 | A created post is represented by the correct string                               | ✓      |
| **PostSerializerTests**                         |
| test_get_like_id                                | Serializer displays like ID for logged in user if they have liked the post        | ✓      |
| test_get_like_id_when_none                      | Serializer displays no like ID for logged in user if they have not liked the post | ✓      |

### [profiles.tests.py](https://github.com/paulio11/project-5-backend/blob/main/profiles/tests.py)

| Name                                        | Testing For                                            | Result |
| ------------------------------------------- | ------------------------------------------------------ | ------ |
| **ProfileListTests**                        |
| test_profile_creation                       | A profile is created when a new user is created        | ✓      |
| test_profile_list                           | Endpoint returns successfully with correct data        | ✓      |
| **ProfileDetailTests**                      |
| test_invalid_profile_id                     | Invalid profile ID parameter returns a 404 response    | ✓      |
| test_valid_profile_id                       | Valid profile ID parameter returns a 200 response      | ✓      |
| test_user_can_update_profile                | A logged in user can edit their profile                | ✓      |
| test_user_cant_update_someone_elses_profile | A user can't edit a profile they don't own             | ✓      |
| **ProfileModelTests**                       |
| test_str_method                             | A created profile is represented by the correct string | ✓      |

## Manual Testing

In addition to automated testing I carried out the following manual tests for aspects not covered:

### Profiles

| Test                                                                                | Result | Link To Result                                                                      |
| ----------------------------------------------------------------------------------- | ------ | ----------------------------------------------------------------------------------- |
| Profiles can be ordered by the owner's username in ascending order                  | ✓      | [Link](https://project-5-backend.herokuapp.com/profiles/?ordering=owner__username)  |
| Profiles can be ordered by the owner's username in descending order                 | ✓      | [Link](https://project-5-backend.herokuapp.com/profiles/?ordering=-owner__username) |
| Profiles can be ordered by their creation date in ascending order                   | ✓      | [Link](https://project-5-backend.herokuapp.com/profiles/?ordering=created)          |
| Profiles can be ordered by theor creation date in descending order                  | ✓      | [Link](https://project-5-backend.herokuapp.com/profiles/?ordering=-created)         |
| Profiles can be ordered by the size of their Pokémon collection in ascending order  | ✓      | [Link](https://project-5-backend.herokuapp.com/profiles/?ordering=col_size)         |
| Profiles can be ordered by the size of their Pokémon collection in descending order | ✓      | [Link](https://project-5-backend.herokuapp.com/profiles/?ordering=-col_size)        |
| Profiles can be filtered by the owner's username - Example: **"ash"**               | ✓      | [Link](https://project-5-backend.herokuapp.com/profiles/?owner__username=ash)       |

### Posts

| Test                                                            | Result | Link To Result                                                                 |
| --------------------------------------------------------------- | ------ | ------------------------------------------------------------------------------ |
| Posts can be ordered by their like count in ascending order     | ✓      | [Link](https://project-5-backend.herokuapp.com/posts/?ordering=like_count)     |
| Posts can be ordered by their like count in descending order    | ✓      | [Link](https://project-5-backend.herokuapp.com/posts/?ordering=-like_count)    |
| Posts can be ordered by their comment count in ascending order  | ✓      | [Link](https://project-5-backend.herokuapp.com/posts/?ordering=comment_count)  |
| Posts can be ordered by their comment count in descending order | ✓      | [Link](https://project-5-backend.herokuapp.com/posts/?ordering=-comment_count) |
| Posts can be ordered by their creation date in ascending order  | ✓      | [Link](https://project-5-backend.herokuapp.com/posts/?ordering=created)        |
| Posts can be ordered by their creation date in descending order | ✓      | [Link](https://project-5-backend.herokuapp.com/posts/?ordering=-created)       |

### Comments

| Test                                                          | Result | Link To Result                                            |
| ------------------------------------------------------------- | ------ | --------------------------------------------------------- |
| Comments are sorted by their creation date in desending order | ✓      | [Link](https://project-5-backend.herokuapp.com/comments/) |

## User Stories
