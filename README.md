README
======

 * I couldn't make famous [subl-handler](https://github.com/asuth/subl-handler) work, so I wrote my own.
 * I don't know/care if this works for everything, but then all I care was to make [better_errors](https://github.com/charliesome/better_errors) work; so there it goes! :wink:

How-to Install
--------------

 1. Download the [latest version](https://github.com/exalted/sublimetext-launcher/archive/master.zip)
 2. Extract the downloaded archive file
 3. Put `Sublime Text 2 Launcher.app` wherever you think is best (e.g., `/Applications`)
 4. Open `Sublime Text 2 Launcher.app` once (it will quickly quit itself, this is the expected behaviour)

You should now be good to go.

Troubleshoot
------------

If you're having trouble getting this work, try:

```bash
/System/Library/Frameworks/CoreServices.framework/Versions/A/Frameworks/LaunchServices.framework/Versions/A/Support/lsregister -kill -r -domain local -domain system -domain user
```

and then open `Sublime Text 2 Launcher.app` once (it will quickly quit itself, this is the expected behaviour).

Then check with the following command that you have only one binding for `subl:`:

```bash
/System/Library/Frameworks/CoreServices.framework/Versions/A/Frameworks/LaunchServices.framework/Versions/A/Support/lsregister -dump | grep -B6 bindings:.*subl:
```
