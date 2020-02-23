# Logs Analysis

The objective here is to create a reporting tool that prints out reports (in plain text) based on the data in the database. This reporting tool is a Python program using the 'psycopg2' module to connect to the database.

## Requirements

[Vagrant](https://www.vagrantup.com/) - A virtual environment, [Virtualbox](https://www.virtualbox.org/) - A virtualization tool, [Git](https://git-scm.com/) - A version control system, [Python](https://www.python.org/download/releases/3.0/) - Latest release of Python software.

## Steps

1. Download and install the above requirements if you do not have them installed in your machine.
2. Download [this](https://d17h27t6h515a5.cloudfront.net/topher/2017/August/59822701_fsnd-virtual-machine/fsnd-virtual-machine.zip) Udacity folder for pre-configured vagrant settings.
3. Navigate to the Udacity folder using the bash interface and cd into vagrant.
4. Bring up the virtual machine using the following using ``` vagrant up ```
5. Log in to vagrant using the following command using ``` vagrant ssh ```
6. Download the [newsdata.sql](https://d17h27t6h515a5.cloudfront.net/topher/2016/August/57b5f748_newsdata/newsdata.zip) file.
7. Extract the contents of the zip file to the same folder as vagrant.
8. To load the data, cd into the vagrant directory and use the command ``` psql -d news -f newsdata.sql ```
9. Run the commands from the VIEW List section below.
10. Use command ``` python MainProgram.py ``` to run the python program.


## Explore the data

1. ``` \dt ``` - lists the tables that are available in the database.
2. ``` \d table ``` - shows the database schema for that particular table (replace table with the name of a table).

## Connecting to the database from your code

The database that you're working with in this project is running PostgreSQL. So in your code, you'll want to use the psycopg2 Python module to connect to it, for instance:

``` db = psycopg2.connect("dbname=news") ```

## VIEW List

1. ``` create VIEW article_count as SELECT title, COUNT(*) AS views FROM articles, log WHERE SUBSTRING(log.path, 10)=articles.slug GROUP BY title ORDER BY views DESC; ```
2. ``` create VIEW author_count_data as select a.author, b.name, c.title, c.views from articles a, authors b, article_count c where a.title = c.title and a.author = b.id group by a.author, b.name, c.title, c.views order by views desc; ```
3. ``` create VIEW error_requests as select date(time) as date, count(*) from log where status = '404 NOT FOUND' group by date order by date; ```
4. ``` create VIEW total_requests as select date(time) as date, count(*) as count from log group by date order by date; ```
5. ``` create VIEW percentage as select b.date, ROUND((((1.0*a.count)/(1.0*b.count))*100.0),1) as percent from error_requests a, total_requests b where a.date = b.date order by percent desc; ```
