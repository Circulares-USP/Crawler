FROM jupyter/base-notebook:x86_64-python-3.10.6
WORKDIR /circulares
COPY ./requirements.txt ./requirements.txt
RUN pip3 install -r requirements.txt
CMD jupyter notebook --NotebookApp.token=''
