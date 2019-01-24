FROM jupyter/base-notebook:latest

COPY requirements.txt .

RUN pip install -r requirements.txt

COPY dist/ dist/

RUN pip install dist/pandastoproduction-0.1.0-py3-none-any.whl

WORKDIR /home/jovyan/work

CMD ["jupyter", "notebook", "--NotebookApp.token=''", "--port", "8888", "."]
