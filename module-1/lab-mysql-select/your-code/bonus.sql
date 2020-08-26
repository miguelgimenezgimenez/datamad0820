SELECT authors.au_id as "AUTHOR ID", authors.au_lname as "LAST NAME", authors.au_fname as "FIRST NAME",  sum(((sales.qty*titles.price) * titles.royalty/100 ) * titleauthor.royaltyper/100 + titles.advance*titleauthor.royaltyper/100) as PROFIT
FROM authors 
  LEFT JOIN titleauthor
  ON titleauthor.au_id = authors.au_id
  LEFT JOIN titles
  ON titles.title_id = titleauthor.title_id
  LEFT JOIN sales
  ON sales.title_id = titles.title_id
	GROUP BY AUTHORS.au_id
    ORDER BY PROFIT DESC