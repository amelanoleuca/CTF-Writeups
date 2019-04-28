# Streams
Misc (70 points, 61 solves)

## Challenge 

White noise is useful whether you are trying to sleep, relaxing, or concentrating on writing papers. Find some natural white noise [here](https://streams.2019.chall.actf.co/).

Note: The flag is all lowercase and follows the standard format (e.g. actf{example_flag})

Author: ctfhaxor

## Hint

Are you sure that's an mp4 file? What's inside the file?

## Solution

We open the website to find some nice streams. Using the hint, I saved opened up the `stream.mp4` file. It appears to be an [MPEG-DASH](https://en.wikipedia.org/wiki/Dynamic_Adaptive_Streaming_over_HTTP) file with three different streams. One is for video, one is for audio, so what was the third one for?

With some quick Google searching I found that VLC could play these streams, all I had to do was concatenate the `init-stream2.m4s` and the several `chunk-stream2-XXXXX.m4s` files into one file and play it. I kept using `curl` until I got a 404. 

```
$ curl https://streams.2019.chall.actf.co/video/init-stream2.m4s > stream
$ curl https://streams.2019.chall.actf.co/video/chunk-stream2-00001.m4s >> stream
$ curl https://streams.2019.chall.actf.co/video/chunk-stream2-00002.m4s >> stream
$ curl https://streams.2019.chall.actf.co/video/chunk-stream2-00003.m4s >> stream
$ curl https://streams.2019.chall.actf.co/video/chunk-stream2-00004.m4s >> stream
$ curl https://streams.2019.chall.actf.co/video/chunk-stream2-00005.m4s >> stream
$ curl https://streams.2019.chall.actf.co/video/chunk-stream2-00006.m4s >> stream
$ curl https://streams.2019.chall.actf.co/video/chunk-stream2-00007.m4s >> stream
$ curl https://streams.2019.chall.actf.co/video/chunk-stream2-00008.m4s >> stream
```

I used VLC to convert it to an MP3 file just for ease of use elsewhere. Taking a listen, we can hear several short and long beeps, which is almost certainly morse code. Plugging it into a morse code decoder, we get this:

```
.. -.-. - ..-. -.--. ..-. .---- ....- ..... .... -....- .---- ..... -....- -.. ...-- ....- -.. -....- .---- ----- -. ----. -....- .---- .---- ...- ...-- -....- -- .--. ...-- ----. -....- -.. ....- ..... .... -.--.-
ICTF<KN>F145H-15-D34D-10N9-11V3-MP39-D45H)
```

The `<KN>` character actually has the same sequence as `(` and common sense tells us that the first `I` is an `A`. Following the flag format (all lowercase and underscores), we get the flag. 

## Flag

```
actf{f145h_is_d34d_l0n9_l1v3_mp39_d45h}
```