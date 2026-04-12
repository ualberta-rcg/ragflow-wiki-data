---
title: "Fortran/fr"
slug: "fortran"
lang: "fr"

source_wiki_title: "Fortran/fr"
source_hash: "67dcd6429ee69740ba38ef7bf07638e8"
last_synced: "2026-04-10T15:28:10.183781+00:00"
last_processed: "2026-04-11T07:06:40.963023+00:00"

tags:
  []

keywords:
  - "interface"
  - "Fortran"
  - "boundInf"
  - "area"
  - "compilateurs"
  - "FunctionToIntegrate"
  - "erreur de segmentation"
  - "boundSup"
  - "function"
  - "algèbre linéaire"
  - "computeIntegral"
  - "débogage"
  - "erreurs de segmentation"

questions:
  - "Quelles sont les options de compilation recommandées pour faciliter le débogage d'un programme Fortran avec gfortran ou ifort ?"
  - "Pourquoi est-il fortement conseillé d'utiliser les fonctions intégrées ou les bibliothèques BLAS/LAPACK pour les opérations d'algèbre linéaire plutôt que de coder ses propres boucles ?"
  - "Comment peut-on résoudre les erreurs de segmentation fréquentes liées à la transmission de pointeurs ou de tableaux alloués dynamiquement dans les sous-routines ?"
  - "Quel type d'erreur le remplacement du code permet-il d'éviter lors de l'exécution du programme ?"
  - "Quelle structure Fortran spécifique est introduite dans le nouveau code pour déclarer correctement la fonction passée en argument ?"
  - "Quelle opération mathématique principale le programme cherche-t-il à accomplir à travers la fonction \"computeIntegral\" ?"
  - "What mathematical operation is the main program attempting to perform using the `computeIntegral` function?"
  - "What is the specific mathematical expression evaluated by the `FunctionToIntegrate` function?"
  - "What are the values of the lower and upper bounds defined for the integration process?"
  - "Quel type d'erreur le remplacement du code permet-il d'éviter lors de l'exécution du programme ?"
  - "Quelle structure Fortran spécifique est introduite dans le nouveau code pour déclarer correctement la fonction passée en argument ?"
  - "Quelle opération mathématique principale le programme cherche-t-il à accomplir à travers la fonction \"computeIntegral\" ?"

status:
  downloaded: true
  converted: true
  tagged: false
  keywords_generated: true
  ragflow_synced: true
  qa_generated: false
---

Fortran est un langage compilé disponible sur les ordinateurs de l'Alliance de recherche numérique du Canada où sont installés les compilateurs `gfortran` et `ifort`. En général, les langages compilés offrent une meilleure performance; nous vous encourageons donc à écrire vos programmes en Fortran, C ou C++.

## Options utiles de compilation

La plupart des compilateurs Fortran modernes offrent des options utiles pour le débogage.

*   ` -fcheck=all ` pour le compilateur gfortran et ` -check ` pour le compilateur ifort vérifient les limites des tableaux et signalent les pointeurs sans cible et les variables non initialisées;
*   ` -fpe0 ` (ifort) interrompt l'application dans des cas de virgule flottante (division par zéro ou racine carrée d'un nombre négatif) plutôt que de simplement générer NaN (*not a number*) et laisser l'application se poursuivre;
*   pendant les tests, utilisez ` -O0 ` pour désactiver les optimisations et ` -g ` pour ajouter les symboles de débogage.

## Algèbre linéaire numérique

À partir de Fortran 90, de nouvelles fonctions sont disponibles pour le traitement des opérations de base : `matmul` et `dot_product` pour les multiplications avec matrices et vecteurs; `transpose` pour la transposition de matrices. Utilisez toujours ces fonctions ou les bibliothèques BLAS/LAPACK fournies et n'essayez jamais de créer vos propres méthodes, à moins que ce ne soit pour des motifs d'apprentissage. La routine BLAS pour la multiplication de matrices peut s'avérer 100 fois plus rapide que l'algorithme primaire avec trois boucles imbriquées.

## Erreurs de segmentation

Une erreur fréquemment observée avec un exécutable Fortran provient de problèmes d'interface. Ces problèmes surviennent lorsque l'on transmet comme argument d'une sous-routine un pointeur, un tableau alloué dynamiquement ou encore un pointeur de fonctions. À la compilation il n'y a pas de problème, cependant à l'exécution vous obtiendrez par exemple le message suivant :

!!! warning "Erreur de segmentation"
    **forrtl: severe (174): SIGSEGV, segmentation fault occurred**

Pour corriger le problème, il faut s'assurer que l'interface de la sous-routine est définie explicitement. Ceci peut se faire en Fortran avec la commande `INTERFACE`. Ainsi, le compilateur arrivera à construire l'interface et les erreurs de segmentation seront réglées.

Dans le cas où l'argument est un tableau allouable, il s'agit de remplacer le code suivant :

```fortran title="error_allocate.f90"
Program Eigenvalue
implicit none

integer                       :: ierr
integer                       :: ntot
real, dimension(:,:), pointer :: matrix

read(5,*) ntot
ierr = genmat( ntot, matrix )

call Compute_Eigenvalue( ntot, matrix )

deallocate( matrix )
end
```

par le code :

```fortran title="interface_allocate.f90"
Program Eigenvalue
implicit none

integer                       :: ierr
integer                       :: ntot
real, dimension(:,:), pointer :: matrix

interface
    function genmat( ntot, matrix )
    implicit none
    integer                       :: genmat
    integer, intent(in)           :: ntot
    real, dimension(:,:), pointer :: matrix
    end function genmat
end interface

read(5,*) ntot
ierr = genmat( ntot, matrix )

call Compute_Eigenvalue( ntot, matrix )

deallocate( matrix )
end
```

Le principe est le même dans le cas où l'argument est un pointeur de fonction. Considérons, par exemple, le code suivant :

```fortran title="error_pointer.f90"
Program AreaUnderTheCurve
implicit none

real,parameter :: boundInf = 0.
real,parameter :: boundSup = 1.
real           :: area
real, external :: computeIntegral
real, external :: FunctionToIntegrate

area = computeIntegral( FunctionToIntegrate, boundInf, boundSup )

end

function FunctionToIntegrate( x )
implicit none

real             :: FunctionToIntegrate
real, intent(in) :: x

FunctionToIntegrate = x

end function FunctionToIntegrate

function computeIntegral( func, boundInf, boundSup )
implicit none

real, external   :: func
real, intent(in) :: boundInf, boundSup

...
```

Pour ne pas obtenir d'erreur de segmentation, il faut remplacer le code précédent par ce qui suit :

```fortran title="interface_pointer.f90"
Program Eigenvalue
implicit none

real,parameter :: boundInf = 0.
real,parameter :: boundSup = 1.
real           :: area
real, external :: computeIntegral

interface
    function FunctionToIntegrate( x )
    implicit none
    real             :: FunctionToIntegrate
    real, intent(in) :: x
    end function FunctionToIntegrate
end interface

area = computeIntegral( FunctionToIntegrate, boundInf, boundSup )

end


function FunctionToIntegrate( x )
implicit none

real             :: FunctionToIntegrate
real, intent(in) :: x

FunctionToIntegrate = x

end function FunctionToIntegrate


function computeIntegral( func, boundInf, boundSup )
implicit none

real, intent(in) :: boundInf, boundSup

interface
    function func( x )
    implicit none
    real             :: func
    real, intent(in) :: x
    end function func
end interface

...