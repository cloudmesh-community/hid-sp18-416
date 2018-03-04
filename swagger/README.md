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

    python InvokeServices.py "The Good Place" "Taylor Swift" "Red Sparrow"
    3 Most Latest Tweets for TV Show: The Good Place
    [{'created_at': 'Sun Mar 04 22:19:10 +0000 2018',
      'id': 970423433988157440,
      'is_retweet': False,
      'likes_for_original': 0,
      'official': False,
      'retweets_for_original': 0,
      'tweet': 'Not good. Ritter went Merkle and Beazley went limp... he will not '
               'be able to continue. Hunter Ritter takes 3rd-plac… '
               'https://t.co/iK0F3scaq0',
      'username': 'WrestlingQuoter'},
     {'created_at': 'Sun Mar 04 22:19:23 +0000 2018',
      'id': 970423488287621122,
      'is_retweet': False,
      'likes_for_original': 0,
      'official': False,
      'retweets_for_original': 0,
      'tweet': '@jessesingal Tumblr might be a good example of why sexism exists '
               'in the first place ;) but I understand.',
      'username': 'BalkanizerBlog'},
     {'created_at': 'Sun Mar 04 22:19:26 +0000 2018',
      'id': 970423499402743808,
      'is_retweet': False,
      'likes_for_original': 0,
      'official': False,
      'retweets_for_original': 0,
      'tweet': 'Lost 1 place in A lobby and finished 13th and couldnt join the 2nd '
               'race but still a good fist of points for the tea… '
               'https://t.co/UmWuXEDkrt',
      'username': 'MuddyGamer82'}]
    
    3 Most Latest Tweets for Music Artist: Taylor Swift
    [{'created_at': 'Sun Mar 04 22:19:52 +0000 2018',
      'id': 970423610165874689,
      'is_retweet': True,
      'likes_for_original': 31,
      'official': False,
      'retweets_for_original': 30,
      'tweet': 'RT @katmerickson: The Taylor Swift Bill has passed house and needs '
               'to pass Senate. This bill was written stop stop US Taxpayer Money '
               'from b…',
      'username': 'LarryTheCableD1'},
     {'created_at': 'Sun Mar 04 22:19:55 +0000 2018',
      'id': 970423619330375682,
      'is_retweet': True,
      'likes_for_original': 16,
      'official': False,
      'retweets_for_original': 1,
      'tweet': 'RT @allisonmaritz: @khloekardashian You mean calling taylor swift '
               'a snake? https://t.co/TZbKtcUNU1',
      'username': '__Yvanna'},
     {'created_at': 'Sun Mar 04 22:20:15 +0000 2018',
      'id': 970423705774866433,
      'is_retweet': True,
      'likes_for_original': 62,
      'official': False,
      'retweets_for_original': 152,
      'tweet': 'RT @SuchAChicagoKid: It just hit me that Camila has been a solo '
               'artist for a year &amp; her first 2 opportunities as an opening '
               'act have been B…',
      'username': 'magicalKobe'}]
    
    3 Most Latest Tweets for Movie Title: Red Sparrow
    [{'created_at': 'Sun Mar 04 22:20:31 +0000 2018',
      'id': 970423772565131264,
      'is_retweet': True,
      'likes_for_original': 51,
      'official': False,
      'retweets_for_original': 24,
      'tweet': 'RT @Thomas1774Paine: Box Office Poison: Jennifer Lawrence’s ‘Red '
               'Sparrow’ Bottoms Out at $17 Million https://t.co/3jxBqXE0ce',
      'username': 'deegrose'},
     {'created_at': 'Sun Mar 04 22:20:36 +0000 2018',
      'id': 970423792303517696,
      'is_retweet': True,
      'likes_for_original': 53,
      'official': False,
      'retweets_for_original': 25,
      'tweet': 'RT @Thomas1774Paine: Box Office Poison: Jennifer Lawrence’s ‘Red '
               'Sparrow’ Bottoms Out at $17 Million https://t.co/3jxBqXE0ce',
      'username': 'TwittaChicca'},
     {'created_at': 'Sun Mar 04 22:20:38 +0000 2018',
      'id': 970423800138432513,
      'is_retweet': False,
      'likes_for_original': 0,
      'official': False,
      'retweets_for_original': 0,
      'tweet': '@luigiv87 Red Sparrow.',
      'username': 'biondario'}]
    
    sleep 1
    python InvokeServices.py "Game of Thrones" "Carrie Underwood" "Jumanji"
    3 Most Latest Tweets for TV Show: Game of Thrones
    [{'created_at': 'Sun Mar 04 22:20:45 +0000 2018',
      'id': 970423832581410821,
      'is_retweet': True,
      'likes_for_original': 760,
      'official': False,
      'retweets_for_original': 850,
      'tweet': 'RT @favechracter: brienne of tarth || game of thrones '
               'https://t.co/6Kgr3s5mnP',
      'username': 'alfiiesolomons'},
     {'created_at': 'Sun Mar 04 22:20:48 +0000 2018',
      'id': 970423843079716864,
      'is_retweet': False,
      'likes_for_original': 0,
      'official': False,
      'retweets_for_original': 0,
      'tweet': '@Maihopawango Game of Thrones und black Sails 🤔',
      'username': 'Sorbamy'},
     {'created_at': 'Sun Mar 04 22:20:51 +0000 2018',
      'id': 970423857659162630,
      'is_retweet': True,
      'likes_for_original': 744,
      'official': False,
      'retweets_for_original': 122,
      'tweet': 'RT @thronesfacts: NEW: The Game of Thrones cast out in Belfast '
               'together last night https://t.co/rdUkcBXECr',
      'username': 'Watch_TV24'}]
    
    3 Most Latest Tweets for Music Artist: Carrie Underwood
    [{'created_at': 'Sun Mar 04 22:21:49 +0000 2018',
      'id': 970424097195905026,
      'is_retweet': False,
      'likes_for_original': 0,
      'official': False,
      'retweets_for_original': 0,
      'tweet': '@ClintonViceB @ItsHimOla Carrie Underwood ft Luda Chris - The '
               'Champion.',
      'username': 'AkohHal'},
     {'created_at': 'Sun Mar 04 22:24:45 +0000 2018',
      'id': 970424835389214725,
      'is_retweet': False,
      'likes_for_original': 0,
      'official': False,
      'retweets_for_original': 0,
      'tweet': '@T3atch @aylinemperez @Iveerenee you forgot Carrie Underwood sis',
      'username': '_soloveleigh'},
     {'created_at': 'Sun Mar 04 22:26:01 +0000 2018',
      'id': 970425155263614978,
      'is_retweet': False,
      'likes_for_original': 0,
      'official': False,
      'retweets_for_original': 0,
      'tweet': 'Carrie Underwood Is Back in a Music Video Following Her Scary '
               'Accident https://t.co/2z667Kvwth https://t.co/1EJfZlBprh',
      'username': 'dj_effarig'}]
    
    3 Most Latest Tweets for Movie Title: Jumanji
    [{'created_at': 'Sun Mar 04 22:26:44 +0000 2018',
      'id': 970425336340004864,
      'is_retweet': False,
      'likes_for_original': 0,
      'official': False,
      'retweets_for_original': 0,
      'tweet': 'Jumanji was actually pretty good',
      'username': 'austin_magdic'},
     {'created_at': 'Sun Mar 04 22:26:44 +0000 2018',
      'id': 970425336763699201,
      'is_retweet': True,
      'likes_for_original': 6,
      'official': False,
      'retweets_for_original': 5,
      'tweet': 'RT @shaqydread: BYoung - Jumanji. 💦💦\U0001f92b\n'
               '\n'
               'YARD MAN STYLE SWITCH UP🇯🇲\n'
               '\n'
               'STOP IT..BOOM FLICK PON ME DICK🍆 LIKE A RABBIT 🐇\n'
               '\n'
               '#RT RT https://t.co/w8…',
      'username': '_missrio'},
     {'created_at': 'Sun Mar 04 22:28:13 +0000 2018',
      'id': 970425709016608768,
      'is_retweet': True,
      'likes_for_original': 12,
      'official': False,
      'retweets_for_original': 2,
      'tweet': 'RT @dn_sutton: What a busy week! I feel bad for waiting so long, '
               'but I have to take a moment and brag on my kids!! On Thursday, my '
               'theatre…',
      'username': 'RBodoin'}]
