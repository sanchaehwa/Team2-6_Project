## 오픈소스SW의 이해 [2-6조] 팀프로젝트
### 간편하게 사용할 수 있는 타이머,스탑워치 구현
### Project Introduction 👋🏻
사용자가 프로그램 실행 시 스탑워치와 타이머 두 가지 모드 중 하나를 선택할 수 있는 프로그램이며. <br>
이 프로그램은 CLI (Command Line Interface) 환경에서 작동하며, 각 모드에 따라 적절한 기능을 수행합니다.
### Project System Architecture 🧾
```
				+---------------------------+
				|   사용자 (User Interface)  |
				+---------------------------+
				              |
				              v
				+---------------------------+
				|     모드 선택 (Main Menu)  |
				+---------------------------+
		                    |                |
		                    v                v
		        +------------------+   +-----------------+
		        |  스탑워치 모드      |   |  타이머 모드       |
		        | (Stopwatch Mode) |   | (Timer Mode)    |
		        +------------------+   +-----------------+
		                    |                   |
		                    v                   v
		        +------------------+   +-----------------+
		        |    시간 측정 및.    |   |    시간 설정 및   |
		        |     표시 기능      |   |     카운트다운     |
		        +------------------+   +-----------------+
		                    |                   |
		                    v                   v
				+---------------------------+
				|      종료 및 초기화 기능      |
				+---------------------------+
```

### Project Tech Stack & File Structure
#### Tech Stack 🔨
 <img src="https://img.shields.io/badge/python-3776AB?style=flat-square&logo=python&logoColor=white"> <br>
 Version: 3.12 이상 <br>
#### File Structure📂
```
.
├── README.md                
├── code
│   └── clock.py                # 스탑워치 및 타이머 기능이 포함된 메인 Python 코드
├── newvenv/                    # Python 가상 환경 폴더 (Python 3.12* 기반)
│   ├── bin/
│   │   ├── activate            # 가상 환경 활성화 스크립트 (Bash, Fish, csh 등)
│   │   ├── Activate.ps1        # 가상 환경 활성화 스크립트 (PowerShell용)
│   │   ├── pip, pip3, pip3.13  # 가상 환경 내 패키지 설치 관리 도구
│   │   ├── python, python3     # Python 실행 파일 (Python 3.12로 연결됨)
│   └── lib/
│       └── python3.13/
│           └── site-packages/  # 가상 환경 내 설치된 라이브러리
├── requirements.txt            # 프로젝트에 필요한 패키지 목록 
```

