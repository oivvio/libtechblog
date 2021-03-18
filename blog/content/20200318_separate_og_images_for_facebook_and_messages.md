Title: How to make iOS Messages and Facebook use different OpenGraph images
Date: 2021-03-18

Here's today's entry from the [Season](https://seasonpods.com) project diary.

I spent approximately 5 hours figuring out how to get iOS Messages to use a different `og:image` than Facebook.

The first part of the trick is to put two og:images in the html.

     <meta property="og:image" content="https://season-artwork.s3.eu-west-2.amazonaws.com/a7/m9/i8/x4/landscape.png" />
     <meta property="og:image:width" content="1200" />
     <meta property="og:image:height" content="630" />


     <meta property="og:image" content="https://season-artwork.s3.eu-west-2.amazonaws.com/a7/m9/i8/x4/450_85.jpg" />
     <meta property="og:image:width" content="450" />
     <meta property="og:image:height" content="450" />

Facebook will now display the correct image (the landscape one).

Unfortunately Messages will display both images side by side.

![Stupid Messages](/images/messages1.jpg "Ahh, it burns, it burns!")

It burns the eyes!

So the next part of the trick is to get our server to deny Messages the first
image. Doing this with nginx or Apache is probably pretty straightforward, but
I'm serving images and all other static data with AWS S3 and doing anything with
AWS is never straight forward.

Using Facebook's [sharing
debugger](https://developers.facebook.com/tools/debug/) I figured out
that Facebook's UserAgent string is

    facebookexternalhit/1.1 (+http://www.facebook.com/externalhit_uatext.php)

So I set up a rule in AWS S3 to only allow requests for the first image when
UserAgent contains `facebookexternalhit`. This seemed to work. Requests from my
browser where denied and requests from Facebook worked as intended. But when I
shared a season via Messages I still got the two side by side images. What
gives? I suspected that maybe Messages was up to some monkey business so I set
up an endpoint that would just dump out the UserAgent for any incoming request,
pointed the og:image to that endpoint and shared another season via Messages. Lo
and behold. Here's the UserAgent string that came in.

    Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_1) AppleWebKit/601.2.4 (KHTML, like Gecko) Version/9.0.1 Safari/601.2.4 facebookexternalhit/1.1 Facebot Twitterbot/1.0

What's that towards the end if not `facebookexternalhit`! I'm surprised that
GoogleBot insn't in there too. What I ended up with a permissions policy that

1. allows access for everyone
2. denies access for any client with a UserAgent string that includes the substring "AppleWebKit".

And it that worked!

Half of the time waste today was around getting AWS to do what I wanted. After a
while i learned that **the best way to create AWS permissions policies is to the
"AWS Policy generator"**. Once I started using that instead of hand editing the
json it went pretty quickly.

So now my shares in messages looks like this:

![Messages](/images/messages2.jpg "Much better!")

And the same season share on Facebook looks like this:

![Facebook](/images/fb.jpg)

And on Twitter it will looks ok too.

![Twitter](/images/twitter.jpg)
