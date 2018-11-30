## Get a 2019 journal
https://journal.singleton.io/
-- David Singleton [@dps](http://www.twitter.com/dps)

# Journal

Designed to help you work better.

I like to write things down. With a pen. It helps me remember and really understand whatever it is I'm writing about. Over the years, I developed a system of working that helps me achieve my goals. In 2016, I started to use a paper journal which reflects that system. Not just a diary, but a structured scratchpad that is designed to help me work the way I want to. I found it really useful. I gave copies to a bunch of friends and co-workers and they found it useful too. They also had lots of feedback and ideas which I've incorporated in several revisions since. Now, you can use it too!

# Prebuilt

A recent prebuilt PDF is available [here](http://singleton.io/2019.pdf).

# HOWTO

## Prerequisites
You'll need `texlive-full` `gnuplot` and `ghostscript` (for `ps2pdf`) installed. On Mac OS [MacTeX](http://www.tug.org/mactex/) works and you can install the rest with Homebrew. I recommend using the docker instructions though as Mac OS upgrades often seem to break MacTeX and gnuplot.

## Docker (also the easiest way on Mac OS)

Build the `Dockerfile` in this repo (it builds a 4.3 GB file, BTW)
```
docker build -t journallatex .
```

Run `make` inside the docker container:
```
./latexdockercmd.sh make
```

# About

Based on DIY Organizer.

DIY Organizer was originally by Rurik Christiansen (rurik) from http://www.diyplanner.com/node/6270 and is licensed under a Creative Commons License.

