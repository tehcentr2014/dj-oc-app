## BlogGenerator


### Overview
The BlogGenerator is a Django App designed to aid in the automatic generation of blog ideas and blog descriptions using OpenAI Assistans API. This application simplifies the process by taking user-provided keywords and generating concise descriptions based on predefined criteria.

### Features
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

### Acknowledgments
- This project utilizes the OpenAI API for natural language processing.
- HTML template for landing page: SeoGram – Free Multipage Bootstrap 4 Landing Page Website Template
- HTML template for dashboard page: Sneat Dashboard PRO – Bootstrap 5 Template


