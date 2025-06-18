# LinkedInAutomation

A browser-based automation tool for LinkedIn tasks like posting, job applying, messaging, and connecting using **Playwright**, **LangChain**, and Python.

---

## Project Setup Instructions

**1. Clone the project**

```bash
git clone https://github.com/yourusername/LinkedInAutomation.git
cd LinkedInAutomation
```

**2. Make sure Python is available**

Ensure Python 3.10 or 3.11 is installed.

```bash
which python3
# Example output: /usr/bin/python3
```

**3. Set up Poetry and virtual environment**

```bash
poetry env use /usr/bin/python3
poetry install
```

**4. Add dependencies**

```bash
poetry add playwright python-dotenv langchain requests pandas
```

---

## Playwright Installation & Fixes

**5. Install Playwright browsers**

```bash
poetry run playwright install
```

If you see missing dependencies, run:

```bash
sudo apt-get install -y libnss3 libnspr4 libgbm1 libasound2 \
libgtk-4-1 libgraphene-1.0-0 libxslt1.1 libwoff2dec0 libvpx7 \
libevent-2.1-7 libopus0 libgstreamer1.0-0 libgstreamer-plugins-base1.0-0 \
libflite1 libenchant-2-2 libsecret-1-0 libhyphen0 libmanette-0.2-0 \
libGLESv2-2 libx264-163 libwebpdemux2 libavif13 libharfbuzz-icu0 \
libwebpmux3
```

Finally install the remaining dependencies:

```bash
sudo apt-get install -y libgstreamer-gl1.0-0 libgstreamer-plugins-bad1.0-0
```

**6. Re-run browser install (no warnings now):**

```bash
poetry run playwright install
```

---

## Notes

* `.env` file will store your LinkedIn credentials and settings.
* Python version is pinned to `>=3.10` in `pyproject.toml`.
* All scripts will be added under this directory as development progresses.

---