---
title: "Including source code within the wiki/en"
slug: "including_source_code_within_the_wiki"
lang: "en"

source_wiki_title: "Including source code within the wiki/en"
source_hash: "28238a0ca137c3de981df79e35ef5f79"
last_synced: "2026-04-10T15:28:10.183781+00:00"
last_processed: "2026-04-11T08:01:05.258476+00:00"

tags:
  []

keywords:
  - "source code"
  - "line option"
  - "syntaxhighlight tag"
  - "lang option"
  - "SyntaxHighlight_GeSHi"

questions:
  - "What extension and specific tag are required to include syntax-highlighted source code within the wiki?"
  - "How does the \"lang\" option work, and what is the default programming language if this option is not specified?"
  - "What is the purpose of including the \"line\" option within the syntax highlight tag?"
  - "What extension and specific tag are required to include syntax-highlighted source code within the wiki?"
  - "How does the \"lang\" option work, and what is the default programming language if this option is not specified?"
  - "What is the purpose of including the \"line\" option within the syntax highlight tag?"

status:
  downloaded: true
  converted: true
  tagged: false
  keywords_generated: true
  ragflow_synced: true
  qa_generated: false
---

To include source code within the wiki, we are using the extension [SyntaxHighlight_GeSHi](http://www.mediawiki.org/wiki/Extension:SyntaxHighlight_GeSHi). You can easily include a code snippet using the tag **`<syntaxhighlight> </syntaxhighlight>`**.

## Options of the `<syntaxhighlight>` tag
For a complete list of options, please refer to [this page](http://www.mediawiki.org/wiki/Extension:SyntaxHighlight_GeSHi).

### *lang* option
The **lang** option defines the language used for syntax highlighting. The default language, if this option is omitted, is C++. The complete list of supported languages is available [here](http://www.mediawiki.org/wiki/Extension:SyntaxHighlight_GeSHi#Supported_languages).

### *line* option
The **line** option displays line numbers.

## Example
Here is an example of a C++ code snippet created with the `<syntaxhighlight lang="cpp" line> ... </syntaxhighlight>` tag.

```cpp
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