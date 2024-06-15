# licenta
This is my bachelors project for my final year. The app is written in python and it's a password manager. The app features a GUI made using pyqt5 and offers options such as password generator, a backend server and a browser extension for viewing the saved data.

![Alt text](/images/newEntry.png)

This is what the GUI looks like. In this picture you can see the add entry window and the password generator. The generator uses random.choices() function to generate a random password from a string made with the selected character sets.
The data is encrypted using the AES algorithm. When saving to a file, the app transforms each line in the table into a list containing strings and passes it to the encypt_and_save() method along the masterKey given by the user. This method generates a hash and a salt in order to store the masterKey and allow for later verifications. After the hash and salt are generated, the method joins all the data inside the list with a separator and proceeds to encrypt the data. The enrypted text and the iv(initialization vector needed for decryption) are then stored in a new file created at the specified file path.

![Alt text](/images/encryptSave.png)

Below is the chrome extension. This extension retrieves data from the Django server and displays it in a table. It allows the user to select a line inside the table and copy the username or password using the appropiate buttons. The javascript file also compares the url of the page that's opened with the urls stored inside the app. If it finds a match, a button will be added under the user and password fields and allow for auto-completion. 

![Alt text](/images/website.png)
