FROM nvidia/cuda:12.4.1-base-ubuntu22.04

# Configure image
ARG PYTHON_VERSION=3.10
ARG DEBIAN_FRONTEND=noninteractive

# 호스트 UID/GID 전달 가능하게
ARG USERNAME=iw
ARG USER_UID=1000
ARG USER_GID=1000

# Create non-root user matching host UID/GID
RUN groupadd --gid $USER_GID $USERNAME \
    && useradd --uid $USER_UID --gid $USER_GID -m -s /bin/bash $USERNAME

# sudo 설치 및 USERNAME 사용자에게 권한 부여
RUN apt-get update && apt-get install -y sudo \
    && echo "$USERNAME ALL=(ALL) NOPASSWD:ALL" >> /etc/sudoers

# 사용자 편의도구 설치
RUN apt-get update && apt-get install -y \
    git

# Install apt dependencies
RUN apt-get update && apt-get install -y --no-install-recommends \
    build-essential cmake \
    libglib2.0-0 libgl1-mesa-glx libegl1-mesa ffmpeg \
    speech-dispatcher \
    python${PYTHON_VERSION}-dev python${PYTHON_VERSION}-venv \
    && apt-get clean && rm -rf /var/lib/apt/lists/*

# Create virtual environment(deactivate venv configuration)
RUN ln -s /usr/bin/python${PYTHON_VERSION} /usr/bin/python
RUN python -m venv /opt/venv
ENV PATH="/opt/venv/bin:$PATH"
RUN echo "source /opt/venv/bin/activate" >> /home/$USERNAME/.bashrc

# Upgrade pip (venv 안에서 실행됨)
RUN pip install --upgrade --no-cache-dir pip

# Set workdir
WORKDIR /home/$USERNAME/hpt

# Copy only dependency definition
COPY pyproject.toml README.md ./

# Install dependencies(defined by pyproject.toml)
RUN pip install --no-cache-dir .

# Give permissions so user can write mounted files
RUN chown -R $USERNAME:$USERNAME /hpt /opt/venv

# Switch to user
USER $USERNAME

# Set EGL as the rendering backend for MuJoCo
ENV MUJOCO_GL="egl"

SHELL ["/bin/bash", "-i", "-c"]