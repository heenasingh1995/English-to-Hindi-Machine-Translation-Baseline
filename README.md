# English to Hindi Machine Translation
## Introduction

Machine Translation (MT) attempts to minimize the communication gap among people from various linguistic backgrounds. Automatic translation between pair of different natural languages is the task of MT mechanism, wherein Neural Machine Translation (NMT) attract attention because it offers reasonable translation accuracy in case of the context analysis and fluent translation.

# Dataset Details & Analysis

<p>Mindi Visual Genome is a multimodal dataset consisting of text and
images suitable for English-to-Hindi multimodal machine translation task
and multimodal research. We have selected short English segments
(captions) from Visual Genome along with associated images and
automatically translated them to Hindi with manual post-editing, taking
the associated images into account.</p>

<p> Dataset Statistics are given below :<br></p>

|Dataset       |	Segments 	|English Words   |	Hindi Words    |
|-------       	|---------	|----------------|	-------------  |
|Train         |	    28930	|          143164	|       145448   |
|Dev           |	      998	|            4922	|         4978   |
|Test          	|     1595	|            7853	 |        7852   |
|Challenge Test	|     1400	|            8186	 |        8639   |
|-------       |	---------	|----------------	|-------------   |
|Total         	|    32923	 |         164125	 |      166917   |

The word counts are approximate, prior to tokenization.

# System Architecture
Encoder Decoder with Attention mechanism model is used for Translation. 
Model's architecture is shown in the figure below.
<br>
<img src = "https://github.com/heenasingh1995/English-to-Hindi-Machine-Translation-Baseline/assets/47137754/787f2477-a461-4405-bda5-b921a8cc5bd3.jpg" width = "600" />

<br>

