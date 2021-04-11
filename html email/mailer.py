import csv
import os
import smtplib, ssl
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

sender_email = str(os.environ.get('iedc_email'))
receiver_email = "adithyaanilkumar1@gmail.com"
password = str(os.environ.get('iedc_pass'))

message = MIMEMultipart("alternative")
message["Subject"] = "Invitation for talk"
message["From"] = sender_email
message["To"] = receiver_email

# Create the plain-text and HTML version of your message
text = """\
Hi,
How are you?
Real Python has many great tutorials:
www.realpython.com"""
html = """\

<html>

<head>
    <link rel="preconnect" href="https://fonts.gstatic.com">
    <link href="https://fonts.googleapis.com/css2?family=Poppins&display=swap" rel="stylesheet">
    <style>
        body {
            padding: 0;
            margin: 0;
            overflow-x: hidden;
            position: relative;
        }
        .header-container{
            margin-bottom: 20px;
        }

        .footer-container {
            display: flex;
            width: 100%;
            flex-direction: row;
            position: relative;
            bottom: 0;
            margin-top: 100px;
        }

        .contact-section {
            display: flex;
            width: 90%;
            flex-direction: row;
            justify-content: space-evenly;
            align-items: center;
            text-align: center;
            
        }

        p {
            font-family: Poppins;
        }

        .name {
            font-weight: 900;
            color: #CA0045;
            text-transform: uppercase;
            font-size: 18px;
        }

        .details {
            color: #702E45;
            font-size: 16px;
        }
        .email{
            color: #702E45;
            font-size: 16px;
        }
        .content-container{
            margin-right: 5%;
            margin-left: 5%;
        }
        .footer-img{
            width: 100%;
        }
        @media screen and (max-width: 900px) {
            .name {
                font-size: 2.5vw;
            }

            .details {
                font-size: 1.75vw;
            }
            .email{
                font-size: 1.75vw;
            }
        }

        @media screen and (max-width: 500px) {
            .name {
                font-size: 2vw;
            }

            .details {
                font-size: 2vw;
            }
            .email{
                font-size: 1.5vw;
            }
        }
    </style>
</head>

<body>
    <div class="header-container">
        <img width="100%" src='https://user-images.githubusercontent.com/53343483/114293870-79e9f300-9ab7-11eb-9b13-f606d1c8a420.png'/>
    </div>
    <div class="content-container">
        <!--Content goes here-->
        Lorem ipsum dolor sit amet, consectetur adipiscing elit. Fusce mattis vel nulla ut porta. Vestibulum ante ipsum primis in faucibus orci luctus et ultrices posuere cubilia curae; Quisque at vestibulum elit. Sed rhoncus turpis et massa tincidunt pulvinar. Duis accumsan purus libero, vel gravida libero maximus a. Phasellus vehicula arcu nulla, vel euismod nisi eleifend quis. Nam nec fringilla tellus, facilisis fringilla tortor. Nulla vestibulum odio aliquam nisl tempus luctus. Vivamus congue vulputate massa, et hendrerit velit lobortis eget. Nunc id orci gravida, aliquet lacus ut, facilisis neque. Maecenas sodales arcu et eleifend iaculis. Proin quis lectus et ligula ornare faucibus eu in neque.

In hac habitasse platea dictumst. Duis mi elit, vehicula eu orci ut, luctus aliquam felis. Cras maximus efficitur fringilla. Duis venenatis est id lectus pretium porttitor. Donec vulputate metus sed augue tempus, ut pretium purus pharetra. Vestibulum libero erat, convallis at finibus in, faucibus quis erat. In eu posuere mauris, sed fringilla odio. Vivamus eget lorem non augue suscipit dignissim. Pellentesque sit amet lectus varius turpis elementum blandit nec id libero. Duis pharetra eu augue at luctus.

Duis tempus rutrum velit, quis hendrerit massa fermentum at. Donec sollicitudin posuere facilisis. Nam a lorem ultricies, mollis dolor nec, commodo velit. Donec luctus viverra sapien, sit amet pulvinar ante fringilla non. Integer ornare dolor in felis luctus pulvinar. Pellentesque blandit ipsum nibh, vitae pretium nulla interdum id. Quisque vitae accumsan augue. Phasellus ut rhoncus dolor, in molestie quam. Aliquam quis nibh sed turpis dapibus aliquet. Suspendisse consectetur sapien quis risus pharetra ultricies.

Praesent porta ullamcorper ipsum, eu rutrum erat consequat non. Proin nisl diam, vestibulum at hendrerit in, consectetur id quam. Pellentesque in tellus lacus. Praesent purus odio, convallis ac est id, ultrices fringilla lectus. Proin maximus, diam eu pretium blandit, metus est rutrum purus, in rutrum ligula risus et tellus. Sed aliquam, dolor vitae scelerisque consequat, metus tellus dignissim tortor, sit amet ornare turpis purus eu ante. Cras tincidunt elit metus, a suscipit ligula faucibus sed. In aliquam lacus eu semper feugiat.

In velit justo, tincidunt in velit a, volutpat ultricies lorem. Praesent et faucibus nunc. Praesent vel tortor dui. Mauris sed fringilla ex, vel imperdiet sem. Proin urna diam, eleifend fermentum quam id, iaculis vestibulum justo. In hac habitasse platea dictumst. Pellentesque habitant morbi tristique senectus et netus et malesuada fames ac turpis egestas. Donec ac odio eget ipsum luctus fermentum. Proin sem diam, porta id condimentum eget, rutrum sit amet est. Nam imperdiet, mi non maximus rhoncus, odio eros accumsan risus, in hendrerit enim nulla sed purus. Pellentesque laoreet lectus sed risus viverra, sed molestie neque tempus. Cras ac sollicitudin neque, et luctus massa. Quisque venenatis lorem in risus hendrerit euismod. Fusce lobortis rhoncus augue, id ullamcorper ipsum sodales eget.
    </div>
    <div class="footer-container">
        <img class = "footer-img"  src='https://user-images.githubusercontent.com/11157848/114299521-5c2d8580-9ad9-11eb-8155-e13be0780806.png'/>
    </div>
</body>

</html>
"""

# Turn these into plain/html MIMEText objects
part1 = MIMEText(text, "plain")
part2 = MIMEText(html, "html")

# Add HTML/plain-text parts to MIMEMultipart message
# The email client will try to render the last part first
message.attach(part1)
message.attach(part2)


context = ssl.create_default_context()
with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=context) as server:
    server.login(sender_email, password)
    with open("list.csv") as file:
        reader = csv.reader(file)
        print(f"reading csv")
        for email in reader:
            print(f"Sending email to {email[0]}")
            try:
                server.sendmail(
                    sender_email, email[0], message.as_string()
                )
                print(f"sent email to {email[0]}")
            except:
                print(f"FAILED Sending email to {email}")


