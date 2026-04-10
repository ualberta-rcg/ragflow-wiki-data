---
title: "Octave"
slug: "octave"
lang: "base"

source_wiki_title: "Octave"
source_hash: "334a4dabf4b719519c17e7ad7874bc51"
last_synced: "2026-04-09T20:02:20.019957+00:00"
last_processed: "2026-04-10T09:20:11.434173+00:00"

tags:
  - software

keywords:
  []

status:
  downloaded: true
  converted: true
  tagged: true
  keywords_generated: false
  ragflow_synced: false
  qa_generated: false
---

[GNU Octave](https://octave.org/) is a scientific programming language that has a powerful mathematics-oriented syntax with built-in 2D/3D plotting and visualization tools. It is free and open-source software (FOSS) and is drop-in compatible with many [MATLAB](matlab.md) scripts.

## Running Octave code
Consider the following example code:
```matlab title="octave_2d_plot.m"
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
```bash title="octave_job_1.sh"
#!/bin/bash -l
#SBATCH --time=0-00:10
#SBATCH --ntasks=1
#SBATCH --cpus-per-task=1
#SBATCH --mem=4000M
module load octave/5.2.0 gnuplot/5.4.2

octave --no-gui octave_2d_plot.m
```

!!! note
    Octave relies on the Gnuplot package to generate plots.

### Running MATLAB code
Octave can often be used as a drop-in replacement for running MATLAB scripts, like the `cosplot.m` example on our [MATLAB](matlab.md#running-a-matlab-code) page:
```bash title="octave_job_1.sh"
#!/bin/bash -l
#SBATCH --time=0-00:10
#SBATCH --ntasks=1
#SBATCH --cpus-per-task=1
#SBATCH --mem=4000M
module load octave/5.2.0 gnuplot/5.4.2

octave --no-gui --traditional --eval "cosplot"
```

## Further reading
*   [GNU Octave Homepage](https://octave.org/)
*   [Documentation for GNU Octave v5.2.0](https://docs.octave.org/v5.2.0/) (available in StdEnv/2020)
*   [Documentation for GNU Octave v4.2.2](https://docs.octave.org/v4.2.2/) (available in StdEnv/2018.3)