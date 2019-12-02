#!/usr/bin/env python3

import psycopg2
import itertools

question1 = '1. What are the most popular three articles of all time?'
ans_query1 = '''SELECT * FROM article_count LIMIT 3;'''

question2 = '2. Who are the most popular article authors of all time?'
ans_query2 = '''SELECT name, SUM(views) AS views FROM author_count_data
 GROUP BY name ORDER BY views DESC;'''

question3 = '3. On which days did more than 1% of requests lead to errors?'
ans_query3 = '''SELECT date, cast(percent as numeric) FROM percentage
 WHERE percent > 1.0;'''


def solution(query):
    db = psycopg2.connect("dbname=news")
    c = db.cursor()
    c.execute(query)
    result = c.fetchall()
    db.close()
    return result


result1 = solution(ans_query1)
result2 = solution(ans_query2)
result3 = solution(ans_query3)


def printAns(ans):
    if ans == result1 or ans == result2:
        for r in ans:
            output1 = '{name} - {calc} Views'.format(title=r[0], calc=r[1])
            print(output1)
        print("\n")
    else:
        for r in ans:
            output2 = '{date} - {calc}% errors'.format(date=r[0], calc=r[1])
            print(output2)
        print("\n")


if __name__ == '__main__':
    print(question1)
    printAns(result1)
    print(question2)
    printAns(result2)
    print(question3)
    printAns(result3)
