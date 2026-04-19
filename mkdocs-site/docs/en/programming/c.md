---
title: "C/en"
slug: "c"
lang: "en"

source_wiki_title: "C/en"
source_hash: "46d8b54c83430b1e8da81990ec6837c7"
last_synced: "2026-04-18T23:39:30.217451+00:00"
last_processed: "2026-04-19T00:45:17.164494+00:00"

tags:
  []

keywords:
  - "C programming language"
  - "ISO standards"
  - "concurrency"
  - "compiler optimizations"
  - "volatile keyword"

questions:
  - "How did the introduction of the C11 standard change the way concurrency and memory models are handled in C?"
  - "Why is it a mistake to use the volatile keyword in C the same way it is used in Java?"
  - "What precautions should developers take regarding optimization flags when using GCC and Intel compilers?"

status:
  downloaded: true
  converted: true
  tagged: false
  keywords_generated: true
  ragflow_synced: true
  qa_generated: false
---

# C

C is a general-purpose, high-level, imperative programming language created by Dennis Ritchie between 1969 and 1973 at Bell Labs. C is now represented as a number of ISO standards corresponding to the years 1989/1990, 1999, and 2011 and are usually referred to as C90 (or C89), C99, and C11. If you are new to C or wish to read an overview of the language and/or how each ISO standard impacted it, check out the following Wikipedia links:

1.  [C](https://en.wikipedia.org/wiki/C_(programming_language)), i.e., the language, history, C90.
2.  [C99](https://en.wikipedia.org/wiki/C99): Adds language and Standard Library features. `int` is no longer implicitly assumed.
3.  [C11](https://en.wikipedia.org/wiki/C11_(C_standard_revision)): Major release adding memory model and concurrency (e.g., threads, atomics, compare-and-swap) support.

Should you have a need to refer to the actual ISO standard document for C, you can obtain a link to the last draft (which may well have errors in it!) before each ISO C standard release in the aforementioned Wikipedia pages' reference sections. (If you need the official document, you may purchase it from [Standards Council of Canada](http://www.scc.ca/).)

## Well-Defined Concurrency and Memory Models

!!! important
    Prior to 2011 the ISO C standard had no definitions of concurrency and memory models. Thus, in pre-C11 compiled code there are no guarantees concerning the ordering of memory reads and writes under concurrency, i.e., such is likely undefined behaviour which the compiler vendor may or may not have documented. It is therefore preferable to compile concurrent C code as C11 code (or newer).

## Pitfalls
### The `volatile` Keyword

!!! warning "Understanding `volatile` in C"
    The reader should note that `volatile` in C and C++ has a very specific meaning, e.g., see [this page](http://en.cppreference.com/w/cpp/language/cv). Actually needing to use `volatile` in C/C++ code is a rare event and it is typically limited to certain kinds of low-level code.

    Misuse of `volatile` might arise because the Java programming language uses the `volatile` keyword as well. Java's `volatile` has a totally different meaning from C's `volatile`. Specifically, Java's `volatile` keyword in C corresponds to using `atomic_*` (i.e., where '*' corresponds to a fundamental type name such as `int`).

### Compilers
#### GCC

!!! warning "GCC Optimization Flags"
    The GCC compiler's `-O3` option includes possibly unsafe optimizations for some types of code (e.g., code relying on aliasing). If unsure, compile and optimize code using the `-O2` option instead. If you've more time, read the man page (e.g., `man gcc`) and unset the appropriate options by searching for "-O3" to see which options are turned on and turn off the settings that are not safe.

#### Intel

!!! warning "Intel Compiler Floating-Point Optimizations"
    Intel C/C++ compilers may default to using possibly unsafe optimizations for floating-point operations. Users using the Intel compilers should read the Intel man pages (e.g., `man icc`) and are recommended to use one of two options, `-fp-model precise` or `-fp-model source`, for ANSI/ISO/IEEE standards-compliant floating-point support. For more details, read this Intel slideshow called, [Floating-point control in the Intel compiler and libraries](https://software.intel.com/sites/default/files/article/326703/fp-control-2012-08.pdf).