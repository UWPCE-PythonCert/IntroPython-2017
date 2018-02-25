# Base Linter

**Version:**  Version 0.1  
**Date:**  Feb 15, 2015  
**Who:** Matt Briggs

Base Linter is a command-line interface app checks for sets of words in a text by order. Each time the app encounters a word belonging to a set, it prompts you to choose which of the words in the set. The app will replace the word in that position in the word order in the text you are checking. When you are done, the app saved the updated text as a file with the date in the filename.

## Operation notes

 - Base Linter checks for sets of words ion your text. and allows you to choose which member of the set you would like to use.
 - You can load additional sets of word for checking in your text.
 - You are not limited to words but can include any string in the set. For example, you can check for a problem word and add a note in your set to be replaced by the linter so that you can review the problem after you have done the check with Base Linter. For example, the following set ["problematic", "\*\*Revise please - problematic\*\*"] would flag "problematic" amd allow you to replace it with the note. After you are done checking, you could revise the text in your text editor.

## How to use Base Linter

I initially built the Base Linter to create a manual check for homophone errors in my text.

A homophone is a word that is pronounced the same, to varying extent, as another word but differs in meaning. A homophone may also differ in spelling. The two words may be spelled the same, such as rose (flower) and rose (past tense of "rise"), or differently, such as carat, caret, and carrot, or to, two, and too. In a text if they are spelled the same and sound the same, then they are a duck and so we can safely ignore those. But if they are spelled differently, that can cause all kind of problems.

I have mild dyslexia. If I was a hunter gather this issue might go unnoticed, but I work as a writer where I am expected to always know the difference between carat, caret, and carrot. I have always committed homophone errors. These errors are nearly impossible to catch with a spellchecker. In fact, a spellchecker can contribute the problem because I may choose a word that spelled correctly but it is the wrong word: a homophone. While Grammar parsers can catch some of these errors, but most of them have specific functions that are checking for specific homophone sets. In my case, I write a lot and so I make a lot of homophone errors that may not show up on lists of the most common homophone errors.

Once a homophone error creeps into a text, many human proofreaders also have difficulty spotting these errors. Occasionally a meme will make the rounds of the difficulty of visualizing misspelled words when the misspelled word contains the same characters of the correctly spelled word. If the errors are invisible to most people, then why bother correcting them? Because they are wrong! And because for a small percentage of the population, these type of errors are as glaring as a smudge of questionable origin on the page. You would think if a person had this type of skill, they would be in high demand as proofreaders? But this hasn't proven the case. Instead most of them become book reviewers. And so this is my conundrum.

Luckily, with a dictionary and a bit of time I can use a machine to point out each of these possible errors.

The tool will open a text file, and then get a list of each word in order. It then loads the homophone list. Each item in the list is a set of homophones such as "their, there, they're" and every time any word in the text is a member of a homophone set, the tool will prompt you to choose which of the homophones you would like to use. You can make your selection, and then the tool will update the occurrence with the correct (I hope) choice.

The word list itself comes from a list based on the book _Handbook of Homophones_ by William Cameron Townsend from 1975. The list contains the words that sound the same, but are spelled differently. The list is also a bit fusty around the margins. While it will flag the most common homophones errors in Standard American English, it will also flag some words that I don't think many people us anymore, and it will not recognize any words have come into existence since 1975.

This is a brute force approach to resolving my problem. I initially created an even more primitive tool  than this one using Microsoft Word's indexing feature. This was in the early 2000s when my programming abilities were limited to cutting and pasting JavaScript into my web pages and adjusting some parameters. I began to code so that I could make this program. So I am happy with this result, but like any task once I began to learn to code I learned there was so much more that could be done and that it could be done better.

The first increase to this tool's primitive capabilities, was to add additional lists. I could use the underlying loop once built to checks sets of words other than homophones. I could check style guide words or problem words. And rather than just have my selections be corrections, I could replace the words with warning notes for me so that I could return to my text and revise those problem words.

## Current limitations and issues with the application

This program is an improvement over using Microsoft Word's index feature. It still has some issues, however.

 - The app is currently grabbing the capitalization and associated punctuation with each word. This means that the first word and the last word of any sentence will be ignored. It also means that any word that is fused to a mark such as a commas, parenthesis, or markdown tokens such as ** will also be ignored. Right now I'm depending on this marriage to sanely reassemble your text when the program is done checking the words. This is the first thing I need to update.
 - The app can only assess a single word in the text rather than a phrase. The result of this is that if you are looking for problem phrases, this tool won't be that useful for you.
 - The app must use a text file. (Actually it must use a text file a UTF-8 text encoding). So this will work well on files with a .txt extension or .md extension. I've been doing most of my writing in Markdown this year. So if you want to use Microsoft Word or Apple Pages, you will need to move your text out of those apps and into text (and thereby lose your formatting!).

 ## My future plans for this app

While future plans always sound provisional to me and therefore unlikely to happen, I do have a desire to make the following updates to the program. It did take me nearly fifteen years to write this program in the first place, but I had to learn to write a program first. And I found out the other day even though I have learned to program, I am a very slow programmer. But for what is worth, here are my thoughts about how to take this primordial app and make it better.

### Next subversion

- Resolve the first bullet under known limitations.
- Add the ability to update and manage your own lists.
- Add the ability to ignore sets of words in the list. Right now you would need to modify the JSON file that handles the list to ignore certain homophones errors such as the check for "the" and "thee" which is really annoying because of the frequency of "the" and the fact that I pretty much never use "thee" in a text.

### Next major version

- Use the Python Natural Language Tool Kit to tokenize and parse the incoming text.
- Use natural language probabilities of word occurrence in a training text to automatically choose the correct homophones in a text being checked.
- Improve the command line interface checking experience. I have become really happy with command line tools in the last couple of years. Changing my writing ot markdown has been part of this. I think the end state of this app will remain a command line tool. However, the underlying approach may be adaptable to plug-ins for Microsoft Word and Visual Studio Code.

## Feedback

This is a work in progress and I am taking one step at a time with the project. Each step I hope ends up being an incremental improvement as I have time. If you have any feedback, please feel to send me an email at **mattbriggs at finalstatepress dot com**.