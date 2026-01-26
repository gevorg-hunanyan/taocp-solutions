# TAOCP Exercise Solutions

This repository documents my ongoing efforts to work through *The Art of Computer Programming* (TAOCP) by Donald E. Knuth. It contains my solutions to selected exercises, along with notes and auxiliary material developed along the way. There are currently <!-- SOLVED_COUNT -->2<!-- /SOLVED_COUNT --> solved exercises in the repository. Solutions are written in Markdown and/or MMIX assembly (*.mms), and links to the solutions are provided below.

---

<!-- SOLVED_ASCII -->
<!-- /SOLVED_ASCII -->

---

<!--ts-->
* [Chapter 1 - Basic Concepts](#chapter-1---basic-concepts)
  * [1.1. Algorithms](#11-algorithms)
  * [1.2. Mathematical Preliminaries](#12-mathematical-preliminaries)
    * [1.2.1. Mathematical Induction](#121-mathematical-induction)
    * [1.2.2. Numbers, Powers, and Logarithms](#122-numbers-powers-and-logarithms)
    * [1.2.3. Sums and Products](#123-sums-and-products)
    * [1.2.4. Integer Functions and Elementary Number Theory](#124-integer-functions-and-elementary-number-theory)
    * [1.2.5. Permutations and Factorials](#125-permutations-and-factorials)
    * [1.2.6. Binomial Coefficients](#126-binomial-coefficients)
    * [1.2.7. Harmonic Numbers](#127-harmonic-numbers)
    * [1.2.8. Fibonacci Numbers](#128-fibonacci-numbers)
    * [1.2.9. Generating Functions](#129-generating-functions)
    * [1.2.10. Analysis of an Algorithm](#1210-analysis-of-an-algorithm)
    * [*1.2.11. Asymptotic Representations](#1211-asymptotic-representations)
      * [*1.2.11.1. The O-notation](#12111-the-o-notation)
      * [*1.2.11.2. Euler's summation formula](#12112-eulers-summation-formula)
      * [*1.2.11.3. Some asymptotic calculations](#12113-some-asymptotic-calculations)
  * [1.3'. MMIX](#13-mix)
    * [1.3.1'. Description of MMIX](#131-description-of-mix)
    * [1.3.2'. The MMIX Assembly Language](132-the-mix-assembly-language)
    * [1.3.3'. Applications to Permutations](133-applications-to-permutations)
  * [1.4'. Some Fundamental Programming Techniques](14-some-fundamental-programming-techniques)
    * [1.4.1'. Subroutines](141-subroutines)
    * [1.4.2'. Сoroutines](142-coroutines)
    * [1.4.3'. Interpretive Routines](143-interpretive-routines)
      * [1.4.3.1. A MIX simulator](1431-a-mix-simulator)
      * [*1.4.3.2. Trace routines](1432-trace-routines)
    * [1.4.4. Input and Output](144-input-and-output)
* [Chapter 2 - Information Structures](#chapter-2---information-structures)
  * [2.1. Introduction](#21-introduction)
  * [2.2. Linear Lists](22-linear-lists)
    * [2.2.1. Stacks, Queues, and Deques](#221-stacks-queues-and-deques)
    * [2.2.2. Sequential Allocation](#222-sequential-allocation)
    * [2.2.3. Linked Allocation](#223-linked-allocation)
    * [2.2.4. Circular Lists](#224-circular-lists)
    * [2.2.5. Doubly Linked Lists](#225-doubly-linked-lists)
    * [2.2.6. Arrays and Orthogonal Lists](#226-arrays-and-orthogonal-lists)
  * [2.3. Trees](#23-trees)
    * [2.3.1. Traversing Binary Trees](#231-traversing-binary-trees)
    * [2.3.2. Binary Tree Representation of Trees](#232-binary-tree-representation-of-trees)
    * [2.3.3. Other Representations of Trees](#233-other-representations-of-trees)
    * [2.3.4. Basic Mathematical Properties of Trees](#234-basic-mathematical-properties-of-trees)
      * [2.3.4.1. Free trees](#2341-free-trees)
      * [2.3.4.2. Oriented trees](#2342-oriented-trees)
      * [*2.3.4.3. The "infinity lemma"](#2343-the-infinity-lemma)
      * [*2.3.4.4. Enumeration of trees](#2344-enumeration-of-trees)
      * [2.3.4.5. Рath length](#2345-path-length)
      * [2.3.4.6. History and Bibliography](#2346-history-and-bibliography)
    * [2.3.5. Lists and Garbage Collection](#235-lists-and-garbage-collection)
  * [2.4. Multilinked Structures](#24-multilinked-structures)
  * [2.5. Dynamic Storage Allocation](#25-dynamic-storage-allocation)
<!--te-->

<!-- SOLUTIONS_START -->

# Chapter 1 - Basic Concepts

## 1.1 Algorithms

[ex1](https://github.com/gevorg-hunanyan/taocp-solutions/blob/main/chapter-1/section-1-1/ex001.md)
[ex2](https://github.com/gevorg-hunanyan/taocp-solutions/blob/main/chapter-1/section-1-1/ex002.md)
[ex3](https://github.com/gevorg-hunanyan/taocp-solutions/blob/main/chapter-1/section-1-1/ex003.md)
[ex4](https://github.com/gevorg-hunanyan/taocp-solutions/blob/main/chapter-1/section-1-1/ex004.md)
[ex5](https://github.com/gevorg-hunanyan/taocp-solutions/blob/main/chapter-1/section-1-1/ex005.md)
[ex6](https://github.com/gevorg-hunanyan/taocp-solutions/blob/main/chapter-1/section-1-1/ex006.md)
[ex7](https://github.com/gevorg-hunanyan/taocp-solutions/blob/main/chapter-1/section-1-1/ex007.md)
ex8
ex9

## 1.2 Mathematical Preliminaries

### 1.2.1 Mathematical Induction

[ex1](https://github.com/gevorg-hunanyan/taocp-solutions/blob/main/chapter-1/section-1-2/subsection-1-2-1/ex001.md)
[ex2](https://github.com/gevorg-hunanyan/taocp-solutions/blob/main/chapter-1/section-1-2/subsection-1-2-1/ex002.md)
[ex3](https://github.com/gevorg-hunanyan/taocp-solutions/blob/main/chapter-1/section-1-2/subsection-1-2-1/ex003.md)
[ex4](https://github.com/gevorg-hunanyan/taocp-solutions/blob/main/chapter-1/section-1-2/subsection-1-2-1/ex004.md)
[ex5](https://github.com/gevorg-hunanyan/taocp-solutions/blob/main/chapter-1/section-1-2/subsection-1-2-1/ex005.md)
[ex6](https://github.com/gevorg-hunanyan/taocp-solutions/blob/main/chapter-1/section-1-2/subsection-1-2-1/ex006.md)
[ex7](https://github.com/gevorg-hunanyan/taocp-solutions/blob/main/chapter-1/section-1-2/subsection-1-2-1/ex007.md)
ex8
[ex9](https://github.com/gevorg-hunanyan/taocp-solutions/blob/main/chapter-1/section-1-2/subsection-1-2-1/ex009.md)
ex10
ex11
ex12
ex13
ex14
ex15

### 1.2.2 Numbers, Powers, and Logarithms

[ex1](https://github.com/gevorg-hunanyan/taocp-solutions/blob/main/chapter-1/section-1-2/subsection-1-2-2/ex001.md)
[ex2](https://github.com/gevorg-hunanyan/taocp-solutions/blob/main/chapter-1/section-1-2/subsection-1-2-2/ex002.md)
[ex3](https://github.com/gevorg-hunanyan/taocp-solutions/blob/main/chapter-1/section-1-2/subsection-1-2-2/ex003.md)
[ex4](https://github.com/gevorg-hunanyan/taocp-solutions/blob/main/chapter-1/section-1-2/subsection-1-2-2/ex004.md)
ex5
ex6
ex7
ex8
ex9
ex10
ex11
ex12
ex13
ex14
ex15
[ex16](https://github.com/gevorg-hunanyan/taocp-solutions/blob/main/chapter-1/section-1-2/subsection-1-2-2/ex016.md)
ex17
ex18
ex19
ex20
ex21
ex22
ex23
ex24
ex25
ex26
ex27
ex28
[ex29](https://github.com/gevorg-hunanyan/taocp-solutions/blob/main/chapter-1/section-1-2/subsection-1-2-2/ex029.md)

### 1.2.3 Sums and Products

[ex1](https://github.com/gevorg-hunanyan/taocp-solutions/blob/main/chapter-1/section-1-2/subsection-1-2-3/ex001.md)
[ex2](https://github.com/gevorg-hunanyan/taocp-solutions/blob/main/chapter-1/section-1-2/subsection-1-2-3/ex002.md)
[ex3](https://github.com/gevorg-hunanyan/taocp-solutions/blob/main/chapter-1/section-1-2/subsection-1-2-3/ex003.md)
ex4
ex5
ex6
ex7
ex8
ex9
ex10
ex11
ex12
ex13
ex14
ex15
ex16
ex17
ex18
ex19
ex20
ex21
ex22
ex23
ex24
ex25
ex26
ex27
ex28
ex29
ex30
ex31
ex32
ex33
ex34
ex35
ex36
ex37
ex38
ex39
ex40
ex41
ex42
ex43
ex44
ex45
ex46
ex47

### 1.2.4 Integer Functions and Elementary Number Theory

[ex1](https://github.com/gevorg-hunanyan/taocp-solutions/blob/main/chapter-1/section-1-2/subsection-1-2-4/ex001.md)
[ex2](https://github.com/gevorg-hunanyan/taocp-solutions/blob/main/chapter-1/section-1-2/subsection-1-2-4/ex002.md)
ex3
ex4
ex5
ex6
ex7
ex8
ex9
ex10
ex11
ex12
ex13
ex14
ex15
ex16
ex17
ex18
ex19
ex20
ex21
ex22
ex23
ex24
ex25
ex26
ex27
ex28
ex29
ex30
ex31
ex32
ex33
ex34
ex35
ex36
ex37
ex38
ex39
ex40
ex41
ex42
ex43
ex44
ex45
ex46
ex47
ex48
ex49

### 1.2.5 Permutations and Factorials

ex1
ex2
ex3
ex4
ex5
ex6
ex7
ex8
ex9
ex10
ex11
ex12
ex13
ex14
ex15
ex16
ex17
ex18
ex19
ex20
ex21
ex22
ex23
ex24
ex25

### 1.2.6 Binomial Coefficients

ex1
ex2
ex3
ex4
ex5
ex6
ex7
ex8
ex9
ex10
ex11
ex12
ex13
ex14
ex15
ex16
ex17
ex18
ex19
ex20
ex21
ex22
ex23
ex24
ex25
ex26
ex27
ex28
ex29
ex30
ex31
ex32
ex33
ex34
ex35
ex36
ex37
ex38
ex39
ex40
ex41
ex42
ex43
ex44
ex45
ex46
ex47
ex48
ex49
ex50
ex51
ex52
ex53
ex54
ex55
ex56
ex57
ex58
ex59
ex60
ex61
ex62
ex63
ex64
ex65
ex66
ex67
ex68

### 1.2.7 Harmonic Numbers

ex1
ex2
ex3
ex4
ex5
ex6
ex7
ex8
ex9
ex10
ex11
ex12
ex13
ex14
ex15
ex16
ex17
ex18
ex19
ex20
ex21
ex22
ex23
ex24

### 1.2.8 Fibonacci Numbers

ex1
ex2
ex3
ex4
ex5
ex6
ex7
ex8
ex9
ex10
ex11
ex12
ex13
ex14
ex15
ex16
ex17
ex18
ex19
ex20
ex21
ex22
ex23
ex24
ex25
ex26
ex27
ex28
ex29
ex30
ex31
ex32
ex33
ex34
ex35
ex36
ex37
ex38
ex39
ex40
ex41
ex42

### 1.2.9 Generating Functions

ex1
ex2
ex3
ex4
ex5
ex6
ex7
ex8
ex9
ex10
ex11
ex12
ex13
ex14
ex15
ex16
ex17
ex18
ex19
ex20
ex21
ex22
ex23
ex24
ex25
ex26

### 1.2.10 Analysis of an Algorithm

ex1
ex2
ex3
ex4
ex5
ex6
ex7
ex8
ex9
ex10
ex11
ex12
ex13
ex14
ex15
ex16
ex17
ex18
ex19
ex20
ex21
ex22
ex23

### *1.2.11 Asymptotic Representations

### *1.2.11.1 The O-notation

ex1
ex2
ex3
ex4
ex5
ex6
ex7
ex8
ex9
ex10
ex11
ex12
ex13

### *1.2.11.2 Euler's summation formula

ex1
ex2
ex3
ex4
ex5
ex6
ex7
ex8
ex9

### *1.2.11.3 Some asymptotic calculations

ex1
ex2
ex3
ex4
ex5
ex6
ex7
ex8
ex9
ex10
ex11
ex12
ex13
ex14
ex15
ex16
ex17
ex18
ex19
ex20

## 1.3. MIX

### 1.3.1. Description of MIX

[ex1](https://github.com/gevorg-hunanyan/taocp-solutions/blob/main/chapter-1/section-1-3/subsection-1-3-1/ex001.md)
[ex2](https://github.com/gevorg-hunanyan/taocp-solutions/blob/main/chapter-1/section-1-3/subsection-1-3-1/ex002.md)
ex3
ex4
ex5
ex6
ex7
ex8
ex9
ex10
ex11
ex12
ex13
ex14
ex15
ex16
ex17
ex18
ex19
ex20
ex21
ex22
ex23
ex24
ex25
ex26

### 1.3.2. The MIX Assembly Language

ex1
ex2
ex3
ex4
ex5
ex6
ex7
ex8
ex9
ex10
ex11
ex12
ex13
ex14
ex15
ex16
ex17
ex18
ex19
ex20
ex21
ex22
ex23

### 1.3.3. Applications to Permutations

ex1
ex2
ex3
ex4
ex5
ex6
ex7
ex8
ex9
ex10
ex11
ex12
ex13
ex14
ex15
ex16
ex17
ex18
ex19
ex20
ex21
ex22
ex23
ex24
ex25
ex26
ex27
ex28
ex29
ex30
ex31
ex32
ex33
ex34
ex35
ex36

## 1.4. Some Fundamental Programming Techniques

### 1.4.1. Subroutines

ex1
ex2
ex3
ex4
ex5
ex6
ex7

### 1.4.2. Сoroutines

ex1
ex2
ex3
ex4
ex5
ex6
ex7

### 1.4.3. Interpretive Routines

### 1.4.3.1. A MIX simulator

ex1
ex2
ex3
ex4
ex5
ex6
ex7
ex8

### *1.4.3.2. Trace routines

ex1
ex2
ex3
ex4
ex5
ex6
ex7

### 1.4.4. Input and Output

ex1
ex2
ex3
ex4
ex5
ex6
ex7
ex8
ex9
ex10
ex11
ex12
ex13
ex14
ex15
ex16
ex17
ex18
ex19

# Chapter 2 - Information Structures

## 2.1. Introduction

ex1
ex2
ex3
ex4
ex5
ex6
ex7
ex8
ex9

## 2.2. Linear Lists

### 2.2.1. Stacks, Queues, and Deques

ex1
ex2
ex3
ex4
ex5
ex6
ex7
ex8
ex9
ex10
ex11
ex12
ex13
ex14

### 2.2.2. Sequential Allocation

ex1
ex2
ex3
ex4
ex5
ex6
ex7
ex8
ex9
ex10
ex11
ex12
ex13
ex14
ex15
ex16
ex17
ex18
ex19

### 2.2.3. Linked Allocation

ex1
ex2
ex3
ex4
ex5
ex6
ex7
ex8
ex9
ex10
ex11
ex12
ex13
ex14
ex15
ex16
ex17
ex18
ex19
ex20
ex21
ex22
ex23
ex24
ex25
ex26
ex27
ex28
ex29
ex30

### 2.2.4. Circular Lists

ex1
ex2
ex3
ex4
ex5
ex6
ex7
ex8
ex9
ex10
ex11
ex12
ex13
ex14
ex15
ex16
ex17
ex18

### 2.2.5. Doubly Linked Lists

ex1
ex2
ex3
ex4
ex5
ex6
ex7
ex8
ex9
ex10
ex11
ex12

### 2.2.6. Arrays and Orthogonal Lists

ex1
ex2
ex3
ex4
ex5
ex6
ex7
ex8
ex9
ex10
ex11
ex12
ex13
ex14
ex15
ex16
ex17
ex18
ex19
ex20
ex21
ex22
ex23
ex24

## 2.3. Trees

ex1
ex2
ex3
ex4
ex5
ex6
ex7
ex8
ex9
ex10
ex11
ex12
ex13
ex14
ex15
ex16
ex17
ex18
ex19
ex20
ex21
ex22

### 2.3.1. Traversing Binary Trees

ex1
ex2
ex3
ex4
ex5
ex6
ex7
ex8
ex9
ex10
ex11
ex12
ex13
ex14
ex15
ex16
ex17
ex18
ex19
ex20
ex21
ex22
ex23
ex24
ex25
ex26
ex27
ex28
ex29
ex30
ex31
ex32
ex33
ex34
ex35
ex36
ex37

### 2.3.2. Binary Tree Representation of Trees

ex1
ex2
ex3
ex4
ex5
ex6
ex7
ex8
ex9
ex10
ex11
ex12
ex13
ex14
ex15
ex16
ex17
ex18
ex19
ex20
ex21
ex22

### 2.3.3. Other Representations of Trees

ex1
ex2
ex3
ex4
ex5
ex6
ex7
ex8
ex9
ex10
ex11
ex12
ex13
ex14
ex15
ex16
ex17
ex18
ex19

### 2.3.4. Basic Mathematical Properties of Trees

### 2.3.4.1. Free trees

ex1
ex2
ex3
ex4
ex5
ex6
ex7
ex8
ex9
ex10
ex11
ex12
ex13

### 2.3.4.2. Oriented trees

ex1
ex2
ex3
ex4
ex5
ex6
ex7
ex8
ex9
ex10
ex11
ex12
ex13
ex14
ex15
ex16
ex17
ex18
ex19
ex20
ex21
ex22
ex23
ex24
ex25
ex26
ex27
ex28

### *2.3.4.3. The "infinity lemma"

ex1
ex2
ex3
ex4
ex5
ex6
ex7
ex8

### *2.3.4.4. Enumeration of trees

ex1
ex2
ex3
ex4
ex5
ex6
ex7
ex8
ex9
ex10
ex11
ex12
ex13
ex14
ex15
ex16
ex17
ex18
ex19
ex20
ex21
ex22
ex23
ex24
ex25
ex26
ex27
ex28
ex29
ex30
ex31
ex32
ex33

### 2.3.4.5. Path length

ex1
ex2
ex3
ex4
ex5
ex6
ex7
ex8
ex9
ex10
ex11
ex12
ex13
ex14
ex15
ex16
ex17

### 2.3.4.6. History and Bibliography

ex1
ex2
ex3
ex4

### 2.3.5. Lists and Garbage Collection

ex1
ex2
ex3
ex4
ex5
ex6
ex7
ex8
ex9
ex10
ex11
ex12

## 2.4. Multilinked Structures

ex1
ex2
ex3
ex4
ex5
ex6
ex7
ex8
ex9
ex10
ex11
ex12
ex13
ex14
ex15

## 2.5. Dynamic Storage Allocation

ex1
ex2
ex3
ex4
ex5
ex6
ex7
ex8
ex9
ex10
ex11
ex12
ex13
ex14
ex15
ex16
ex17
ex18
ex19
ex20
ex21
ex22
ex23
ex24
ex25
ex26
ex27
ex28
ex29
ex30
ex31
ex32
ex33
ex34
ex35
ex36
ex37
ex38
ex39
ex40
ex41
ex42
ex43
ex44

<!-- SOLUTIONS_END -->
