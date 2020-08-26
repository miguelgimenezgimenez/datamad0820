SELECT authors.au_id as "AUTHOR ID", authors.au_lname as "LAST NAME", authors.au_fname as "FIRST NAME",  publishers.pub_name as "PUBLISHER", count(*)
FROM authors
  RIGHT JOIN titleauthor
  ON titleauthor.au_id = authors.au_id
  LEFT JOIN titles
  ON titles.title_id = titleauthor.title_id
  LEFT JOIN publishers
  ON publishers.pub_id = titles.pub_id
  GROUP BY publishers.pub_name, authors.au_id ,authors.au_lname,authors.au_fname
  