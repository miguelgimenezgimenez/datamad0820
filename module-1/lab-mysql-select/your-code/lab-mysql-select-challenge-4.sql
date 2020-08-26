SELECT authors.au_id as "AUTHOR ID", authors.au_lname as "LAST NAME", authors.au_fname as "FIRST NAME", IFNULL(sum(sales.qty),0) as TOTAL
FROM authors 
  LEFT JOIN titleauthor
  ON titleauthor.au_id = authors.au_id
  LEFT JOIN titles
  ON titles.title_id = titleauthor.title_id
  LEFT JOIN sales
  ON sales.title_id = titles.title_id
    GROUP BY  authors.au_id ,authors.au_lname,authors.au_fname
  ORDER BY TOTAL desc
