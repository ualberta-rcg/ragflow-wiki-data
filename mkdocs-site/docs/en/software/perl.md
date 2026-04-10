---
title: "Perl/en"
tags:
  - software

keywords:
  []
---

## Description 
[Perl](http://www.perl.org) is a free programming language which is interpreted and has acquired a vast library of contributed packages over the 25+ years of its existence. Its strengths are manipulating strings, database access and its portability ([according to this article](http://www.cio.com/article/175450/You_Used_Perl_to_Write_WHAT_)). Its weaknesses are its poor performance and the ease with which one can write obscure and illegible code. By design, Perl offers several different ways of accomplishing the same task. Many programmers have adopted this language and write code that is very compact but difficult to decipher. 

## Loading the Interpreter 
The Perl language is made available on Compute Canada's servers using a module which you can load like any other, e.g. 

```bash
module spider perl
```

to see which versions are installed and then 

```bash
module load perl/5.36.1
```

to load a particular version.

## Installing Packages 
A large number of Perl packages can be installed by means of the [Comprehensive Perl Archive Network](http://www.cpan.org/), by using the tool <tt>cpan</tt>, which however must first be initialized correctly in order to install them in your home directory. 

### Initial Configuration for Package Installation 
During the first execution of the command <tt>cpan</tt> the utility will ask you if you want to allow it to configure the majority of settings automatically. Respond <tt>yes</tt>. 

The <tt>cpan</tt> utility will offer to append a variety of environment variable settings to your .bashrc file, which you should agree to. You can then type the command <tt>quit</tt> at the interface to exit the <tt>cpan</tt> software. Before installing any Perl modules you will need to restart your shell for these new settings to take effect.

### Package Installation 
When the initial configuration is done, you can install any of the more than 25,000 packages available on CPAN. For example: