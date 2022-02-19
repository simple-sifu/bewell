# b.well Django challenge

#### Summary:
Load a public dataset from into a SQLite database and build a RESTful API interface using Django REST Framework in Django version 2.2 and Python3.

#### Dataset:
- State of New York - Health Facility General Information (1.6 MB)
  - Included in /data folder or downloadable from [healthdata.gov](https://healthdata.gov/dataset/health-facility-general-information)

#### Requested tasks:
- [x] For the dataset above, download the data in an appropriate dataset file and evaluate the contents
   > Actually I was initially overwhelmed with all that data, but I didnt need to worry, becoz you told me I needed 2 FK(s) for desc and loc. This is all the info I needed to design the tables.
- [x] Create a Django app to serve information about the facilities
- Create models in a SQLite database to hold the data with the following conditions:
  - [x] Description information should be in its own table with a FK relationship
  - [x] Address/location information should be stored in its own table with FK relationship
- [x] Write a management command or migration to load the data from the dataset file into the database using the models
- Create REST-ful endpoints via Django REST Framework which provide the following:
  - [x] Detail page for a facility with all data
    - [x] Ability to CRUD facilities using the above endpoints
  - [x] An end-point which accepts a “description” or “short description” and returns only facilities that match 
- [x] Please try to write all API end-points to be as performant as possible while still using the Django ORM
 > 1. using select_related, prefetch_related for joining querysets to avoid issues with nested serializers where
 extra hits to database might inadvertently occur.
 > 2. cache - We dont want to use middleware caching for now, because our list api would only change when cache is refreshed.
 > 3. index - added db_index to facilities primary key and to foreign key of description and location tables. I did some
 initial tests and it actually seems slower....not sure if using a real database would make a difference. Will need to investigate.
 > 4. performance monitoring - Overrided dispatch method to count number of hits to db to confirm. This shows up on django server output under ***** # of Queries: 3 *********
 > 5. performance monitoring - django-debug-toolbar will show up on the right side of browser and even show you sql queries executed

#### Stretch goals:
- [x] Paged listing of facilities with subset of data with 50 results per page
 > Done automagically, using pagination library.

- [x] Write unit tests for all above end-points and CRUD operations

#### Please deliver a zip file containing:
- Your Django project in its own directory
- A copy of your SQLite database with all data loaded
- A requirements.txt file
- [x] Instructions on how to load the data, and a brief explanation of how to use the API endpoints

  > Place the CVS input file in data directory located in baseDir of application.

  > 0. Remove all files like sqlite, migrations, etc.
  > 1. python manage.py makemigrations <app>
  > 2. python manage.py migrate
  > 3. python manage.py **uploadcsv** --filename Health_Facility_General_Information.csv 

  > 1. I have included postman collections in the postman folder under the base dir
  > 2. API endpoints can also be tested using Swagger document, make sure django application is running.
  [Swagger document ](http://localhost:8000/swagger/)


- [x] Any docker file or other manifest file that would help us run the application
> 1. docker build .
> 2. docker-compose up

- A document in which you describe the following:
  - [x] What assumptions you made, and how those assumptions might affect the project.

   > 1. After noticing that facilities code was **not unique** contrary to my initial guess, I made the
   > assumption that the csv contains not only initial records but updates that occurred later down the file.
   > I begrudgingly created records using update_or_create option. I also added warning prompt for user that they were reloading on top of existing data, since a reload would wipe out any manual updates.

   > 2. Versioned the url **api/v1/facilties** for possible future version changes.

   > 3. Could not do a prefetch on the update method in Serializer because I could not save updates on the loc/desc tables. I ended up doing a separate Fetch for each object.

    
  - [x] Any trade offs you made based on the assumptions above.

   > 1. To save time, I didnt research further if the later records were truly updates or not because the
     use case of this test doesnt specify that data needs to be accurate realtime. Normally at work I would
     take the time and do the proper research to confirm that data integrity is not jeopardized.

   > 2. In regards to performance testing, some people say that it is better to wait until your website recieves
     alot of traffic before you implement - premature optimization. Adding indexes and cache seems like overkill
     on this project but would definitely make more sense on a production website, but cache in memory will be 
     expensive form of horizontal scaling and has to be evaluated properly while indexing will require more disc space.

   > 3. Viewsets over Views really made a difference for me. It helped development time and encouraged me to rely on
     the best practices inherent in how serializers are setup and called and still allows me to configure the queryset
     for different use cases. The concept of Dry is a big win for me in this case.

  - [x] Approximately how long you spent working on this project.

  > 1. 5 hours on Tuesday, 
  > 2. 8 hours on Wednesday, 
  > 3. 10 hours on Thursday, 
  > 4. 5 hours on Friday
  > 5. 5 hours on Sunday

  - [x] The most difficult aspect of the project.

  > Nothing really difficult, because instructions were very clear and explanations were meaningful.

  >  1. I had some difficulty getting nested serialization to work in the viewset. 
  > Finally figured out I needed a many=True kwargs to make it work. Also doing create/update 
  > in serialization with nested data required some thought.

  >  2. If I hit an issue or didnt know what to do, just focused on getting the immediate situation resolved 
  > first. Even though I have not touched Django in a year since I was doing more JS, I still knew what my viewsets
  > and serializers should look like.  I also love Python/Django as much as React because they make your life 
  > easier than when you use Java which I used
  > for many years but got tired of using because of its verboseness and massive OOP nature of many production 
  > applications. I actually remembered when my hands would hurt coding in Java. With Django/Python/React/JS, I spend
  > more time reading about the best practice and it always ends up being less code and prettier.


  - [x] The easiest aspect of the project.

  > creating the mgmt command, docker, db design, and pagination.

  Refactoring
  > Added 2 Unit Tests for insert/update api
  > Added use of Reverse in Unit tests.
  > refactored ReadMe file to reflect changes
  > refactored LoadCSV Prompt to use proper flag y/Y
  > refactored urls to only use one Viewset.
  > removed pip install on dockerFile and replaced with requirements.txt install instead.

Please reach out to the b.well interviewer, if you have any questions.

This assignment may not be shared with anyone or posted on any blog or website.


All Rights Reserved.  
b.well Connected Health  
http://www.icanbwell.com
# bwell_django_challenge-master

