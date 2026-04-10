---
title: "Including source code within the wiki"
tags:
  []

keywords:
  []
---

__NOTOC__

To include source code within the wiki, we are using the extension [SyntaxHighlight_GeSHi](http://www.mediawiki.org/wiki/Extension:SyntaxHighlight_GeSHi). You can easily include a code snippet using the tag **<nowiki><syntaxhighlight> </syntaxhighlight></nowiki>**. 

== Options of the <nowiki><syntaxhighlight></nowiki> tag == 
For a complete list of options, please refer to [this page](http://www.mediawiki.org/wiki/Extension:SyntaxHighlight_GeSHi).

=== *lang* option === 
The **lang** option defines the language used for syntax highlighting. The default language, if this option is omitted, is C++. The complete list of supported languages is available  [here](http://www.mediawiki.org/wiki/Extension:SyntaxHighlight_GeSHi#Supported_languages). 

=== *line* option === 
The **line** option displays line numbers. 

== Example == 
Here is an example of a C++ code snippet created with the <nowiki><syntaxhighlight lang="cpp" line> ... </syntaxhighlight></nowiki> tag.

<syntaxhighlight lang="cpp" line>
#include <iostream>
#include <fstream>
#include <unistd.h>
#include <sstream>
using namespace std;

void flushIfBig(ofstream & out, ostringstream & oss, int size, bool force=false) {
	if (oss.tellp() >= size) {
		out << oss.str();
		oss.str(""); //reset buffer
	}
}
int main() {
	int buff_size = 50*1024*1024;

ofstream out ("file.dat");
	ostringstream oss (ostringstream::app);
	oss.precision(5);
	for (int i=0; i<100*buff_size; i++)
	{
		oss << i << endl;
		flushIfBig(out,oss,buff_size);
	}
	flushIfBig(out,oss,buff_size,true);
	out.close();
}
</syntaxhighlight>