---
title: "GDB"
slug: "gdb"
lang: "base"

source_wiki_title: "GDB"
source_hash: "97bfbfe42c7b070f0edc6f8f34c6fb3d"
last_synced: "2026-04-10T15:28:10.183781+00:00"
last_processed: "2026-04-11T07:18:34.378133+00:00"

tags:
  []

keywords:
  - "debugger"
  - "breakpoints"
  - "profiling"
  - "debugging"
  - "backtrace"
  - "debugging symbols"
  - "commands"
  - "core file"
  - "running process"
  - "debug"
  - "GDB"
  - "variables"
  - "Core dump"
  - "program.cpp"
  - "debuginfo-install"
  - "STL structures"
  - "segmentation fault"
  - "Segmentation fault"
  - "signal 11"
  - "call stack"
  - "program state"

questions:
  - "What is GDB and what types of software problems is it primarily used to resolve?"
  - "Why is it necessary to compile a program with the `-g` option when preparing to debug it with GDB?"
  - "How can a developer generate and use a `core` file to investigate a segmentation fault after a program has already crashed?"
  - "How do you find the process ID and attach the GDB debugger to a program that is already running?"
  - "What information does the `backtrace` or `bt` command provide during a debugging session?"
  - "What advanced interactive commands can be used to analyze a program's state once its execution is interrupted?"
  - "What signal and specific error caused the program to terminate?"
  - "Which line of code and file triggered the segmentation fault?"
  - "What missing debug information packages does the system recommend installing?"
  - "What are the different ways you can set breakpoints to stop the execution of a program?"
  - "How can you analyze the state of the program once its execution has been interrupted?"
  - "Where can a user find a comprehensive list of the main debugging commands mentioned in the text?"
  - "What are the primary GDB commands, their shortcuts, and their specific functions during debugging?"
  - "How can you configure GDB to properly display C++ STL structures using a configuration file?"
  - "What external websites and tutorials are provided as additional resources for learning GDB?"
  - "What are the primary GDB commands, their shortcuts, and their specific functions during debugging?"
  - "How can you configure GDB to properly display C++ STL structures using a configuration file?"
  - "What external websites and tutorials are provided as additional resources for learning GDB?"

status:
  downloaded: true
  converted: true
  tagged: false
  keywords_generated: true
  ragflow_synced: true
  qa_generated: false
---

# GDB

[GDB](https://www.gnu.org/software/gdb/) is a debugger used to investigate software problems.
GDB is an acronym for *GDB: The GNU Project Debugger*

## Description

With a debugger, it is possible to quickly find the cause of a problem in a piece of software.
Often it is used to resolve [segmentation faults](https://en.wikipedia.org/wiki/Segmentation_fault).
If you wish to resolve a problem relating to memory (for example, a [memory leak](https://en.wikipedia.org/wiki/Memory_leak)), we recommend using [Valgrind](debugging_and_profiling.md#valgrind).

## Use cases

### Finding a bug with the debugger

In this section, the following program is used:
```cpp title="program.cpp"
#include <iostream>
#include <vector>
using namespace std;

int main(int argc, char**argv) {
	
	vector<int> numbers;

	int iterator = 1000;

	while(iterator --) {
		numbers.push_back(iterator);
	}

	cout << numbers[1000000] << endl;

	return 0;
}
```
This program generates a segmentation fault when it is run.
```bash
g++ -g program.cpp  -o program
./program
Segmentation fault (core dumped)
```

!!! note
    We compile using the option `-g` to include debugging symbols within the binary, which allows the debugger to provide more information about the bug.

We may then run the program inside the debugger:
```bash
gdb ./program
(gdb) run
Starting program: /home/seb/program ./program

Program received signal SIGSEGV, Segmentation fault.
0x0000000000400c17 in main (argc=2, argv=0x7fffffffda88) at program.cpp:15
15		cout << numbers[1000000] << endl;
Missing separate debuginfos, use: debuginfo-install glibc-2.16-31.fc18.x86_64 libgcc-4.7.2-8.fc18.x86_64 libstdc++-4.7.2-8.fc18.x86_64

(gdb) bt
#0  0x0000000000400c17 in main (argc=2, argv=0x7fffffffda88) at program.cpp:15
```
So, the above error is caused by line 15. The code tries to use index 1000000, but the array only contains 1000 elements.

### Finding the cause of a segmentation fault using a `core` file

In this example, we use the same program as in the previous section. We however do so without using the debugger directly. This is useful for a bug that happens a long time after the program has started.

To find the cause for this error, a `core` file must be generated. To do this, you must enable the creation of such files.
```bash
ulimit -c unlimited
```

Executing the same program again, a `core` file is written.
```bash
./program
Segmentation fault (core dumped)
file core.18158
core.18158: ELF 64-bit LSB core file x86-64, version 1 (SYSV), SVR4-style, from './program'
```

Using the `program` binary executable and the `core` file, it is possible to trace its execution up to the error.
```bash
gdb -q ./program 
Reading symbols from /home/seb/program...done.

(gdb) core-file core.18246
[New LWP 18246]
Core was generated by './program'.
Program terminated with signal 11, Segmentation fault.
#0  0x0000000000400c17 in main (argc=1, argv=0x7fff2315c848) at
program.cpp:15
15              cout << numbers[1000000] << endl;
Missing separate debuginfos, use: debuginfo-install
glibc-2.16-31.fc18.x86_64 libgcc-4.7.2-8.fc18.x86_64
libstdc++-4.7.2-8.fc18.x86_64

(gdb) bt
#0  0x0000000000400c17 in main (argc=1, argv=0x7fff2315c848) at
program.cpp:15
```
We here get the same result as if we had run it inside the debugger.

### Attaching the debugger to a running process

It is possible to debug a process that is already running, for example a job running on one of the compute nodes. To do so, we first need the process ID.

```bash
ps aux | grep firefox | grep -v grep
seb      12691  6.4  7.5 1539672 282656 ?      Sl   08:53   6:48 /usr/lib64/firefox/firefox http://www.google.ca/
```

After that, it is possible to attach the debugger directly.
```bash
gdb attach 12691
```

After having done this, a lot of information is displayed.

There are many commands available within GDB. One of the most useful is `backtrace`, or `bt`.
This command shows the current call stack.
```bash
(gdb) bt
#0  0x00000033646e99ad in poll () from /lib64/libc.so.6
#1  0x0000003db86849f3 in PollWrapper(_GPollFD*, unsigned int, int) () from /usr/lib64/firefox/xulrunner/libxul.so
#2  0x0000003366e47d24 in g_main_context_iterate.isra.24 () from /lib64/libglib-2.0.so.0
#3  0x0000003366e47e44 in g_main_context_iteration () from /lib64/libglib-2.0.so.0
#4  0x0000003db86849a2 in nsAppShell::ProcessNextNativeEvent(bool) () from /usr/lib64/firefox/xulrunner/libxul.so
#5  0x0000003db869a7d1 in nsBaseAppShell::DoProcessNextNativeEvent(bool, unsigned int) () from /usr/lib64/firefox/xulrunner/libxul.so
#6  0x0000003db869a8ea in nsBaseAppShell::OnProcessNextEvent(nsIThreadInternal*, bool, unsigned int) () from /usr/lib64/firefox/xulrunner/libxul.so
#7  0x0000003db89810c2 in nsThread::ProcessNextEvent(bool, bool*) () from /usr/lib64/firefox/xulrunner/libxul.so
#8  0x0000003db89563eb in NS_ProcessNextEvent(nsIThread*, bool) () from /usr/lib64/firefox/xulrunner/libxul.so
#9  0x0000003db873056f in mozilla::ipc::MessagePump::Run(base::MessagePump::Delegate*) () from /usr/lib64/firefox/xulrunner/libxul.so
#10 0x0000003db89a4ab7 in MessageLoop::Run() () from /usr/lib64/firefox/xulrunner/libxul.so
#11 0x0000003db869a1b3 in nsBaseAppShell::Run() () from /usr/lib64/firefox/xulrunner/libxul.so
#12 0x0000003db857d92d in nsAppStartup::Run() () from /usr/lib64/firefox/xulrunner/libxul.so
#13 0x0000003db7d18f4a in XREMain::XRE_mainRun() () from /usr/lib64/firefox/xulrunner/libxul.so
#14 0x0000003db7d1b007 in XREMain::XRE_main(int, char**, nsXREAppData const*) () from /usr/lib64/firefox/xulrunner/libxul.so
#15 0x0000003db7d1b259 in XRE_main () from /usr/lib64/firefox/xulrunner/libxul.so
#16 0x0000000000402c23 in do_main(int, char**, nsIFile*) ()
#17 0x0000000000402403 in main ()

(gdb) quit
A debugging session is active.

Inferior 1 [process 12691] will be detached.

Quit anyway? (y or n) y
Detaching from program: /usr/lib64/firefox/firefox, process 12691
```

## Advanced usage

In the previous sections, we used the `run` and `backtrace` commands. Many more commands are available to debug in an interactive way, by stopping the program. For example, you can set breakpoints on functions or lines of code, or whenever a given variable is modified. When execution is interrupted, you can analyse the state of the program by printing the value of variables. The following table contains a list of the main commands.

**Main GDB commands**

| Command           | Shortcut | Argument                      | Description                                                  |
| :---------------- | :------- | :---------------------------- | :----------------------------------------------------------- |
| run/kill          | r/k      | -                             | begin/stop execution                                         |
| where / backtrace | bt       | -                             | displays the backtrace                                       |
| break             | b        | src.c:line_number or function | sets a breakpoint at the given line of code or function      |
| watch             | -        | variable name                 | interrupts the program when a variable is modified           |
| continue          | c        | -                             | resume the program                                           |
| step              | s        | -                             | execute the next operation                                   |
| print             | p        | variable name                 | displays the content of a variable                           |
| list              | l        | src.c:number                  | displays the given line of code                              |

### Displaying STL structures

By default, GDB does not display C++ STL structures very well. Many solutions are given [here](https://sourceware.org/gdb/wiki/STLSupport). The simplest solution is probably [this one](http://www.yolinux.com/TUTORIALS/GDB-Commands.html#STLDEREF), which is to copy [this file](http://www.yolinux.com/TUTORIALS/src/dbinit_stl_views-1.03.txt) into your home folder, with the name `~/.gdbinit`.

## Other resources

*   [GDB website](http://www.sourceware.org/gdb/)
*   [GDB tutorial](http://oucsace.cs.ohiou.edu/~bhumphre/gdb.html)
*   [Talk from the TACC on debugging and profiling](http://goo.gl/rLPvR0)