# MernStack
Contact Manager Mern Automated Tests


📦 Project Overview
This repository includes automated test scripts for a MERN stack Contact Manager application using Python.

Test automation follows the Page Object Model (POM) design pattern.

Test data is loaded dynamically from a CSV file (contacts.csv) located in the data/ directory.

Tests can be executed by running the file:

python tests/test_add_contact.py
🚀 How to Run
To run tests locally or via GitHub Actions, ensure:

MongoDB is running (either locally or via Atlas).

Backend server is running (http://localhost:3000 or your configured host).

Frontend server is running, if relevant to your test coverage.

Once the servers are active:

Run Postman Tests using Newman
newman run "postman/contact-manager-api.postman_collection.json" -e "postman/env.local.json"

🧪 Postman Integration
Postman collection is located in the postman/ directory.

Environment file: env.local.json uses {{baseUrl}} as http://localhost:3000.

✅ GitHub Actions CI Integration
GitHub Actions is configured to run Postman tests on push.

Ensure that your environment and servers are running or mocked properly in CI context.

If MongoDB or backend isn't available in the CI environment, GitHub Actions will show failures (e.g., request url is empty).

Let me know if you want me to include a GitHub Actions YAML explanation too.








Ask ChatGPT
