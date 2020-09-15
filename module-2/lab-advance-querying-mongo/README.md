![logo_ironhack_blue 7](https://user-images.githubusercontent.com/23629340/40541063-a07a0a8a-601a-11e8-91b5-2f13e4e6b441.png)

# MongoDB | Compass CRUD

## Introduction

We are back with our queries! :wink:

We have learned some super useful query operators, that will helps us to make much better queries to retrieve the data we need. We will continue using the **Crunchbase** database we used on the last exercise.

## Submission

- Upon completion, create Pull Request so your TAs can check up your work.

## Deliverables

In the `your_code/main.ipynb` file, you will find the instructions about the queries you need to do. Complete the code with your queries on a `pymongo` format. Remember not to print all results as there may be quite a lot for some queries. Printing the first element is enough. :wink:
You may test your queries on Mongo Compass, but you will need to write it on a format compatible with `pymongo` python library. 

## Instructions

### Iteration 1

First, we need to import the database we will be using for the `lab`. We will use the Crunchbase database. Crunchbase is the premier destination for discovering industry trends, investments, and news about hundreds of thousands of companies globally. From startups to Fortune 500s, Crunchbase is recognized as the primary source of company intelligence by millions of users globally.

The database contains more than 18k documents, and each of them has a lot of information about each of the companies. A document looks like the following:

![image](https://user-images.githubusercontent.com/23629340/36494916-d6db1770-1733-11e8-903e-5119b3c1b688.png)

1. You will find the `.zip` file of the Database on the **lab** folder.
2. Unzip the file
3. Navigate to this lab's folder in your terminal, and when inside, import the database to Mongo using the following command:

__When running the `mongoimport` you should be located in the same folder as the `companies.json` file.__

```bash
$ mongoimport --db companies --collection companies --file companies.json
```

_Side note_: In case errors or hanging with no response when running this command, add [--jsonArray](https://docs.mongodb.com/manual/reference/program/mongoimport/#cmdoption-mongoimport-jsonarray) in the end of the previous command.

4. Check on Mongo Compass if everything goes ok:

![image](https://user-images.githubusercontent.com/23629340/36534191-1f1bc5ec-17c6-11e8-9463-4945679b98c0.png)

### Iteration 2

You already know how this goes, so let's start working:

1. All the companies whose name match 'Babelgum'. Retrieve only their `name` field.
```db.getCollection('companies').find({"name":"Babelgum" },{"name":1})```
2. All the companies that have more than 5000 employees. Limit the search to 20 companies and sort them by **number of employees**.
```db.getCollection('companies').find({"number_of_employees" :{"$gt":20  }  }).sort( { "number_of_employees": -1 } ).limit(20)```

3. All the companies founded between 2000 and 2005, both years included. Retrieve only the `name` and `founded_year` fields.



```db.getCollection('companies').find({"created_at":{ $gt: new Date('01/01/2000').toISOString(), $lt: new Date('01/01/2005').toISOString()} }, {name:1, founded_year:1} );```
4. All the companies that had a Valuation Amount of more than 100.000.000 and have been founded before 2010. Retrieve only the `name` and `ipo` fields.
```
{$and:[{founded_year:{$lt:2010}}, {number_of_employees:{$gt:100000}}]}
```
5. All the companies that have less than 1000 employees and have been founded before 2005. Order them by the number of employees and limit the search to 10 companies.
`
  find({$and:[{founded_year:{$lt:2005}}, {number_of_employees:{$lt:1000}}]}).sort({number_of_employees:1})
`
6. All the companies that don't include the `partners` field.

find({ partners : { $exists : false } } )

7. All the companies that have a null type of value on the `category_code` field.
find({ category_code : null
} )
8. All the companies that have at least 100 employees but less than 1000. Retrieve only the `name` and `number of employees` fields.
find({ number_of_employees:{$lte:1000, $gte:100}
} , { name:1, number_of_employees:1}
)

9. Order all the companies by their IPO price in a descending order.
`db.getCollection('companies').find({"ipo":{$ne:null} }).sort({"ipo.valuation_amount":1})`
10. Retrieve the 10 companies with more employees, order by the `number of employees`

`.sort({number_of_employees:-1})`

11. All the companies founded on the second semester of the year. Limit your search to 1000 companies.
`find({"founded_month": { $gte:6  }}).limit(1000)`


12. All the companies founded before 2000 that have an acquisition amount of more than 10.000.000
`find({founded_year:{$lt:2000}, "acquisition.price_amount" :{"$gte":10000000 } })`


13. All the companies that have been acquired after 2010, order by the acquisition amount, and retrieve only their `name` and `acquisition` field.

`find({acquisition:{$ne:null}, "acquisition.acquired_year": { $gt:2010 }})`


14. Order the companies by their `founded year`, retrieving only their `name` and `founded year`.
`find({},{name:1,"founded_year":1 } ).sort({"founded_year":1})`


15. All the companies that have been founded on the first seven days of the month, including the seventh. Sort them by their `acquisition price` in a descending order. Limit the search to 10 documents.

`find({founded_day:{$exists:true}, founded_day:{$lte:7}}).limit(10)`

16. All the companies on the 'web' `category` that have more than 4000 employees. Sort them by the amount of employees in ascending order.
`find({category_code:"web",number_of_employees:{"$gt":4000}}) `

17. All the companies whose acquisition amount is more than 10.000.000, and currency is 'EUR'.
`find({acquisition:{$ne:null},"acquisition.price_amount":{"$gte":10000000   } ,"acquisition.price_currency_code":'EUR'  })`

18. All the companies that have been acquired on the first trimester of the year. Limit the search to 10 companies, and retrieve only their `name` and `acquisition` fields.
`find({acquisition:{$ne:null},"acquisition.acquired_month":{"$lte":4   } ,"acquisition.price_currency_code":'EUR'  }, {name:1,aquisition:1 }).limit(10)`


19. All the companies that have been founded between 2000 and 2010, but have not been acquired before 2011.

`find({acquisition:{$ne:null},"acquisition.acquired_year":{"$gte":2011 },founded_year:{$gt:2000, $lt:2010}  })`


Happy Coding! :heart: :rocket:
