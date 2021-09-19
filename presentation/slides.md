# PCGG. Portfolio Progress

Anna Boronina

---

# Portfolio / ~~caves~~ mountains

<div class="row">
    <img src="/img/caves/caves_1.png" class="paper">
    <img src="/img/caves/caves_qr.png" class="paper_qr" />
</div>

<style>
    .row {
        margin-top: 5em;
        display: flex;
        justify-content: center;
        align-items: center;
    }

    .paper {
        width: 70%;
        border-radius: 5px;
        margin-right: 1em;
    }

    .paper_qr {
        width: 10%;
        border-radius: 5px;
        margin-top: 2.6em;
    }
</style>

---

# What are LSystems?

An **L-system** is a type of formal grammar. An L-system consists of:
- an alphabet of symbols
- macros
- an initial string of symbols - axiom - from which to begin construction
- **a mechanism for translating generated strings into geometric structures**

<img src="/img/caves/Fractal_weeds.jpg" class="weeds"/>

<style>
    h1 + p {
        opacity: 1;
    }
    .weeds {
        width: 70%;
        height: 50%;
        margin-left: 7.3em;
        margin-top: 1em;
    }
</style>

---

# Just a minute to admire LSystems

<div>
    <iframe src="https://player.vimeo.com/video/175538630?h=5d49e66cdd" width="640" height="360" frameborder="0" allow="autoplay; fullscreen; picture-in-picture" allowfullscreen>
    </iframe>
    <p>
        <a href="https://vimeo.com/175538630">Growing Tree</a> from <a href="https://vimeo.com/user49693381">Rocken Qin</a> on <a href="https://vimeo.com">Vimeo
        </a>.
    </p>
</div>

<style>
    div {
        margin-left: 6em;
    }

    iframe {
        border-radius: 5px;
    }
</style>

---

# The authors' alphabet and macros

<div class="row">
    <img src="/img/caves/caves_3.png" class="caves_4" />
    <img src="/img/caves/caves_4.png" class="caves_4" />
</div>

<style>
    .row {
        display: flex;
        justify-content: center;
        align-items: center;
        width: 87%;
        margin-left: 3.5em;
    }

    .caves_3 {
        width: 50%;
        border-radius: 5px;
        margin-right: 1em;
    }

    .caves_4 {
        width: 50%;
        border-radius: 5px;
    }
</style>

<!--
mountainsssssss
-->

---

# The authors' results

<img src="/img/caves/caves_5.png">

<style>
    img {
        height: 90%;
        margin-left: 8em;
    }
</style>

---

# Exciting? Let's see what I have!

---

# These are mountains, by the way

<img src="/img/caves/caves_6.png">

<style>
    h1 + p {
        opacity: 1;
    }
    img {
        width: 95%;
        margin-top: 3em;
        margin-left: 0.5em;
    }
</style>

---

# Now, seriously, what I have

---

# Now, seriously, what I have - an alphabet!

I can use the same idea to generate mountains.

<img src="/img/caves/caves_me_1.png"/>

<style>
    h1 + p {
        opacity: 1;
    }
    img {
        height: 90%;
        margin-left: 5em;
        margin-top: -1em;
    }
</style>

---

# Now, seriously, what I have - macros!

<img src="/img/caves/caves_me_2.png"/>

<style>
    img {
        height: 90%;
        margin-left: 5em;
    }
</style>

---

# 2D mountains are boring, so...

I decided to move on to 3D. So far so bad :)

<div>
    <iframe src="/img/caves/demo.mp4" width="700" height="380" frameborder="0" allow="autoplay; fullscreen; picture-in-picture" allowfullscreen>
    </iframe>
</div>

<style>
    h1 + p {
        opacity: 1;
    }
    div {
        margin-top: 1em;
        margin-left: 4.5em;
    }
    
    iframe {
        border-radius: 5px;
    }
</style>

---

# What comes next

1. Play around with an alphabet
2. Generate macros (that's time-consuming)
3. Switch from scatter plotting to normal surface plotting

---

# Porfolio / Music

---

# Porfolio / Music

I'm using evolutionary algorithm to generate music!

Big credit to this guy:

<div class="row">
    <img src="/img/music/kiecodes.png" class="kiecodes" />
    <img src="/img/music/kiecodes_qr.png" class="kiecodes_qr" />
</div>

<style>
    h1 + p {
        opacity: 1;
    }

    .row {
        display: flex;
        justify-content: center;
        align-items: center;
    }

    .kiecodes {
        width: 60%;
        border-radius: 5px;
        margin-right: 1em;
    }

    .kiecodes_qr {
        width: 10%;
        border-radius: 5px;
    }
</style>

---

# Beat vs Bit

---

<img src="/img/music/evol_2.png" class="" />

<style>
    img {
        position: absolute;
        width: 100%;
        height: 100%;
        left: 0;
        top: -2em;
    }
</style>

---

<img src="/img/music/evol_1.png" class="" />

<style>
    img {
        position: absolute;
        width: 100%;
        height: 100%;
        top: -0.4em;
        left: 1.6em;
    }
</style>

---

<img src="/img/music/evol_3.png" class="" />

<style>
    img {
        position: absolute;
        width: 100%;
        height: 100%;
        bottom: 0.1em;
    }
</style>

---

# The timeline

<img src="/img/music/evol_plans_1.png" class="timeline"/>

<style>
    .timeline {
        position: absolute;
        height: 100%;
        left: 4.8em;
        top: 1em;
        bottom: 1em;
        z-index: -1;
    }
</style>

---

# What is next?

1. try to actually go through several populations
2. friendly user-interface
3. introduce chords
4. get the final melody


<img src="/img/music/evol_plans_2.png" class="timeline"/>

<style>
    h1 + p {
        opacity: 1;
    }
    .timeline {
        position: absolute;
        height: 90%;
        left: 0em;
        top: 1em;
        z-index: -1;
    }
</style>
