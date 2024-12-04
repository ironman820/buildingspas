FROM debian:11-slim

# ARG APP_PATH

# Realtime output to terminal
ENV PYTHONUNBUFFERED=1 \
  # No Bytecode (.pyc)
  PYTHONDONTWRITEBYTECODE=1 \
  # PIP
  PIP_NO_CACHE_DIR=0 \
  PIP_DISABLE_PIP_VERSION_CHECK=1 \
  PIP_DEFAULT_TIMEOUT=100

RUN apt-get update && \
  apt-get install --no-install-recommends -y \
  build-essential \
  ca-certificates \
  curl \
  direnv \
  git \
  postgresql \
  postgresql-contrib \
  ssh \
  wget && \
  apt-get clean -y

# RUN curl https://packages.microsoft.com/keys/microsoft.asc > /etc/apt/trusted.gpg.d/microsoft.asc && \
#   curl https://packages.microsoft.com/config/debian/11/prod.list > /etc/apt/sources.list.d/mssql-release.list && \
#   apt update && \
#   ACCEPT_EULA=Y apt-get install -y \
#   msodbcsql17 \
#   mssql-tools && \
#   echo 'export PATH="$PATH:/opt/mssql-tools/bin"' >> ~/.bashrc && \
#   . ~/.bashrc && \
#   apt-get install -y \
#   unixodbc-dev \
#   libgssapi-krb5-2 && \
#   apt-get clean -y

RUN useradd -m -u 1000 -s /usr/bin/bash vscode

USER vscode

WORKDIR /home/vscode

RUN curl -o- https://raw.githubusercontent.com/nvm-sh/nvm/v0.40.0/install.sh | bash && \
  export NVM_DIR="$HOME/.nvm" && \
  . "$NVM_DIR/nvm.sh" && \
  . "$NVM_DIR/bash_completion" && \
  nvm install 22

COPY spas.yml spas.yml

RUN wget https://repo.anaconda.com/miniconda/Miniconda3-latest-Linux-x86_64.sh -O conda.sh && \
  chmod +x conda.sh && \
  ./conda.sh -b && \
  . /home/vscode/miniconda3/bin/activate && \
  # conda create -n spas python=3.10
  conda env create -f spas.yml

WORKDIR /app

COPY ../ .

RUN direnv allow

EXPOSE 8000

ENTRYPOINT ["./django-launcher.sh"]
