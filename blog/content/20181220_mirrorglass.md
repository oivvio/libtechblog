Title: I made an Ira Glass bot
Date: 2018-12-20

A couple of weeks back *This American Life* ran an
[episode](https://www.thisamericanlife.org/663/how-i-read-it) on how
we read things differently depending on the context. They started the
show with a section about [InspiroBot](https://inspirobot.me/). Host
Ira Glass declared his love for the InspiroBot and interviewed the
people behind it.

Since I love semi auto generated texts and Ira Glass is one of my
favorite journalists I decided to make an [Ira Glass
"bot"](https://mirrorglass.oivvio.com). Calling it a bot is actually
a bit overstated. It's not like it can hold a conversation or
anything. Here's what I did:

## Downloaded all the *This American Life* transcripts

~~~~
:::python
import os
from requests import get

def download(url, file_name):
	with open(file_name, "wb") as file:
		response = get(url)
		file.write(response.content)


for i in range(1, 664):
	url = f"https://www.thisamericanlife.org/{i}/transcript"
	fn = f"./data/raw_{i}.html"

	if not os.path.exists(fn):
		print(f"Downloading ep. {i}")
		download(url, fn)
~~~~

## Extracted everything Ira Glass said

I first tried a regex but that got hairy fast. So I picked up
[Scrapy](https://scrapy.org/) that I've used before. That got me
reacquainted with [Xpath](https://en.wikipedia.org/wiki/XPath)
selectors. The syntax is about as readable as regexes but it's very
powerful.

~~~~
:::python
import os
from scrapy.selector import Selector


def keep(text):
	result = True

	if "[" in text:
		result = False

	if "]" in text:
		result = False

	if len(text) == 0:
		result = False

	return result


for i in range(1, 664):
	input = f"./data/raw_{i}.html"
	output = f"./data/raw_{i}.txt"

	items = []
	if not os.path.exists(output):
		data = open(input).read()
		xpath = "//h4[text()='Ira Glass']/following-sibling::*//descendant-or-self::*//text()"
		items.extend(Selector(text=data).xpath(xpath).extract())

		items = [i for i in items if keep(i)]

		text = " ".join(items)

		fh = open(output, "w")
		fh.write(text)
		print(output)
~~~~


## Generated 100000 text snippets

Here I used [pydodo](https://github.com/Liberationtech/pydodo), a
Markov text generator that I wrote ages ago.

~~~~
:::python
from pydodo import EnglishMarkov
import time
import os

outputfolder = "./generated"


def get_start_number(folder):
    ls = os.listdir(folder)
    try:
        result = max([int(item.split(".")[0]) for item in ls]) + 1
    except ValueError:
        result = 0
    return result


def get_model(input):
    mm = EnglishMarkov()
    mm.construct(open(input))
    mm = mm.remove_pines()
    return mm


def generate(model, n, start_number, folder):
    t1 = time.time()
    count = 0
    while count < n:
        # Generate a sentence
        sent = model.generate_sentence()
        # Only hang on to it if it's longer then 90 characters.
        if len(sent) > 90:

            fn = os.path.join(folder, f"{start_number + count}.txt")
            fh = open(fn, "w")
            fh.write(sent)
            fh.close()
            count += 1
            print(f"{count} / {n}")
    t2 = time.time()

    print(n / (t2 - t1))


model = get_model("./data/all_data.txt")
generate(model, 100000, get_start_number("./generated"), "./generated")

~~~~


# The front end

The front end is all static HTML/CSS with at dash of JavaScript to
load in new text snippets. The `loadRandomUrl` function picks a random
number in the range 1 - 100000, fetches the corresponding text snippet
and inserts it on the page.

~~~~
:::javascript
reload = function(url, number, reloadbuttontext){
    placeholder = document.getElementById("placeholder");
    reloadbutton = document.getElementById("reloadbutton");
    placeholder.classList.add("loading");

    buttontexts = ["More!", "Go!", "Deeper!", "Into!", "The!", "Abyss!"];
    index = buttontexts.indexOf(reloadbutton.textContent);
    if (index == -1) {
	newbuttontext = buttontexts[1];
    } else {
	newbuttontext = buttontexts[(index + 1) % buttontexts.length];
    }

    fetch(url)
	.then(function(response) {
	    return response.text();
	}).then(function(text){
	    placeholder.textContent = text;
	    if (reloadbuttontext) {
		reloadbutton.textContent = newbuttontext;
	    }

	    placeholder.classList.remove("loading");	    
	});
}


randomUrl = function(number){
    return 'https://mirrorglass.oivvio.com/script_to_track/'+ number + '.txt';
}

randomNumber = function(){
    max = 100000;
    return Math.floor(Math.random() * Math.floor(max)) + 1;
};

loadRandomUrl = function(reloadbuttontext=true){
    newUrl = randomUrl(randomNumber());
    reload(newUrl, randomNumber, reloadbuttontext);
}

window.onload = function(){
    loadRandomUrl(false);
}
~~~~
