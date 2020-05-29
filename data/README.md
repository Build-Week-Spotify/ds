# data-science
TEAM DOCS:
 - [Product Vision Document](https://docs.google.com/document/d/12xxUc99Jrm3hWjPMIQEDg0PrAdt2xSLLVqvg2ekIe38/edit)


Github Links:

- [DATA-SCIENCE](https://github.com/Build-Week-Spotify/ds)
 
- [FRONT-END](hhttps://github.com/Build-Week-Spotify/front-end)

- [BACK-END](https://github.com/Build-Week-Spotify/back-end)

- [MARKETING](https://github.com/Build-Week-Spotify/marketing-page)

 
## **Contributers**
|[Doug Cohen](https://github.com/dougscohen)                                        |[Kyle Yates](https://github.com/KyleTy1er)                                        |[Martin Herbert](https://github.com/mherbert93)                                        |[Thomas McDaniel](hhttps://github.com/ThomasMcDaniel91)                                        |
| :-----------------------------------------------------------------------------------------------------------: | :-----------------------------------------------------------------------------------------------------------: | :-----------------------------------------------------------------------------------------------------------: | :-----------------------------------------------------------------------------------------------------------: |
|                      [<img src="https://avatars1.githubusercontent.com/u/60849521?s=460&u=1c0422c701fc566ecd9edcea912801a88f1ce720&v=4" width = "200" />](https://github.com/dougscohen)                       |                      [<img src="https://avatars0.githubusercontent.com/u/53956594?s=460&u=c75a90473ca33926d32e1bca8fb1746020e3ab23&v=4" width = "200" />](https://github.com/KyleTy1er)                       |                      [<img src="https://avatars1.githubusercontent.com/u/61983078?s=460&u=93f8bf6e6814f5805d5cf132f4ba1a8f4106e7ee&v=4" width = "200" />](hhttps://github.com/mherbert93)                       |                      [<img src="https://avatars1.githubusercontent.com/u/61952859?s=460&v=4"  width = "200" />](hhttps://github.com/ThomasMcDaniel91)                       
|                 [<img src="https://github.com/favicon.ico" width="15"> ](https://github.com/dougscohen)                 |            [<img src="https://github.com/favicon.ico" width="15"> ](https://github.com/KyleTy1er)             |           [<img src="https://github.com/favicon.ico" width="15"> ](https://github.com/mherbert93)            |           [<img src="https://github.com/favicon.ico" width="15"> ](https://github.com/ThomasMcDaniel91)            |
| [ <img src="https://static.licdn.com/sc/h/al2o9zrvru7aqj8e1x2rzsrca" width="15"> ](https://www.linkedin.com/in/dougcohen3/) | [ <img src="https://static.licdn.com/sc/h/al2o9zrvru7aqj8e1x2rzsrca" width="15"> ](https://www.linkedin.com/in/kyle-tyler-b50a1b169/) | [ <img src="https://static.licdn.com/sc/h/al2o9zrvru7aqj8e1x2rzsrca" width="15"> ](https://www.linkedin.com/in/martin-herbert-7243101a7/) | [ <img src="https://static.licdn.com/sc/h/al2o9zrvru7aqj8e1x2rzsrca" width="15"> ](https://www.linkedin.com/in/thomas-mcdaniel-ab26901a7/)

## **Our Application**

[Suggestify](https://spotify-song-suggester.netlify.app/)

We have built an appliacation that enables users to browse and visualize features of spotify songs. The user simply inputs a song of his or her choice, and the app recommends 5 song recommendations for him or her to listen to.

*Suggestify* includes registation functionality, and will allow a user to save songs to his or her profile. 

How do we recommend songs? This was the work of the Machine Learning Engineers. Simply put, we used a K Nearest Neighbors model (fit to 60,000+ of the most popular songs in spotify over the last 100 years), and predicted similar songs based on audio features. The audio features come from Spotify's API and include: 
- acousticness
- danceability
- energy
- instrumentalness
- key
- liveness
- loudness
- speechiness
- tempo
- valence

Description for what those represent can be found [here](https://developer.spotify.com/documentation/web-api/reference/tracks/get-audio-features/)

## **Data Science Roles**

### <ins>Data Engineers</ins>

describe the work of the data engineers here

### <ins>Machine Learning Engineers</ins>

The ML engineers were responsible for generating a model that would recommend songs simlar to the user's input. *Suggestify* used a K Nearest Neigbors model to identify an input song's "nearest neigbors" based on audio features. We fit the model on over 60,000 of the most popular songs in spotify. Simply put, a user puts in a song, we take it's audio features, and the model finds 5 songs whose audio features are most like said input song.

Additionally, we wanted the user to be able to visualize similarities between his or her searched song, and the recommendations that came back from the model. For the visualizations, we decided to use Plotly's bar-polar charts. For a given visualization, the 10 audio features are plotted for each of the 6 songs (1 input song + 5 recommendations). A user can see how his or her searched song's audio features compares to each of the other 5 songs being recommended. Visually, you can look and say "Hey, the song I searched has a danceability value of 1.5, and this recommended song has a value of 1.49. That makes sense why it was recommended."