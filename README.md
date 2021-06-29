# Smart Pick Web app

This application is powered by an NLP algorithm which provide users a
hassle free shopping experience. This app compare products from Amazon
and Flipkart and suggest best matches for a particular product, thereby
giving users a direct comparison between products from the two sites.

## Live Testing The App
<STRONG>NOTE: Below listed methods are only for our internal testing and debugging
purpose. Once testing is done; app will be deployed and a single link will be
provided in this section for production purpose. </STRONG>  
```sh
$ pip install -r requirements.txt
```
> Download MySQL. <a href="https://dev.mysql.com/downloads/installer/" target="_blank">Click Here To Download</a>

>Install `Amazon.py`, `Flipkart.py`, `distance_matrices.py`, `helperfuncs.py`
`IVIS_LABS logo.jpg`, `MySQL_DB.py`, `UI.py`

> Create a database named `scrapped_db` from MySQL, and include the following table in it:

```shell script
CREATE TABLE product(id int PRIMARY KEY AUTO_INCREAMENT,
name text, price VARCHAR(10), isprime VARCHAR(10), url text, imgurl text)
```

> Put your username and password within scripts at respective positions
>for establishing connection with the database Then run the following command in cmd.

```shell script
$ streamlit run UI.py
```

## Prototype Insights
### Best Match Page
Here best matches with highest confidence score along with all the related search results will be shown.
