# lab3: Train finger counting classifier

## Ultimate goal
In the coming three labs, we would like to build a Tkinter GUI application that can recognize finger counting for digits from 1 to 5. The final applictation will capture images form a webcam and display the finger count as a string overlay. We will proceed in 3 steps:
1. Lab2: Data acquisition from webcam: Build a GUI application to acquire image data.
2. Lab3: Train a fastai learner to recognize the 5 finger counts.
3. Lab4: Wrap the model in a GUI application to predict digits from live webcam stream.

We will implement the [American counting system](https://en.wikipedia.org/wiki/Finger-counting#Western_world)

## Lab3 Goal
In this lab, we will focus on training an image classifier with fastai.

You will use concepts learned in Chapter 5:
- Presizing
- augmentations
- learning rate finder
- transfer learning with unfreezing
- discriminative learning rates
- reproducible training

The file `lab3_train_finger_count.ipynb` contains some starter code to be extended.

The image data to be used are images collected in Lab3: (at least) 40 training, and 10 valiation images for each digit with variations. Images should be in the following directory structure:
```
train
  |--one
  |  |-- 00000000.jpg
  |  ...
  |--two
  |  |-- 00000000.jpg
  |  ...
  ...
valid
  |--one
  |  |-- 00000000.jpg
  |  ...
  |--two
  |  |-- 00000000.jpg
  |  ...
  ...
```


## What to hand in
- In the Jupyter notebook `lab3_train_finger_count.ipynb`:
  - implement the steps indicated.
  - answer questions.
  - complete *Summary and Conclusion*
  - complete *Reflection*
- Keep code clean, comment/document and remove any unnecessary cells in the notebook.

During development, save progress with git and use descriptive commit messages.

Hand in: git push `lab3_train_finger_count.ipynb`, verify on github, submit url on D2L.

**Important:** Do **not** commit image data to github. Images do **not** need to be handed in.

