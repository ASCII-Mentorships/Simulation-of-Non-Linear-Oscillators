

<div id="top"></div>
<!--
*** Thanks for checking out the Best-README-Template. If you have a suggestion
*** that would make this better, please fork the repo and create a pull request
*** or simply open an issue with the tag "enhancement".
*** Don't forget to give the project a star!
*** Thanks again! Now go create something AMAZING! :D
-->



<!-- PROJECT SHIELDS -->
<!--
*** I'm using markdown "reference style" links for readability.
*** Reference links are enclosed in brackets [ ] instead of parentheses ( ).
*** See the bottom of this document for the declaration of the reference variables
*** for contributors-url, forks-url, etc. This is an optional, concise syntax you may use.
*** https://www.markdownguide.org/basic-syntax/#reference-style-links
-->




<!-- PROJECT LOGO -->
<br />
<div align="center">
  <a href="https://github.com/github_username/repo_name">
    <img src="images/logo.gif" alt="Logo" width="80" height="80">
  </a>

<h3 align="center">Simulation of nonlinear oscillators</h3>

  <p align="center">
    This project is a part of the ASCII mentorship program for the year 2022-23
    <br />
    <a href="https://github.com/github_username/repo_name"><strong>Explore the docs »</strong></a> 
  </p>
</div>



<!-- TABLE OF CONTENTS -->
<details>
  <summary>Table of Contents</summary>
  <ol>
    <li>
      <a href="#introduction">Introduction</a>
      <ul>
        <li><a href="#prerequisites">Prerequisites</a></li>
      </ul>
    </li>
    <li><a href="#contributing">Contributing</a></li>
    <li><a href="#contact">Contact</a></li>
    <li><a href="#acknowledgments">Acknowledgments</a></li>
    <li><a href="#references">References</a></li>
  </ol>
</details>



<!-- ABOUT THE PROJECT -->
## About The Project

<img src="images/movie_s2.gif" alt="synchronization" align="center">

A research project on the synchronization of various models of nonlinear oscillators.

<p align="right">(<a href="#top">back to top</a>)</p>



<!-- INTRODUCTION -->
## Introduction
<q> In 1665, Christiaan Huygens observed that two pendulum clocks suspended on a beam always ended up swinging in exact anti-phase motion (1) regardless of each pendulum’s initial displacement. He explained this self-emergent synchronization as resulting from the coupling between the clocks, which was mediated by vibrations traveling across the beam. Huygens’ serendipitous discovery has inspired many studies to establish that self-emergent synchronization is a central process to a spectacular variety of natural systems, including the beating of the heart (2), flashing fireflies (3), pedestrians on a bridge locking their gait (4), circadian clocks in the brain (5), superconducting Josephson junctions (6), chemical oscillations (7, 8), metabolic oscillations in yeast cells (9), and life cycles of phytoplankton (10). </q>
[You can find the cited resources at the end of this file]

Nonlinear Oscillators are strikingly crucial in modelling most of the complex dynamic problems. To a large extent, first order approximations provides a decent linear model for these problems. But to really study the depths of synchronization and the various emergent states associated to it, nonlinear oscillators are inevitable to be tackled with. There is no analytical approach that fully solves these differential equations - although, many analytical approximations are extremely useful to get a qualitative feel to them. So, the numerical simulations of such systems are often the only way to study the evolution of nonlinear differential equations.  

### Phases of the project
#### Phase I:
The simulation of a system of metronomes coupled by a swing. Specifically, this will be the simulation of the Van der Pol oscillator - one of the most important nonlinear oscillators. This will be a work to reproduce the simulations that I have previously worked with. You will be using in-built MATLAB libraries and ode solvers to simply get a feel of how numerical simulations in MATLAB works. The final simulation is already attached in this repo, although I would implore you to try to write the code on your own before you look at the solution.
<div align="center">
<img src="images/metronomes.gif" alt="synchronization" length="400" width="400">
</div>

#### Phase II:
There are two equally important branch of contributions to be made to this project, depending on your domain of interest. You can either work further on the computational physics surrounding a different model that Prof. Gaurav Dar and Aniket Saha have been trying to simulate. Or you can work on analysing the Kuramoto system using analytical methods, which is currently what I am researching.
<ul>
  <li> If you are interested in the simulation aspect of this project, we will spend some time learning the basics of computational physics - the various numerical methods that these MATLAB functions use to integrate complex differential equations. After you have some idea of tracking and tackling divergent solutions, the main line of work is to simulate a significantly harder equation that more accurately models the metronome systems than the cookie cutter Van der Pol model. The biggest hurdle to simulate such an equation is the presence of non-differentiable functions that have kinks in the graph. You'll learn how such functions can lead to garbage simulation results if you're not careful enough.
   <li> If you are looking to dive deeper into the physics of nonlinear oscillators, we will simulate the Kuramoto model which is a significantly easier set of differential equations to model as compared to the toy Van der Pol problem you have already worked on. Currently, I am working to find the various phase-locked states of Kuramoto models and study the critical connectivity required in a ring of oscillators to achieve global synchrony. There are many open problems in the field, and we will be mainly working on developing analytical approaches to predict the evolution of the Kuramoto oscillators. For this, you might need to also spend some time learning the basics of Nonlinear Dynamics.
 </ul> 

### Prerequisites
<ul>
  <li> A basic coding background (You should be able to run loops in some language at the least)
  <li> Interest in dynamical systems (You have already been introduced to linear oscillators)
</ul>



<!-- CONTRIBUTING -->
## Contributing

If you have a suggestion that would make this better, please fork the repo and create a pull request. You can also simply open an issue with the tag "enhancement".

1. Fork the Project
2. Create your Feature Branch (`git checkout -b feature/AmazingFeature`)
3. Commit your Changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the Branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

<p align="right">(<a href="#top">back to top</a>)</p>



<!-- CONTACT -->
## Contact

Yashee Sinha - (WA: 9971559110) - f20190652@goa.bits-pilani.ac.in / yasheesinha@gmail.com

Project Link: [https://github.com/Bluish-y/Simulation-of-Non-Linear-Oscillators](https://github.com/Bluish-y/Simulation-of-Non-Linear-Oscillators)

<p align="right">(<a href="#top">back to top</a>)</p>



<!-- ACKNOWLEDGMENTS -->
## Acknowledgments

* Dr. Gaurav Dar

<p align="right">(<a href="#top">back to top</a>)</p>



<!-- References -->
## References
* Huygens C (1967) Oeuvres complètes (Swets & Zeitlinger Publishers, Amsterdam), Vol 15.
* Michaels DC, Matyas EP, Jalife J (1987) Mechanisms of sinoatrial pacemaker synchronization: A new hypothesis. Circ Res 61(5):704–714.
* Buck J, Buck E (1968) Mechanism of rhythmic synchronous flashing of fireflies. Fireflies of Southeast Asia may use anticipatory time-measuring in synchronizing their flashing. Science 159(3821):1319–1327.
* Strogatz SH, Abrams DM, McRobie A, Eckhardt B, Ott E (2005) Theoretical mechanics: Crowd synchrony on the Millennium Bridge. Nature 438(7064):43–44.
* Liu C, Weaver DR, Strogatz SH, Reppert SM (1997) Cellular construction of a circadian clock: Period determination in the suprachiasmatic nuclei. Cell 91(6):855–860.
* Wiesenfeld K, Colet P, Strogatz S (1998) Frequency locking in Josephson arrays: Connection with the Kuramoto model. Phys Rev E Stat Phys Plasmas Fluids Relat Interdiscip Topics 57(2):1563–1569
* Kiss IZ, Zhai Y, Hudson JL (2002) Emerging coherence in a population of chemical
oscillators. Science 296(5573):1676–1678.
* Taylor AF, Tinsley MR, Wang F, Huang Z, Showalter K (2009) Dynamical quorum
sensing and synchronization in large populations of chemical oscillators. Science
323(5914):614–617.
* Danø S, Sørensen PG, Hynne F (1999) Sustained oscillations in living cells. Nature
402(6759):320–322.
*  Massie TM, Blasius B, Weithoff G, Gaedke U, Fussmann GF (2010) Cycles, phase synchronization, and entrainment in single-species phytoplankton populations. Proc Natl
Acad Sci USA 107(9):4236–4241.
