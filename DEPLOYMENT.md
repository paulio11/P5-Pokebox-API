# Deployment

To further develop this project, a copy can be made using the following steps:

## ElephantSQL - Database

My database is hosted on [ElephantSQL](https://www.elephantsql.com/). But you could host your PostgreSQL database wherever. These steps outline the process of the creation of a new database on ElephantSQL.

1. [Login](https://customer.elephantsql.com/login) or [sign up](https://customer.elephantsql.com/signup) to ElephantSQL.
2. Once you have an account click the green **Create New Instance** button, or click [here](https://customer.elephantsql.com/instance/create).
3. Name your database.
4. Keep the default plan selected. The **Tiny Turtle (Free)** plan is adequate.
5. Click the green **Select Region** button.
6. Choose a region local to you.
7. Click the green **Review** button.
8. Confirm the shown details are correct then finish by clicking the green **Create Instance** button.
9. From the list of instances select your newly created database.
10. Make note of the **URL** - you will need this later.

## Cloudinary - Static and Media Files

Static and media files are hosted on Cloudinary, an online host and API provider for all kinds of media adjustments.

1. [Login](https://cloudinary.com/users/login) or [sign up](https://cloudinary.com/users/register_free) to Cloudinary.
2. Navigate to your **Dashboard**.
3. Make note of your **API Environment Variable** for later.

## Copying My Repository

Forking will create a copy of my original repository on your own GitHub account.

1. [Login](https://github.com/login) or [sign up](https://github.com/join) to GitHub.
2. Locate [this](https://github.com/paulio11/P5-Pokebox-API) GitHub repository.
3. Click the **Fork** button at the top right of the page.
4. You will now have a copy on your GitHub account.

## GitPod

If you want to edit any of the files I would suggest using Gitpod - a browser based IDE.

1. Install the [Gitpod](https://www.gitpod.io/docs/browser-extension/) browser extension.
2. Locate your copy of the repository.
3. Click the new green **GitPod** button above the file list.
4. [Login](https://gitpod.io/workspaces/) to Gitpod with your GitHub account.
5. Requirements will automatically be installed thanks to [requirements.txt](https://github.com/paulio11/P5-Pokebox-API/blob/main/requirements.txt).
6. In the terminal window type `touch env.py` to create your environmental variables file.
7. Enter the following into the empty **env.py** file:

```
import os


os.environ["DATABASE_URL"] = "Your Elephant SQL URL from earlier"
os.environ["SECRET_KEY"] = "Any secret key"
os.environ["CLOUDINARY_URL"] = "Your Cloudinary url from earlier (without the CLOUDINARY_URL= at the start)"
os.environ["DEV"] = "1" // "1" if you want to enable debug, "0" if not.
os.environ["DEV_ORIGIN"] = "http://localhost:3000" // if running the front-end server locally
os.environ["ALLOWED_HOST"] = "Your deployed back-end Heroku app URL"
os.environ["CLIENT_ORIGIN"] = "Your deployed front-end Heroku app URL"
```

8. Before you commit any changes back to GitHub remember to create a **.gitignore** file by typing `touch .gitignore` into the terminal.
9. Add `env.py` to **.gitignore**.
10. To set up your database type `python manage.py makemigrations` in the terminal, then `python manage.py migrate`.
11. Type `python manage.py createsuperuser` into the terminal window and follow the instructions to create your first admin user.
12. To run the server type `python manage.py runserver`.

## Heroku

Pokébox API is currently deployed to Heroku. Follow these steps if you want to deploy your copy.

1. [Login](https://id.heroku.com/login) or [sign up]() to Heroku.
2. Once on your [Dashboard](https://dashboard.heroku.com/apps), click the **New** and **Create New App** buttons.
3. Enter a name for your app and your local region.
4. Click **Create App**.
5. Click **Settings**.
6. Click **Reveal Config Vars**.
7. Enter the following environmental variables - these are the same as in **env.py** if you followed the Gitpod steps:

| Key            | Value                                                                                                              |
| -------------- | ------------------------------------------------------------------------------------------------------------------ |
| DATABASE_URL   | Your ElephantSQL URL from earlier                                                                                  |
| SECRET_KEY     | Any secret key                                                                                                     |
| CLOUDINARY_URL | Your Cloudinary URL from earlier (without the CLOUDINARY_URL= at the start)                                        |
| ALLOWED_HOST   | Your deployed back-end Heroku app URL (example: `project-5-backend.herokuapp.com`)                                 |
| CLIENT_ORIGIN  | Your deployed front-end Heroku app URL including the protocol (example: `https://project-5-pokebox.herokuapp.com`) |

8. Click **Deploy** from the menu.
9. Click **GitHub - Connect to GitHub**, and if prompted to login to GitHub.
10. In the **repo-name** box type the name of your fork from earlier.
11. Click **Search**.
12. Click **Connect** next to the correct repository.
13. Scroll to the bottom and click **Deploy Branch**.
14. Pay attention to the log and look out for any errors.
15. If it was successful your app will now be live.
