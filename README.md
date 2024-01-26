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

# Experiment

## Data Pre-Processing
<p>
The following steps have been done to pre-process the text data:<br>
1. Converted the text into lower case. <br>
2. Contractions have been expanded. Ex. can’t to cannot.<br>
3. Removed special characters and symbols like ’,?/+=)( and numeric values also.<br>
4. Truncated the source sentences after 10 words and target sentences after 10 words.<br>
5. Removed Hindi words from source sentences and English words from target sentences.<br>
Source and target sentence's length analysis is shown below.<br>
</p>

<img src="https://github.com/heenasingh1995/English-to-Hindi-Machine-Translation-Baseline/assets/47137754/70b99f23-83f4-47d7-875a-da25bc95c6eb.jpg" width="300" />

## Creating Vocabulary
<p>
For source vocabulary and target, only words with minimum of 3 occurrence
were taken. The source vocabulary size was 2214 and the
target vocabulary size was 2625. 
</p>

## Training

<p>
In this experiment, a bi-directional LSTM is used as an Encoder which outputs a 512-
dimensional hidden state with a dropout rate 0.3 and an LSTM Decoder which outputs a hidden
state of 256-dimensions with a dropout rate 0.3. Each word is embedded in
256 dimensions. A batch size of 256 and adagrad optimizer with a learning rate of 0.001 are used. The model was trained with early-stopping of 50 epochs. Best BLEU score of 37.3 was observed at epoch 117. 

Model’s training loss, validation loss and validation BLEU score is shown by graph in
figure below.

</p>
<br>

<img src="https://github.com/heenasingh1995/English-to-Hindi-Machine-Translation-Baseline/assets/47137754/085600b3-4488-45a2-9d40-bac3df588412.jpg" width="400" />

<br>

<img src="https://github.com/heenasingh1995/English-to-Hindi-Machine-Translation-Baseline/assets/47137754/0be70d35-3ef3-4bab-ba5b-37d82a36e9a9.jpg" width="400" />

# Results & Analysis
<p>
We have evaluated our generated summary on BLEU score.
 </p>
 
<b> BLEU Score Results on Test Dataset : BLEU = 34.21, 64.2/42.3/28.1/18.0 </b> <br>
<b> BLEU Score Results on Challenge Dataset : BLEU = 20.19, 52.3/28.9/16.3/9.2 </b>

 ## Translation Example

<img src="https://github.com/heenasingh1995/English-to-Hindi-Machine-Translation-Baseline/assets/47137754/95cd3d0b-773b-40cd-a28d-af11dcd479c9.jpg" width="500" />


 

