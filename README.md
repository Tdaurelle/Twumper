# Twumper
# Twitter Trump Analyzer 

# This project is the best. the best project. gonna be yuuuuge.
# No one has ever seen a project so great

# Create virtual environment:
# Navigate to project root 

```
cd ~/Documents/GitHub/Twumper/
```
# and create a virtual environment:

```
python3 -m venv env
```

# Activate the environment and install dependencies:

```
source env/bin/activate
pip install --upgrade pip
pip install -r requirements.txt
```
### Create a credentials file.
# Log in to apps.twitter.com
# Click [Create New App]
# Navigate to [Keys and Access Tokens]
# Click [Create my access token]
# Open Twumper/twitter-api/creds_template.py and fill in the details, saving the file as creds.py
# Create credentials file and delete script

```
python3 creds.py
rm creds.py
```

# Protect your credentials file

```
chmod 700 twitter_credentials.json
```

