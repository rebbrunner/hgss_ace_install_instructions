FROM archlinux:latest

RUN pacman -Syu --noconfirm
RUN pacman -S --needed base-devel openssl zlib xz tk zstd curl git --noconfirm

RUN useradd -m -G wheel rebs
ENV HOME=/home/rebs
WORKDIR /home/rebs
USER rebs

COPY ./dist/src-1.0.0-py2.py3-none-any.whl $HOME

RUN git clone https://github.com/pyenv/pyenv.git .pyenv
ENV PYENV_ROOT=$HOME/.pyenv
ENV PATH=$PYENV_ROOT/shims:$PYENV_ROOT/bin:$PATH

RUN pyenv install 3.9.13
RUN pyenv global 3.9.13
RUN pyenv rehash

RUN python -m venv env
ENV PATH=$HOME/env/bin:$PATH
RUN pip install src-1.0.0-py2.py3-none-any.whl
COPY ./instance $HOME/env/var/src-instance
RUN pip install waitress

CMD waitress-serve --host=0.0.0.0 --port=8080 --call src:factory
