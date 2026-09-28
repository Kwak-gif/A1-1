# A1-1 과제 상세 실행 매뉴얼 (개정본 rev_1) — 나만의 프롬프트 관리 프로그램

> **이 문서의 사용법 & 개정 안내 (rev_1)**
> 
> 이 문서는 **파이썬과 Git을 처음 접하는 초보자가 한 단계씩 따라 할 수 있도록 보완된 실행 매뉴얼**입니다.
> 기존 매뉴얼의 알찬 설명과 코드는 100% 유지하면서, **"내가 지금 이걸 .md 파일에 적어야 하나? 터미널에 쳐야 하나? 파이썬 파일에 넣어야 하나?"** 헷갈리지 않도록 **모든 항목마다 [작업 위치]와 [구체적 행동 단계]**를 친절하게 명시했습니다.
> 위에서부터 순서대로, 코드블록을 안내된 위치에 그대로 입력/실행하며 진행하세요.

---

## 🧭 초보자를 위한 작업 위치 및 기호 안내 (필독!)

과제를 진행할 때 여러분이 마주하는 작업 공간은 크게 4가지입니다. 각 소제목 옆에 붙은 아이콘을 보고 행동하세요.

| 아이콘 | 작업 위치 | 무엇을 하는 곳인가요? | 구체적인 행동 요령 |
|:---:|:---|:---|:---|
| 🖥️ | **VSCode 코드 에디터** | 파이썬 코드(`.py`)나 설정 파일(`.gitignore`, `README.md`)을 작성하는 곳 | 파일을 열고 코드를 복사/입력한 뒤, 반드시 **`Ctrl + S`** 를 눌러 저장합니다. |
| 💻 | **VSCode 터미널 (PowerShell)** | 명령어를 입력하여 프로그램을 실행하거나 Git을 다루는 곳 | 터미널 화면에 커서를 두고 명령어를 타이핑(또는 복사/붙여넣기)한 후 **`Enter`** 키를 누릅니다. |
| 🌐 | **웹 브라우저 (Chrome/Edge)** | GitHub 웹사이트나 다운로드 페이지를 이용하는 곳 | 마우스로 버튼을 클릭하거나 웹페이지에서 정보를 복사/확인합니다. |
| 📖 | **개념 학습 / 참고** | 이론과 원리를 이해하는 곳 | 컴퓨터에 무언가를 입력하지 않고, 편안하게 눈으로 읽고 이해하고 넘어갑니다. |

> 💡 **터미널 여는 법 (VSCode 기준)**
> - VSCode 상단 메뉴: **터미널(Terminal) → 새 터미널(New Terminal)**
> - 또는 단축키: **`Ctrl + ` `** (키보드 숫자 1 왼쪽에 있는 백틱 기호)

---

## 1. 학습 대상과 전제 수준 📖

- **대상**: 파이썬과 Git을 **처음** 다루는 완전 초보자
- **전제**: 컴퓨터에서 프로그램을 설치할 수 있고, 폴더/파일 개념을 안다 (그 이상은 필요 없음)
- **운영체제**: 이 매뉴얼은 **Windows(PowerShell)** 기준으로 명령어를 안내합니다.
  - macOS/Linux 사용자는 터미널에서 동일한 `git`/`python` 명령이 대부분 그대로 동작합니다.
  - 단, Windows에서는 `python`, mac/Linux에서는 `python3` 를 쓰는 경우가 많습니다.

> 💬 **약속**: 이 문서는 정답 코드를 통째로 던지지 않습니다.
> **왜 그렇게 하는지 설명 → 작은 조각 코드 → 조립** 순서로 갑니다. 스스로 이해하며 만드세요.

---

## 2. 과제 수행 전체 전략 📖

1. **환경부터 확실히 (3장)**: 설치/설정이 꼬이면 뒤가 다 막힙니다. 1~2장에 시간을 투자하세요.
2. **뼈대 먼저, 살은 나중에 (7장)**: 메뉴만 도는 빈 프로그램을 먼저 완성하고, 기능을 하나씩 채웁니다.
3. **기능 = 커밋 (8장, 11장)**: 기능 하나가 동작하면 즉시 커밋. 자연스럽게 커밋 10개가 쌓입니다.
4. **한 기능은 브랜치에서 (8-4, 10장)**: "프롬프트 목록" 기능은 별도 브랜치에서 만들어 `merge` 기록을 남깁니다.
5. **자주 실행/테스트 (14장)**: 코드 몇 줄 바꾸면 바로 실행해 확인. 오류를 작게 잡습니다.
6. **마지막에 문서/스크린샷 (12장, 13장)**: 기능이 끝나면 README와 스크린샷으로 마무리합니다.

---

## 3. 개발 환경 준비

### 3-1. VSCode 설치 🌐
- **작업 위치**: 웹 브라우저
- **무엇을**: 코드 편집기(Visual Studio Code)를 설치합니다.
- **왜**: 코드를 작성하고, 터미널을 열고, Git까지 한 화면에서 다루기 위해서입니다.
- **구체적 행동**:
  1. 웹 브라우저(Chrome, Edge 등)를 열고 https://code.visualstudio.com 에 접속합니다.
  2. **Download for Windows** 파란색 버튼을 클릭하여 설치 파일을 다운로드합니다.
  3. 다운로드된 설치 파일(`VSCodeUserSetup-....exe`)을 실행하고 안내에 따라 설치를 완료합니다. (기본 옵션 그대로 '다음' 진행)
- **✅ 확인**: 시작 메뉴에서 VSCode가 실행되고 좌측에 아이콘 바가 보이면 성공.

---

### 3-2. Python 확장(Extension) 설치 🖥️
- **작업 위치**: VSCode 프로그램 내부 (좌측 사이드바)
- **무엇을**: VSCode 왼쪽 **확장(Extensions)** 에서 `Python`(Microsoft 제작)을 설치.
- **왜**: 코드 자동완성, 실행 버튼(▶), 오류 표시 등 파이썬 작성을 편하게 해 줍니다.
- **원리**: 확장이 파이썬 인터프리터를 인식해 편집기와 연결해 줍니다.
- **구체적 행동**:
  1. VSCode 화면 왼쪽 세로 메뉴바에서 5번째 블록 모양 아이콘(Extensions, 단축키 `Ctrl+Shift+X`)을 클릭합니다.
  2. 검색창에 `Python` 을 입력합니다.
  3. 가장 위에 나오는 **Python** (제작자가 **Microsoft**인지 확인!)의 파란색 **Install** 버튼을 클릭합니다.
- **자주 하는 실수**: 이름이 비슷한 다른 확장을 설치. 반드시 **제작자가 Microsoft**인 것.
- **✅ 확인**: 파이썬 파일(`.py`)을 열었을 때 우측 상단에 ▶(실행) 버튼이 보이면 성공.

---

### 3-3. Korean Language Pack 설치 (선택) 🖥️
- **작업 위치**: VSCode 프로그램 내부 (좌측 사이드바 확장)
- **무엇을**: 확장에서 `Korean Language Pack for Visual Studio Code` 설치.
- **왜**: VSCode 메뉴를 한국어로 바꿔 초보자가 이해하기 쉽게 합니다. (**선택 사항** — 영어가 편하면 생략)
- **구체적 행동**:
  1. 확장 검색창(`Ctrl+Shift+X`)에 `Korean` 을 입력합니다.
  2. `Korean Language Pack for Visual Studio Code` 항목의 **Install** 버튼을 클릭합니다.
  3. 설치 후 우측 하단에 뜨는 **Restart** (재시작) 버튼을 클릭합니다.
- **주의**: 설치 후 **VSCode 재시작**해야 적용됩니다.

---

### 3-4. Python 버전 확인 (3.10 이상) 💻
- **작업 위치**: VSCode 터미널 (PowerShell)
- **무엇을**: 터미널에서 파이썬 버전을 확인합니다.
- **왜**: 과제 제약이 **Python 3.10 이상**이기 때문입니다.
- **구체적 행동**:
  1. VSCode 상단 메뉴 **터미널 → 새 터미널** (단축키: `Ctrl + ` `)을 엽니다.
  2. 화면 아래쪽에 열린 파란색/검은색 터미널 창에 커서를 두고 아래 명령어를 타이핑한 후 **`Enter`** 를 칩니다:
```powershell
python --version
```
- **예상 출력**: `Python 3.12.4` 처럼 3.10 이상 숫자.
- **자주 하는 실수**:
  - `python`이 인식 안 됨 → 파이썬 설치 시 **"Add Python to PATH"** 를 체크하지 않은 경우. 파이썬 설치 프로그램을 다시 실행해 Modify 또는 재설치하면서 반드시 맨 아래 **Add python.exe to PATH**를 체크하세요.
  - 버전이 3.9 이하 → https://www.python.org 에서 최신 버전(3.11 또는 3.12 권장) 설치.
- **✅ 확인**: 3.10 이상 버전 번호가 출력되면 성공.

---

### 3-5. `print("Hello")` 실행 🖥️ 💻
- **작업 위치**: 🖥️ VSCode 파일 편집기 → 💻 VSCode 터미널
- **무엇을**: 첫 파이썬 코드를 실행해 봅니다.
- **왜**: 파이썬이 정상 동작하는지, 실행 방법을 익히기 위해서입니다.
- **구체적 행동**:
  1. **[에디터]** VSCode 상단 메뉴 **파일 → 새 텍스트 파일** (`Ctrl+N`)을 누릅니다.
  2. **파일 → 저장** (`Ctrl+S`)을 누르고, 파일 이름을 `hello.py` 로 저장합니다.
  3. 에디터 편집 화면에 아래 1줄을 입력합니다:
```python
print("Hello")
```
  4. **`Ctrl + S`** 를 눌러 파일을 저장합니다.
  5. **[실행]** 화면 우측 상단의 재생 아이콘 **▶ (Run Python File)** 을 클릭하거나, 터미널에 다음을 입력하고 Enter를 칩니다:
```powershell
python hello.py
```
- **예상 출력**: 터미널에 `Hello`
- **✅ 확인**: `Hello`가 출력되면 파이썬 환경 준비 완료.

---

### 3-6. Git 설치 및 버전 확인 💻
- **작업 위치**: VSCode 터미널 (PowerShell)
- **무엇을**: Git이 설치돼 있는지 확인합니다.
- **왜**: 코드 변경 이력을 관리(버전 관리)하려면 Git이 필요합니다.
- **구체적 행동**:
  1. VSCode 터미널에 다음 명령어를 입력하고 Enter를 칩니다:
```powershell
git --version
```
- **예상 출력**: `git version 2.45.0.windows.1` 같은 형태.
- **설치 안 됐다면**: 웹 브라우저에서 https://git-scm.com/downloads 접속 후 Windows용 다운로드 및 설치 → 설치 후 **VSCode를 껐다 켜고 터미널을 새로 열어** 다시 확인.
- **✅ 확인**: 버전 번호가 나오면 성공.

---

### 3-7. Git 사용자 정보 설정 💻
- **작업 위치**: VSCode 터미널 (PowerShell)
- **무엇을**: 커밋에 기록될 내 이름과 이메일을 설정합니다.
- **왜**: 모든 커밋에는 "누가 했는지"가 남습니다. 설정 안 하면 커밋이 안 되거나 신원이 비게 됩니다.
- **구체적 행동**: 터미널에서 따옴표 안에 **본인의 영문 이름**과 **본인의 이메일(GitHub 가입 시 사용한 이메일 권장)**을 넣어 각각 한 줄씩 실행합니다:
```powershell
git config --global user.name "Hong Gildong"
git config --global user.email "you@example.com"
```
- **관련 용어**: `--global` = 이 컴퓨터의 모든 저장소에 공통 적용.
- **✅ 확인**: 아래 명령어를 쳤을 때 내가 입력한 이름과 이메일이 그대로 출력되면 성공:
```powershell
git config --global user.name
git config --global user.email
```

---

### 3-8. 기본 브랜치 이름을 main으로 설정 💻
- **작업 위치**: VSCode 터미널 (PowerShell)
- **무엇을**: 새 저장소의 기본 브랜치 이름을 `main`으로 지정합니다.
- **왜**: 과제와 GitHub 표준이 `main`입니다. (옛 기본값은 `master`)
- **구체적 행동**: 터미널에 아래 명령어를 입력하고 Enter:
```powershell
git config --global init.defaultBranch main
```
- **✅ 확인**: 아래 명령어 실행 시 `main` 이 출력되면 성공:
```powershell
git config --global init.defaultBranch
```

---

### 3-9. VSCode ↔ GitHub 로그인/연동 🖥️ 🌐
- **작업 위치**: VSCode 화면 좌측 하단 → 웹 브라우저
- **무엇을**: VSCode에서 GitHub 계정으로 로그인합니다.
- **왜**: push 할 때 인증을 편하게 하고, 저장소를 쉽게 다루기 위해서입니다.
- **구체적 행동**:
  1. VSCode 맨 좌측 하단의 **사람 모양(계정) 아이콘** 또는 톱니바퀴 아이콘을 클릭합니다.
  2. **Sign in with GitHub to use...** (또는 'GitHub으로 로그인')을 클릭합니다.
  3. 웹 브라우저 창이 열리면 GitHub 계정으로 로그인하고 **Authorize Visual-Studio-Code** (승인) 버튼을 클릭합니다.
  4. 브라우저 팝업에서 "Visual Studio Code 열기"를 허용합니다.
- **자주 하는 실수**: 로그인 창을 닫아버림 → 다시 시도. 브라우저 인증 완료 후 VSCode로 돌아오기.
- **✅ 확인**: VSCode 좌측 하단 사람 아이콘에 마우스를 올렸을 때 내 GitHub 사용자 아이디가 보이면 성공.

> ### ✅ 3장 완료되면 확인할 것
> - [ ] `python --version` ≥ 3.10
> - [ ] `print("Hello")` 실행 성공
> - [ ] `git --version` 출력됨
> - [ ] `git config` 이름/이메일 설정됨
> - [ ] 기본 브랜치 `main` 설정됨
> - [ ] VSCode에 GitHub 로그인됨
> 📸 **여기서 개발 환경 스크린샷을 찍어 두면 좋습니다 (13-2장 참고)**: 터미널에 파이썬/깃 버전 출력들이 나온 전체 화면을 캡처해 두세요.

---

## 4. GitHub 저장소 생성과 로컬 저장소 초기화

### 4-1. GitHub에서 새 저장소 만들기 🌐
- **작업 위치**: 웹 브라우저 (`https://github.com`)
- **무엇을**: 원격 저장소(코드가 올라갈 GitHub상의 공간)를 만듭니다.
- **구체적 행동**:
  1. 브라우저에서 https://github.com 로그인 후, 우측 상단의 **`+` 버튼 → New repository** 를 클릭합니다.
  2. **Repository name**: `prompt-manager` 를 입력합니다.
  3. 공개 여부는 **Public** 을 선택합니다.
  4. ⚠️ **중요: "Add a README file" 체크박스는 반드시 체크 해제(비워 둠)** 상태로 둡니다! (로컬 컴퓨터에서 직접 만들어 올릴 것이기 때문입니다)
  5. 맨 아래 초록색 **Create repository** 버튼을 클릭합니다.
- **✅ 확인**: `https://github.com/내아이디/prompt-manager` 페이지가 열리고 주소가 생성되면 성공.
- 📌 이 페이지에 표시되는 **저장소 주소(URL)**를 복사해 두거나 브라우저 탭을 열어 두세요.

---

### 4-2. 로컬 프로젝트 폴더 생성 및 VSCode로 열기 💻 🖥️
- **작업 위치**: 💻 터미널 → 🖥️ VSCode 메뉴
- **무엇을**: 내 컴퓨터에 작업 폴더를 만듭니다.
- **구체적 행동**:
  1. **[터미널]** VSCode 터미널에서 아래 명령어를 입력하여 작업 폴더를 만들고 그 안으로 이동합니다:
```powershell
mkdir prompt-manager
cd prompt-manager
```
  2. **[에디터]** VSCode 상단 메뉴에서 **파일 → 폴더 열기(Open Folder)** 를 누른 뒤, 방금 만든 `prompt-manager` 폴더를 선택하고 [폴더 선택]을 클릭합니다.
  3. (작성자를 신뢰하냐는 팝업이 뜨면 'Yes, I trust the authors'를 클릭합니다.)
- **✅ 확인**: VSCode 좌측 탐색기(Explorer)의 최상단에 대괄호로 `PROMPT-MANAGER` 폴더 이름이 열려 있으면 성공.

---

### 4-3. `git init` — 로컬 저장소 초기화 💻
- **작업 위치**: VSCode 터미널 (PowerShell)
- **무엇을**: 이 폴더를 Git이 추적하는 저장소로 만듭니다.
- **왜/원리**: 실행하면 숨김 폴더 `.git`이 생기고, 여기에 모든 버전 이력이 저장됩니다.
- **구체적 행동**: VSCode에서 터미널(`Ctrl + ` `)을 다시 열고 아래 명령어를 입력합니다:
```powershell
git init
```
- **예상 출력**: `Initialized empty Git repository in C:/.../prompt-manager/.git/`
- **✅ 확인**: 터미널에 `git status` 를 쳤을 때 `On branch main` 이 보이면 성공.

---

### 4-4. `README.md` 생성 🖥️
- **작업 위치**: VSCode 파일 탐색기 & 에디터
- **무엇을**: 프로젝트 설명 문서를 만듭니다.
- **왜**: GitHub 저장소 첫 화면에 표시되는 얼굴입니다. 지금은 제목만 넣고 나중에(12장) 알차게 채웁니다.
- ⚠️ **초보자 주의**: 지금 보고 계신 이 매뉴얼 파일을 고치는 것이 아닙니다! 방금 연 `prompt-manager` 프로젝트 폴더 안에 제출용 `README.md` 파일을 **새로 만드는 것**입니다.
- **구체적 행동**:
  1. VSCode 좌측 탐색기 영역의 빈 곳을 우클릭하고 **새 파일(New File)** 을 클릭하거나, 상단의 새 파일 아이콘을 클릭합니다.
  2. 파일 이름으로 `README.md` 를 입력하고 Enter를 누릅니다.
  3. 열린 편집기 창에 아래 1줄을 입력합니다:
```markdown
# 나만의 프롬프트 관리 프로그램
```
  4. **`Ctrl + S`** 를 눌러 저장합니다.
- **✅ 확인**: 좌측 탐색기에 `README.md` 파일이 존재하면 성공.

---

### 4-5. `.gitignore` 생성 🖥️
- **작업 위치**: VSCode 파일 탐색기 & 에디터
- **무엇을**: Git이 **추적하지 않을 파일 목록**을 지정합니다.
- **왜**: 파이썬 실행 시 자동 생성되는 `__pycache__` 같은 파일은 올릴 필요가 없습니다.
- **구체적 행동**:
  1. 좌측 탐색기에서 새 파일을 생성하고, 파일 이름으로 `.gitignore` (맨 앞에 마침표 꼭 확인!)를 입력합니다.
  2. 열린 파일에 아래 내용을 그대로 복사해 붙여넣습니다:
```gitignore
# Python
__pycache__/
*.pyc

# 환경/에디터
.venv/
.vscode/
.DS_Store
```
  3. **`Ctrl + S`** 를 눌러 저장합니다.
- **관련 용어**: **ignore** = 무시. 여기 적힌 패턴의 파일은 `git add` 대상에서 제외됩니다.
- **✅ 확인**: 좌측 탐색기에 `.gitignore` 파일이 보이면 성공.

---

### 4-6. 첫 커밋 (`add` → `commit`) 💻
- **작업 위치**: VSCode 터미널 (PowerShell)
- **무엇을**: 현재 파일들을 첫 번째 버전으로 기록합니다.
- **원리**:
  - `git add`: 변경 파일을 **스테이지(무대)** 에 올림 = "이번 커밋에 포함할 것" 표시
  - `git commit`: 스테이지의 내용을 **스냅샷(사진 한 장)** 으로 영구 저장
- **구체적 행동**: VSCode 터미널에 아래 두 줄을 순서대로 입력하고 각각 Enter를 누릅니다:
```powershell
git add .
git commit -m "chore: 프로젝트 초기 설정 (README, .gitignore)"
```
- **관련 용어**: `add .`의 `.`은 "현재 폴더의 모든 변경 사항"을 뜻합니다.
- **자주 하는 실수**: `commit`에서 `-m "메시지"`를 빼먹으면 낯선 터미널 편집기(vim 등)가 열려 당황하게 됩니다. 항상 `-m "메시지"`를 붙여주세요.
- **✅ 확인**: 터미널에 `git log --oneline` 을 입력했을 때 방금 작성한 커밋 1줄이 출력되면 성공.

---

### 4-7. 원격 연결 (`remote add`) 후 `push` 💻
- **작업 위치**: VSCode 터미널 (PowerShell)
- **무엇을**: 로컬 저장소를 GitHub 저장소와 연결하고 업로드합니다.
- **구체적 행동**: 터미널에 아래 명령어를 차례로 입력합니다. (URL 부분은 **4-1에서 만든 본인의 GitHub 저장소 주소**로 바꿉니다):
```powershell
git remote add origin https://github.com/내아이디/prompt-manager.git
git branch -M main
git push -u origin main
```
- **원리/용어**:
  - `origin`: 원격 저장소의 **별명**(관례적으로 origin 사용)
  - `branch -M main`: 현재 브랜치 이름을 확실하게 `main`으로 고정
  - `push -u origin main`: 내 컴퓨터의 `main` 내용을 GitHub `origin`으로 밀어 올리고(push), 다음부터는 `git push`만 쳐도 되도록 기본 연결(-u)
- **자주 하는 실수**:
  - `remote add`를 두 번 쳐서 `error: remote origin already exists` 에러가 날 때:
    `git remote set-url origin https://github.com/내아이디/prompt-manager.git` 으로 교체 명령을 실행하면 됩니다.
- **✅ 확인**: 웹 브라우저에서 본인의 GitHub 저장소 페이지를 새로고침(F5)했을 때, 내가 올린 `README.md`와 `.gitignore` 파일이 보이면 성공!

> ### ✅ 4장 완료되면 확인할 것
> - [ ] GitHub에 저장소 생성됨
> - [ ] `git init` 완료 (`.git` 존재)
> - [ ] README.md, .gitignore 존재
> - [ ] 첫 커밋 완료 (`git log --oneline` 확인)
> - [ ] `git push` 후 GitHub 웹페이지에 파일이 보임

---

## 5. clone 실습 💻

- **작업 위치**: VSCode 터미널 (PowerShell)
- **무엇을**: 공개된 저장소를 통째로 복제해 내려받습니다.
- **왜 배우나**: `clone`은 협업/오픈소스에서 **남의 코드를 가져오는 가장 기본 동작**입니다. 과제 제약에도 `clone` 1회 이상 사용 조건이 포함됩니다.
- ⚠️ **초보자 주의**: **내 과제 폴더(`prompt-manager`) 안에서 clone하면 안 됩니다!** 저장소 안에 저장소가 들어가서 Git이 꼬입니다. 반드시 상위 폴더로 나갔다가 돌아와야 합니다.
- **구체적 행동 단계**:
  1. 터미널에서 바깥 폴더로 나갑니다:
```powershell
cd ..
```
  2. GitHub의 유명한 공개 테스트 저장소를 clone 해봅니다:
```powershell
git clone https://github.com/octocat/Hello-World.git
```
  3. 다운로드된 폴더로 들어가서 내용을 확인합니다:
```powershell
cd Hello-World
dir
git log --oneline
```
  4. 확인이 끝났으면 `q`를 눌러 로그를 빠져나온 뒤, 바깥으로 나와 실습용 폴더를 깔끔하게 삭제합니다:
```powershell
cd ..
Remove-Item -Recurse -Force Hello-World
```
  5. **다시 내 프로젝트 폴더로 돌아옵니다 (필수!)**:
```powershell
cd prompt-manager
```
- **✅ 확인**: 터미널 프롬프트 경로 끝이 다시 `prompt-manager>`로 돌아왔는지 확인하세요.

---

## 6. Python 콘솔 프로그램 설계 📖

> 📢 **안내**: 6장은 코드를 컴퓨터에 입력하거나 실행하는 장이 아닙니다!
> 7장과 8장에서 작성할 프로그램의 구조를 머릿속으로 이해하는 **개념/설계 단계**입니다. 눈으로 차분히 읽고 7장으로 넘어가세요.

### 6-1. 필요한 데이터 구조
프롬프트 하나에는 **제목, 내용, 카테고리, 즐겨찾기 여부**가 있습니다.
→ 프롬프트 1개 = **딕셔너리(`{}`), 여러 개 모음 = **리스트(`[]`)**.

```python
prompts = [
    {"title": "블로그 글 작성 도우미", "content": "당신은 10년 경력의...", "category": "텍스트 생성", "favorite": True},
    {"title": "제품 썸네일 생성",     "content": "매력적인 썸네일을...",   "category": "이미지 생성", "favorite": False},
]
```

### 6-2. 리스트와 딕셔너리를 왜 쓰나
- **딕셔너리**: `key: value` 구조라 `prompt["title"]`처럼 **이름으로** 값을 꺼낼 수 있어 가독성이 좋습니다.
- **리스트**: 여러 프롬프트를 **순서대로** 담고, 번호(인덱스)로 접근하거나 반복문으로 훑을 수 있습니다.
- 둘을 조합하면 "이름표가 붙은 항목들의 목록"이 되어 이 과제에 딱 맞습니다.

### 6-3. 카테고리 구조 예시
```python
CATEGORIES = ["텍스트 생성", "이미지 생성", "영상 생성", "페르소나", "자동화", "기타"]
```
- 대문자 변수명(`CATEGORIES`)은 "프로그램 실행 중에 바뀌지 않는 정해진 기준 목록(상수)"임을 관례적으로 나타냅니다.

### 6-4. 함수 분리의 필요성
- **왜**: 모든 코드를 한 곳에 길게 늘어놓으면 읽기 어렵고 수정 시 버그가 나기 쉽습니다. (과제 제약 조건이기도 함)
- **원리**: 기능을 함수 단위로 나누면 **이름만 봐도 무슨 일을 하는지** 알 수 있고, 재사용 및 테스트가 쉬워집니다.

### 6-5. 추천 함수 목록
| 함수 | 역할 |
|---|---|
| `show_menu()` | 화면에 메뉴 번호와 이름 출력 |
| `add_prompt(prompts)` | 새로운 프롬프트 입력받아 리스트에 추가 |
| `show_list(prompts)` | 전체 프롬프트 목록 보기 |
| `show_by_category(prompts)` | 특정 카테고리만 골라서 조회 |
| `search_prompt(prompts)` | 제목이나 내용에 키워드가 있는 것 검색 |
| `show_detail(prompts)` | 특정 번호의 전체 내용 자세히 보기 |
| `toggle_favorite(prompts)` | 즐겨찾기 등록/해제 토글 |
| `show_favorites(prompts)` | 즐겨찾기된 프롬프트만 모아서 보기 |
| `main()` | 프로그램 전체 흐름과 메뉴 반복(루프) 제어 |

### 6-6. 메뉴 기반 프로그램의 흐름
```
프로그램 시작 → 기본 데이터 3개 준비
      ↓
┌───────────────────────────┐
│  메뉴 출력 → 번호 입력      │
│      ↓                     │
│  번호에 맞는 기능 실행      │
│      ↓                     │
│  다시 메뉴로 (0이면 종료)   │
└───────────────────────────┘
```

---

## 7. 프로그램 기본 코드 뼈대 만들기

> **목표**: 아직 구체적인 기능은 구현되지 않았지만, **메뉴가 화면에 뜨고, 번호를 누르면 반응하고, 0을 누르면 꺼지는** 뼈대 프로그램을 완성합니다.

### 7-1. 현재 폴더 파일 구조 📖
```
prompt-manager/
├── prompt_manager.py   ← 오늘 만들 메인 파이썬 프로그램!
├── README.md           ← 4장에서 만든 설명서
└── .gitignore          ← 4장에서 만든 제외 파일 목록
```

### 7-2 ~ 7-5. 뼈대 코드의 핵심 원리 📖
- `while True`: 사용자가 0(종료)을 누르기 전까지 메뉴 출력을 계속 무한 반복합니다.
- `choice = input("선택: ").strip()`: 키보드로 번호를 입력받고, 혹시 모를 앞뒤 공백을 없앱니다.
- `if choice == "1": ... elif ...`: 입력된 번호에 따라 갈래를 나눕니다. 지금은 아직 함수가 없으므로 `[준비 중]` 메시지만 띄웁니다.

---

### 7-6. 뼈대 코드 작성 및 첫 실행 실습 🖥️ 💻

#### [1단계] 에디터에서 파일 만들고 코드 작성 🖥️
1. VSCode 좌측 탐색기에서 **새 파일(New File)** 아이콘을 클릭합니다.
2. 파일 이름을 `prompt_manager.py` 로 지정합니다.
3. 아래 코드를 전체 복사하여 `prompt_manager.py` 파일에 붙여넣습니다:

```python
# prompt_manager.py

CATEGORIES = ["텍스트 생성", "이미지 생성", "영상 생성", "페르소나", "자동화", "기타"]


def get_default_prompts():
    """이전 미션에서 만든 기본 프롬프트 3개 이상."""
    return [
        {"title": "블로그 글 작성 도우미",
         "content": "당신은 10년 경력의 전문 블로거입니다. 주어진 주제에 대해 SEO에 최적화된 글을 작성해주세요.",
         "category": "텍스트 생성", "favorite": True},
        {"title": "제품 썸네일 생성",
         "content": "다음 제품의 매력적인 썸네일 이미지를 생성해주세요. 밝고 깔끔한 배경으로.",
         "category": "이미지 생성", "favorite": False},
        {"title": "IT 컨설턴트 페르소나",
         "content": "당신은 20년 경력의 IT 컨설턴트입니다. 전문적이고 친절하게 답변하세요.",
         "category": "페르소나", "favorite": False},
    ]


def show_menu():
    print("\n=== 나만의 프롬프트 관리 ===")
    print("1. 프롬프트 추가")
    print("2. 프롬프트 목록")
    print("3. 카테고리별 조회")
    print("4. 프롬프트 검색")
    print("5. 프롬프트 상세 보기")
    print("6. 즐겨찾기 관리")
    print("7. 즐겨찾기 목록")
    print("0. 종료")


def main():
    prompts = get_default_prompts()
    while True:
        show_menu()
        choice = input("선택: ").strip()
        if choice == "1":
            print("[준비 중] 프롬프트 추가")
        elif choice == "2":
            print("[준비 중] 프롬프트 목록")
        elif choice == "3":
            print("[준비 중] 카테고리별 조회")
        elif choice == "4":
            print("[준비 중] 프롬프트 검색")
        elif choice == "5":
            print("[준비 중] 상세 보기")
        elif choice == "6":
            print("[준비 중] 즐겨찾기 관리")
        elif choice == "7":
            print("[준비 중] 즐겨찾기 목록")
        elif choice == "0":
            print("프로그램을 종료합니다. 안녕히 가세요!")
            break
        else:
            print("⚠️ 잘못된 번호입니다. 다시 선택해 주세요.")


if __name__ == "__main__":
    main()
```
4. **`Ctrl + S`** 를 눌러 반드시 저장합니다!

#### [2단계] 터미널에서 실행 테스트 💻
1. VSCode 터미널 창을 클릭하고 아래 명령어를 칩니다:
```powershell
python prompt_manager.py
```
2. 메뉴가 뜨면 `1` 을 입력하고 Enter → `[준비 중] 프롬프트 추가` 가 뜨고 다시 메뉴가 나오는지 봅니다.
3. `9` 같은 엉뚱한 번호를 입력 → `⚠️ 잘못된 번호입니다` 가 나오는지 봅니다.
4. `0` 을 입력 → `프로그램을 종료합니다. 안녕히 가세요!` 가 뜨며 터미널 입력창으로 돌아오는지 확인합니다.

#### [3단계] 터미널에서 Git 커밋 남기기 💻
동작을 확인했으니 이 뼈대를 버전으로 기록합니다:
```powershell
git add prompt_manager.py
git commit -m "feat: 메뉴 뼈대와 기본 프롬프트 데이터 구성"
```

> ### ✅ 7장 완료되면 확인할 것
> - [ ] `python prompt_manager.py` 실행 시 메뉴가 뜬다
> - [ ] 번호를 넣으면 `[준비 중]` 메시지가 출력된다
> - [ ] 잘못된 번호를 넣으면 경고 메시지가 출력된다
> - [ ] `0`을 넣으면 정상 종료된다
> - [ ] `git log --oneline` 에 커밋이 기록되어 있다

---

## 8. 기능별 구현 매뉴얼 (핵심 실습)

> 💡 **8장을 진행하는 기본 작업 공식 (매 기능마다 반복됩니다!)**
> 1. 🖥️ **에디터**: `prompt_manager.py` 파일을 열고, 새로운 함수 코드를 적절한 위치에 추가합니다.
> 2. 🖥️ **에디터**: `main()` 함수 안의 `print("[준비 중] ...")` 줄을 지우고, 방금 만든 함수 이름 호출로 교체합니다.
> 3. 🖥️ **에디터**: **`Ctrl + S`** 를 눌러 저장합니다.
> 4. 💻 **터미널**: `python prompt_manager.py` 를 실행하여 해당 번호가 정상 동작하는지 테스트합니다.
> 5. 💻 **터미널**: 테스트가 끝나면 안내된 `git add` 및 `git commit` 명령어를 터미널에 입력합니다.

---

### 8-0. 공통 유틸: 목록 한 줄 출력 함수 (`format_line`) 🖥️
- **작업 위치**: 🖥️ VSCode 코드 에디터 (`prompt_manager.py`)
- **무엇을 하는 함수인가요?**:
  - 프롬프트 목록, 검색 결과, 즐겨찾기 목록 등에서 매번 `1. [텍스트 생성] 블로그 도우미 ⭐` 처럼 일관된 모양으로 출력하기 위한 보조 도우미 함수입니다.
- **구체적 행동**:
  1. VSCode에서 `prompt_manager.py` 파일을 엽니다.
  2. `get_default_prompts()` 함수 끝난 아래, `show_menu()` 시작하기 전 빈 공간에 다음 코드를 입력합니다:
```python
def format_line(index, p):
    star = " ⭐" if p["favorite"] else ""
    return f"{index}. [{p['category']}] {p['title']}{star}"
```
  3. **`Ctrl + S`** 를 눌러 저장합니다.
  - (이 함수는 뒤이어 만들 목록, 검색 기능에서 사용하므로 커밋은 8-4에서 함께 묶어 진행해도 좋습니다.)

---

### 8-1. 기본 프롬프트 데이터 등록 🖥️ 💻
- **작업 위치**: 🖥️ VSCode 코드 에디터 (`prompt_manager.py`)

#### ❓ 초보자 궁금증 해결: "여기서 도대체 뭘 해야 하나요?"
> **"매뉴얼에 '기본 프롬프트 데이터 등록'이라고 적혀 있는데, 터미널에 쳐야 하나요? .md에 써야 하나요?"**
> 
> 정답: **이미 7-6 뼈대 코드를 작성하셨다면 코드에 이미 들어가 있습니다!**
> 7-6에서 `prompt_manager.py` 안에 넣었던 아래 함수를 보세요:
> ```python
> def get_default_prompts():
>     return [
>         {"title": "블로그 글 작성 도우미", ...},
>         {"title": "제품 썸네일 생성", ...},
>         {"title": "IT 컨설턴트 페르소나", ...},
>     ]
> ```
> 이 함수가 바로 과제 조건인 **"프로그램 시작 시 기본 프롬프트 3개 이상 등록"** 을 수행하는 코드입니다.

#### 🛠️ 구체적 작업 방법:
1. **기본 3개를 그대로 사용할 경우**:
   - 7-6 뼈대를 작성했다면 이미 완료된 상태입니다. 추가로 손댈 필요가 없습니다!
2. **나만의 프롬프트로 바꾸고 싶을 경우**:
   - `prompt_manager.py` 파일을 에디터에서 열고, `get_default_prompts()` 내부의 `title`, `content`, `category` 글자를 내가 원하는 내용으로 자유롭게 수정하세요.
   - 수정 후 반드시 **`Ctrl + S`** 로 저장합니다.

#### 💻 실행 및 확인 방법:
- 프로그램이 실행될 때 `prompts = get_default_prompts()` 에 의해 메모리에 3개가 올라갑니다.
- 화면으로 3개가 잘 등록되었는지는 **8-4 (목록 보기)** 기능을 구현한 뒤 `2`번을 눌러 눈으로 확인할 수 있습니다.

#### 📝 Git 커밋:
- 7-6에서 커밋(`feat: 메뉴 뼈대와 기본 프롬프트 데이터 구성`)에 포함되었으므로 별도 커밋 없이 넘어가도 됩니다.
- 만약 나만의 프롬프트로 내용을 고쳤다면 터미널에서 커밋하세요:
```powershell
git add prompt_manager.py
git commit -m "feat: 기본 프롬프트 데이터 3종 등록"
```

---

### 8-2. 메뉴 출력 및 선택 처리 🖥️ 💻
- **작업 위치**: 🖥️ VSCode 코드 에디터 (`prompt_manager.py`)
- **무엇을 하나요?**:
  - 이 기능 역시 7-6의 `show_menu()` 와 `main()` 함수의 `while` 루프 및 `if/elif/else` 문으로 이미 기본 동작이 완성되어 있습니다.
- **예외 처리 원리**:
  - 사용자가 `1~7`, `0` 외에 `99`나 엔터(빈칸)를 치면 `else` 문에서 `⚠️ 잘못된 번호입니다. 다시 선택해 주세요.` 경고를 띄우고 메뉴를 다시 보여줍니다.
- **💻 터미널 테스트**:
  1. 터미널에서 `python prompt_manager.py` 실행
  2. 아무 문자(예: `abc`, `9`) 입력 후 경고 메시지 출력 확인
  3. `0` 입력하여 종료 확인
- **📝 Git 커밋**: 7-6에서 커밋했으므로 다음 단계로 넘어갑니다.

---

### 8-3. 프롬프트 추가 기능 (`add_prompt`) 🖥️ 💻
- **작업 위치**: 🖥️ VSCode 코드 에디터 (`prompt_manager.py`) → 💻 VSCode 터미널

#### 🛠️ [1단계] 에디터에서 함수 작성 🖥️
1. `prompt_manager.py` 파일을 엽니다.
2. `show_menu()` 함수 바로 위(또는 아래)에 다음 3개의 함수를 복사해서 붙여넣습니다:

```python
def ask_nonempty(label):
    """빈 값이면 다시 물어보는 입력 도우미."""
    while True:
        value = input(label).strip()
        if value:
            return value
        print("⚠️ 값을 비워둘 수 없습니다. 다시 입력해 주세요.")


def choose_category():
    """카테고리 번호를 선택하거나 직접 입력받는 도우미."""
    print("\n카테고리 선택:")
    for i, c in enumerate(CATEGORIES, start=1):
        print(f"{i}) {c}")
    while True:
        sel = input("선택(번호, 없으면 직접 입력): ").strip()
        if sel.isdigit() and 1 <= int(sel) <= len(CATEGORIES):
            return CATEGORIES[int(sel) - 1]
        if sel:  # 목록에 없는 새로운 카테고리는 직접 입력값 사용
            return sel
        print("⚠️ 카테고리를 입력해 주세요.")


def add_prompt(prompts):
    """새로운 프롬프트를 입력받아 리스트에 추가."""
    print("\n=== 프롬프트 추가 ===")
    title = ask_nonempty("제목: ")
    content = ask_nonempty("내용: ")
    category = choose_category()
    prompts.append({
        "title": title,
        "content": content,
        "category": category,
        "favorite": False
    })
    print("✅ 프롬프트가 추가되었습니다!")
```

#### 🛠️ [2단계] main() 함수에서 호출 연결 🖥️
`prompt_manager.py` 맨 아래 `main()` 함수를 찾아가서, 1번 선택 시 `[준비 중]`이었던 부분을 수정합니다:

```python
# 수정 전:
        if choice == "1":
            print("[준비 중] 프롬프트 추가")

# 아래처럼 수정:
        if choice == "1":
            add_prompt(prompts)
```
수정 후 **`Ctrl + S`** 를 눌러 저장합니다!

#### 💻 [3단계] 터미널에서 실행 테스트 💻
1. VSCode 터미널에 입력: `python prompt_manager.py`
2. `1` 입력 후 Enter
3. 제목 입력창에서 아무것도 안 치고 Enter만 쳤을 때: `⚠️ 값을 비워둘 수 없습니다` 경고가 뜨는지 확인!
4. 정상적으로 제목, 내용 입력하고 카테고리 번호(예: `1`) 입력
5. `✅ 프롬프트가 추가되었습니다!` 메시지가 뜨고 다시 메뉴로 돌아오면 성공!
6. `0` 입력하여 프로그램 종료

#### 📝 [4단계] 터미널에서 Git 커밋 💻
터미널에 아래 명령어를 복사하여 실행합니다:
```powershell
git add prompt_manager.py
git commit -m "feat: 프롬프트 추가 기능 및 입력값 검증"
```

---

### 8-4. 프롬프트 목록 보기 (`show_list`) — ⚠️ 브랜치 실습 대상! 💻 🖥️
- **작업 위치**: 💻 터미널(브랜치 이동) → 🖥️ 에디터(코드 작성) → 💻 터미널(커밋 & 머지)
- 📌 **매우 중요**: 이 기능은 과제 필수 제약인 **"브랜치를 생성하여 작업하고 main으로 merge"** 를 수행하는 핵심 실습입니다! (10장 내용과 바로 연결)

#### 💻 [1단계] 터미널에서 새 브랜치 생성 및 이동 💻
터미널에 아래 명령어를 입력합니다:
```powershell
git checkout -b feature/list
```
- `Switched to a new branch 'feature/list'` 메시지가 나오면 성공.

#### 🛠️ [2단계] 에디터에서 목록 함수 작성 🖥️
1. `prompt_manager.py` 파일을 열고, 8-0의 `format_line` 함수가 있는지 확인합니다.
2. 그 아래에 `show_list` 함수를 추가합니다:
```python
def show_list(prompts):
    """등록된 모든 프롬프트 목록을 출력."""
    print("\n=== 프롬프트 목록 ===")
    if not prompts:
        print("등록된 프롬프트가 없습니다.")
        return
    for i, p in enumerate(prompts, start=1):
        print(format_line(i, p))
    print(f"\n총 {len(prompts)}개의 프롬프트")
```
3. `main()` 함수에서 2번 부분을 교체합니다:
```python
# 수정 전:
        elif choice == "2":
            print("[준비 중] 프롬프트 목록")

# 아래처럼 수정:
        elif choice == "2":
            show_list(prompts)
```
4. **`Ctrl + S`** 를 눌러 저장합니다.

#### 💻 [3단계] 터미널에서 실행 테스트 💻
1. 터미널에서 `python prompt_manager.py` 실행
2. `2` 입력 후 Enter
3. 기본 등록된 3개의 프롬프트가 번호와 카테고리, 즐겨찾기(⭐) 표시와 함께 예쁘게 출력되는지 확인!
4. `0` 입력하여 프로그램 종료

#### 📝 [4단계] 브랜치에서 커밋 남기기 💻
터미널에서 현재 브랜치(`feature/list`)에 커밋을 기록합니다:
```powershell
git add prompt_manager.py
git commit -m "feat: 프롬프트 목록 출력 기능"
```

#### 💻 [5단계] main 브랜치로 돌아와서 병합(merge)하기 💻
터미널에서 아래 3줄을 순서대로 실행합니다:
```powershell
git checkout main
git merge feature/list
git push
```
- **✅ 확인**: 터미널에 `Updating ... Fast-forward` 또는 병합 완료 메시지가 뜨고 GitHub 원격 저장소까지 push되면 브랜치 실습 완료!

---

### 8-5. 카테고리별 조회 (`show_by_category`) 🖥️ 💻
- **작업 위치**: 🖥️ VSCode 코드 에디터 (`prompt_manager.py`) → 💻 VSCode 터미널

#### 🛠️ [1단계] 에디터에서 함수 작성 🖥️
1. `prompt_manager.py` 파일을 엽니다.
2. 아래 함수를 파일에 추가합니다:
```python
def show_by_category(prompts):
    """선택한 카테고리에 속한 프롬프트만 필터링하여 출력."""
    print("\n=== 카테고리별 조회 ===")
    category = choose_category()
    matched = [p for p in prompts if p["category"] == category]
    if not matched:
        print(f"[{category}] 카테고리에 프롬프트가 없습니다.")
        return
    print(f"\n[{category}] 카테고리 프롬프트:")
    for i, p in enumerate(matched, start=1):
        star = " ⭐" if p["favorite"] else ""
        print(f"{i}. {p['title']}{star}")
    print(f"\n총 {len(matched)}개의 프롬프트")
```
3. `main()` 함수에서 3번 부분을 교체합니다:
```python
# 수정 전:
        elif choice == "3":
            print("[준비 중] 카테고리별 조회")

# 아래처럼 수정:
        elif choice == "3":
            show_by_category(prompts)
```
4. **`Ctrl + S`** 를 눌러 저장합니다.

#### 💻 [2단계] 터미널 실행 테스트 💻
1. 터미널: `python prompt_manager.py` 실행
2. `3` 입력 → 카테고리 목록에서 `1` (텍스트 생성) 선택 → 기본 프롬프트 중 텍스트 생성 프롬프트만 출력되는지 확인!
3. `0` 입력하여 종료

#### 📝 [3단계] 터미널에서 Git 커밋 💻
```powershell
git add prompt_manager.py
git commit -m "feat: 카테고리별 조회 기능"
```

---

### 8-6. 프롬프트 검색 (`search_prompt`) 🖥️ 💻
- **작업 위치**: 🖥️ VSCode 코드 에디터 (`prompt_manager.py`) → 💻 VSCode 터미널

#### 🛠️ [1단계] 에디터에서 함수 작성 🖥️
1. `prompt_manager.py` 에 아래 함수를 추가합니다:
```python
def search_prompt(prompts):
    """키워드가 제목 또는 내용에 포함된 프롬프트를 검색."""
    print("\n=== 프롬프트 검색 ===")
    keyword = input("검색어: ").strip()
    if not keyword:
        print("⚠️ 검색어를 입력해 주세요.")
        return
    results = [p for p in prompts
               if keyword in p["title"] or keyword in p["content"]]
    if not results:
        print("검색 결과가 없습니다.")
        return
    print("\n검색 결과:")
    for i, p in enumerate(results, start=1):
        print(format_line(i, p))
    print(f"\n{len(results)}개의 프롬프트를 찾았습니다.")
```
2. `main()` 함수에서 4번 부분을 교체합니다:
```python
# 수정 전:
        elif choice == "4":
            print("[준비 중] 프롬프트 검색")

# 아래처럼 수정:
        elif choice == "4":
            search_prompt(prompts)
```
3. **`Ctrl + S`** 를 눌러 저장합니다.

#### 💻 [2단계] 터미널 실행 테스트 💻
1. 터미널: `python prompt_manager.py` 실행
2. `4` 입력 → 검색어에 `블로그` 입력 → 1건의 검색 결과가 뜨는지 확인!
3. 없는 단어(예: `우주선`) 입력 시 `검색 결과가 없습니다` 뜨는지 확인.
4. `0` 입력하여 종료

#### 📝 [3단계] 터미널에서 Git 커밋 💻
```powershell
git add prompt_manager.py
git commit -m "feat: 제목/내용 키워드 검색 기능"
```

---

### 8-7. 프롬프트 상세 보기 (`show_detail`) 🖥️ 💻
- **작업 위치**: 🖥️ VSCode 코드 에디터 (`prompt_manager.py`) → 💻 VSCode 터미널

#### 🛠️ [1단계] 에디터에서 함수 작성 🖥️
1. `prompt_manager.py` 에 아래 함수를 추가합니다:
```python
def show_detail(prompts):
    """번호를 선택받아 해당 프롬프트의 전체 내용을 상세 출력."""
    print("\n=== 프롬프트 상세 보기 ===")
    if not prompts:
        print("등록된 프롬프트가 없습니다.")
        return
    sel = input("번호 입력: ").strip()
    if not sel.isdigit() or not (1 <= int(sel) <= len(prompts)):
        print("⚠️ 올바른 번호가 아닙니다.")
        return
    p = prompts[int(sel) - 1]
    star = "⭐" if p["favorite"] else "없음"
    print("\n" + "─" * 30)
    print(f"제목: {p['title']}")
    print(f"카테고리: {p['category']}")
    print(f"즐겨찾기: {star}")
    print("─" * 30)
    print("내용:")
    print(p["content"])
    print("─" * 30)
```
2. `main()` 함수에서 5번 부분을 교체합니다:
```python
# 수정 전:
        elif choice == "5":
            print("[준비 중] 상세 보기")

# 아래처럼 수정:
        elif choice == "5":
            show_detail(prompts)
```
3. **`Ctrl + S`** 를 눌러 저장합니다.

#### 💻 [2단계] 터미널 실행 테스트 💻
1. 터미널: `python prompt_manager.py` 실행
2. `5` 입력 → 번호에 `1` 입력 → 블로그 글 작성 도우미의 상세 내용이 구분선과 함께 출력되는지 확인!
3. 번호에 `99` 나 문자 입력 시 `⚠️ 올바른 번호가 아닙니다` 가 뜨는지 확인.
4. `0` 입력하여 종료

#### 📝 [3단계] 터미널에서 Git 커밋 💻
```powershell
git add prompt_manager.py
git commit -m "feat: 프롬프트 상세 보기 기능"
```

---

### 8-8. 즐겨찾기 추가/해제 (`toggle_favorite`) 🖥️ 💻
- **작업 위치**: 🖥️ VSCode 코드 에디터 (`prompt_manager.py`) → 💻 VSCode 터미널

#### 🛠️ [1단계] 에디터에서 함수 작성 🖥️
1. `prompt_manager.py` 에 아래 함수를 추가합니다:
```python
def toggle_favorite(prompts):
    """번호를 받아 즐겨찾기 상태를 토글(참↔거짓 반전)."""
    print("\n=== 즐겨찾기 관리 ===")
    if not prompts:
        print("등록된 프롬프트가 없습니다.")
        return
    sel = input("프롬프트 번호 입력: ").strip()
    if not sel.isdigit() or not (1 <= int(sel) <= len(prompts)):
        print("⚠️ 올바른 번호가 아닙니다.")
        return
    p = prompts[int(sel) - 1]
    p["favorite"] = not p["favorite"]
    state = "추가했습니다" if p["favorite"] else "해제했습니다"
    print(f"'{p['title']}' 프롬프트를 즐겨찾기에 {state}!")
```
2. `main()` 함수에서 6번 부분을 교체합니다:
```python
# 수정 전:
        elif choice == "6":
            print("[준비 중] 즐겨찾기 관리")

# 아래처럼 수정:
        elif choice == "6":
            toggle_favorite(prompts)
```
3. **`Ctrl + S`** 를 눌러 저장합니다.

#### 💻 [2단계] 터미널 실행 테스트 💻
1. 터미널: `python prompt_manager.py` 실행
2. `6` 입력 → 번호 `2` 입력 → `즐겨찾기에 추가했습니다!` 메시지 확인
3. `2` (목록 보기) 입력 → 2번 제품 썸네일 항목에 `⭐` 이 붙어있는지 확인!
4. 다시 `6` 입력 → 번호 `2` 입력 → `즐겨찾기에 해제했습니다!` 메시지 확인
5. `0` 입력하여 종료

#### 📝 [3단계] 터미널에서 Git 커밋 💻
```powershell
git add prompt_manager.py
git commit -m "feat: 즐겨찾기 추가/해제 토글 기능"
```

---

### 8-9. 즐겨찾기 목록 보기 (`show_favorites`) 🖥️ 💻
- **작업 위치**: 🖥️ VSCode 코드 에디터 (`prompt_manager.py`) → 💻 VSCode 터미널

#### 🛠️ [1단계] 에디터에서 함수 작성 🖥️
1. `prompt_manager.py` 에 아래 함수를 추가합니다:
```python
def show_favorites(prompts):
    """즐겨찾기(favorite == True)된 프롬프트만 모아서 출력."""
    print("\n=== 즐겨찾기 목록 ===")
    favs = [p for p in prompts if p["favorite"]]
    if not favs:
        print("즐겨찾기된 프롬프트가 없습니다.")
        return
    for i, p in enumerate(favs, start=1):
        print(format_line(i, p))
    print(f"\n총 {len(favs)}개의 즐겨찾기")
```
2. `main()` 함수에서 7번 부분을 교체합니다:
```python
# 수정 전:
        elif choice == "7":
            print("[준비 중] 즐겨찾기 목록")

# 아래처럼 수정:
        elif choice == "7":
            show_favorites(prompts)
```
3. **`Ctrl + S`** 를 눌러 저장합니다.

#### 💻 [2단계] 터미널 실행 테스트 💻
1. 터미널: `python prompt_manager.py` 실행
2. `7` 입력 → 기본으로 즐겨찾기(⭐) 되어 있는 1번(블로그 글 작성 도우미)만 깔끔하게 출력되는지 확인!
3. `0` 입력하여 종료

#### 📝 [3단계] 터미널에서 Git 커밋 💻
```powershell
git add prompt_manager.py
git commit -m "feat: 즐겨찾기 목록 보기 기능"
```

---

### 8-10. 종료 처리 및 안내 🖥️ 💻
- **작업 위치**: 🖥️ VSCode 코드 에디터 (`prompt_manager.py`)
- **설명**:
  - `choice == "0"` 일 때 `break` 로 `while` 루프를 빠져나오며 프로그램이 끝납니다.
  - 이미 7-6 뼈대에 구현되어 있으므로 안내 문구가 마음에 들면 그대로 두셔도 됩니다.
- **📝 커밋**: 필요시 종료 메시지를 다듬고 커밋합니다:
```powershell
git add prompt_manager.py
git commit -m "feat: 종료 처리 및 종료 안내 메시지"
```

---

### 8-11. main에 모든 기능 연결 최종 점검 🖥️ 💻
- **작업 위치**: 🖥️ VSCode 코드 에디터 (`prompt_manager.py`)
- **확인**: 내 `prompt_manager.py` 파일 맨 아래의 `main()` 함수가 아래처럼 1번부터 7번까지 모든 함수를 호출하고 있는지 최종 점검합니다:

```python
def main():
    prompts = get_default_prompts()
    while True:
        show_menu()
        choice = input("선택: ").strip()
        if choice == "1":
            add_prompt(prompts)
        elif choice == "2":
            show_list(prompts)
        elif choice == "3":
            show_by_category(prompts)
        elif choice == "4":
            search_prompt(prompts)
        elif choice == "5":
            show_detail(prompts)
        elif choice == "6":
            toggle_favorite(prompts)
        elif choice == "7":
            show_favorites(prompts)
        elif choice == "0":
            print("프로그램을 종료합니다. 안녕히 가세요!")
            break
        else:
            print("⚠️ 잘못된 번호입니다. 다시 선택해 주세요.")
```
- 이상이 없으면 저장(`Ctrl + S`)하고 터미널에서 최종 연결 커밋을 남깁니다:
```powershell
git add prompt_manager.py
git commit -m "refactor: 메뉴와 각 기능 함수 연결"
```

---

## 9. 여기까지의 커밋 이력 흐름 확인 📖 💻

터미널에서 `git log --oneline` 을 실행하면 다음과 같은 예쁜 커밋 히스토리가 완성되어 있을 것입니다:

```
chore: 프로젝트 초기 설정 (README, .gitignore)
feat: 메뉴 뼈대와 기본 프롬프트 데이터 구성
feat: 프롬프트 추가 기능 및 입력값 검증
feat: 프롬프트 목록 출력 기능        ← 8-4에서 브랜치 작업 후 merge됨
feat: 카테고리별 조회 기능
feat: 제목/내용 키워드 검색 기능
feat: 프롬프트 상세 보기 기능
feat: 즐겨찾기 추가/해제 토글 기능
feat: 즐겨찾기 목록 보기 기능
refactor: 메뉴와 각 기능 함수 연결
```
👉 이 단계까지 왔다면 과제 필수 조건인 **"커밋 10개 이상"** 을 자연스럽게 달성하게 됩니다!

---

## 10. 브랜치 실습 복습 매뉴얼 📖 💻

> 8-4에서 브랜치 실습을 이미 진행했습니다. 혹시 흐름이 헷갈리셨던 분들을 위해 전체 원리와 단계를 한곳에 정리합니다.

### 왜 브랜치를 쓰나?
- **원리**: `main`은 언제나 고객이나 평가자에게 보여줄 수 있는 **동작하는 안정 버전**이어야 합니다.
- 새로운 기능이나 실험적인 코드는 `feature/...` 같은 별도의 작업선(브랜치)을 파서 작업하다가, 완벽히 동작하는 것이 확인되면 그때 `main`에 합칩니다(merge). 이렇게 하면 작업 중 에러가 나도 메인 프로그램은 망가지지 않습니다.

### 브랜치 작업 6단계 요약 (PowerShell 터미널):
1. **[터미널] 새 브랜치 생성 및 이동**:
```powershell
git checkout -b feature/list
```
2. **[에디터] 코드 작성 및 저장**: `prompt_manager.py` 에 함수 작성 및 `Ctrl + S`.
3. **[터미널] 브랜치에 커밋**:
```powershell
git add prompt_manager.py
git commit -m "feat: 프롬프트 목록 출력 기능"
```
4. **[터미널] main 브랜치로 복귀**:
```powershell
git checkout main
```
5. **[터미널] 만든 기능 합치기(merge)**:
```powershell
git merge feature/list
```
6. **[터미널] GitHub에 반영하기**:
```powershell
git push
```

### 충돌(Conflict)이 났을 때는 어떻게 하나요?
- 두 브랜치에서 **같은 파일의 같은 줄**을 서로 다르게 수정했을 때 발생합니다.
- 파일 안에 `<<<<<<< HEAD`, `=======`, `>>>>>>>` 표시가 나타나면, 에디터에서 원하는 코드만 남기고 표시 기호들을 전부 지운 뒤 `git add` → `git commit` 을 진행하면 해결됩니다.

---

## 11. 커밋 전략 가이드 📖

### 의미 있는 커밋이란?
- **하나의 논리적 변경 = 하나의 커밋**.
- "무엇을, 왜 바꿨는지"를 메시지만 보고도 알 수 있어야 합니다.
- ❌ **나쁜 커밋 메시지**: `수정`, `test`, `asdf`, 하루 종일 한 작업 1개에 몰아넣기.
- ⭕ **좋은 커밋 메시지**: `feat: 검색 기능 추가`, `fix: 상세 보기 범위 밖 번호 에러 수정`.

### 좋은 커밋 메시지 예시 목록:
```
chore: 프로젝트 초기 설정 (README, .gitignore)
feat: 메뉴 출력 및 번호 선택 처리 구현
feat: 기본 프롬프트 데이터 3종 등록
feat: 프롬프트 추가 기능 구현
feat: 프롬프트 추가 시 빈 값 재입력 검증 추가
feat: 프롬프트 목록 출력 기능 구현
feat: 카테고리별 조회 기능 구현
feat: 제목/내용 키워드 검색 기능 구현
feat: 프롬프트 상세 보기 기능 구현
feat: 즐겨찾기 추가/해제 토글 기능 구현
feat: 즐겨찾기 목록 보기 기능 구현
fix: 상세 보기에서 범위 밖 번호 입력 처리
refactor: 목록 출력 형식을 format_line 함수로 분리
docs: README에 실행 방법과 기능 목록 작성
chore: .gitignore에 __pycache__ 추가
style: 메뉴 출력 정렬 및 이모지 정리
```

---

## 12. README.md 완성 가이드 🖥️ 💻

- **작업 위치**: 🖥️ VSCode 코드 에디터 (`README.md` 파일 열기) → 💻 터미널 커밋 & push
- ⚠️ **초보자 주의**: 이 매뉴얼 파일이 아닙니다! 프로젝트 폴더 안의 **`README.md`** 파일을 열어서 아래 템플릿 내용으로 채우는 것입니다.

### 🛠️ [1단계] README.md 작성 🖥️
1. VSCode 탐색기에서 `README.md` 파일을 클릭하여 엽니다.
2. 4장에서 적어두었던 1줄 제목 밑으로, 아래 템플릿 내용을 복사하여 붙여넣습니다 (URL의 `내아이디` 부분은 본인 아이디로 수정):

```markdown
# 나만의 프롬프트 관리 프로그램

AI 프롬프트를 카테고리별로 정리하고 검색·즐겨찾기할 수 있는 콘솔 프로그램입니다.
터미널에서 메뉴 번호를 입력해 사용합니다.

## 실행 방법
1. Python 3.10 이상 설치
2. 저장소 클론
   ```bash
   git clone https://github.com/내아이디/prompt-manager.git
   cd prompt-manager
   ```
3. 프로그램 실행
   ```bash
   python prompt_manager.py
   ```

## 기능 목록
- 프롬프트 추가 (제목/내용/카테고리 선택 및 빈 값 검증)
- 프롬프트 목록 보기 (카테고리, 즐겨찾기 ⭐ 표시)
- 카테고리별 조회 (원하는 카테고리만 필터링)
- 키워드 검색 (제목과 내용에서 키워드 포함 여부 검색)
- 상세 보기 (구분선과 함께 전체 내용 확인)
- 즐겨찾기 추가/해제 (상태 토글)
- 즐겨찾기 목록 보기 (즐겨찾기된 프롬프트만 모아보기)
- 종료 (0번 선택 시 프로그램 정상 종료)

## 프롬프트 카테고리
| 카테고리 | 설명 |
|---|---|
| 텍스트 생성 | 글쓰기·요약 등 텍스트 관련 프롬프트 |
| 이미지 생성 | 이미지 생성용 프롬프트 |
| 영상 생성 | 영상/스크립트 프롬프트 |
| 페르소나 | 역할·성격 설정 프롬프트 |
| 자동화 | 반복 작업 자동화 프롬프트 |
| 기타 | 그 외 프롬프트 |

## 참고 사항
- 데이터는 프로그램 실행 중에 메모리에서 유지되며 프로그램 종료 시 초기화됩니다.
```
3. **`Ctrl + S`** 를 눌러 저장합니다.

#### 📝 [2단계] 터미널에서 Git 커밋 & Push 💻
터미널에 아래 명령어를 입력하여 GitHub에 올립니다:
```powershell
git add README.md
git commit -m "docs: README에 실행 방법과 기능 목록 작성"
git push
```

---

## 13. 제출물 준비 가이드 🌐 💻

과제 제출 시 필요한 3대 요소: **저장소 URL**, **개발 환경 스크린샷**, **실행 및 Git 그래프 스크린샷**.

### 13-1. GitHub 저장소 URL 🌐
- 웹 브라우저에서 본인 저장소 페이지(`https://github.com/내아이디/prompt-manager`)에 접속합니다.
- 브라우저 상단 주소창을 클릭하여 복사(`Ctrl + C`)합니다.
- **확인 팁**: 브라우저의 '시크릿 창'(`Ctrl+Shift+N`)을 열고 복사한 주소를 붙여넣어 보세요. 로그인하지 않아도 파일들이 잘 보인다면 'Public'으로 정상 공개된 것입니다.

### 13-2. 개발 환경 설정 스크린샷 💻 (Windows 단축키: `Win + Shift + S`)
VSCode 화면에서 터미널을 열고 다음 명령어들을 친 화면을 캡처합니다:
1. 터미널에 순서대로 입력:
```powershell
python --version
git --version
git config user.name
git config user.email
```
2. 키보드에서 **`Windows 키 + Shift + S`** 를 눌러 화면 캡처 도구를 실행합니다.
3. VSCode 창 전체(터미널 출력 내용과 왼쪽 하단 GitHub 로그인 상태 포함)를 드래그하여 캡처하고 이미지 파일로 저장합니다.

### 13-3. 프로그램 실행 결과 스크린샷 💻
1. 터미널에서 `python prompt_manager.py` 를 실행합니다.
2. `2`번(목록 보기)을 눌러 프롬프트 목록과 `⭐`이 예쁘게 나오는 화면을 띄웁니다.
3. `Win + Shift + S` 로 해당 터미널 실행 화면을 캡처하여 저장합니다. (검색이나 상세 보기 화면을 추가로 캡처해도 좋습니다)

### 13-4. `git log --graph` 스크린샷 (가장 중요!) 💻
- **작업 위치**: VSCode 터미널
- 브랜치가 갈라졌다가 합쳐진 그래프 형태의 이력을 확인하고 캡처합니다:
```powershell
git log --oneline --graph --all
```
- **화면 설명**: 좌측에 `*`, `|\`, `|/` 모양의 선이 보이면서 브랜치 생성과 merge 기록이 시각적으로 표시됩니다.
- (로그가 길어서 아래에 `:` 표시가 뜨면 키보드 `q` 를 누르면 터미널로 돌아옵니다)
- 이 그래프가 보이는 터미널 화면을 `Win + Shift + S` 로 캡처하여 저장합니다.

---

## 14. 테스트 체크리스트 💻

터미널에서 `python prompt_manager.py` 를 실행하고 하나씩 직접 눌러보며 체크하세요:

### 정상 기능 테스트
- [ ] 프로그램 실행 시 메뉴 1~7번과 0번이 바르게 출력된다.
- [ ] `1`번 추가: 새로운 프롬프트를 추가한 뒤 `2`번 목록에서 바로 확인된다.
- [ ] `2`번 목록: 기본 프롬프트 3개가 카테고리, 즐겨찾기(⭐)와 함께 번호대로 출력된다.
- [ ] `3`번 카테고리: 특정 카테고리를 골랐을 때 해당 카테고리 항목만 필터링되어 나온다.
- [ ] `4`번 검색: '블로그' 검색 시 제목/내용에 포함된 항목이 검색된다.
- [ ] `5`번 상세: 번호를 입력하면 구분선과 함께 제목, 카테고리, 전체 내용이 출력된다.
- [ ] `6`번 즐겨찾기: 번호를 입력하여 추가/해제 토글이 되고 `2`번 목록에 `⭐`이 반영된다.
- [ ] `7`번 즐겨찾기 목록: 즐겨찾기(⭐)된 항목만 쏙 뽑아서 출력된다.
- [ ] `0`번 종료: 프로그램 종료 안내 문구가 나오고 터미널로 완전히 복귀한다.

### 예외/오류 입력 방어 테스트
- [ ] 메뉴에서 `9`, `abc`, 빈칸 엔터 입력 시 프로그램이 꺼지지 않고 경고 후 메뉴로 돌아온다.
- [ ] 프롬프트 추가 시 제목이나 내용에 아무것도 안 치고 엔터를 누르면 재입력을 요구한다.
- [ ] 상세 보기나 즐겨찾기에서 리스트에 없는 번호(`99`)나 문자를 입력하면 경고 메시지가 나온다.

---

## 15. 초보자 디버깅 가이드 📖

오류가 나면 당황하지 말고 터미널 빨간 글씨의 **맨 마지막 줄**을 먼저 읽으세요!

| 에러 메시지 | 발생 원인 | 초보자 해결 방법 |
|---|---|---|
| `IndentationError` | 코드 들여쓰기가 비뚤어졌거나 탭/스페이스가 섞임 | 파이썬은 들여쓰기가 생명입니다. 함수 안쪽 코드는 반드시 **스페이스 4칸**으로 맞추세요. |
| `IndexError: list index out of range` | 리스트에 없는 번호를 꺼내려고 함 | `prompts[번호]` 접근 전 `1 <= int(번호) <= len(prompts)` 검사를 확인하세요. |
| `KeyError: 'title'` | 딕셔너리 키 철자 오타 | `'title'`, `'content'`, `'category'`, `'favorite'` 철자를 정확히 확인하세요. |
| `TypeError: ... str and int` | 문자열과 숫자를 잘못 비교함 | `input()`으로 받은 값은 문자열(`"1"`)입니다. 숫자와 비교하려면 `int(sel)`로 변환하세요. |
| `SyntaxError` | 괄호 닫기 누락, 쌍따옴표 짝 안 맞음 | 에러가 난 줄의 `()`, `{}`, `""` 짝이 맞는지 확인하세요. |
| `git push` 인증 오류 | GitHub 로그인이 풀림 | VSCode 좌측 하단 사람 아이콘 클릭 후 GitHub 로그인을 다시 진행하세요. |
| `fatal: remote origin already exists` | 원격 주소 등록 명령을 중복 실행함 | `git remote set-url origin <내URL>` 명령어로 덮어씌우세요. |

---

## 16. 핵심 용어 사전 📖

- **저장소 (Repository)**: 내 프로젝트의 모든 파일과 변경 이력이 영구히 보관되는 상자.
- **커밋 (Commit)**: 어떤 시점의 코드 상태를 사진 찍듯이 영구 저장한 스냅샷.
- **브랜치 (Branch)**: 메인 줄기(`main`)에 영향을 주지 않고 안전하게 독립적으로 작업하는 별도의 가지.
- **병합 (Merge)**: 브랜치에서 완성된 작업을 `main` 줄기로 합치는 동작.
- **푸시 (Push)**: 내 컴퓨터(로컬)에 기록된 커밋들을 GitHub(원격)에 업로드하는 것.
- **풀 (Pull)**: GitHub에 있는 최신 변경 사항을 내 컴퓨터로 내려받는 것.
- **클론 (Clone)**: GitHub에 있는 원격 저장소를 내 컴퓨터에 통째로 복제해 오는 것.

---

## 17. 최종 제출 전 최종 점검표

- [ ] 프로그램이 오류 없이 실행되고 1~7번, 0번 기능이 정상 동작한다.
- [ ] 기본 프롬프트가 3개 이상 등록되어 있다.
- [ ] 모든 기능이 각각 함수(`def`)로 깔끔하게 분리되어 있다.
- [ ] 커밋이 10개 이상 쌓여 있다 (`git log --oneline` 으로 확인).
- [ ] 브랜치 생성 및 머지(`git merge`) 기록이 그래프에 남아있다.
- [ ] **`git pull` 1회 이상 사용 조건 달성 여부 확인**:
  > 💡 **꿀팁: `git pull` 기록 쉽게 만드는 법 (1분 컷)**
  > 1. 웹 브라우저에서 본인의 GitHub 저장소 페이지에 들어갑니다.
  > 2. `README.md` 파일을 클릭하고 우측 상단의 **연필 모양(Edit)** 아이콘을 클릭합니다.
  > 3. 맨 끝에 엔터를 한 번 치고 화면 아래 초록색 **Commit changes** 버튼을 누릅니다.
  > 4. VSCode 터미널로 돌아와서 다음 명령어를 입력합니다:
  >    ```powershell
  >    git pull origin main
  >    ```
  > 👉 이렇게 하면 GitHub 웹의 변경 사항을 내 로컬로 가져오면서 `pull` 1회 사용 조건을 깔끔하게 달성하게 됩니다!
- [ ] `README.md` 가 완성되어 있다 (실행 방법, 기능 목록 포함).
- [ ] 터미널에 `git status` 를 쳤을 때 `working tree clean` (커밋 안 된 찌꺼기 파일 없음) 상태이다.
- [ ] 스크린샷 3종(환경 설정, 프로그램 실행, git log 그래프) 파일이 준비되었다.
- [ ] GitHub 저장소 URL을 복사해 두었다.

---

## 18. 부록

### 18-1. 완성된 `prompt_manager.py`의 전체 함수 구조도 📖
```
prompt_manager.py
├── CATEGORIES                (카테고리 상수 리스트)
├── get_default_prompts()     (기본 데이터 3종 생성)
├── format_line()             (목록 한 줄 형식 통일 유틸)
├── ask_nonempty()            (빈 값 재입력 유효성 검증 유틸)
├── choose_category()         (카테고리 번호 선택 도우미)
├── show_menu()               (콘솔 메뉴 출력)
├── add_prompt()              (1. 프롬프트 추가)
├── show_list()               (2. 프롬프트 목록 보기)
├── show_by_category()        (3. 카테고리별 조회)
├── search_prompt()           (4. 키워드 검색)
├── show_detail()             (5. 상세 보기)
├── toggle_favorite()         (6. 즐겨찾기 등록/해제)
├── show_favorites()          (7. 즐겨찾기 목록 보기)
└── main()                    (메뉴 반복 제어 루프)
```

### 18-2. 초보자를 위한 1줄 행동 원칙
- **코드를 고치면?** → 에디터에서 **`Ctrl + S`** 로 저장한다.
- **프로그램을 확인하려면?** → 터미널에서 **`python prompt_manager.py`** 친다.
- **기능이 잘 돌면?** → 터미널에서 **`git add .`** 하고 **`git commit -m "..."`** 한다.
- **작업이 끝나면?** → 터미널에서 **`git push`** 로 GitHub에 올린다.
