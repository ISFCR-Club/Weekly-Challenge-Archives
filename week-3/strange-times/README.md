# Strange Times

**Category:** OSINT, Steganography

```
Chａlｌeｎｇe － Sｔraｎｇe Ｔｉmeｓ
Ｃａtegｏry - ＯＳΙNТ

Аye thｉs ｐeοｐle keep ｄｅleｔing ｔweets ａnd it ｋeｅpｓ getting ｄｅｌｅtｅd sо ｃould yoｕ ｆｉｎd some way to reverse time :starstruck:?
Oh, and do you know twitter has secrets?
```

flag format: CTF{xxx}

**Author:** `0xe11i0t#2534`

**Flag:** `CTF{hehe_y0u_4rent_4_t1m3trav3ll3r}`



A few days before the challenges were released, the ISFCR Team took part in T3n4ci0us-CTF-2022. A challenge from there involved figuring out about twitter secrets, which is yet another form of base change steganography.

The text in the description of the challenge is familiar to the one from the ctf and an archive for the same was created in a Discord channel. We can use [this](https://holloway.nz/steg/) site to decode the message, which is as follows:

```
e11i0t_

i wonder who that could be?
```

Using some OSINT tool such as [sherlock](https://github.com/sherlock-project/sherlock), we can figure out that it is the [twitter handle](https://twitter.com/e11i0t_) of 0xe11i0t.

Visiting the page doesn't give us much information. However, one other detail in the problem statement is related to "reversing time". This hints towards internet archives. We can use popular archive search engines like [Wayback Machine](https://archive.org/web/) and see if anything of interest comes up. Searching for the twitter archive of e11i0t_'s profile, we can find the flag lost in time.

Find it [here](https://web.archive.org/web/20220331120639/https://twitter.com/e11i0t_).