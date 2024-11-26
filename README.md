# Bulk Email Sender using Flask and Yagmail
# Free-Bulk-Mailer
This project is a bulk email sender web application built using Flask, Pandas, and Yagmail. It allows users to send personalized bulk emails by uploading an Excel file containing recipient email addresses. The app is designed to handle email automation, supporting both text-based emails and custom email content.The system also integrates with Yagmail for a seamless email sending experience and uses Flask as the backend framework to handle form submissions, file uploads, and email processing.

# Key Features:
Flask-based Web Application: Simple and lightweight web app for sending bulk emails.
Excel File Upload: Users can upload an Excel file containing recipient email addresses, subject, and body content.
Email Personalization: Automatically sends emails to recipients with custom subjects and bodies.
Yagmail Integration: Utilizes Yagmail to send emails securely with Gmail credentials.
Error Handling: The app gracefully handles missing or invalid emails from the uploaded Excel file.
File Upload & Storage: Supports the upload and temporary storage of email lists.

# Technologies Used:
Flask: Web framework to handle routing and HTTP requests.
Pandas: For reading and processing the uploaded Excel file containing email data.
Yagmail: Python library for sending emails using Gmail.
HTML5: Frontend to allow users to upload files and input email content.
Python: Programming language for building the application logic.

# How it Works:
The user uploads an Excel file containing a list of recipient email addresses, email subject, and body content.
The Flask app processes the file and iterates over the list of emails.
Each email is sent with the provided subject and body using Yagmail and the Gmail credentials entered by the user.
Successful execution returns a confirmation message, and any errors encountered are displayed.

# Requirements:
Python 3.x
Flask
Yagmail
Pandas
An active Gmail account for sending emails
