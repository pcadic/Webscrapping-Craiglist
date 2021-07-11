The script scrapes rows of content from three pages of a site uniform.
Here are the main features:
-search for content on the site. This will involve automation to send a search term to a search box and clicking a search button
-scrape 3 pages of the site. It automates the clicking of a button or link to advance to the next page to scrape the second and third pages
-create a class that has properties to store the cleansed data once extracted
-during each iteration for every row of content scraped, the parsed and cleansed content is stored in a new object of the class. The object is added to a list
-after scaping all pages, loop through the list to display the content of each object in the list
-a data frame is built from the list
-save data frame into a CSV file.     