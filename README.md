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
|Total         	|    32923	 |         164125	 |      166917   |

The word counts are approximate, prior to tokenization.

# System Architecture
Encoder Decoder with Attention mechanism model is used for Translation. Encoder-Decoder with attention model was introduced by Bahdanau for machine translation and is depicted in Figure below. Later it has been used by many researchers as a baseline system for their research work. In this encoder-decoder model, encoder compress input sequence W = (w1 , w2 , ......, wTx ) to a fixed-length vector. The decoder produces output at each timestamp. The encoder will produce hidden state  by taking word and previous hidden state  in every time step. The output of the last timestamp of the encoder is given to the decoder as initial input. At each timestamp t, the decoder will predict a target word by a soft search for the relevant part of the source sentence.
Model's architecture is shown in the figure below.

<br>

<img src = "https://github.com/heenasingh1995/English-to-Hindi-Machine-Translation-Baseline/assets/47137754/787f2477-a461-4405-bda5-b921a8cc5bd3.jpg" width = "600" />

<br>

