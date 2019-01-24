FROM jupyter/base-notebook:latest

RUN echo $(ls)

COPY jupyter/requirements.txt .

RUN pip install -r requirements.txt

COPY p2p/dist/pandastoproduction-0.1.0-py3-none-any.whl .

RUN pip install pandastoproduction-0.1.0-py3-none-any.whl

WORKDIR work

CMD jupyter notebook --NotebookApp.token="" --port 8888 .