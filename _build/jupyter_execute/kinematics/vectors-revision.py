#!/usr/bin/env python
# coding: utf-8

# ## Vectors Fundamentals

# ```{figure} ./images/2.png
# ---
# name: 2
# ---
# ```
# ```{attention}
# In rigid body kinematics, we aim to mathematically describe the motion of $B$ and $P$ in $R$.
# ```
# 
# - This requires pre-requiste knowledge on:<br>
#     (i) **vectors**: unit vector, general vector, component form<br>
#     (ii) **vector algebra**: addition of vectors multiplication of vectors<br>
#     (iii) **vector calculus**: vector differentiation<br>

# - **scalar**: A quantity described purely by a number. <br>
# &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;e.g. $1, 2, 3\ldots$; one pint of beer<br>
# - **vector**: a quantity characterised by both magnitude and direction.
# - _Notation_: commonly, written using letters from the English and Greek alphabets.
# 
# ```{figure} ./images/3.png
# ---
# name: 3
# ---
# ```
# ### Representation
# > Vectors are drawn as a directed line segment (i.e., a line segment with an arrow at one end). 
# 
# They are typically represented for two cases:
#   
# ```{figure} ./images/4.png
# ---
# name: 4
# ---
# ```
# 
# Conversely, by the same rule, a clockwise vector will have a negative direction and points into the plane of the paper. The convention is shown below for a vector $\vec{\mathcal{L}}$:
# 
# ```{figure} ./images/5.png
# ---
# name: 5
# ---
# ```
# 
# ```{attention}
# The inclination of clockwise and counterclockwise vectors is $90^{\circ{}}$ with respect to the plane of the paper.
# ```
# 
# ### Unit vector
# >A vector of unit magnitude (i.e., its magnitude is $1$). 
# 
# Unit vectors are commonly written with a caret $(\widehat{\ })$ over a letter in the alphabet. For example, $\hat{i}$ is a unit vector and $\left|\left|\hat{i}\right|\right|=1$ says that magnitude of $\hat{i}$ is $1$.
# 
# ### Reference frames 
# 
# > A set of three unit vectors that are mutually orthogonal.
# 
# In the figure below, $X-Y-Z$ form a Cartesian coordinate system. $\hat{i},\;\hat{j}\;\& \;\hat{k}$ are a set of unit vectors that are mutually orthogonal and directed along $X-Y-Z$ respectively.
# 
# ```{figure} ./images/6.png
# ---
# name: 6
# ---
# ```
# 
# The set of unit vectors are right-handed (also known as a “dextral set”), which means the following relationships hold true:
# 
# $$
# \hat{i} \times \hat{j} = \hat{k}  \\
# \hat{j} \times \hat{k} = \hat{i}  \\
# \hat{k} \times \hat{i} = \hat{j}  \\
# $$
# 
# The set of unit vector form a reference frame $R$.
# 
# Reference frames are useful for studying moving objects. This will become apparent in the coming weeks of lectures.
# 
# An alternate notation for unit vectors that make up a reference frame commonly used for dynamics is shown in the figure below; it makes use of subscripts in $x$, $y$, and $z$ directions to make it explicit along which coordinate axis the unit vectors are aligned. We will (almost always) see (and use) such subscript-based notations in these notes for sake of clarity.
# 
# ```{figure} ./images/7.png
# ---
# name: 7
# ---
# ```
# 
# * $\hat{a}_x$ is the unit vector along the $X$-direction
# * $\hat{a}_y$ is the unit vector along the $Y$-direction
# * $\hat{a}_z$ is the unit vector along the $Z$-direction
# 
# This is a dextral set of unit vectors, which form a reference frame $A$.
# 
# $$
# \begin{align}
# \hat{a}_x \times \hat{a}_y =& \hat{a}_z  \\
# \hat{a}_y \times \hat{a}_z =& \hat{a}_x  \\
# \hat{a}_z \times \hat{a}_x =& \hat{a}_y  \\
# \hat{a}_x \times \hat{a}_z =& -\hat{a}_y  \\
# \hat{a}_z \times \hat{a}_y =& -\hat{a}_x  \\
# \hat{a}_y \times \hat{a}_x =& -\hat{a}_z  \\
# \end{align}
# $$
# 
# ### Component form
# 
# In the figure below, $\vec{r}$ is a vector with coordinates $a,\;b,\;c$ in $X-Y-Z$, respectively.
# 
# ```{figure} ./images/8.png
# ---
# name: 8
# ---
# ```
# 
# ```{note}
# $a,\;b,\;c$ are scalars.
# ```
# 
# The component form of $\vec{r}$ is given by:
# 
# $$
# \vec{r} = a\hat{i} + b\hat{j} + c\hat{k}
# $$
# 
# This is the “component form” of expressing vectors, which makes use of scalars and unit vectors.

# ### Vector algebra using a CAS (Computer Algebra Systems)

# ```{attention}
# Please review addition and multiplication of vectors.
# ```
# 
# In this module on dynamics, we will exploit a computer algebra system (CAS, for short) to perform some key vector algebra operations. A CAS is a software that allows manipulation of non-numerical as well as numerical mathematical expressions in a manner similar to that done manually, by humans.
# 
# `SymPy` is a free CAS that we will use in studying dynamics. It has many advanced features that are particularly useful in studying rigid body dynamics.
