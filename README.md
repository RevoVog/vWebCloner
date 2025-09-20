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


### Page Library Upto Now

In my libraty I have maintain following login pages all contain thair originl Metadata as well so it's difficult to identify in a browser tls/ssl certificates provided by cloudflair and hosting as https so un detectable if didn't check URl
#### My updated clones are iddentical to actual pages

- **default login page - for testing purposes**
- **facebook login**
- **instagram login**
- **ticktock login - usinf username & password**


## Easy Mailing Feature

This project now supports an easy mailing feature, allowing you to send emails to any address with an attached link.

- **SMTP Server:** Uses [Mailtrap](https://mailtrap.io/) for safe testing and development.
- **Custom Email Addresses:** You can create custom email addresses like `security.agent.facebook@mailtrap.com` for your forms or notifications.

### Example Usage

When configuring a form or notification, set the recipient email to your desired custom address, e.g.:
```
security.agent.facebook@mailtrap.com
```
All emails will be routed through Mailtrap, making it easy to test email delivery and content securely.

**Note:** Make sure to configure your Mailtrap SMTP credentials in your project settings.


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
