# Swagger Codegen

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
 - ```make create_service```
 - ```make run service```
2. In a different terminal window (within the same or different virtual environment)
- ```make create_client```
- ```make test_service``` 

## Results

- You can also invoke the services separately as follows by giving arguments for TV show title, artist name and movie title each within double quotes and separated by a space. For ex:

    ```python InvokeServices.py "The Good Place" "Taylor Swift" "Red Sparrow"```

- Following are the results from testing the service on 2 invocations using the ```make test_service``` command. 
As you can see at the time of the invocation you will be getting the real time tweets of twitter users via **Twitter Streams**.
1. 

    3 Most Latest Tweets for TV Show: The Good Place
    [{'created_at': 'Sun Mar 04 21:18:00 +0000 2018',
      'id': 970408038250287109,
      'is_retweet': True,
      'likes_for_original': 17,
      'official': False,
      'retweets_for_original': 2,
      'tweet': 'RT @theaudreynevins: In the next month I’ll be married to my high '
               'school sweetheart, we’ll have our own place and I’ll be starting '
               'cosmetol…',
      'username': 'kickpush_420'},
     {'created_at': 'Sun Mar 04 21:18:02 +0000 2018',
      'id': 970408046773129217,
      'is_retweet': True,
      'likes_for_original': 83001,
      'official': False,
      'retweets_for_original': 129778,
      'tweet': 'RT @justinbieber: Write down the things in your life that make u '
               'happy. Think about all your blessings. Be in a good place. Stay '
               'smiling',
      'username': 'xbyyi'},
     {'created_at': 'Sun Mar 04 21:18:14 +0000 2018',
      'id': 970408099529019393,
      'is_retweet': False,
      'likes_for_original': 0,
      'official': False,
      'retweets_for_original': 0,
      'tweet': 'Immigration Service doing the right thing for once, good. '
               'https://t.co/axRVIkNPbU',
      'username': 'PaulGP2'}]
    
    3 Most Latest Tweets for Music Artist: Taylor Swift
    [{'created_at': 'Sun Mar 04 21:18:34 +0000 2018',
      'id': 970408182127497216,
      'is_retweet': True,
      'likes_for_original': 251,
      'official': False,
      'retweets_for_original': 60,
      'tweet': 'RT @GustBrian: Taylor Swift https://t.co/GIZXxRzfNV',
      'username': 'TatianeMoreir'},
     {'created_at': 'Sun Mar 04 21:18:35 +0000 2018',
      'id': 970408186690842625,
      'is_retweet': True,
      'likes_for_original': 6,
      'official': False,
      'retweets_for_original': 9,
      'tweet': 'RT @ALgmd11: RT IF YOU STAN\n'
               '\n'
               '- Lady Gaga\n'
               '- Avril Lavigne \n'
               '- Taylor Swift\n'
               '- Selena Gomez\n'
               '- Ariana Grande\n'
               '- Bridgit Mendler\n'
               '- Miley Cyrus\n'
               '- C…',
      'username': 'millionhookers'},
     {'created_at': 'Sun Mar 04 21:18:37 +0000 2018',
      'id': 970408196400545792,
      'is_retweet': True,
      'likes_for_original': 147,
      'official': False,
      'retweets_for_original': 43,
      'tweet': 'RT @tswiftchart13: 🇺🇸 Total Weeks on Billboard 200 US (Album '
               'Chart)\n'
               '\n'
               '"Taylor Swift" — 275 weeks (peak #5)\n'
               '"Fearless" — 254 weeks\n'
               '"Speak Now…',
      'username': 'lastkissoutsold'}]
    
    3 Most Latest Tweets for Movie Title: Red Sparrow
    [{'created_at': 'Sun Mar 04 21:18:48 +0000 2018',
      'id': 970408241640411138,
      'is_retweet': True,
      'likes_for_original': 246,
      'official': False,
      'retweets_for_original': 40,
      'tweet': 'RT @robertliefeld: I very much enjoyed RED SPARROW. Hard core spy '
               'intrigue for adults. Great direction, performances, intrigue. '
               'Earns all i…',
      'username': 'glendagoodwich'},
     {'created_at': 'Sun Mar 04 21:18:53 +0000 2018',
      'id': 970408262230298624,
      'is_retweet': True,
      'likes_for_original': 16,
      'official': False,
      'retweets_for_original': 5,
      'tweet': 'RT @BarryHart7: THIS IS why she’s taking a break. She can’t act '
               '&amp; now we realize that.  https://t.co/ofIvIFWhKv',
      'username': 'misstozak'},
     {'created_at': 'Sun Mar 04 21:19:04 +0000 2018',
      'id': 970408307012919298,
      'is_retweet': False,
      'likes_for_original': 0,
      'official': False,
      'retweets_for_original': 0,
      'tweet': 'so i just got done seeing red sparrow and let me tell you that '
               'shit was intense.',
      'username': 'lizzygranvt'}]

2. 

    3 Most Latest Tweets for TV Show: The Good Place
    [{'created_at': 'Sun Mar 04 21:19:49 +0000 2018',
      'id': 970408497362776064,
      'is_retweet': False,
      'likes_for_original': 0,
      'official': False,
      'retweets_for_original': 0,
      'tweet': '2018 girl crush: @jameelajamil. Follow her. Also watch The Good '
               'Place. https://t.co/3aFIIQpkds',
      'username': 'freialobo'},
     {'created_at': 'Sun Mar 04 21:19:59 +0000 2018',
      'id': 970408536583884801,
      'is_retweet': False,
      'likes_for_original': 0,
      'official': False,
      'retweets_for_original': 0,
      'tweet': '@MattressGod804 The taco place I wemt to was pretty good. Just '
               'took forever. 40 minute wait smh.',
      'username': 'fromParisWithXO'},
     {'created_at': 'Sun Mar 04 21:20:08 +0000 2018',
      'id': 970408575146315776,
      'is_retweet': True,
      'likes_for_original': 83002,
      'official': False,
      'retweets_for_original': 129779,
      'tweet': 'RT @justinbieber: Write down the things in your life that make u '
               'happy. Think about all your blessings. Be in a good place. Stay '
               'smiling',
      'username': 'karen096765'}]
    
    3 Most Latest Tweets for Music Artist: Taylor Swift
    [{'created_at': 'Sun Mar 04 21:20:17 +0000 2018',
      'id': 970408611787825152,
      'is_retweet': False,
      'likes_for_original': 0,
      'official': False,
      'retweets_for_original': 0,
      'tweet': 'Day 1\nTaylor Swift- Red https://t.co/hGKIOV0DLg',
      'username': 'bizzledjs'},
     {'created_at': 'Sun Mar 04 21:20:18 +0000 2018',
      'id': 970408616649019392,
      'is_retweet': False,
      'likes_for_original': 0,
      'official': False,
      'retweets_for_original': 0,
      'tweet': 'THIS BITCH WENT THERE. https://t.co/AybGWFzLg5',
      'username': 'naturallylilac'},
     {'created_at': 'Sun Mar 04 21:20:28 +0000 2018',
      'id': 970408660471025664,
      'is_retweet': False,
      'likes_for_original': 0,
      'official': False,
      'retweets_for_original': 0,
      'tweet': 'she liked https://t.co/w4YCVHa7E5',
      'username': 'greatmanoela'}]
    
    3 Most Latest Tweets for Movie Title: Red Sparrow
    [{'created_at': 'Sun Mar 04 21:20:47 +0000 2018',
      'id': 970408740984832000,
      'is_retweet': True,
      'likes_for_original': 147,
      'official': False,
      'retweets_for_original': 61,
      'tweet': 'RT @ScottMendelson: Box Office: A $17 Million Opening Weekend For '
               '#RedSparrow Shows That #JenniferLawrence Is Still A Bankable Movie '
               'Star..…',
      'username': 'krjenlaw'},
     {'created_at': 'Sun Mar 04 21:21:10 +0000 2018',
      'id': 970408837038604290,
      'is_retweet': True,
      'likes_for_original': 0,
      'official': False,
      'retweets_for_original': 1,
      'tweet': 'RT @dominkaegorova: My family loved Red Sparrow! YASS. I’m a proud '
               'daughter/sister https://t.co/ANBPpSyJX4',
      'username': 'jenlaw_edit'},
     {'created_at': 'Sun Mar 04 21:21:11 +0000 2018',
      'id': 970408842021531648,
      'is_retweet': True,
      'likes_for_original': 17,
      'official': False,
      'retweets_for_original': 10,
      'tweet': 'RT @nytimesarts: “Red Sparrow” flew low at the domestic box '
               'office, becoming the third lackluster opening in a row for '
               'Jennifer Lawrence ht…',
      'username': 'hobarthobo'}]
