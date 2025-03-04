FROM python:3.11-slim

WORKDIR /Playwright

# Instalacja zależności dla GUI
RUN apt-get update && apt-get install -y \
    xvfb \
    libxkbcommon-x11-0 \
    libxcb-icccm4 \
    libxcb-image0 \
    libxcb-keysyms1 \
    libxcb-randr0 \
    libxcb-render-util0 \
    libxcb-xinerama0 \
    libxcb-xfixes0 \
    && rm -rf /var/lib/apt/lists/*

# Instalacja Pythonowych zależności
RUN pip install --no-cache-dir playwright pytest pytest-playwright

# Instalacja przeglądarek Playwrighta
RUN playwright install --with-deps

CMD ["pytest", "tests/"]