---
title: "Java/fr"
slug: "java"
lang: "fr"

source_wiki_title: "Java/fr"
source_hash: "a29d24fb3997577e914abf7073b6b48f"
last_synced: "2026-04-09T20:02:20.019957+00:00"
last_processed: "2026-04-10T07:30:41.863396+00:00"

tags:
  - software

keywords:
  []

status:
  downloaded: true
  converted: true
  tagged: true
  keywords_generated: false
  ragflow_synced: false
  qa_generated: false
---

Java est un langage de programmation de haut niveau orienté objet créé en 1995 par Sun Microsystems (rachetée en 2009 par Oracle). L'objectif central de Java est que les logiciels écrits dans ce langage obéissent au principe *write once, run anywhere* et sont très facilement portables sur plusieurs systèmes d’exploitation par le fait que le code source Java se compile en code octal (*bytecode*) pouvant être exécuté sur un environnement Java (JVM pour *Java virtual machine*); différentes architectures et plateformes peuvent donc constituer un environnement uniforme. Cette caractéristique fait de Java un langage populaire dans certains contextes et notamment pour l'apprentissage de la programmation. Même si l'accent n'est pas sur la performance, il existe des moyens d'augmenter la vitesse d'exécution et le langage a connu une certaine popularité auprès des scientifiques dans des domaines comme les sciences de la vie, d'où sont issus par exemple les outils d'analyse génomique [GATK](https://software.broadinstitute.org/gatk/) du Broad Institute. Le but de cette page n'est pas d'enseigner le langage Java, mais de fournir des conseils et suggestions pour son utilisation sur les grappes de l'Alliance.

L'Alliance offre plusieurs environnements Java via la commande [module](utiliser-des-modules.md). En principe, vous aurez un seul module Java chargé à la fois. Les principales commandes associées aux modules Java sont :
* `java` pour lancer un environnement Java;
* `javac` pour appeler le compilateur Java qui convertit un fichier source Java en bytecode.

Les logiciels Java sont fréquemment distribués sous forme de fichiers JAR portant le suffixe `jar`. Pour utiliser un logiciel Java, utilisez la commande

```bash
java -jar file.jar
```

## Parallélisme

### Fils d'exécution
Java permet la programmation avec fils, éliminant ainsi le recours à des interfaces et librairies comme OpenMP, pthreads et Boost qui sont nécessaires avec d'autres langages. L'objet Java principal pour traiter la concurrence est la classe `Thread`; on peut l'employer en fournissant une méthode `Runnable` à la classe `Thread` standard ou encore en définissant la classe `Thread` comme sous-classe, comme démontré ici :

```java title="thread.java"
public class HelloWorld extends Thread {
        public void run() {
            System.out.println("Hello World!");
        }
        public static void main(String args[]) {
            (new HelloWorld()).start();
        }
}
```
Cette approche est généralement la plus simple, mais présente cependant le désavantage de ne pas permettre l'héritage multiple; la classe qui implémente l'exécution concurrente ne peut donc pas avoir en sous-classe une autre classe potentiellement plus utile.

### MPI
On utilise souvent la librairie [MPJ Express](http://mpj-express.org/) pour obtenir un parallélisme de type MPI.

## Pièges

### Mémoire
Une instance Java s'attend à avoir accès à toute la mémoire physique d'un nœud alors que l'ordonnanceur ou un interpréteur pourrait imposer ses limites (souvent différentes) dépendant des spécifications du script de soumission ou des limites du nœud de connexion. Dans un environnement de ressources partagées, ces limites font en sorte que des ressources à capacité finie comme la mémoire et les cœurs CPU ne sont pas épuisées par une tâche au détriment d'une autre.

Quand une instance Java est lancée, elle fixe la valeur de deux paramètres selon la quantité de mémoire physique plutôt que la quantité de mémoire disponible comme suit :
* taille initiale du monceau (*heap*), 1/64 de la mémoire physique
* taille maximale du monceau (*heap*), 1/4 de la mémoire physique

En présence d'une grande quantité de mémoire physique, cette valeur de 1/4 peut aisément dépasser les limites imposées par l'ordonnanceur ou par un interpréteur et Java peut s'arrêter et produire des messages comme

```
Could not reserve enough space for object heap
There is insufficient memory for the Java Runtime Environment to continue.
```

Ces deux paramètres peuvent toutefois être explicitement contrôlés par l'un ou l'autre des énoncés suivants :

```bash
java -Xms256m -Xmx4g -version
```
ou
```bash
java -XX:InitialHeapSize=256m -XX:MaxHeapSize=4g -version
```

Pour voir toutes les options en ligne de commande que l'instance exécutera, utilisez l'indicateur `-XX:+PrintCommandLineFlags` comme suit :

```bash
$ java -Xms256m -Xmx4g -XX:+PrintCommandLineFlags -version
-XX:InitialHeapSize=268435456 -XX:MaxHeapSize=4294967296 -XX:ParallelGCThreads=4 -XX:+PrintCommandLineFlags -XX:+UseCompressedOops -XX:+UseParallelGC
```

Vous pouvez utiliser la variable d'environnement `JAVA_TOOL_OPTIONS` pour configurer les options d'exécution plutôt que de les spécifier en ligne de commande. Ceci s'avère utile quand des appels multiples sont lancés ou qu'un programme est appelé par un autre programme Java. Voici un exemple :

```bash
export JAVA_TOOL_OPTIONS="-Xms256m -Xmx2g"
```

À l'exécution, le programme émet un message de diagnostic semblable à *Picked up JAVA_TOOL_OPTIONS*; ceci indique que les options ont été prises en compte.

!!! attention "Mémoire"
    N'oubliez pas que l'instance Java crée elle-même une réserve d'utilisation de la mémoire. Nous recommandons que la limite par tâche soit fixée à 1 ou 2Go de plus que la valeur de l'option `-Xmx`.

### Récupération de mémoire (GC)
Java utilise le processus automatique de *récupération de mémoire* (Garbage Collection) pour identifier les variables avec des valeurs non valides et retourner la mémoire qui leur est associée au système d'exploitation. Par défaut, l'instance Java utilise un GC parallèle et détermine un nombre de fils de récupération de mémoire égal au nombre de cœurs CPU du nœud, que la tâche Java soit ou non multifil. Chacun des fils de récupération de mémoire consomme de la mémoire. De plus, la quantité de mémoire consommée par les fils de récupération de mémoire est proportionnelle à la quantité de mémoire physique.

!!! tip "Récupération de mémoire"
    Nous vous recommandons fortement d'avoir un nombre de fils de récupération de mémoire (GC) égal au nombre de cœurs CPU que vous demandez à l'ordonnanceur dans le script de soumission avec, par exemple, `-XX:ParallelGCThreads=12`. Vous pouvez aussi utiliser la récupération de mémoire séquentielle avec l'option `-XX:+UseSerialGC`, que la tâche soit ou non parallèle.

### Mot-clé `volatile`
Le sens de ce mot-clé est très différent de celui du même terme utilisé en programmation C/C++. La valeur d'une variable Java ayant cet attribut est toujours lue directement de la mémoire principale et toujours écrite directement dans la mémoire principale; toute modification à la variable sera donc visible par tous les autres fils. Dans certains contextes cependant, `volatile` ne suffit pas à empêcher les situations de compétition (*conditions de course*) et `synchronized` est nécessaire pour maintenir la cohérence du programme.

## Références
OAKS, Scott et Henry Wong, Java Threads: Understanding and Mastering Concurrent Programming, 3e édition, O'Reilly, 2012.