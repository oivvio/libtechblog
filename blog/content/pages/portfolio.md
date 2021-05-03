Title: Portfolio

<script src="https://cdn.plyr.io/3.6.7/plyr.js" type="text/javascript">
</script>
<link rel="stylesheet" href="https://cdn.plyr.io/3.6.7/plyr.css" />
<script>
window.onload = function () {
const player = new Plyr('#player');
window.player = player;
console.log("loaded plyr");
}
</script>

<style>
.embed-container { position: relative; padding-bottom: 56.25%; height: 0; overflow: hidden; max-width: 100%; margin-bottom: 3rem; } 
.embed-container iframe, .embed-container object, .embed-container embed { position: absolute; top: 0; left: 0; width: 100%; height: 100%; }</style>

Sorry internet folks, this will all be in Swedish.

{% with %}
{% set   mp4="https://libtechblogstaticresources.s3.eu-north-1.amazonaws.com/presentation2014.mp4" %}
{% set   poster="/images/videoposters/presentation.png" %}

<video  id="player" controls  poster="{{poster}}">
  <source src="{{mp4}}"  type="video/mp4">
      Sorry, your browser doesn't support embedded videos.
</video>

{% endwith %}

<!--

<div class='embed-container'><iframe src='https://player.vimeo.com/video/91548323' frameborder='0' webkitAllowFullScreen mozallowfullscreen allowFullScreen></iframe></div>


# Schyst resande

<div class='embed-container'><iframe src='https://player.vimeo.com/video/544246060' frameborder='0' webkitAllowFullScreen mozallowfullscreen allowFullScreen></iframe></div>

# Season

<div class='embed-container'><iframe src='https://player.vimeo.com/video/544217333' frameborder='0' webkitAllowFullScreen mozallowfullscreen allowFullScreen></iframe></div>

# Micro Action Movement

<div class='embed-container'><iframe src='https://player.vimeo.com/video/544050558' frameborder='0' webkitAllowFullScreen mozallowfullscreen allowFullScreen></iframe></div>

# Curatron

<div class='embed-container'><iframe src='https://player.vimeo.com/video/119949494' frameborder='0' webkitAllowFullScreen mozallowfullscreen allowFullScreen></iframe></div>

# Förskjutningar

<div class='embed-container'><iframe src='https://player.vimeo.com/video/61094120' frameborder='0' webkitAllowFullScreen mozallowfullscreen allowFullScreen></iframe></div>

# DHEN

<div class='embed-container'><iframe src='https://player.vimeo.com/video/64066326' frameborder='0' webkitAllowFullScreen mozallowfullscreen allowFullScreen></iframe></div>ppp

-->
