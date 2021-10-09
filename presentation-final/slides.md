# PCGG. Final Presentation

Anna Boronina

---

# Portfolio / mountains

<div class="row">
    <img src="/img/caves/paper2.png" class="paper">
    <img src="/img/caves/paper2_qr.png" class="paper_qr" />
</div>

<style>
    .row {
        margin-top: 5em;
        display: flex;
        justify-content: center;
        align-items: center;
    }

    .paper {
        width: 80%;
        border-radius: 5px;
        margin-right: 1em;
    }

    .paper_qr {
        width: 10%;
        border-radius: 5px;
        margin-top: 1em;
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

# L-System for 3D

<img src="/img/caves/mountain_gen.png">

<style>
    img {
        width: 80%;
        margin-left: 4em;
    }
</style>


---

# My midterm results

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

# And now!

---

<img src="/img/caves/types.png">


---

# Type: Calm 16x16

<img src="/img/caves/calm_mount.png">

<style>
    img {
        width: 90%;
        margin-top: 2.5em;
        margin-left: 3em;
    }
</style>

---

# Type: Hill 16x16

<img src="/img/caves/hill_mount.png">

<style>
    img {
        width: 90%;
        margin-top: 2.5em;
        margin-left: 3em;
    }
</style>

---

# Type: Steep 16x16

<img src="/img/caves/steep_mount.png">

<style>
    img {
        width: 90%;
        margin-top: 2.5em;
        margin-left: 3em;
    }
</style>

---

# Several connected tiles (4x4 field, 8x8 tiles)

<div>
    <img src="/img/caves/connected1.png">
    <img src="/img/caves/connected2.png">
</div>


<style>
    h1 + p {
        opacity: 1;
    }
    img {
        width: 45%;
        margin-top: 3em;
        margin-left: 0.5em;
    }
    div {
        margin-left: 4em;
        display: flex;
    }
</style>


---

# Several connected tiles (4x4 field, 8x8 tiles)

<div>
    <img src="/img/caves/connected3.png">
    <img src="/img/caves/connected4.png">
</div>


<style>
    h1 + p {
        opacity: 1;
    }
    img {
        width: 45%;
        margin-top: 3em;
        margin-left: 0.5em;
    }
    div {
        margin-left: 4em;
        display: flex;
    }
</style>

---

# Metrics

- tyles are connected with each other
- _calm_ is flatter than _hill_
- _hill_ is flatter than _steep_
- the fact that there are square tiles is not so obvious

---

# Porfolio / Music

---

<img src="/img/music/cheapmusic.png">

---

<img src="/img/music/hug.png">

<style>
    img {
        margin-top: -1.5em;
    }
</style>

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

<img src="img/music/fitness-reality.png">

<style>
    img {
        margin-top: -2em;
    }
</style>

---

# The problem: it doesn't evolve

```python
88000 [66, 66, 66, 66, 66, 66, 66, 66, 63, 35, 34, 27, 3, -4, -11, -16, -17]
89000 [66, 66, 66, 66, 66, 66, 66, 66, 35, 33, 32, 28, -4, -16, -17, -18, -24]
90000 [66, 66, 66, 66, 66, 66, 66, 66, 66, 46, 27, 26, 2, -5, -11, -16, -17]
91000 [66, 66, 66, 66, 66, 66, 66, 66, 42, 30, 19, 18, -11, -12, -12, -23, -24]
92000 [66, 66, 66, 66, 66, 66, 66, 66, 66, 40, 38, 21, 3, -3, -4, -16, -17]
93000 [66, 66, 66, 66, 66, 66, 66, 66, 48, 30, 23, 20, 3, -9, -16, -18, -23]
```

---

# My question from the midterm: What is next?

1. try to actually go through several populations
2. ~~friendly~~ user-interface
3. ~~introduce chords~~
4. get ~~the final melody~~ a melody


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

---

# Initial VS Last Epoch

Generation 0

<audio controls src="/img/music/audio/gen0.mp3"/>

16 notes per bar, 2 bars, 4 bits per note, 15 initial genoms, 100k epochs

<audio controls src="/img/music/audio/gen99999.mp3"/>

<style>
    h1 + p {
        opacity: 1;
    }
    audio {
        margin-bottom: 0.5em;
    }
</style>

---

# Metrics

- repeatedness of a melody
- going up at the beginning, going down at the end

---

# THE PROJECT

---

<img src="/img/project/1.png">

---

<img src="/img/project/2.png">

---

<img src="/img/project/3.png">

---

<img src="/img/project/fewmomlater.jpg">

---

<img src="/img/project/4.png">

---

<img src="/img/project/5.png">

---

<img src="/img/project/tv.png">


---

<img src="/img/project/whereisyourrage.jpg">

<style>
    img {
        margin-top: -1.5em;
        width: 90%;
        margin-left: 2.5em;
    }
</style>

---

<img src="/img/project/actupresist.jpeg">

<style>
    img {
        margin-top: 1.5em;
    }
</style>

---

<img src="/img/project/ballroom1.jpg">

<style>
    img {
        margin-top: -1.5em;
        margin-left: 2.3em;
        width: 90%;
    }
</style>

---

<img src="/img/project/ballroom2.jpg">

<style>
    img {
        margin-top: -1.5em;
        width: 90%;
        margin-left: 2em;
    }
</style>

---

# So, the game...

---

<img src="/img/project/groups.png">

<style>
    img {
        margin-top: -1.5em;
        margin-left: 1em;
    }
</style>

---

<img src="/img/project/progress_bars.png">

<style>
    img {
        margin-top: -2em;
        margin-left: 4em;
    }
</style>


---

<img src="/img/project/pcg.png">

<style>
    img {
        margin-top: -2em;
        margin-left: 1em;
    }
</style>

---


# Dice

- rolled once every 2-4 rounds (an adjustable rule)
- can be rolled more often for gay people and less often for non-gay people

---

# Discussion

- each group is given a limited time for a discussion
- one group can speak only once during a round (an adjustable rule)
- if an action card is targeted at a particular group, other groups can still react

---

# Game Master or Mistress

**They can**
- change the dice rule but not remove it completely
- choose a set of cards to play
- configure the initial status bars
- limit discussion time

**They must**
- resolve arguments
- update the status bars and number of people per group bars

<style>
    h1 + p {
        opacity: 1;
    }
</style>

---

# Cards

---

<img src="/img/project/aztcard.png">

<style>
    img {
        margin-top: -2em;
        margin-left: 12em;
    }
</style>

---

<img src="/img/project/church_card.png">

<style>
    img {
        margin-top: -2em;
        margin-left: 12em;
    }
</style>

---

<img src="/img/project/madonna_card.png">

<style>
    img {
        margin-top: -2em;
        margin-left: 12em;
    }
</style>

---

# Other possible cards

**1. New gay bar opened! Nevertheless, they do not let HIV-positive and transgender people in.**
- ACT UP can choose to protest or let it be
- T-Community can stand up for themselves or choose not to
- Journalists can choose to write about it or not


**2. Cosmopolitan magazine published an interview with a doctor and claims that women cannot get HIV.**
- Women from ACT UP and outside of ACT UP can choose to protest or let it be


**3. ACT UP is running out of money, they need to organize a fund raising**
- ACT UP can organize a fund raising event
- Rich people can choose to support them or not

<style>
    h1 + p {
        opacity: 1;
    }
</style>

---

# Other possible cards

**4. Police came to the ball and arrested some people**
- T-Community can try and raise money to bail them out


**5. Government decided to bury first HIV-positive on Hard Island under seven feet of dirt instead of usual three.** 

<style>
    h1 + p {
        opacity: 1;
    }
</style>

---

# Hm, who wins?

Whoever doesn't die or has the highest score by the end of the game

<style>
    h1 + p {
        opacity: 1;
    }
</style>

---

# Metrics

- it's history-based
- simulation of dying
- at least one of you got interested

<style>
    h1 + p {
        opacity: 1;
    }
</style>