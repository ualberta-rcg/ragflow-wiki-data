---
title: "GCC C++ Dual ABI/fr"
slug: "gcc_c___dual_abi"
lang: "fr"

source_wiki_title: "GCC C++ Dual ABI/fr"
source_hash: "19dce9bcde9eb5510654d76819fb33fe"
last_synced: "2026-04-10T15:28:10.183781+00:00"
last_processed: "2026-04-11T07:17:00.119346+00:00"

tags:
  []

keywords:
  - "noms de symboles"
  - "édition des liens"
  - "std=c++11"
  - "-std=c++98"
  - "C++ ABIs"
  - "_GLIBCXX_USE_CXX11_ABI"
  - "diff"
  - "nm"
  - "ABI C++"
  - "symbols"
  - "-std=c++11"
  - "main.cxx"
  - "ABI"
  - "Interface binaire-programme (ABI)"
  - "std=c++98"
  - "basic_string"
  - "GCC"
  - "code C++"
  - "Makefile"

questions:
  - "Quel problème majeur peut survenir lors de l'édition des liens si l'on utilise des versions de GCC différentes (notamment entre 4.9 et 5.1) pour compiler un projet et ses bibliothèques externes ?"
  - "Quelle option de compilation permet d'utiliser la fonction \"Dual ABI\" pour forcer la compatibilité avec l'ancienne interface binaire-programme ?"
  - "Quel est le rôle de l'interface binaire-programme (ABI) dans la génération et l'exportation des noms de symboles par les compilateurs C++ ?"
  - "Quelle version minimale de GCC doit être chargée avant d'exécuter la commande make pour cet exemple ?"
  - "Quelles options de compilation spécifiques sont utilisées pour forcer l'utilisation de l'ancienne ou de la nouvelle ABI C++ ?"
  - "Quels outils en ligne de commande le Makefile utilise-t-il pour extraire et comparer les symboles générés par les différentes ABI ?"
  - "What is the purpose of the `_GLIBCXX_USE_CXX11_ABI` macro used in the compilation commands?"
  - "How do the different C++ standards (`-std=c++98` versus `-std=c++11`) affect the generated object files in this Makefile?"
  - "What specific information is being extracted and saved to the `.symbols` files using the `nm` and `cut` commands?"
  - "What are the primary differences between the old and new C++ ABIs when compiling with the -std=c++11 flag?"
  - "How does the C++11 ABI change affect the mangling of standard library symbols like `std::string`?"
  - "What specific symbol changes are highlighted by the `diff` command comparing the old and new ABI object files?"
  - "Quel est le rôle de la macro `_GLIBCXX_USE_CXX11_ABI` lors de la compilation d'un code C++ ?"
  - "Quel est l'impact de l'utilisation exclusive des options `-std=c++98` ou `-std=c++11` sur le choix de l'ABI par le compilateur ?"
  - "Comment doit-on procéder pour lier du nouveau code C++ avec des binaires qui ont été compilés en utilisant une ancienne ABI ?"
  - "Quel est le rôle de la macro `_GLIBCXX_USE_CXX11_ABI` lors de la compilation d'un code C++ ?"
  - "Quel est l'impact de l'utilisation exclusive des options `-std=c++98` ou `-std=c++11` sur le choix de l'ABI par le compilateur ?"
  - "Comment doit-on procéder pour lier du nouveau code C++ avec des binaires qui ont été compilés en utilisant une ancienne ABI ?"

status:
  downloaded: true
  converted: true
  tagged: false
  keywords_generated: true
  ragflow_synced: true
  qa_generated: false
---

Une modification importante a été introduite à l'interface binaire-programme (ABI) entre les versions 4.9 et 5.1 de GCC. Aucun problème ne survient si tout le code source, incluant les bibliothèques dépendantes, est compilé avec la même version du compilateur. Par contre, l'utilisation de versions différentes peut empêcher l'édition des liens de se faire correctement en raison de cette modification, surtout si les liens se font vers des bibliothèques précompilées offertes par les produits de fournisseurs externes. Dans un tel cas, utilisez la fonctionnalité *Dual ABI* pour que l'édition des liens s'effectue correctement avec l'ancienne interface ABI [Free Software Foundation. The GNU C++ Library, Chapter 3.](https://gcc.gnu.org/onlinedocs/libstdc++/manual/using_dual_abi.html). Il faudrait donc par exemple passer `-D_GLIBCXX_USE_CXX11_ABI=0` à GCC si vous utilisez une version supérieure à 5.1.

!!! note
    Dans certains cas, `-D_GLIBCXX_USE_CXX11_ABI=0` résout des erreurs comme
    `.../extensions.hpp(38): error: "std::list" is ambiguous`
    La classe n'est pas nécessairement `std::list`.

## Interface binaire-programme (ABI)

Par défaut, les compilateurs utilisent chacun un algorithme particulier pour composer des noms uniques et exporter les noms de symboles `extern "C++"`. Ces noms de symboles constituent une partie de l'ABI utilisée pour lier le code compilé avec les bibliothèques. Si plusieurs fournisseurs essaient de toujours utiliser la même ABI sur une plateforme (par exemple Linux), certaines modifications s'imposent à l'occasion. Pour cela, toute modification à l'ABI d'un compilateur peut empêcher l'édition des liens de se faire.

## Exemple

Dans cet exemple, nous voyons l'effet des options passées à GCC (>=v5.1) sur l'ABI utilisée par les binaires générés. Pour que l'édition des liens s'effectue correctement pour le programme ou la bibliothèque, tous les noms de symboles doivent concorder, autrement l'édition échouera. Ici, les noms de symboles générés par le compilateur diffèrent selon la configuration du compilateur.

### Code source

Le programme C++ suivant sera compilé pour générer les noms de symboles ABI qu'il contient.

```c++ title="main.cxx"
#include <iostream>
#include <string>

int main()
{
  using namespace std;
  string mystring = "Hello World!";
  cout << mystring << endl;
}
```

Ce programme devra être compilé avec certains paramètres différents pour montrer la différence des appels à l'ABI, comme suit :

```makefile title="Makefile"
all: \
        main-cxx98.o main-cxx98-newabi.o main-cxx98-oldabi.o \
        main-cxx11.o main-cxx11-newabi.o main-cxx11-oldabi.o \
        diff-cxx98 diff-cxx11 diff-cxx-default

clean:
        rm -f *.o *.ii *.s
        rm -f *.symbols

main-cxx98.o: main.cxx
        $(CXX) -c -o $@ -std=c++98 $<
        nm $@ | cut -c 20- >$@.symbols

main-cxx98-newabi.o: main.cxx
        $(CXX) -c -o $@ -std=c++98 -D_GLIBCXX_USE_CXX11_ABI=1 $<
        nm $@ | cut -c 20- >$@.symbols

main-cxx98-oldabi.o: main.cxx
        $(CXX) -c -o $@ -std=c++98 -D_GLIBCXX_USE_CXX11_ABI=0 $<
        nm $@ | cut -c 20- >$@.symbols

main-cxx11.o: main.cxx
        $(CXX) -c -o $@ -std=c++11 $<
        nm $@ | cut -c 20- >$@.symbols

main-cxx11-newabi.o: main.cxx
        $(CXX) -c -o $@ -std=c++11 -D_GLIBCXX_USE_CXX11_ABI=1 $<
        nm $@ | cut -c 20- >$@.symbols

main-cxx11-oldabi.o: main.cxx
        $(CXX) -c -o $@ -std=c++11 -D_GLIBCXX_USE_CXX11_ABI=0 $<
        nm $@ | cut -c 20- >$@.symbols

diff-cxx98: main-cxx98-newabi.o main-cxx98-oldabi.o
        @echo "=============================================================================="
        @echo "Différence entre les anciennes et nouvelles ABIs C++ avec -std=c++98..."
        diff --suppress-common-lines main-cxx98-oldabi.o.symbols main-cxx98-newabi.o.symbols || true

diff-cxx11: main-cxx11-newabi.o main-cxx11-oldabi.o
        @echo "=============================================================================="
        @echo "Différence entre les anciennes et nouvelles ABIs C++ avec -std=c++11..."
        diff --suppress-common-lines main-cxx11-oldabi.o.symbols main-cxx11-newabi.o.symbols || true

diff-cxx-default: main-cxx98.o main-cxx11.o
        @echo "=============================================================================="
        @echo "Différence entre les ABIs -std=c++98 et -std=c++11 sans _GLIBCXX_USE_CXX11_ABI..."
        diff --suppress-common-lines main-cxx98.o.symbols main-cxx11.o.symbols || true
```

!!! note "Remarque"
    Avant d'exécuter `make`, assurez-vous d'avoir chargé un module GCC 5.1 ou plus.

### Exécution de l'exemple

Voici le résultat de l'exécution de `make` sur le même `Makefile`, avec des options de compilation différentes.

```bash title="Exécution du Makefile"
$ make
c++ -c -o main-cxx98.o -std=c++98  main.cxx
nm main-cxx98.o | cut -c 20- >main-cxx98.o.symbols
c++ -c -o main-cxx98-newabi.o -std=c++98 -D_GLIBCXX_USE_CXX11_ABI=1  main.cxx
nm main-cxx98-newabi.o | cut -c 20- >main-cxx98-newabi.o.symbols
c++ -c -o main-cxx98-oldabi.o -std=c++98 -D_GLIBCXX_USE_CXX11_ABI=0  main.cxx
nm main-cxx98-oldabi.o | cut -c 20- >main-cxx98-oldabi.o.symbols
c++ -c -o main-cxx11.o -std=c++11  main.cxx
nm main-cxx11.o | cut -c 20- >main-cxx11.o.symbols
c++ -c -o main-cxx11-newabi.o -std=c++11 -D_GLIBCXX_USE_CXX11_ABI=1  main.cxx
nm main-cxx11-newabi.o | cut -c 20- >main-cxx11-newabi.o.symbols
c++ -c -o main-cxx11-oldabi.o -std=c++11 -D_GLIBCXX_USE_CXX11_ABI=0  main.cxx
nm main-cxx11-oldabi.o | cut -c 20- >main-cxx11-oldabi.o.symbols
==============================================================================
Différence entre les anciennes et nouvelles ABIs C++ avec -std=c++98...
diff --suppress-common-lines main-cxx98-oldabi.o.symbols main-cxx98-newabi.o.symbols || true
7,8c7,8
< _ZNSsC1EPKcRKSaIcE
< _ZNSsD1Ev
---
> _ZNSt7__cxx1112basic_stringIcSt11char_traitsIcESaIcEEC1EPKcRKS3_
> _ZNSt7__cxx1112basic_stringIcSt11char_traitsIcESaIcEED1Ev
14c14
< _ZStlsIcSt11char_traitsIcESaIcEERSt13basic_ostreamIT_T0_ES7_RKSbIS4_S5_T1_E
---
> _ZStlsIcSt11char_traitsIcESaIcEERSt13basic_ostreamIT_T0_ES7_RKNSt7__cxx1112basic_stringIS4_S5_T1_EE
==============================================================================
Différence entre les anciennes et nouvelles ABIs C++ avec -std=c++11...
diff --suppress-common-lines main-cxx11-oldabi.o.symbols main-cxx11-newabi.o.symbols || true
7,8c7,8
< _ZNSsC1EPKcRKSaIcE
< _ZNSsD1Ev
---
> _ZNSt7__cxx1112basic_stringIcSt11char_traitsIcESaIcEEC1EPKcRKS3_
> _ZNSt7__cxx1112basic_stringIcSt11char_traitsIcESaIcEED1Ev
15c15
< _ZStlsIcSt11char_traitsIcESaIcEERSt13basic_ostreamIT_T0_ES7_RKSbIS4_S5_T1_E
---
> _ZStlsIcSt11char_traitsIcESaIcEERSt13basic_ostreamIT_T0_ES7_RKNSt7__cxx1112basic_stringIS4_S5_T1_EE
==============================================================================
Différence entre les ABIs -std=c++98 et -std=c++11 sans _GLIBCXX_USE_CXX11_ABI...
diff --suppress-common-lines main-cxx98.o.symbols main-cxx11.o.symbols || true
12a13
> _ZStL19piecewise_construct
$
```

soit,

*   dans le dernier cas, en utilisant seulement `-std=c++98` ou `-std=c++11`, l'ABI ne diffère pas; le compilateur utilisera l'ABI par défaut (la plus récente);
*   dans les deux cas précédents, `_GLIBCXX_USE_CXX11_ABI` a la valeur `0` (*ancienne ABI*) ou `1` (*nouvelle ABI*) avec `-std=c++98` ou `-std=c++11`; ceci fait en sorte que l'ancienne ou la nouvelle ABI est utilisée.

Ainsi, pour lier avec des binaires compilés avec une ancienne ABI, il faut spécifier `-D_GLIBCXX_USE_CXX11_ABI=0` pour compiler du code C++.

## Références