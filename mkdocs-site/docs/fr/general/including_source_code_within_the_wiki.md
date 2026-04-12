---
title: "Including source code within the wiki/fr"
slug: "including_source_code_within_the_wiki"
lang: "fr"

source_wiki_title: "Including source code within the wiki/fr"
source_hash: "baf5cf042ba3f3661f4527b93b1bc767"
last_synced: "2026-04-10T15:28:10.183781+00:00"
last_processed: "2026-04-11T08:01:18.355630+00:00"

tags:
  []

keywords:
  - "option lang"
  - "balise syntaxhighlight"
  - "code source"
  - "option line"
  - "SyntaxHighlight_GeSHi"

questions:
  - "Quelle extension et quelle balise sont utilisées pour inclure du code source dans le wiki ?"
  - "À quoi sert l'option \"lang\" et quel est le langage appliqué par défaut si elle est omise ?"
  - "Quelle option permet d'afficher les numéros de ligne à côté de l'extrait de code ?"
  - "Quelle extension et quelle balise sont utilisées pour inclure du code source dans le wiki ?"
  - "À quoi sert l'option \"lang\" et quel est le langage appliqué par défaut si elle est omise ?"
  - "Quelle option permet d'afficher les numéros de ligne à côté de l'extrait de code ?"

status:
  downloaded: true
  converted: true
  tagged: false
  keywords_generated: true
  ragflow_synced: true
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

```cpp linenums
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