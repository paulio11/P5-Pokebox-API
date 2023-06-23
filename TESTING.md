# Testing

## Contents

1. [Validation](#validation)
2. [Automated Testing](#automated-testing)
3. [Manual Testing](#manual-testing)

## Validation

### Python Code ([CI Python Linter](https://pep8ci.herokuapp.com/))

All python files with code written by myself were run through the CI Python Linter. These are the results:

| File                                                                                                    | Result | Notes                      | Screenshot                                                                                                                         |
| ------------------------------------------------------------------------------------------------------- | ------ | -------------------------- | ---------------------------------------------------------------------------------------------------------------------------------- |
| [comments/admin.py](https://github.com/paulio11/P5-Pokebox-API/blob/main/comments/admin.py)             | ✓      | All clear, no errors found | [Screenshot](https://raw.githubusercontent.com/paulio11/P5-Pokebox-API/main/documentation/images/testing-comments-admin.png)       |
| [comments/models.py](https://github.com/paulio11/P5-Pokebox-API/blob/main/comments/models.py)           | ✓      | All clear, no errors found | [Screenshot](https://raw.githubusercontent.com/paulio11/P5-Pokebox-API/main/documentation/images/testing-comments-models.png)      |
| [comments/serializers.py](https://github.com/paulio11/P5-Pokebox-API/blob/main/comments/serializers.py) | ✓      | All clear, no errors found | [Screenshot](https://raw.githubusercontent.com/paulio11/P5-Pokebox-API/main/documentation/images/testing-comments-serializers.png) |
| [comments/tests.py](https://github.com/paulio11/P5-Pokebox-API/blob/main/comments/tests.py)             | ✓      | All clear, no errors found | [Screenshot](https://raw.githubusercontent.com/paulio11/P5-Pokebox-API/main/documentation/images/testing-comments-tests.png)       |
| [comments/urls.py](https://github.com/paulio11/P5-Pokebox-API/blob/main/comments/urls.py)               | ✓      | All clear, no errors found | [Screenshot](https://raw.githubusercontent.com/paulio11/P5-Pokebox-API/main/documentation/images/testing-comments-urls.png)        |
| [comments/views.py](https://github.com/paulio11/P5-Pokebox-API/blob/main/comments/views.py)             | ✓      | All clear, no errors found | [Screenshot](https://raw.githubusercontent.com/paulio11/P5-Pokebox-API/main/documentation/images/testing-comments-views.png)       |
| [likes/admin.py](https://github.com/paulio11/P5-Pokebox-API/blob/main/likes/admin.py)                   | ✓      | All clear, no errors found | [Screenshot](https://raw.githubusercontent.com/paulio11/P5-Pokebox-API/main/documentation/images/testing-likes-admin.png)          |
| [likes/models.py](https://github.com/paulio11/P5-Pokebox-API/blob/main/likes/models.py)                 | ✓      | All clear, no errors found | [Screenshot](https://raw.githubusercontent.com/paulio11/P5-Pokebox-API/main/documentation/images/testing-likes-models.png)         |
| [likes/serializers.py](https://github.com/paulio11/P5-Pokebox-API/blob/main/likes/serializers.py)       | ✓      | All clear, no errors found | [Screenshot](https://raw.githubusercontent.com/paulio11/P5-Pokebox-API/main/documentation/images/testing-likes-serializers.png)    |
| [likes/tests.py](https://github.com/paulio11/P5-Pokebox-API/blob/main/likes/tests.py)                   | ✓      | All clear, no errors found | [Screenshot](https://raw.githubusercontent.com/paulio11/P5-Pokebox-API/main/documentation/images/testing-likes-tests.png)          |
| [likes/urls.py](https://github.com/paulio11/P5-Pokebox-API/blob/main/likes/urls.py)                     | ✓      | All clear, no errors found | [Screenshot](https://raw.githubusercontent.com/paulio11/P5-Pokebox-API/main/documentation/images/testing-likes-urls.png)           |
| [likes/views.py](https://github.com/paulio11/P5-Pokebox-API/blob/main/likes/views.py)                   | ✓      | All clear, no errors found | [Screenshot](https://raw.githubusercontent.com/paulio11/P5-Pokebox-API/main/documentation/images/testing-likes-views.png)          |
| [news/admin.py](https://github.com/paulio11/P5-Pokebox-API/blob/main/news/admin.py)                     | ✓      | All clear, no errors found | [Screenshot](https://raw.githubusercontent.com/paulio11/P5-Pokebox-API/main/documentation/images/testing-news-admin.png)           |
| [news/models.py](https://github.com/paulio11/P5-Pokebox-API/blob/main/news/models.py)                   | ✓      | All clear, no errors found | [Screenshot](https://raw.githubusercontent.com/paulio11/P5-Pokebox-API/main/documentation/images/testing-news-models.png)          |
| [news/serializers.py](https://github.com/paulio11/P5-Pokebox-API/blob/main/news/serializers.py)         | ✓      | All clear, no errors found | [Screenshot](https://raw.githubusercontent.com/paulio11/P5-Pokebox-API/main/documentation/images/testing-news-serializers.png)     |
| [news/tests.py](https://github.com/paulio11/P5-Pokebox-API/blob/main/news/tests.py)                     | ✓      | All clear, no errors found | [Screenshot](https://raw.githubusercontent.com/paulio11/P5-Pokebox-API/main/documentation/images/testing-news-tests.png)           |
| [news/urls.py](https://github.com/paulio11/P5-Pokebox-API/blob/main/news/urls.py)                       | ✓      | All clear, no errors found | [Screenshot](https://raw.githubusercontent.com/paulio11/P5-Pokebox-API/main/documentation/images/testing-news-urls.png)            |
| [news/views.py](https://github.com/paulio11/P5-Pokebox-API/blob/main/news/views.py)                     | ✓      | All clear, no errors found | [Screenshot](https://raw.githubusercontent.com/paulio11/P5-Pokebox-API/main/documentation/images/testing-news-views.png)           |
| [pokebox/permissions.py](https://github.com/paulio11/P5-Pokebox-API/blob/main/pokebox/permissions.py)   | ✓      | All clear, no errors found | [Screenshot](https://raw.githubusercontent.com/paulio11/P5-Pokebox-API/main/documentation/images/testing-pokebox-permissions.png)  |
| [pokebox/serializers.py](https://github.com/paulio11/P5-Pokebox-API/blob/main/pokebox/serializers.py)   | ✓      | All clear, no errors found | [Screenshot](https://raw.githubusercontent.com/paulio11/P5-Pokebox-API/main/documentation/images/testing-pokebox-serializers.png)  |
| [pokebox/tests.py](https://github.com/paulio11/P5-Pokebox-API/blob/main/pokebox/tests.py)               | ✓      | All clear, no errors found | [Screenshot](https://raw.githubusercontent.com/paulio11/P5-Pokebox-API/main/documentation/images/testing-pokebox-tests.png)        |
| [pokebox/urls.py](https://github.com/paulio11/P5-Pokebox-API/blob/main/pokebox/urls.py)                 | ✓      | All clear, no errors found | [Screenshot](https://raw.githubusercontent.com/paulio11/P5-Pokebox-API/main/documentation/images/testing-pokebox-urls.png)         |
| [pokebox/views.py](https://github.com/paulio11/P5-Pokebox-API/blob/main/pokebox/views.py)               | ✓      | All clear, no errors found | [Screenshot](https://raw.githubusercontent.com/paulio11/P5-Pokebox-API/main/documentation/images/testing-pokebox-views.png)        |
| [posts/admin.py](https://github.com/paulio11/P5-Pokebox-API/blob/main/posts/admin.py)                   | ✓      | All clear, no errors found | [Screenshot](https://raw.githubusercontent.com/paulio11/P5-Pokebox-API/main/documentation/images/testing-posts-admin.png)          |
| [posts/models.py](https://github.com/paulio11/P5-Pokebox-API/blob/main/posts/models.py)                 | ✓      | All clear, no errors found | [Screenshot](https://raw.githubusercontent.com/paulio11/P5-Pokebox-API/main/documentation/images/testing-posts-models.png)         |
| [posts/serializers.py](https://github.com/paulio11/P5-Pokebox-API/blob/main/posts/serializers.py)       | ✓      | All clear, no errors found | [Screenshot](https://raw.githubusercontent.com/paulio11/P5-Pokebox-API/main/documentation/images/testing-posts-serializers.png)    |
| [posts/tests.py](https://github.com/paulio11/P5-Pokebox-API/blob/main/posts/tests.py)                   | ✓      | All clear, no errors found | [Screenshot](https://raw.githubusercontent.com/paulio11/P5-Pokebox-API/main/documentation/images/testing-posts-tests.png)          |
| [posts/urls.py](https://github.com/paulio11/P5-Pokebox-API/blob/main/posts/urls.py)                     | ✓      | All clear, no errors found | [Screenshot](https://raw.githubusercontent.com/paulio11/P5-Pokebox-API/main/documentation/images/testing-posts-urls.png)           |
| [posts/views.py](https://github.com/paulio11/P5-Pokebox-API/blob/main/posts/views.py)                   | ✓      | All clear, no errors found | [Screenshot](https://raw.githubusercontent.com/paulio11/P5-Pokebox-API/main/documentation/images/testing-posts-views.png)          |
| [profiles/admin.py](https://github.com/paulio11/P5-Pokebox-API/blob/main/profiles/admin.py)             | ✓      | All clear, no errors found | [Screenshot](https://raw.githubusercontent.com/paulio11/P5-Pokebox-API/main/documentation/images/testing-profiles-admin.png)       |
| [profiles/models.py](https://github.com/paulio11/P5-Pokebox-API/blob/main/profiles/models.py)           | ✓      | All clear, no errors found | [Screenshot](https://raw.githubusercontent.com/paulio11/P5-Pokebox-API/main/documentation/images/testing-profiles-models.png)      |
| [profiles/serializers.py](https://github.com/paulio11/P5-Pokebox-API/blob/main/profiles/serializers.py) | ✓      | All clear, no errors found | [Screenshot](https://raw.githubusercontent.com/paulio11/P5-Pokebox-API/main/documentation/images/testing-profiles-serializers.png) |
| [profiles/tests.py](https://github.com/paulio11/P5-Pokebox-API/blob/main/profiles/tests.py)             | ✓      | All clear, no errors found | [Screenshot](https://raw.githubusercontent.com/paulio11/P5-Pokebox-API/main/documentation/images/testing-profiles-tests.png)       |
| [profiles/urls.py](https://github.com/paulio11/P5-Pokebox-API/blob/main/profiles/urls.py)               | ✓      | All clear, no errors found | [Screenshot](https://raw.githubusercontent.com/paulio11/P5-Pokebox-API/main/documentation/images/testing-profiles-urls.png)        |
| [profiles/views.py](https://github.com/paulio11/P5-Pokebox-API/blob/main/profiles/views.py)             | ✓      | All clear, no errors found | [Screenshot](https://raw.githubusercontent.com/paulio11/P5-Pokebox-API/main/documentation/images/testing-profiles-views.png)       |

[Back to top 🔺](#testing)

## Automated Testing

My goal for automated testing was to reach 100% coverage using the Python library [Coverage](https://pypi.org/project/coverage/). 100% coverage was achieved excluding `manage.py` and `settings.py` as this is built in django code. I further developed each test to cover things usc has testing for login requirements and changes to the database. **See each test file for the full list of things tested for**.

**Note** - due to my profile model having an `ArrayField` which is incompatible with the default testing database engine (sqlite3), I had to temporarily remove all references to this field and `col_size` (in profiles/models.py, profiles/serializers.py and profiles/views.py) in order to make the tests run. The ArrayField was manually tested instead.

### Terminal Test Output

![Terminal test output](https://raw.githubusercontent.com/paulio11/P5-Pokebox-API/main/documentation/images/testing-terminaltestresults.png)

### Coverage Report

![Coverage report](https://raw.githubusercontent.com/paulio11/P5-Pokebox-API/main/documentation/images/testing-coveragereport.png)

**The following tests were carried out:**

### [comments.tests.py](https://github.com/paulio11/P5-Pokebox-API/blob/main/comments/tests.py)

| Name                                        | Testing For                                                      | Result |
| ------------------------------------------- | ---------------------------------------------------------------- | ------ |
| **CommentListTests**                        |
| test_get_comment_list                       | Endpoint returns successfully with correct data                  | ✓      |
| test_get_comment_list_for_post              | Endpoint with post parameter returns only comments for that post | ✓      |
| test_perform_create_without_user            | Logged out users can't create a comment                          | ✓      |
| test_perform_create_with_user               | Logged in users can create a comment                             | ✓      |
| **CommentDetailTests**                      |
| test_invalid_comment_id                     | Invalid comment ID parameter returns a 404 response              | ✓      |
| test_valid_comment_id                       | Valid comment ID parameter returns a 200 response                | ✓      |
| test_user_can_edit_comment                  | A logged in user can edit their own comments                     | ✓      |
| test_user_cant_edit_someone_elses_comment   | A user can't edit a comment they don't own                       | ✓      |
| test_logged_out_user_cant_edit              | A logged out user can't edit a comment                           | ✓      |
| test_user_can_delete_comment                | A logged in user can delete their comments                       | ✓      |
| test_user_cant_delete_someone_elses_comment | A user can't delete a comment they don't own                     | ✓      |
| test_logged_out_user_cant_delete            | A logged out user can't delete a comment                         | ✓      |
| **CommentModelTests**                       |
| test_str_method                             | A created comment is represented by the correct string           | ✓      |

### [likes.tests.py](https://github.com/paulio11/P5-Pokebox-API/blob/main/likes/tests.py)

| Name                                     | Testing For                                               | Result |
| ---------------------------------------- | --------------------------------------------------------- | ------ |
| **LikeListTests**                        |
| test_get_like_list                       | Endpoint returns successfully with correct data           | ✓      |
| test_perform_create_without_user         | Logged out users can't create a like                      | ✓      |
| test_perform_create_with_user            | Logged in users can create a like                         | ✓      |
| **LikeDetailTests**                      |
| test_invalid_like_id                     | Invalid like ID parameter returns a 404 response          | ✓      |
| test_valid_like_id                       | Valid like ID parameter returns a 200 response            | ✓      |
| test_user_can_delete_like                | A logged in user can delete their likes                   | ✓      |
| test_user_cant_delete_someone_elses_like | A user can't delete a like they don't own                 | ✓      |
| test_logged_out_user_cant_delete_like    | A logged out user can't delete a comment                  | ✓      |
| **LikeModelTests**                       |
| test_str_method                          | A created like is represented by the correct string       | ✓      |
| **LikeSerializerTests**                  |
| test_create_duplicate_like               | User can't create duplicate likes, returns a 400 response | ✓      |

### [news.tests.py](https://github.com/paulio11/P5-Pokebox-API/blob/main/news/tests.py)

| Name                             | Testing For                                                                                                 | Result |
| -------------------------------- | ----------------------------------------------------------------------------------------------------------- | ------ |
| **NewsModelTests**               |
| test_str_method                  | A created news item is represented by the correct string                                                    | ✓      |
| **AnnouncementModelTests**       |
| test_str_method                  | A created announcement is represented by the correct string                                                 | ✓      |
| **NewsFilterTests**              |
| test_filter_off                  | Response returns all news objects                                                                           | ✓      |
| test_category_other              | Response returns just objects with the category Other                                                       | ✓      |
| test_category_anime              | Response returns just objects with the category Anime                                                       | ✓      |
| test_category_TCG                | Response returns just objects with the category TCG                                                         | ✓      |
| test_category_games              | Response returns just objects with the category Games                                                       | ✓      |
| test_id_filter                   | Response returns just the news item requested in the url parameter                                          | ✓      |
| **NewsListTests**                |
| test_get_news_list               | Endpoint returns successfully with correct data                                                             | ✓      |
| test_perform_create_without_user | Attempting to create a news item logged out fails and returns response 403                                  | ✓      |
| test_perform_create_with_user    | Attempting to create a news item when logged in as a normal user fails and returns response 403             | ✓      |
| test_perform_create_with_admin   | Attempting to create a news item when logged in as an admin is successful and returns response 201          | ✓      |
| **NewsDetailTests**              |
| test_invalid_news_id             | Invalid news ID parameter returns a 404 response                                                            | ✓      |
| test_valid_news_id               | Valid post ID parameter returns a 200 response                                                              | ✓      |
| test_no_user_cant_edit           | Editing a news item when logged out returns a 403 response and fails                                        | ✓      |
| test_user_cant_edit              | Editing a news item as a normal user returns a 403 response and fails                                       | ✓      |
| test_admin_can_edit              | Editing a news item as an admin user returns a 200 response and successfully updates                        | ✓      |
| test_no_user_cant_delete         | Deleting a news item when logged out returns a 403 response and fails                                       | ✓      |
| test_user_cant_delete            | Deleting a news item as a normal user returns a 403 response and fails                                      | ✓      |
| test_admin_can_delete            | Deleting a news item as an admin user returns a 200 response and successfully deletes                       | ✓      |
| **AnnouncementListTests**        |
| test_get_announcement_list       | Endpoint returns successfully with correct data                                                             | ✓      |
| test_perform_create_without_user | Attempting to create an announcement logged out fails and returns response 403                              | ✓      |
| test_perform_create_with_user    | Attempting to create an announcement when logged in as a normal user fails and returns response 403         | ✓      |
| test_perform_create_with_admin   | Attempting to create an announcement when logged in as an admin user is successful and returns response 201 | ✓      |
| **AnnouncementDetailTests**      |
| test_invalid_announcement_id     | Invalid announcement ID parameter returns a 404 response                                                    | ✓      |
| test_valid_announcement_id       | Valid announcement ID parameter resturns a 200 response                                                     | ✓      |
| test_no_user_cant_edit           | Editing an announcement when logged out returns a 403 response and fails                                    | ✓      |
| test_user_cant_edit              | Editing an announcement as a normal user returns a 403 response and fails                                   | ✓      |
| test_admin_can_edit              | Editing an announcement as an admin user returns a 200 response and successfully updates                    | ✓      |
| test_no_user_cant_delete         | Deleting an announcement when logged out returns a 403 response and fails                                   | ✓      |
| test_user_cant_delete            | Deleting an announcement as a normal user returns a 403 response and fails                                  | ✓      |
| test_admin_can_delete            | Deleting an announcement as an admin user returns a 200 response and successfully deletes                   | ✓      |

### [pokebox.tests.py](https://github.com/paulio11/P5-Pokebox-API/blob/main/pokebox/tests.py)

| Name                    | Testing For                                                   | Result |
| ----------------------- | ------------------------------------------------------------- | ------ |
| **RootRouteTests**      |
| test_root_route         | Root route shows message                                      | ✓      |
| **LogoutRouteTests**    |
| test_logout_route       | Correct response and cookies and their attributes are cleared | ✓      |
| **UserSerializerTests** |
| test_user_is_not_staff  | The serialized data for user has the value False for is_staff | ✓      |
| test_admin_is_staff     | The serialized data for admin has the value True for is_staff | ✓      |

### [posts.tests.py](https://github.com/paulio11/P5-Pokebox-API/blob/main/posts/tests.py)

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

### [profiles.tests.py](https://github.com/paulio11/P5-Pokebox-API/blob/main/profiles/tests.py)

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

[Back to top 🔺](#testing)

## Manual Testing

In addition to automated testing I carried out the manual tests below for aspects not covered with automated testing, note this is also covered in manual front-end testing.

### Profiles

| Test                                                                                | Result | Link To Result                                                                      |
| ----------------------------------------------------------------------------------- | ------ | ----------------------------------------------------------------------------------- |
| Profiles can be ordered by the owner's username in ascending order                  | ✓      | [Link](https://project-5-backend.herokuapp.com/profiles/?ordering=owner__username)  |
| Profiles can be ordered by the owner's username in descending order                 | ✓      | [Link](https://project-5-backend.herokuapp.com/profiles/?ordering=-owner__username) |
| Profiles can be ordered by their creation date in ascending order                   | ✓      | [Link](https://project-5-backend.herokuapp.com/profiles/?ordering=created)          |
| Profiles can be ordered by their creation date in descending order                  | ✓      | [Link](https://project-5-backend.herokuapp.com/profiles/?ordering=-created)         |
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

| Test                                                           | Result | Link To Result                                            |
| -------------------------------------------------------------- | ------ | --------------------------------------------------------- |
| Comments are sorted by their creation date in descending order | ✓      | [Link](https://project-5-backend.herokuapp.com/comments/) |

### Pokemon ArrayField in Profile Model

This field was manually tested due to the issues mentioned [above](#automated-testing).

| Test                                    | Result | Link To Screenshot                                                                                                    |
| --------------------------------------- | ------ | --------------------------------------------------------------------------------------------------------------------- |
| Only integers can be added to the array | ✓      | [Screenshot](https://raw.githubusercontent.com/paulio11/P5-Pokebox-API/main/documentation/images/testing-array-1.png) |
| Array can be empty                      | ✓      | [Screenshot](https://raw.githubusercontent.com/paulio11/P5-Pokebox-API/main/documentation/images/testing-array-2.png) |

[Back to top 🔺](#testing)
