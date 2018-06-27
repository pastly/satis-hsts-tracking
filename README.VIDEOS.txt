                HSTS Chrome CSS transparent tracking
                ------------------------------------

This video should play when opened in Firefox and Chrome.

This video will demonstrate that HSTS state is set for an entirely different
domain than the one we are visiting without any user interaction. This will
work in all tested browsers except Safari.

At 0:00: Notice the domain we are visiting is pastly.xyz.

At 0:07: One domain that will have HSTS state set for it is
08.hsts.satis.system33.pw, and it is shown that the state doesn't exist yet.

At 0:15: We visit a page on pastly.xyz. In doing so we load a CSS resource. See
the text in the video for more explanation.

At 0:33: We check our local HSTS state again and 08.hsts.satis.system33.pw is
now present. So is 09.hsts.satis.system33.pw.

                HSTS Chrome clickjacking kitten
                -------------------------------

This video should play when opened in Firefox and Chrome.

This video will demonstrate three things. First, (after opting in to this test)
we can set max-age of a couple of HSTS state entries to determine the last time
the user visited our site. Second, *in all tested browsers including Safari* we
can "clickjack" and set HSTS state when a user interacts with our site.
Finally, we show that it is not obvious how to remove HSTS state in Chrome.

At 0:00: Notice the domain the user is visiting is hsts.satis.system33.pw.

At 0:03: The user opts in to this test. HSTS state is set with max-age
parameters such that we can determine the last time the user visited our site.
The page reloads and demonstrates this.

At 0:12: We "clickjack" the link to stackexchange and set HSTS state in the
user's browser indicating to us that they are interested in Chrome.

At 0:19: The user reloads the page. The Chrome logo is now a kitten and there
is new text on the page. Consider the significance of a censor learning that a
user wants to circumvent censorship or of an advertiser learning more about a
user's interests. Content in the page was modified based solely on the user's
HSTS state. New content could be added, and old content could be removed.

At 0:29: The user visits Chrome's history settings and tries removing traces of
the hsts.satis.system33.pw site he has visited.

At 0:37: The user reloads the page and learns that removing the site from his
history was not enough to prevent tracking.

At 0:48: The user finds where to clear more browsing data, verifies that
"Cached images and files" is checked, and clears data.

At 0:57: The user reloads the page and finds he is no longer being tracked
because HSTS state is cleared when "Cached images and files" are cleared.
