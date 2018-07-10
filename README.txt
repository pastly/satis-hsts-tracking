                Contents
                --------

hsts.satis.system33.pw/

  The website files for the hsts.satis.system33.pw part of this demo.

hsts.satis.system33.pw/redirects/

  A bunch of files that -- when combined with appropriate nginx rules -- can
  help one determine how many redirects their browser allows in a chain.

pastly.xyz/

  The website files for the pastly.xyz part of this demo.

HSTS Chrome clickjacking kitten.webm

  Video demonstrating the final product of the hsts.satis.system33.pw site.
  Shows "clickjacking" and temporal tracking.

HSTS Chrome CSS transparent tracking.webm

  Video demonstrating the final product of the pastly.xyz site, with help from
  the hsts.satis.system33.pw site. Shows fetching CSS resources can set HSTS
  state without the user realizing.

nginx.conf

  The nginx config file necessary for these two websites.

plist-parse.py

  A script to parse a plist file on OS X. HSTS state in Safari is stored in a
  plist.

