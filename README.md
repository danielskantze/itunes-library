itunesLibrary
==============

itunesLibrary represents an iTunes Library. It allows the caller to retrieve items, playlists, etc.

itunesLibrary is a port of Drew Stephen's excellent Perl module, https://github.com/dinomite/Mac-iTunes-Library. The Perl
library will be **not** re-created verbatim.

This repository is a fork of Steven Scholnick's repository (https://github.com/scholnicks/itunes-library). Hacked the reading of the library using a lookup instead of iterating across iTunes items. Parsing my huge iTunes lib went from several minutes to about 10 seconds. Also, see the discussion below. 

Installation : pip install itunesLibrary

Example Code

```python
import os
from itunesLibrary import library

path = os.path.join(os.getenv("HOME"),"Music/iTunes/iTunes Music Library.xml")

# must first parse...
lib = library.parse(path)

print len(lib)    # number of items stored

for playlist in lib.playlists:
    for item in playlist.items:
        print(item)          # perform function on each item in the playlist

# get a single playlist
playlist = lib.getPlaylist("Gray")

# get a list of all of the David Bowie songs
bowie_items = lib.getItemsForArtist("David Bowie")

# get a single song
single_song = lib.getItemsById("16116")

# get the iTunes application version
print(lib.applicationVersion)
```

## Discussion
the library.getItemsById scans through all item IDs and finds the matching items. This turned out to be inefficient, especially for large libraries. I added a lookup dict for the trackIDs in addition to the items list. I have blatantly assumed the trackID is unique. Hope this is not wrong, the name 'getItemsById' suggests there can be more than one but the comments suggests it returns one item or None. 

MIT License, see https://scholnick.net/license.txt
