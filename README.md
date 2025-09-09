# vWebCloner

**vWebCloner** is a project designed for hosting login pages or forms and capturing submitted data directly to your local machine. The main goal is to clone login pages and collect credentials via phishing links for educational and testing purposes.

## How It Works

1. **Choose a Login Page:**  
   Select a login page you want to clone. Copy its URL and run the `clonner.py` script to fetch the HTML file of the page, or manually obtain the HTML using your browser's inspect feature.

2. **Modify the HTML:**  
   Make necessary changes to the HTML code to suit your needs. After editing, save the modified code in your `library` folder.

3. **Host the Page:**  
   When you want to host a login page, copy the desired HTML code and paste it into the `index.html` file.

4. **Run the Server:**  
   Start the server using `server.py`. The server will monitor `index.html` for username and password submissions.

5. **Credential Capture:**  
   When someone submits credentials, they are displayed in your terminal. You can use Cloudflare tunneling for remote access.

## Future Plans

- Expand the library of login pages and forms.
- Transform vWebCloner into a full-featured terminal tool.
- Automate the extraction and modification of raw HTML files for easier cloning.

> **Note:**  
> This project is for educational and ethical testing purposes only. Please ensure you have proper authorization before using it in any environment.

## Tech Stack

- **HTML**: Used for creating and customizing login pages/forms.
- **Python**: Powers the backend server (`server.py`) that handles form submissions and data capturing.
- **Bash**: Automates server setup, starting scripts, and Cloudflare tunneling for remote access.
