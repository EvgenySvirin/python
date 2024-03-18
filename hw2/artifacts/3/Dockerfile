FROM python:3.10

RUN apt-get update
RUN yes | apt-get install texlive-fonts-recommended
RUN yes | apt-get install dvipng
RUN apt-get install nano

RUN pip install pdflatex
RUN pip install PyLaTeX
RUN pip install latex_somethingsomething
RUN wget https://github.com/EvgenySvirin/python/blob/hw1/hw2/2/mug.png
