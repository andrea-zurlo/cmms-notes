<link rel="stylesheet" type="text/css" href="https://tikzjax.com/v1/fonts.css">
<script src="https://tikzjax.com/v1/tikzjax.js"></script>

<script type="text/x-mathjax-config">
    MathJax.Hub.Config({
    tex2jax: {
        skipTags: ['script', 'noscript', 'style', 'textarea', 'pre'],
        inlineMath: [['$','$']]
    }
    });
</script>
<script src="https://cdn.mathjax.org/mathjax/latest/MathJax.js?config=TeX-AMS-MML_HTMLorMML" type="text/javascript"></script>


# Computational Methods in Material Science

- [Computational Methods in Material Science](#computational-methods-in-material-science)
  - [1. Recap of statistical mechanics](#1-recap-of-statistical-mechanics)
  - [3. Molecular dynamics](#3-molecular-dynamics)

## 1. Recap of statistical mechanics

## 3. Molecular dynamics

MD is based on the application of Newton's equations of motion to atomic or molecular systems. The motion of the particles is simulated over a finite period of time by solving the equations numerically. The various way to solve differential equations numerically are called *integration schemes*.

- Newton's equation of motion
- numerical solution (integration)
- sympletic integrator
- foreward Euler
- Verlet
- velocity Verlet
- energy conservation
- chaotic behaviour
- timestep