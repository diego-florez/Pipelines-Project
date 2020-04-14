# Pipelines-Project

# 1. Step 1 - Project Description
  # Intro:
  In this repository you will find a project about data enrichment through web scraping.
  In this case, we will enrinch data for a movie; the one you select.

  # Goals:
  The main goal of this project is to enrich basic data with related data obtained through api-request, scraping or both.     Also, the second goal is to create a PDF with that data and send an html email with the file.

  # Steps:
  To fulfil the previous goals the next steps have been done:
  1. src-adq_api.py (acquire data through api request)
  2. src-adq_imdb.py (acquire related data through web scraping)
  3. src-adq_oscars.py.py (acquire related data through web scraping)
  4. src-merge_data.py (merge both data, basic/api and related/scraped)
  5. src-plot.py (plot with basic data and descriptive stats)
  6. src-pdf.py (pdf with all previous data)
  7. src-send_email.py (html email with pdf to input receiver)

  # Final Output:
  The final output is an html email with a PDF of enriched data.

# 2. Step 2 - Description by steps
  # Data sources:
  The basic data is obtained from http://www.omdbapi.com/. This is a free API which contains info about movies.
  The related data to enrich the basic one is obtained from https://www.imdb.com/ and                          https://en.wikipedia.org/wiki/List_of_Academy_Award-winning_films.
  # Merge:
  After all data has been obtained, it is merged to generate enriched data.
  # Plot, pdf & email:
  Finally a plot, a PDF and email will be send to the address you specify.
  
# 3. Step 3 - How it works
  a) You will have to create a key in the api --> http://www.omdbapi.com/apikey.aspx. And then save it in a .env file in a var called "omdbapi_key".
  
  b) It works with the command line. You will have to type python3 main.py -m 'the movie you want' (you can use -m or --movie).
  
  c) After you select the movie you want you will be asked to write your email and then your password account. To be able to receive the email you will have to turn off the "less secure app access opt" for that moment (if your account requires it). You can do it here: https://myaccount.google.com/lesssecureapps (for google accounts). Don't worry! Nothing bad will happen to your account.
