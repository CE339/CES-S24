---
title: "Getting Started With Google Colab and Python"
layout: single
permalink: /docs/modules/codes/colab/
sidebar:
 nav: modules
---

We will use Python and Google Colaboratory to solve LP models. Google Colaboratory, or “Colab” for short, is a web-based iPython Notebook service for interactive coding. It allows you to write and execute Python in your browser, with zero configuration required, free access to GPUs and easy sharing. Zero configuration required means you do not need to have Python, Anaconda and libraries installed to your local machine. Google Colab is very similar to Jupyter Notebook.

Google Colab documents have extension *.ipynb* and use the Markdown format which means you can create a document that contains text, images and executable code.

### Set Up Google Colab

To set up your Google Colab go to your Google Drive and select New. If you don't have a google account, you will need to set up one. You can use your duke email or personal email to set up your account.

![Screenshot](images/Picture1.png)

Navigate to More > Connect more apps.

![Screenshot](images/Picture2.png)

A pop-up window will appear. Scroll down until you find Colaboratory.

![Screenshot](images/Picture3.png)

Select Colaboratory and on the next pop-up window click Install.

![Screenshot](images/Picture4.png)

You are all set!

### Storing your Colab Scripts

The easiest way to save Colab notebooks is to save it in your Google Drive. Click File > Save a copy in Drive. Once you saved a copy, you can open it from your Google Drive or Colab dashboard.

Once you create your first Colab file and mount to your google drive, a folder called "Colab Notebooks" will be created on you Google Drive. All files you create, edit and save a copy will be stored in that folder.

### Installing libraries on Google's GPU to run your codes

Bash commands can be run in your notebook (similar to how you would do in your terminal) by prefixing the command with ''!''. For example, '!pwd' command prints out the pathway to the current working directory. '!ls' command prints out a list of contents in current directory.

Bash command can be used to install libraries. Most common libraries are already installed on Colab. If you need to install additional libraries you can use ‘!pip’

!pip install [library name]

To install other libraries available through Advanced Package Tool (apt) use ‘!apt-get’

!apt-get install [package name]

For more info visit
https://colab.research.google.com/drive/1YKHHLSlG-B9Ez2-zf-YFxXTVgfC_Aqtt#scrollTo=UTRJlO55LdKf

### Writing your First Code in Colab

Now to check if everything is working, you can write a command to display a simple sentence “Hello World”. Open a new notebook on Colab and type the following command.

print('Hello World')

This will output the following:

![Screenshot](images/Picture5.png)

If you get the same output above, then you’ve finished your first, and probably the simplest program using Python! Feel free to play with it and write anything else you want!
