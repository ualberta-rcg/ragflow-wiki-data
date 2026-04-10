---
title: "Including source code within the wiki/fr"
slug: "including_source_code_within_the_wiki"
lang: "fr"

source_wiki_title: "Including source code within the wiki/fr"
source_hash: "baf5cf042ba3f3661f4527b93b1bc767"
last_synced: "2026-04-09T20:02:20.019957+00:00"
last_processed: "2026-04-10T07:22:05.671571+00:00"

tags:
  []

keywords:
  []

status:
  downloaded: true
  converted: true
  tagged: false
  keywords_generated: false
  ragflow_synced: false
  qa_generated: false
---

Pour inclure du code source dans le wiki, nous utilisons l'extension [SyntaxHighlight_GeSHi](http://www.mediawiki.org/wiki/Extension:SyntaxHighlight_GeSHi). Vous pouvez facilement inclure un extrait de code source grâce à la balise **`<syntaxhighlight> </syntaxhighlight>`**.

## Options de la balise `<syntaxhighlight>`
Pour la liste des options, veuillez vous référer à [cette page](http://www.mediawiki.org/wiki/Extension:SyntaxHighlight_GeSHi).

### Option *lang*
L'option **lang** permet de définir le langage utilisé pour la détection de la syntaxe. Le langage par défaut, si ce paramètre est omis, est le C++. La liste des langages supportés est disponible [ici](http://www.mediawiki.org/wiki/Extension:SyntaxHighlight_GeSHi#Supported_languages).

### Option *line*
L'option **line** permet d'afficher des numéros de ligne.

## Exemple
Voici un exemple de code C++ créé avec la balise `<syntaxhighlight lang="cpp" line> ... </syntaxhighlight>`.

```cpp linenums="true"
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