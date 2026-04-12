---
title: "Gaussian error messages"
slug: "gaussian_error_messages"
lang: "base"

source_wiki_title: "Gaussian error messages"
source_hash: "e4c1c0c5157728c57e19d1091ec36da3"
last_synced: "2026-04-10T15:28:10.183781+00:00"
last_processed: "2026-04-11T07:34:57.444178+00:00"

tags:
  - computationalchemistry

keywords:
  - "FOPT requested"
  - "polarization functions"
  - "re-calculate"
  - "CEP-121G"
  - "code"
  - "markup"
  - "Distance matrix"
  - "linked jobs"
  - "Convergence criterion not met"
  - "Read-in occupied orbitals"
  - "Checkpoint file"
  - "Gaussian errors"
  - "Lnk1e"
  - "Fixing the error"
  - "malloc failed"
  - "Convergence failure"
  - "Molecular orbitals"
  - "Link 9999"
  - "geom=modify"
  - "Basis set"
  - "translate"
  - "checkpoint file"
  - "retrieve information"
  - "closing tag"
  - "Optimization algorithm"
  - "Erroneous Write"
  - "Geometry optimization"
  - "KLT.ge.NIJTC in GetRSB"
  - "Error termination"
  - "missing directory"
  - "GAUSS_SCRDIR"
  - "XML"
  - "Z-matrix"
  - "Opt=ReadFC"
  - "geometry specification"
  - "segmentation violation"
  - "%mem"
  - "error termination"
  - "Input error"
  - "fixing the error"
  - "optimization"
  - "step sizes"
  - "zero exponent"
  - "Gaussian error"
  - "Normal termination"
  - "input error"
  - "mkdir"
  - "SCF convergence failure"
  - "SCF Done"
  - "z-matrix"
  - "run out of memory"
  - "memory allocation"
  - "Gaussian"
  - "force constants"
  - "Point group"
  - "error explanation"
  - "Unrecognized atomic symbol"
  - "job script"

questions:
  - "What are the common reasons a Gaussian job might fail to terminate normally if no specific error message is produced?"
  - "What causes the \"Erroneous Write\" error in Gaussian, and how can a user resolve it?"
  - "Why does the \"Link 9999\" error occur, and what strategies can be used to fix geometry optimization convergence issues?"
  - "What specific conditions during an optimization process necessitate the use of linked jobs or modified force constant calculations?"
  - "How should a user choose between the Opt=ReadFC, Opt=CalcFC, and Opt=CalcAll commands when utilizing data from a previous job?"
  - "What discrepancy between force convergence and step size convergence typically appears in the final output under these circumstances?"
  - "How can a poorly defined z-matrix cause an optimization algorithm to fail, and what are the recommended solutions?"
  - "What causes the \"Reading basis center\" error during a job, and how can it be resolved?"
  - "Why might the \"Operation on file out of range\" error occur when attempting to retrieve data from a checkpoint file?"
  - "What causes the \"End of file in GetChg\" error, and how can it be resolved by modifying the charge, multiplicity, or route section?"
  - "How should a user troubleshoot a \"Change in point group or standard orientation\" error that occurs during the optimization process?"
  - "What triggers the \"Unrecognized atomic symbol\" error when reading a general basis set, and how can this input issue be fixed?"
  - "What specific commands or actions trigger this error when interacting with the checkpoint file?"
  - "Why might the requested information be missing from the checkpoint file in the first place?"
  - "What are the recommended steps to fix this error and provide the missing information?"
  - "What was the primary reason for the job termination according to the log output?"
  - "What were the final energy value and the number of cycles completed before the SCF calculation failed?"
  - "Which specific executable triggered the error termination, and how much CPU time did the job consume?"
  - "What are the recommended methods for fixing an SCF convergence failure when running a calculation?"
  - "How should a user address the error indicating a mismatch between the number of variables (NVar) and degrees of freedom (NDOF) during a full optimization?"
  - "What causes the \"Unable to project read-in occupied orbitals\" error, and how can it be resolved?"
  - "How does Gaussian handle situations where polarization functions are specified but do not actually exist?"
  - "What are the recommended fixes and workarounds for the error associated with using CEP-121G*?"
  - "Where does the description for the \"KLT.ge.NIJTC in GetRSB\" error typically appear in the system output?"
  - "What is the recommended fix for an MP2 calculation failure related to the CEP-121G* pseudopotential?"
  - "How can a user resolve the \"Problem with the distance matrix\" error caused by atoms being placed too close together?"
  - "What specific formatting mistakes in the input file commonly trigger the \"invalid number of steps\" or \"End of file in ZSymb\" errors?"
  - "How can you resolve the \"Linear search skipped for unknown reason\" error when the Hessian becomes invalid during optimization?"
  - "What are the common causes and solutions for Z-matrix input errors, such as \"Variable index out of range\" or \"Unknown center\"?"
  - "Why does the \"malloc failed\" error occur, and what steps can be taken to fix memory allocation issues?"
  - "What specific Gaussian error message and termination process are detailed in the text?"
  - "What is the fundamental root cause of the \"End of file in ZSymb\" error?"
  - "What common formatting omission in the input file triggers this specific z-matrix issue?"
  - "What is the general meaning of the \"Resource temporarily unavailablemalloc failed\" error message?"
  - "What specific configuration might cause the computer to run out of memory and trigger this error?"
  - "What are the two recommended methods for fixing this memory-related error?"
  - "How do missing title lines or incorrect variables in the checkpoint file cause input errors when using the `geom=modify` command?"
  - "What is the proper way to configure memory settings in both the Gaussian input file and the job submission script to prevent \"galloc\" allocation errors?"
  - "How can you resolve the \"No such file or directory\" error related to the `GAUSS_SCRDIR` environment variable?"
  - "What is the primary function of the `</translate>` closing tag within a markup or programming context?"
  - "How do parsers or translation systems process the content that immediately precedes this specific tag?"
  - "In which specific software frameworks or document formats is this tag typically implemented?"
  - "What specific error message is being addressed in the text?"
  - "What is the underlying cause of this segmentation violation error?"
  - "How can a user fix the error related to the missing directory or GAUSS_SCRDIR variable?"
  - "What is the primary function of the `</translate>` closing tag within a markup or programming context?"
  - "How do parsers or translation systems process the content that immediately precedes this specific tag?"
  - "In which specific software frameworks or document formats is this tag typically implemented?"

status:
  downloaded: true
  converted: true
  tagged: true
  keywords_generated: true
  ragflow_synced: true
  qa_generated: false
---

*Parent page: [Gaussian](gaussian.md)*
This list was originally assembled by Professor Cory C. Pye.

## Normal Termination of Gaussian
Normally Gaussian will terminate with a line such as

```
 Job cpu time:       0 days  0 hours 26 minutes 18.3 seconds.
 Elapsed time:       0 days  0 hours  6 minutes 43.3 seconds.
 Normal termination of Gaussian 16 at Tue Nov 14 15:31:56 2017.
```

If a job does not end with these lines and no other error message is produced, it usually means that:
* your disk quota was exceeded (see [File quotas and policies](storage-and-file-management.md#filesystem-quotas-and-policies));
* the job exceeded the time requested from the [scheduler](running-jobs.md) (`--time=HH:MM:SS`);
* the job exceeded the memory requested (`--mem=`) (see [Monitoring jobs](running-jobs.md#monitoring-jobs)); or
* the job produced more data that can fill up the local disk on the compute node.

## Erroneous Write

**Description of error**
Near the end of the output, it reads something similar to

```
Erroneous write. write 122880 instead of 4239360.
fd = 3
Erroneous write. write 122880 instead of 4239360.
fd = 3
writwa
writwa: File exists
```

or

```
Erroneous write. write -1 instead of 3648000. 

fd = 4
writwa
writwa: No space left on device
```

or

```
Erroneous write during file extend. write -1 instead of 8192
Probably out of disk space.
Write error in NtrExt1
```

!!! info "Explanation of error"
    Typically, this occurs when you have run out of disk space. This could occur if you have exceeded your quota, if a disk is physically full, or (more rarely) a network drive is unavailable because of a communication time out.

!!! tip "Fixing the error"
    * Check your disk quota with `quota`. Delete unnecessary files.
    * Your job may simply be too big to run on current hardware. Try using a smaller basis set.

## Link 9999

**Description of error**
At the end of your output, you get lines such as

```
 Error termination request processed by link 9999.
 Error termination via Lnk1e in /disc30/g98/l9999.exe.
```

A few pages above, the following lines appear:

```
         Item               Value     Threshold  Converged?
 Maximum Force            0.020301     0.000450     NO 
 RMS     Force            0.007068     0.000300     NO 
 Maximum Displacement     0.078972     0.001800     NO 
 RMS     Displacement     0.023716     0.001200     NO 
 Predicted change in Energy=-3.132299D-05
 Optimization stopped.
    -- Number of steps exceeded,  NStep=  34
    -- Flag reset to prevent archiving.
                       ----------------------------
                       ! Non-Optimized Parameters !
                       ! (Angstroms and Degrees)  !
```

!!! info "Explanation of error"
    This means that the Gaussian job terminated abnormally for some reason internal to Gaussian. The most common cause is that a geometry optimization has not converged.

!!! tip "Fixing the error"
    Geometry optimizations usually fail to converge for one of these reasons:
    * If your initial starting structure is not good, can you provide a better starting structure? For example, optimize the structure at a lower level of theory and use that as the new starting structure. However, if it looks as if the structure is converging to what you want, as seen in your visualizer of choice, then restart the optimization from the last step, for example by using `geom=allcheck` in the route line. It may also be a good idea to use `opt=CalcFC` in these situations if it is not too expensive. It is probably not too expensive at the HF or DFT level of theory.
    * If your starting force constants matrix (Hessian) is poor, use a better one. This typically manifests itself when the force constants vary a lot between levels, or if there is a large geometry change during the optimization. One can carry out a series of linked jobs using `--Link1--`. If you have a previous job, then usually `Opt=ReadFC` works well, but occasionally `Opt=CalcFC`, or rarely `Opt=CalcAll` are needed. In these cases, the forces are often converged, but the step sizes are not, and the final output will look like
        ```
                 Item               Value     Threshold  Converged?
         Maximum Force            0.000401     0.000450     YES
         RMS     Force            0.000178     0.000300     YES
         Maximum Displacement     0.010503     0.001800     NO 
         RMS     Displacement     0.003163     0.001200     NO 
        ```
    * Rarely, the coordinate system itself may be at fault. If coordinates are specified with a z-matrix, it is easy to make poor choices which result in three of the four atoms used to define a torsion angle (also called a dihedral angle) being collinear, meaning the angle is close to 0 or 180 degrees. This can cause the optimization algorithm to fail. In this case you should either formulate a better z-matrix or use the default redundant internal coordinates.
    * If these methods fail, another option is to change the optimization method from the default to another type, such as `opt=ef` (if the number of variables is less than 50) or `opt=gdiis` (for floppy molecules).

## Angle Alpha Is Outside the Valid Range of 0 to 180

**Description of error**
At the end of your output, you get a line such as

```
 ------------------------------------------------------------------------
 Error termination via Lnk1e in /disc30/g98/l716.exe.
```

The lines above will be a z-matrix, above which will contain lines such as

```
  Error on Z-matrix card number    9
 angle Alpha is outside the valid range of 0 to 180.
 Conversion from Z-matrix to cartesian coordinates failed:
 ------------------------------------------------------------------------
                         Z-MATRIX (ANGSTROMS AND DEGREES)
 CD Cent Atom  N1     Length/X     N2    Alpha/Y     N3     Beta/Z      J
 ------------------------------------------------------------------------
...
  9   9  H     8   0.962154(  8)   1   -1.879( 16)   2    0.000( 23)   0
...
```

!!! info "Explanation of error"
    This means that the Gaussian job terminated abnormally because an angle x in the z-matrix changed to become outside the allowed range of 0 < x < 180.

!!! tip "Fixing the error"
    This can happen if there are large geometry changes in a molecule, especially one composed of interacting fragments. Re-define the z-matrix, or use a different coordinate system.

## Reading Basis Center

**Description of error**
At the end of your output, you get a line such as

```
 End of file reading basis center.
 Error termination via Lnk1e in /disc30/g98/l301.exe.
 Job cpu time:  0 days  0 hours  0 minutes  1.9 seconds.
 File lengths (MBytes):  RWF=   11 Int=    0 D2E=    0 Chk=   10 Scr=    1
```

!!! info "Explanation of error"
    This is an input error. You are attempting to read in a general basis set but you forgot to put in the basis set.

!!! tip "Fixing the error"
    Put in the basis set, or remove the `gen` from the route line and specify an internal basis set.

## Operation on File Out of Range

**Description of error**
At the end of your output, you get a line such as

```
 Error termination in NtrErr:
 NtrErr Called from FileIO.
```

Above this, you have something like

```
 Operation on file out of range.
FileIO: IOper= 2 IFilNo(1)=-19999 Len=     1829888 IPos=  -900525056 Q=       4352094416

dumping /fiocom/, unit = 1 NFiles =   109 SizExt =    524288 WInBlk =      1024
                   defal = T LstWrd =  7437256704 FType=2 FMxFil=10000
```

...followed by a lot of numbers.

!!! info "Explanation of error"
    This typically happens when you try to retrieve something from the checkpoint file (with `Opt=ReadFC` or `guess=read` or `geom=allcheck/modify`) that is not there, either because you did not calculate it previously, or you ran out of disk space or time while running the earlier job and the information needed wasn't written to the checkpoint file.

!!! tip "Fixing the error"
    Re-calculate or type in the information required.

## End of File in GetChg

**Description of error**
At the end of your output, you get a line such as

```
 Symbolic Z-matrix:
 End of file in GetChg.
 Error termination via Lnk1e in /disc30/g98/l101.exe.
 Job cpu time:  0 days  0 hours  0 minutes  0.5 seconds.
 File lengths (MBytes):  RWF=    6 Int=    0 D2E=    0 Chk=   11 Scr=    1
```

!!! info "Explanation of error"
    You have specified an input in which the charge/multiplicity line is required, but you forgot to put it in. Alternatively, you meant to read the charge/multiplicity from the checkpoint, but forgot to put `geom=allcheck` in the route section.

!!! tip "Fixing the error"
    Put the charge/multiplicity line in, or put `geom=allcheck` in the route section.

## Change in Point Group or Standard Orientation

**Description of error**
At the end of your output, you get a line such as

```
 Stoichiometry    CdH14O7(2+)
 Framework group  C2[C2(CdO),X(H14O6)]
 Deg. of freedom   30
 Full point group                 C2      NOp   2
 Omega: Change in point group or standard orientation.

Error termination via Lnk1e in /disc30/g98/l202.exe.
 Job cpu time:  0 days  3 hours 35 minutes 40.8 seconds.
 File lengths (MBytes):  RWF=   58 Int=    0 D2E=    0 Chk=   19 Scr=    1
```

!!! info "Explanation of error"
    During the optimization process, either the standard orientation or the point group of the molecule has changed. If the former, a visualization program will show this as a sudden flipping of the structure, typically by 180 degrees. This error is a lot less common since Gaussian 03 was released.

!!! tip "Fixing the error"
    * This can indicate that your z-matrix is not correctly specified, if you go from a point group (e.g C2v) to a subgroup of the point group (C2 or Cs or C1).
    * If the point group here is correct, it could indicate that your starting structure had too high symmetry and you should desymmetrize it.
    * Rarely: If the point group here is incorrect (of higher symmetry), then your z-matrix should be reformulated with more symmetry.
    * If you don't care about symmetry, then you could turn symmetry completely off.

## Unrecognized Atomic Symbol

**Description of error**
At the end of your output, you get a line such as

```
 General basis read from cards:  (6D, 7F)
 Unrecognized atomic symbol ic2 

Error termination via Lnk1e in /disc30/g98/l301.exe.
 Job cpu time:  0 days  0 hours  0 minutes  1.6 seconds.
 File lengths (MBytes):  RWF=    6 Int=    0 D2E=    0 Chk=   12 Scr=    1
```

!!! info "Explanation of error"
    You are reading in a general basis set, but the atom specified (in the above example, `ic2`) does not match any standard atomic symbol. This can also happen in a link job if a previous step uses default coordinates (which wipes the z-matrix) and then you try to modify the z-matrix with `geom=modify`. The z-matrix variable section is ignored, but Gaussian may attempt to interpret it as basis set information.

!!! tip "Fixing the error"
    Type in the correct atomic symbol.

## Convergence Failure -- Run Terminated

**Description of error**
At the end of your output, you get a line such as

```
 >>>>>>>>>> Convergence criterion not met.
 SCF Done:  E(RHF) =  -2131.95693715     A.U. after  257 cycles
             Convg  =    0.8831D-03             -V/T =  2.0048
             S**2   =   0.0000
 Convergence failure -- run terminated.
 Error termination via Lnk1e in /disc30/g98/l502.exe.
 Job cpu time:  0 days  0 hours  5 minutes  0.5 seconds.
 File lengths (MBytes):  RWF=   15 Int=    0 D2E=    0 Chk=    8 Scr=    1
```

or

```
  >>>>>>>>>> Convergence criterion not met.
 SCF Done:  E(UHF) =  -918.564956094     A.U. after   65 cycles
             Convg  =    0.4502D-04             -V/T =  2.0002
             S**2   =   0.8616
 Annihilation of the first spin contaminant:
 S**2 before annihilation     0.8616,   after     0.7531
 Convergence failure -- run terminated.
 Error termination via Lnk1e in /disc30/g98/l502.exe.
 Job cpu time:  0 days  0 hours  3 minutes 56.2 seconds.
 File lengths (MBytes):  RWF=   11 Int=    0 D2E=    0 Chk=    8 Scr=    1
```

!!! info "Explanation of error"
    The SCF (self-consistent field) procedure has failed to converge.

!!! tip "Fixing the error"
    The SCF procedure might fail to converge if a poor guess is provided for the molecular orbitals.
    * Try using a better guess (`guess=read`) by carrying out an SCF using the same starting structure, but at a lower level of theory such as HF/STO-3G.
    * If this doesn't work, try using an alternate SCF converger such as `SCF=QC` or `SCF=XQC`.
    In some cases, a poor geometry can result in an unconverged SCF, if a bond is way too long or too short.
    * Fixing the initial geometry may fix the problem.
    In some cases, the optimizer itself takes a bad step, resulting in this error.
    * Resubmitting the job with the penultimate (or earlier) geometry and a newly evaluated Hessian can fix this.

## FOPT Requested but NVar= XX while NDOF= YY

**Description of error**
At the end of your output, you get a line such as

```
 FOPT requested but NVar= 29 while NDOF= 15.
 Error termination via Lnk1e in /disc30/g98/l202.exe.
 Job cpu time:  0 days  0 hours  0 minutes  1.3 seconds.
 File lengths (MBytes):  RWF=   11 Int=    0 D2E=    0 Chk=    1 Scr=    1
```

!!! info "Explanation of error"
    You have requested a full optimization (FOpt), including checking the variables to make sure the correct number are present. The check indicates that there is an error.

!!! tip "Fixing the error"
    If NDOF is less than NVar, then it means that the molecule is being run in a lower symmetry than it actually is, and you should consider running it with higher symmetry.
    If NVar is less than NDOF, it usually means that your z-matrix has too many constraints, not appropriate to the actual symmetry.
    You can bypass the check using `Opt` instead of `FOpt`, but this is not recommended.

## Unable to Project Read-in Occupied Orbitals

**Description of error**
At the end of your output, you get lines such as

```
 Initial guess read from the checkpoint file:
 BiAq7_3+_C2.chk
 Unable to project full set of read-in orbitals.
 Projecting just the  36 occupied ones.
 Unable to project read-in occupied orbitals.
 Error termination via Lnk1e in /disc30/g98/l401.exe.
 Job cpu time:  0 days  0 hours  0 minutes 29.5 seconds.
 File lengths (MBytes):  RWF=   18 Int=    0 D2E=    0 Chk=   17 Scr=    1
```

!!! info "Explanation of error"
    You are reading in a molecular-orbital guess from the checkpoint file, but the projection from the old to the new basis set has failed. This can happen if certain pseudopotential basis sets (CEP-121G*) are used with polarization functions where no polarization functions actually exist. In some cases Gaussian uses placeholder polarization functions with zero exponent.

!!! tip "Fixing the error"
    * Don't use `CEP-121G*`, use `CEP-121G` for the elements in question. They are the same for many elements.
    * A workaround is not to use the guess.

## KLT.ge.NIJTC in GetRSB

**Description of error**
At the end of your output, you get lines such as

```
 (rs|ai) integrals will be sorted in core.
 KLT.ge.NIJTC in GetRSB.
 Error termination via Lnk1e in /disc30/g98/l906.exe.
 Job cpu time:  0 days  0 hours  0 minutes 32.7 seconds.
 File lengths (MBytes):  RWF=  514 Int=    0 D2E=    0 Chk=   10 Scr=    1
```

!!! info "Explanation of error"
    The MP2 calculation has failed. It may be related to the pseudopotential problem above.

!!! tip "Fixing the error"
    Don't use `CEP-121G*`, use `CEP-121G` for the elements in question. They are the same for many elements.

## Symbol XXX Not Found in Z-matrix

**Description of error**
At the end of your output, you get lines such as

```
 Symbol "H3NNN" not found in Z-matrix.
 Error termination via Lnk1e in /disc30/g98/l101.exe.
 Job cpu time:  0 days  0 hours  0 minutes  0.5 seconds.
 File lengths (MBytes):  RWF=    6 Int=    0 D2E=    0 Chk=   14 Scr=    1
```

!!! info "Explanation of error"
    This is an input error. You have typed in a variable name (in the above example, `H3NNN`) that is not in the z-matrix.

!!! tip "Fixing the error"
    Either type the correct symbol, or add it to the z-matrix, as appropriate.

## Variable X Has Invalid Number of Steps

**Description of error**
At the end of your output, you get lines such as

```
 Scan the potential surface.
 Variable   Value     No. Steps Step-Size
 -------- ----------- --------- ---------
 Variable  1 has invalid number of steps      -1.
 Error termination via Lnk1e in /disc30/g98/l108.exe.
 Job cpu time:  0 days  0 hours  0 minutes  0.7 seconds.
 File lengths (MBytes):  RWF=   11 Int=    0 D2E=    0 Chk=   13 Scr=    1
```

!!! info "Explanation of error"
    This is an input error. You are attempting to do a generate rigid potential energy scan. Most likely, you have two blank lines instead of one between the z-matrix and the variables.

!!! tip "Fixing the error"
    Delete the extra blank line.

## Problem with the Distance Matrix

**Description of error**
At the end of your output, you get lines such as

```
  Problem with the distance matrix.
 Error termination via Lnk1e in /disc30/g98/l202.exe.
 Job cpu time:  0 days  9 hours 11 minutes 14.3 seconds.
 File lengths (MBytes):  RWF=  634 Int=    0 D2E=    0 Chk=   10 Scr=    1
```

!!! info "Explanation of error"
    This can be an input error. At least two atoms are too close together, with the list given above.
    Rarely, this can be a program error, particularly when one of the distances is NaN. This can happen when trying to optimize diatomics and you start off with too large a distance.

!!! tip "Fixing the error"
    You will need to check variables and the z-matrix of the atoms in question to make sure there are no atoms close together. This can be a result of a missing minus sign in a torsion angle for molecules with planes of symmetry, in which the two atoms related by the plane of symmetry are now coincident, that is, they have distance 0 between them.

## End of File in ZSymb

**Description of error**
At the end of your output, you get lines such as

```
 Symbolic Z-matrix:
 Charge =  0 Multiplicity = 1
 End of file in ZSymb.
 Error termination via Lnk1e in /disc30/g98/l101.exe.
 Job cpu time:  0 days  0 hours  0 minutes  0.6 seconds.
 File lengths (MBytes):  RWF=    6 Int=    0 D2E=    0 Chk=    9 Scr=    1
```

!!! info "Explanation of error"
    This is an input error. Gaussian can't find the z-matrix. There are two common causes:
    1. You may have omitted the blank line at the end of the geometry specification.
    2. You may have intended to get the z-matrix and parameters from the checkpoint file, but forgot to type `geom=check`.

!!! tip "Fixing the error"
    Add a blank line at the end or add `geom=check`.

## Linear Search Skipped for Unknown Reason

**Description of error**
At the end of your output, you get lines such as

```
 RFO could not converge Lambda in  999 iterations.
 Linear search skipped for unknown reason.
 Error termination via Lnk1e in /disc30/g98/l103.exe.
 Job cpu time:  0 days  7 hours  9 minutes 17.0 seconds.
 File lengths (MBytes):  RWF=   21 Int=    0 D2E=    0 Chk=    6 Scr=    1
```

!!! info "Explanation of error"
    The rational function optimization was not successful during a linear search. Most likely the Hessian is no longer valid.

!!! tip "Fixing the error"
    Restart optimization using `Opt=CalcFC`.

## Variable Index of 3000 on Card XXX Is Out of Range, NVar=XX

**Description of error**
At the end of your output, you get lines such as

```
 Variable index of 3000 on card  15 is out of range, NVar=  42.
 Termination in UpdVr1.
 Error termination via Lnk1e in /disc30/g98/l101.exe.
 Job cpu time:  0 days  0 hours  0 minutes  0.5 seconds.
 File lengths (MBytes):  RWF=   11 Int=    0 D2E=    0 Chk=    8 Scr=    1
```

!!! info "Explanation of error"
    This is an input error. You forgot to add a variable in your Z-matrix to your list. In the above example, it is a variable which defines atom #15.

!!! tip "Fixing the error"
    Add the variable.

## Unknown Center XXX

**Description of error**
At the end of your output, you get lines such as

```
 Unknown center X
 Error termination via Lnk1e in /disc30/g98/l101.exe.
 Job cpu time:  0 days  0 hours  0 minutes  0.5 seconds.
 File lengths (MBytes):  RWF=    6 Int=    0 D2E=    0 Chk=    8 Scr=    1
```

!!! info "Explanation of error"
    This is an input error. You are trying to define an atom in a Z-matrix using another non-existent atom (in the above example, X)

!!! tip "Fixing the error"
    Fix the atom name.

## Determination of Dummy Atom Variables in Z-matrix Conversion Failed

**Description of error**
At the end of your output, you get lines such as

```
 Error termination request processed by link 9999.
 Error termination via Lnk1e in /disc30/g98/l9999.exe.
 Job cpu time:  0 days  1 hours 53 minutes 10.4 seconds.
 File lengths (MBytes):  RWF=   20 Int=    0 D2E=    0 Chk=   11 Scr=    1
```

and just before

```
 Determination of dummy atom variables in z-matrix conversion failed.
 Determination of dummy atom variables in z-matrix conversion failed.
 NNew=      6.03366976D+01 NOld=      5.07835896D+01 Diff= 9.55D+00
```

!!! info "Explanation of error"
    The conversion from redundant internal coordinates to Z-matrix coordinates failed because of the dummy atoms. You will have to make do with Cartesian coordinates.

!!! tip "Fixing the error"
    The geometry optimization converged, but Gaussian couldn't convert back to the input z-matrix.

## malloc Failed

**Description of error**
At the end of your output, you get lines such as

```
malloc failed.: Resource temporarily unavailable
malloc failed.
```

!!! info "Explanation of error"
    This is not strictly a Gaussian error. It typically means that the computer has run out of memory, perhaps because you asked for too much memory in the `%mem` line.

!!! tip "Fixing the error"
    * Reduce the amount specified with `%mem`.
    * Or, increase the amount of memory requested in the job script with `--mem=`.

## Charge and Multiplicity Card Seems Defective

**Description of error**
At the end of your output, you get lines such as

```
 ----
 -2 1
 ----
 Z-Matrix taken from the checkpoint file:
 oxalate_2-_Aq1_C2.chk
 Charge and multiplicity card seems defective:
 Charge is bogus.
  WANTED AN INTEGER AS INPUT.
  FOUND A STRING AS INPUT.
 CX      =  0.7995                                                              
                                                        
   ?
 Error termination via Lnk1e in /disc30/g98/l101.exe.
```

!!! info "Explanation of error"
    This is an input error. If the title line is forgotten when using `geom=modify`, then it interprets the charge/multiplicity line (in the above example, "-2 1") as the title, and then tries to interpret the variable list as the charge/multiplicity line.

!!! tip "Fixing the error"
    Put in a title line.

## Attempt to Redefine Unrecognized Symbol "XXXXX"

**Description of error**
At the end of your output, you get lines such as

```
 O2WXC  90. 
 Attempt to redefine unrecognized symbol "O2WXC".
 Error termination via Lnk1e in /disc30/g98/l101.exe.
 Job cpu time:  0 days  0 hours  0 minutes  0.5 seconds.
 File lengths (MBytes):  RWF=    6 Int=    0 D2E=    0 Chk=    8 Scr=    1
```

!!! info "Explanation of error"
    This is an input error. You are attempting a `geom=modify`, but a variable whose value you are attempting to replace is not in the checkpoint file.

!!! tip "Fixing the error"
    Either specify the correct checkpoint file or the correct variable.

## Inconsistency #2 in MakNEB

**Description of error**
At the end of your output, you get lines such as

```
 Standard basis: 3-21G (6D, 7F)
 Inconsistency #2 in MakNEB.
 Error termination via Lnk1e in /disc30/g98/l301.exe.
 Job cpu time:  0 days  3 hours 46 minutes 57.4 seconds.
 File lengths (MBytes):  RWF=  245 Int=    0 D2E=    0 Chk=   11 Scr=    1
```

!!! info "Explanation of error"
    This is an input error. You have had a change in point group, and you specified `iop(2/15=4,2/16=2,2/17=7)` to try to avoid program crashing.

!!! tip "Fixing the error"
    Be very careful with `iop`, or remove altogether.

## galloc: Could Not Allocate Memory

**Description of error**
In the output file, you get

```
  galloc: could not allocate memory
```

!!! info "Explanation of error"
    This is a memory allocation error due to lack of memory. Gaussian handles memory in such a way that it actually uses about 1GB more than `%mem`.

!!! tip "Fixing the error"
    The value for `%mem` should be at least 1GB less than the value specified in the job submission script. Conversely, the value specified for `--mem` in your job script should be at least 1GB greater than the amount specified in the `%mem` directive in your Gaussian input file. The exact increment needed seems to depend on the job type and input details; 1GB is a conservative value determined empirically.

## No Such File or Directory

**Description of error**
In the job output file you get something like

```
PGFIO/stdio: No such file or directory
PGFIO-F-/OPEN/unit=11/error code returned by host stdio - 2.
 File name = /home/johndoe/scratch/Gau-12345.inp
 In source file ml0.f, at line number 181
  0  0x42bb41
Error: segmentation violation, address not mapped to object
```

!!! info "Explanation of error"
    The file named in the third line doesn't exist, possibly because the containing directory does not exist. This happens, for example, if you set `GAUSS_SCRDIR` to a directory that doesn't exist.

!!! tip "Fixing the error"
    Create the directory with `mkdir`, or change the definition of `GAUSS_SCRDIR` to name an existing directory.