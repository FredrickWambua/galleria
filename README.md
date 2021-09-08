# Galleria
This is an application that acts as an online photo gallery. It displays various categories of the pictures and the location they were taken from. 
## Author
Fredrick Wambua

## User Stories
- View different photos that interest me.
- Click on a single photo to expand it and also view the details of the photo. The photo details must appear on a modal within the same route as the main page.
- Search for different categories of photos. (ie. Travel, Food)
- Copy a link to the photo to share with my friends.
- View photos based on the location they were taken.

## Set up and Installation Requirements
### Prerequisites
- python 3.8
- django
- pipenv
- dotenv

### Cloning the repository
- Fork the repository
```
$ git clone https://github.com/FredrickWambua/galleria
```
- Navigate to the repository.
### Running the application
- Creating virtual environment
```
$ python3 pipenv shell
$ pip freeze > requirements.txt
$ . .env
```
- Runing application
```
$ make server 
$ make makemigrations (this creates database migrations)
$ make migrate (this performs migrations)
```
## Deployment
You can get the deployed application [here](https://fredspichas.herokuapp.com/). 

Follow [heroku documentation](https://devcenter.heroku.com/articles/git) to know more about deployin app to heroku.

## License
Copyright 2021 Fredrick Wambua

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.



