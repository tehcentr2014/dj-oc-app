## BlogGenerator

### Overview
The BlogGenerator is a Django App designed to aid in the automatic generation of blog ideas and blog descriptions using OpenAI Assistans API. This application simplifies the process by taking user-provided keywords and generating concise descriptions based on predefined criteria.

![1-4](https://github.com/user-attachments/assets/2cf7a9e0-cc57-4652-852e-4601018069da)


### Features
The BlogGenerator Django App has the starting Landing page and Dasboard section.

### Landing Page

- __Navigation Bar__

  - link to Home page
  - link to Login page

![1-3](https://github.com/user-attachments/assets/6cde5e22-70ad-4809-8eb4-7697ca50e714)

- __ABOUT US__

![image](https://github.com/user-attachments/assets/3c23385e-df21-4558-aea6-a68b8a0b9420)

### Login page:

![image](https://github.com/user-attachments/assets/06b61b79-e8cc-4e9e-944d-5fb00bb6bd89)

### Register page:

![image](https://github.com/user-attachments/assets/769002fb-6d33-4b16-ac71-132a02b0cb65)

### Dashboard interface:
- Dashboard main page
- My Profile link
- Blog Topic Generator
- Generated Blog Ideas
- Logout

![image](https://github.com/user-attachments/assets/a0d6ef77-cb79-4aec-9af4-2b04e2b89100)



- **Keywords Input**: Users can input keywords related to the blog idea for which they want to generate descriptions.
- **Sections Removal**: The application provides a functionality to remove previously generated blog ideas.
- **Blog Generation**: Using the previously generated blog ideas, the application generates detaled blog descriptions based on the blog idea, keywords and audience.

### Installation
1. Clone the repository:

    ```bash
    git clone <repository-url>
    ```

2. Install the required dependencies:

    ```bash
    pip install -r requirements.txt
    ```

3. Set up OpenAI API access by creating a `.env` file in the root directory and adding your OpenAI API key:

    ```
    OPENAI_API_KEY=<your-openai-api-key>
    ```

### Usage
1. Run the application:

    ```bash
    python main.py
    ```

2. Access the application through the provided URL in your browser.
3. Follow the on-screen instructions to enter keywords and generate blog ideas and descriptions.
4. Click the Blog Topic Generator button to initiate the blog ideas generation process.
5. Wait for the application to generate the blog ideas based on the provided keywords.
6. The generated blog ideas will be displayed on the interface.
6. Delete or choise the blog idea to generate detaled blog description and its will be displayed on the interface.

### Deployment
#### Heroku

*The App live link is: [https://cherry-leaves-5-4-67299393f5ab.herokuapp.com/](https://dj-oc-app-95fdf0716ca4.herokuapp.com/)
*Set the runtime.txt Python version 3.12.3 to a Heroku-22 stack currently supported version.
*The project was deployed to Heroku using the following steps:
- Log in to Heroku and create an App
- At the Deploy tab, select GitHub as the deployment method.
- Select your repository name and click Search. Once it is found, click Connect.
- Select the branch you want to deploy, then click Deploy Branch.
- The deployment process should happen smoothly if all deployment files are fully functional. Click the button Open App on the top of the page to access your App.
- If the slug size is too large, then add large files not required for the app to the .slugignore file.


### Acknowledgments
- This project utilizes the OpenAI API for natural language processing.
- HTML template for landing page: SeoGram – Free Multipage Bootstrap 4 Landing Page Website Template
- HTML template for dashboard page: Sneat Dashboard PRO – Bootstrap 5 Template


