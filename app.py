from flask import Flask, request, jsonify, render_template
import yagmail
import pandas as pd
import os

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')  # Ensure index.html is in a 'templates' folder

@app.route('/send-emails', methods=['POST'])
def send_emails():
    sender_email = request.form['senderEmail']
    sender_password = request.form['senderPassword']
    email_file = request.files['emailFile']
    email_subject = request.form['emailSubject']
    email_body = request.form['emailBody']

    # Save the uploaded file
    file_path = os.path.join('uploads', email_file.filename)
    email_file.save(file_path)

    try:
        data = pd.read_excel(file_path)

        yag = yagmail.SMTP(sender_email, sender_password)

        for index, row in data.iterrows():
            recipient_email = row['Email']
            if pd.isna(recipient_email) or recipient_email.strip() == '':
                continue

            yag.send(
                to=recipient_email,
                subject=email_subject,
                contents=email_body
            )

        return jsonify({'message': 'Emails sent successfully!'}), 200

    except Exception as e:
        return jsonify({'message': str(e)}), 500

if __name__ == '__main__':
    os.makedirs('uploads', exist_ok=True)
    app.run(debug=True)
