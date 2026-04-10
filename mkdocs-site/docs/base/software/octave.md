---
title: "Octave"
tags:
  - software

keywords:
  []
---

[GNU Octave](https://octave.org/) is a scientific programming language that has a Powerful mathematics-oriented syntax with built-in 2D/3D plotting and visualization tools.  It is free and open-source software (FOSS) and is Drop-in compatible with many [MATLAB](matlab.md) scripts.

## Running Octave code 
Consider the following example code:

**`octave_2d_plot.m`**
```matlab
x = -10:0.1:10;
y = sin (x);
plot (x, y);
title ("Simple 2-D Plot");
xlabel ("x");
ylabel ("sin (x)");

print -dpng octave_2d_plot.png
quit
```

Here is a simple Slurm script that you can use to run `octave_2d_plot.m`:

**`octave_job_1.sh`**
```bash
#!/bin/bash -l
#SBATCH --time=0-00:10
#SBATCH --ntasks=1
#SBATCH --cpus-per-task=1
#SBATCH --mem=4000M
module load octave/5.2.0 gnuplot/5.4.2

octave --no-gui octave_2d_plot.m
```

Note that Octave relies on the Gnuplot package to generate plots.

### Running MATLAB code 
Octave can often be used as a drop-in replacement for running MATLAB scripts, like the `cosplot.m` example on our [MATLAB](matlab#running_a_matlab_code.md) page:

**`octave_job_1.sh`**
```bash
#!/bin/bash -l
#SBATCH --time=0-00:10
#SBATCH --ntasks=1
#SBATCH --cpus-per-task=1
#SBATCH --mem=4000M
module load octave/5.2.0 gnuplot/5.4.2

octave --no-gui --traditional --eval "cosplot"
```

## Further reading 
* [GNU Octave Homepage](https://octave.org/)
* [Documentation for GNU Octave v5.2.0](https://docs.octave.org/v5.2.0/) (available in StdEnv/2020)
* [Documentation for GNU Octave v4.2.2](https://docs.octave.org/v4.2.2/) (available in StdEnv/2018.3)