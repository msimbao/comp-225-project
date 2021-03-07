COMP 225 Project - tympdeja
======================================================

### System


<!-- TABLE OF CONTENTS -->
<details open="open">
  <summary>Table of Contents</summary>
  <ol>
    <li>
      <a href="#about-the-project">About The Project</a>
      <ul>
        <li><a href="#built-with">Built With</a></li>
      </ul>
    </li>
    <li>
      <a href="#getting-started">Getting Started</a>
      <ul>
        <li><a href="#prerequisites">Prerequisites</a></li>
        <li><a href="#running">Running The App</a></li>
      </ul>
    </li>
    <li><a href="#usage">Usage</a></li>
    <li><a href="#roadmap">Roadmap</a></li>
    <li><a href="#contributing">Contributing</a></li>
    <li><a href="#acknowledgements">Acknowledgements</a></li>
  </ol>
</details>



<!-- ABOUT THE PROJECT -->
## About The Project

### Product Vision:
* To make it easier to get articles about a sports team(s) in one place
* It allows fans to have their news in a single place
* It will present links to certain articles based on preferences for a certain sports team
### Audience: 
* Sports fans
* Release unknown
### Risks:
* Not knowing how to scrape articles onto the webpage
* Difficult to get access to certain APIs
* We don’t know what languages we are going to use

### Display
* Shows a preview of the article
* General feed
* Individual team display

### Built With

![Image 1](images/system/1.jpg)

The system is a simple app built with flask (Python) and Vue (Javascript) and hosted on glitch. Firebase stands as the main database for storing user preferences.
* [Vue JS](https://vuejs.org/)
* [Flask](https://flask.palletsprojects.com/en/1.1.x/)
* [Firebase](https://firebase.google.com/)

<!-- GETTING STARTED -->
## Getting Started

This is an example of how you may give instructions on setting up your project locally.
To get a local copy up and running follow these simple example steps.

### Prerequisites

All modules are listed in the requirements.txt file and can be installed using pip. This step is included in the running section as well.

  ```sh
  pip install -r requirments.txt
  ```

NOTE: These are all python3 modules and some have specific versions so make sure you are using python3 to run this app.

  
### Running

1. Clone the repo
   ```sh
   git clone https://github.com/msimbao/comp-225-project.git
   ```
2. Change your directory to the project directory
   ```sh
   cd comp-225-project
   ```
3. Install python3 packages

  ```sh
  pip install -r requirments.txt
  ```

4. Run app.py
   ```sh
   python3 app.py
   ```
5. Check the port that flask is running on in your terminal (last line in terminal). It should be http://127.0.0.1:5000/ by default.
   ```sh
   #Last line in Terminal tells you the port it is running on
   
   * Running on http://127.0.0.1:5000/ (Press CTRL+C to quit)
   ```

6. If the last line looks like that above (localhost port=5000), then click this link to launch the webapp: [http://127.0.0.1:5000/](http://127.0.0.1:5000/)

7. If the last line does not go to port=5000, then open the client.js file and change the beginning parts of the flask routes from http://127.0.0.1:5000/ to whatever your terminal gives you.

<!-- USAGE EXAMPLES -->
## Usage

Use this space to show useful examples of how a project can be used. Additional screenshots, code examples and demos work well in this space. You may also link to more resources.

_For more examples, please refer to the [Documentation](https://example.com)_



<!-- ROADMAP -->
## Roadmap


<!-- CONTRIBUTING -->
## Contributing

Contributions are what make the open source community such an amazing place to be learn, inspire, and create. Any contributions you make are **greatly appreciated**.

1. Fork the Project
2. Create your Feature Branch (`git checkout -b feature/AmazingFeature`)
3. Commit your Changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the Branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request



<!-- ACKNOWLEDGEMENTS -->
## Acknowledgements
* [Vue JS](https://vuejs.org/)
* [Flask](https://flask.palletsprojects.com/en/1.1.x/)
* [Firebase](https://firebase.google.com/)



