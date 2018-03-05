# Swagger Codegen

This is the README for the swagger assignment for the **Streams** resource. Please make sure to follow the prerequisites section before creating and invoking the services. 

## Prerequisites

1. Create or log in to Twitter Developer Account at [https://apps.twitter.com](https://apps.twitter.com/). 
2. Create a new Twitter app (Fill in the required information and you can use a dummy value for the ```wesbite``` field such as ```http://dummy.value/```).
3. Go to the ```Key and Access Token``` tab and generate the following tokens if it is not already available.
   - Consumer Key
   - Consumer Secret
   - Access Token
   - Access Token Secret
4. Copy the values generated above in to the file ```credentials.yaml```.
5. Make sure to have Swagger Codegen (swagger-codegen-cli-2.3.1.jar) downloaded in the ``` ~/swagger/``` folder. If swagger is not installed in the above folder please make sure to update the ```Makefile``` with the correct folder.
6. Install Python Twitter in the virtual environment you are going to run the service in.
	```
    pip install tweepy
	```
7. If you want your swagger server to run on a port other than port ```9550``` which is what I have used by default, please update the following files.
   - ```swagger.yaml``` - host key
   - ```__main.py__``` - port in Line 12


## Run and Test the service

1. Invoke the following commands to create and test the service.
   - ```make service```
   - ```make start```
2. In a different terminal window (within the same or different virtual environment).
   - ```make client```
   - ```make test```
3. Stop the service.
   - ```make stop```
4. Clean all the generated server and client files.
   - ```make clean```

## Results

- You can invoke the services as follows by giving arguments for TV show title, artist name and movie title each within double quotes and separated by a space. For ex:

    ```python InvokeServices.py "The Good Place" "Taylor Swift" "Red Sparrow"```

- Following are the results from testing the service on 2 invocations using the ```make test``` command. 
As you can see at the time of the invocation you will be getting the real time tweets of twitter users via **Twitter Streams**.

```
	python InvokeServices.py "The Good Place" "Taylor Swift" "Red Sparrow"
	3 Most Latest Tweets for TV Show: The Good Place
	{'name': 'The Good Place',
	 'tweets': [{'created_at': 'Mon Mar 05 04:13:23 +0000 2018',
	             'id': 970512575665328130,
	             'is_retweet': False,
	             'likes_for_original': 0,
	             'official': False,
	             'retweets_for_original': 0,
	             'tweet': 'I want to fly somewhere just to get some good food 😋😋 '
	                      'where’s the place to go? Any suggestions?!?',
	             'user': 'Puntha13'},
	            {'created_at': 'Mon Mar 05 04:13:26 +0000 2018',
	             'id': 970512585517817856,
	             'is_retweet': False,
	             'likes_for_original': 0,
	             'official': False,
	             'retweets_for_original': 0,
	             'tweet': "Oh no, I'm sad to hear about the end of Aussie Farmers "
	                      'Direct. I used them a bunch, loved the service. I only '
	                      'stopp… https://t.co/Aw54R1xSHw',
	             'user': 'kplyley'},
	            {'created_at': 'Mon Mar 05 04:13:28 +0000 2018',
	             'id': 970512594820911104,
	             'is_retweet': False,
	             'likes_for_original': 0,
	             'official': False,
	             'retweets_for_original': 0,
	             'tweet': '@skotteeduzntkno @TSN1290Radio This is assuming the '
	                      '@NHLJets finish top 3 in their division which is likely '
	                      'but not… https://t.co/aebqeTojqv',
	             'user': 'McCFarms'}]}

	3 Most Latest Tweets for Music Artist: Taylor Swift
	{'name': 'Taylor Swift',
	 'tweets': [{'created_at': 'Mon Mar 05 04:13:31 +0000 2018',
	             'id': 970512607307354112,
	             'is_retweet': False,
	             'likes_for_original': 0,
	             'official': False,
	             'retweets_for_original': 0,
	             'tweet': 'Now Playing: Taylor Swift - Sparks Fly Is On Q106.8 '
	                      'Country #NowPlayingOnTheQ',
	             'user': 'QCountryKnox'},
	            {'created_at': 'Mon Mar 05 04:13:37 +0000 2018',
	             'id': 970512632808648704,
	             'is_retweet': False,
	             'likes_for_original': 0,
	             'official': False,
	             'retweets_for_original': 0,
	             'tweet': 'Emma Stone = Taylor Swift #Oscars',
	             'user': 'xgbiel'},
	            {'created_at': 'Mon Mar 05 04:13:38 +0000 2018',
	             'id': 970512635191054336,
	             'is_retweet': True,
	             'likes_for_original': 0,
	             'official': False,
	             'retweets_for_original': 1,
	             'tweet': 'RT @blackthornboy: •in memorian•Old Taylor Swiftsinger, '
	                      'songwriter',
	             'user': 'Luuhecia'}]}

	3 Most Latest Tweets for Movie Title: Red Sparrow
	{'name': 'Red Sparrow',
	 'tweets': [{'created_at': 'Mon Mar 05 04:14:21 +0000 2018',
	             'id': 970512818804961280,
	             'is_retweet': False,
	             'likes_for_original': 0,
	             'official': False,
	             'retweets_for_original': 0,
	             'tweet': 'I’ve seen almost every movie in theaters right now, so '
	                      'I have to watch Red Sparrow even though I drag Lawrence '
	                      'ever… https://t.co/6HU2f9xfzd',
	             'user': '_uyuyuiii'},
	            {'created_at': 'Mon Mar 05 04:14:31 +0000 2018',
	             'id': 970512859309383681,
	             'is_retweet': True,
	             'likes_for_original': 340,
	             'official': False,
	             'retweets_for_original': 139,
	             'tweet': 'RT @Thomas1774Paine: Box Office Poison: Jennifer '
	                      'Lawrence’s ‘Red Sparrow’ Bottoms Out at $17 Million '
	                      'https://t.co/3jxBqXE0ce',
	             'user': 'RobinPa05355413'},
	            {'created_at': 'Mon Mar 05 04:14:37 +0000 2018',
	             'id': 970512886048047104,
	             'is_retweet': False,
	             'likes_for_original': 0,
	             'official': False,
	             'retweets_for_original': 0,
	             'tweet': 'Red Sparrow gets a 8.4/10 from me Possibly the first '
	                      'non-rated movie I’ve seen in theaters',
	             'user': 'youngjack_young'}]}

	sleep 1
	python InvokeServices.py "Game of Thrones" "Carrie Underwood" "Jumanji"
	3 Most Latest Tweets for TV Show: Game of Thrones
	{'name': 'Game of Thrones',
	 'tweets': [{'created_at': 'Mon Mar 05 04:14:52 +0000 2018',
	             'id': 970512946488061952,
	             'is_retweet': False,
	             'likes_for_original': 0,
	             'official': False,
	             'retweets_for_original': 0,
	             'tweet': '@Elaines2cents @greggutfeld You should watch Game of '
	                      'Thrones and the Marvel Studios movies',
	             'user': 'FakeKahwi'},
	            {'created_at': 'Mon Mar 05 04:15:18 +0000 2018',
	             'id': 970513056366145536,
	             'is_retweet': False,
	             'likes_for_original': 0,
	             'official': False,
	             'retweets_for_original': 0,
	             'tweet': 'Game of Thrones TVC 🙂🐉@TheAcademy #Oscars #Oscars2018 '
	                      '#GameOfThrones',
	             'user': 'konOHanicOH'},
	            {'created_at': 'Mon Mar 05 04:15:30 +0000 2018',
	             'id': 970513107427590144,
	             'is_retweet': False,
	             'likes_for_original': 0,
	             'official': False,
	             'retweets_for_original': 0,
	             'tweet': 'Game of Thrones and Westworld teasers during Oscars '
	                      'commercial. 💪',
	             'user': 'caxychick'}]}

	3 Most Latest Tweets for Music Artist: Carrie Underwood
	{'name': 'Carrie Underwood',
	 'tweets': [{'created_at': 'Mon Mar 05 04:17:36 +0000 2018',
	             'id': 970513633875673088,
	             'is_retweet': True,
	             'likes_for_original': 11,
	             'official': False,
	             'retweets_for_original': 1,
	             'tweet': 'RT @bethie_booo: @PhillyD Totally thought that said '
	                      'Carrie Underwood and I thought "Phil\'s Lost his mind"😂',
	             'user': 'BotanicPanicked'},
	            {'created_at': 'Mon Mar 05 04:17:44 +0000 2018',
	             'id': 970513669405622274,
	             'is_retweet': False,
	             'likes_for_original': 0,
	             'official': False,
	             'retweets_for_original': 0,
	             'tweet': '@netflix Carrie Underwood... @RealRobinWright !! '
	                      '#HouseofCards please &amp; thanks!!',
	             'user': 'OITNB_Beyond'},
	            {'created_at': 'Mon Mar 05 04:18:34 +0000 2018',
	             'id': 970513876210143232,
	             'is_retweet': False,
	             'likes_for_original': 0,
	             'official': False,
	             'retweets_for_original': 0,
	             'tweet': 'I liked a @YouTube video https://t.co/sqh0pdwrSe Carrie '
	                      'Underwood - The Champion ft. Ludacris',
	             'user': 'KellyM_Cook'}]}

	3 Most Latest Tweets for Movie Title: Jumanji
	{'name': 'Jumanji',
	 'tweets': [{'created_at': 'Mon Mar 05 04:20:07 +0000 2018',
	             'id': 970514266783670272,
	             'is_retweet': False,
	             'likes_for_original': 0,
	             'official': False,
	             'retweets_for_original': 0,
	             'tweet': "Jumanji's inevitable sequel is now in the works "
	                      'https://t.co/AgMg9tvQm4',
	             'user': 'WomanSBuzz'},
	            {'created_at': 'Mon Mar 05 04:20:55 +0000 2018',
	             'id': 970514471667011585,
	             'is_retweet': False,
	             'likes_for_original': 0,
	             'official': False,
	             'retweets_for_original': 0,
	             'tweet': 'I could leave my dog for 10 minutes and when I come '
	                      'back you would’ve thought he was just freed from being '
	                      'in jumanji for twenty years...😂',
	             'user': 'krislynwoolley'},
	            {'created_at': 'Mon Mar 05 04:21:46 +0000 2018',
	             'id': 970514682397077504,
	             'is_retweet': True,
	             'likes_for_original': 5,
	             'official': False,
	             'retweets_for_original': 2,
	             'tweet': 'RT @illegalironman: I’m sorry but ‘Jumanji: Welcome to '
	                      'the Jungle’ deserved a nomination for best picture Tbh '
	                      'it deserved to win I’ll f…',
	             'user': 'jasonwhyte'}]}
```
