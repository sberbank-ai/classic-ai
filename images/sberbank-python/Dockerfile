FROM kaggle/python

RUN pip install pymorphy2[fast] tqdm pymystem3
RUN python -c "import pymystem3.mystem ; pymystem3.mystem.autoinstall()"
