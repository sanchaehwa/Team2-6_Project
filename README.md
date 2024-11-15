## 오픈소스SW의 이해 [2-6조] 팀프로젝트
### 간편하게 사용할 수 있는 타이머,스톱워치 구현
### Project Introduction 👋🏻
사용자가 프로그램 실행 시 스톱워치와 타이머 두 가지 모드 중 하나를 선택할 수 있으며, <br>
또한 이 프로그램은 CLI (Command Line Interface) 환경에서 작동하며, 각 모드에 따라 적절한 기능을 수행하는 프로그램입니다.

### Feature Responsible 👤
<table>
  <tr>
    <td align="center">
      <a href="https://github.com/DriedSlime">
        <img src="https://avatars.githubusercontent.com/DriedSlime" width="50px;" alt="DriedSlime"/>
      </a>
    </td>
    <td align="center">
      <a href="https://github.com/Hermes765">
        <img src="https://avatars.githubusercontent.com/Hermes765" width="50px;" alt="Hermes765"/>
      </a>
    </td>
	  <td align="center">
      <a href="https://github.com/sanchaehwa">
        <img src="https://avatars.githubusercontent.com/sanchaehwa" width="50px;" alt="sanchaehwa"/>
      </a>
    </td>
  </tr>
  <t>
    <td align="center">
      <b>심건우(Timer Feature)</b>
    </td>
	 <td align="center">
      <b>김성열(Stopwatch Feature)</b>
    </td>
    <td align="center">
      <b>양화영(Main Function)</b>
    </td>
   
  </tr>
</table>

### Project System Architecture 🧾
```
				+---------------------------+
				|   사용자 (User Interface)   |
				+---------------------------+
                                             |
                                             v
				+---------------------------+
				|     모드 선택 (Main Menu)   |
				+---------------------------+
		                    |                |
		                    v                v
		        +------------------+   +-----------------+
		        |  스톱워치 모드      |   |  타이머 모드       |
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
#### Tech Stack 🔨<br>

 <img src="https://img.shields.io/badge/python-3776AB?style=flat-square&logo=python&logoColor=white"> <br> `version: 3.12 이상` <br>

#### File Structure📂 <br>
```
.
├── README.md                
├── code
│   └── clock.py                # 스톱워치 및 타이머 기능이 포함된 메인 Python 코드
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

### cooperation strategy🥊
#### Git Branch Workflow <br>
```
    main["main (Stable)"] -->|Merge for Release| develop["develop (Integration)"]
    subgraph Features
        Stopwatch["Stopwatch 기능 구현"] --> develop 
        Timer["Timer 기능 구현"] --> develop
        Main["Main 함수 구현"] --> develop 
    end
    develop --> main 
```
<br>

develop 브렌치에서 기능을 구현한뒤, Main 브렌치에 병합하기전에 테스팅한 후, 병합 <br>
최종 테스팅은 메인에서 진행 <br>

