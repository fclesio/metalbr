# Rebirth the Remains
## An analysis using NLP tools across the lyrics of two greatest bands of Brazilian Heavy Metal: Angra and Sepultura


### Motivation
In most of my time, I used to experiment some NLP techniques and I noticed that even with the plethora of resources available, it's very hard to find some NLP tech stuff attached with Data Analysis, _i.e._ related to general knowledge over the data like Text Mining.  

It's very cool to have a lot of scripts, applied blog posts, repositories in Github with code, but at least for me the analysis it's where the technique shines most because anyone it's able to write a script but only a few ones can extract knowledge of the data. 

The idea here it's getting the lyrics of two bands that I like and check their literary characteristics and try to find some relation or distinction between them.  

For very deep and technical posts about NLP, LDA and so on, feel free to jump directly to the end of this post and choose a lot of very nice references about these topics.

And this is what this post what about.  

### Why Angra and Sepultura?  
Heavy Metal it's one of the most boardeless music styles in the world and I would like to show two of the most iconic bands of my country and their literary characteristics in a simple way using Python, LDA, NLP and some imagination (you will see during the "interpretation" of topics.  

### About the Bands

#### Sepultura
According to [Wikipedia](https://en.wikipedia.org/wiki/Sepultura), Sepultura is a Brazilian heavy metal band from Belo Horizonte. Formed in 1984 by brothers Max and Igor Cavalera, the band was a major force in the groove metal, thrash metal, and death metal genres during the late 1980s and early 1990s. Sepultura has also been credited as one of the second wave of thrash metal acts from the late 1980s and early-to-mid 1990s.  

[Sepultura Oficial Website](https://www.sepultura.com.br/) - [Sepultura in Spotify](https://open.spotify.com/artist/6JW8wliOEwaDZ231ZY7cf4)

#### Angra
According to [Wikipedia](https://en.wikipedia.org/wiki/Angra_(band)), Angra is a Brazilian heavy metal band formed in 1991 that has gone through some line-up changes since its foundation. Led by Rafael Bittencourt, the band has gained a degree of popularity in Japan and Europe.   

[Angra Oficial Website](http://www.angra.net/) - [Angra in Spotify](https://open.spotify.com/artist/7IAXZaLTb6nkJr8RmVPn5y)



### Questions
Some personal questions that I always had about these bands and I'll try to answer with this notebook is: 
- 1) What's the literary characteristics for Angra and Sepultura?
- 2) Which type of thematics they talk about?
- 3) Who has more diversity in their topics?

### Some limitations 

- NLP it's still an unsolved problem even with all [over promissing](https://openai.com/blog/better-language-models/) about it. This two anthologic pieces by [Yoav Goldberg](https://medium.com/@yoav.goldberg/an-adversarial-review-of-adversarial-generation-of-natural-language-409ac3378bd7) and [The Gradient](https://thegradient.pub/frontiers-of-generalization-in-natural-language-processing/) put that in perspective;
- The creative process even with some patterns it's a very complex that can envolves a lot of poetic license. [In this video](https://www.youtube.com/watch?v=G8eqnWVY_rU) Rafael Bittencourt explains the whole process to compose a single lyric for the new album, and in [this video](https://www.youtube.com/watch?v=kYf6GgkGfzA) Max Cavalera speaks about the creative process behind the classic album ["Roots"](https://www.youtube.com/watch?v=KuMlv7hmrFg&list=PLfUV806q_Ri4WN5omBcgzDxHcWMaHL_i1) from 1996.
