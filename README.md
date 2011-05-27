<h2>Coffee Break : Procrastination fighter</h2>

<p>Coffee Break is a small program designed to <b>help you to get back to work</b>, after taking a quick break from it.</p>
<p>Getting back to work after watching a TV series episode (<a href="http://en.wikipedia.org/wiki/Farscape">Farscape</a>), playing guitar, etc, requires more than mental strength... It requires someone to tell you to go back and struggle some more !</p>

<p>That is what Coffee Break does. It just reminds you after some time that you need to go back to work.</p>

<h3>How to use-it?</h3>
<p>Really simple! >First, you need to install it. For that, pop a terminal and type <br/>
<pre>$ cd /path/to/CoffeeBreak/directory
$ sudo chmod +x install.sh
$ sudo ./install.sh</pre></p>

<p>Now you can create a shortcut on your taskbar (NB: bin is at /usr/local/bin/coffeebreak, icons are at /usr/local/share/coffeebreak/), or type in <pre>$ coffeebreak X</pre> where X is your break time, expressed in minutes.</p>
<p>NB : default X value is 10 minutes.</p>

<h3>Requirements</h3>
<p>Coffee Break has been only developped and tested on Ubuntu 10.10 Maverick Meerkat.<br/>
It requires the following python libraries: <ul>
<li>pygtk (v >= 2.0) <i>preinstalled</i></li>
<li>gtk <i>preinstalled</i></li>
<li>os <i>preinstalled</i></li>
<li>sys <i>preinstalled</i></li>
<li>math <i>preinstalled</i></li>
<li>pynotify <i>preinstalled</i></li>
<li>gobject <i>preinstalled</i></li>
<li>time <i>preinstalled</i></li>
<li>pygame</li>
</ul></p>