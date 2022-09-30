## 📎 목차

1. [Posting Service](#-posting-service)
2. [개발 기간](#-개발-기간)
3. [개발 인원](#-개발-인원)
4. [요구사항 및 분석](#-요구사항-및-분석)
5. [기술 스택](#-기술-스택)
6. [API Endpoints](#api-endpoints)
7. [ERD](#-erd)
8. [참조 문서](#-참조-)

## 🚀Posting Service
SNS에 접속하여 게시물을 업로드 하거나 다른 사람의 게시물을 확인하고, 좋아요를 누를 수 있다.

## 📆 개발 기간
- 2022.09.27 ~ 2022.09.30(4일)

## 🧑🏻‍💻 개발 인원(1명)
- 박민하

## 📝 요구사항 및 구현 정도
\ | 기능 | 구현 여부 | 세부 사항
:--: | :--: | :--: | :--
유저 | 유저 회원가입 | ○ 
` | 유저 로그인 및 인증 | △ | - 비회원은 읽기만 가능하지만 회원은 다른 사람의 글도 수정/삭제가 가능한 문제가 있다.
게시글 | 게시글 생성 | ○ | - 제목, 내용, 해시태그 등을 입력하여 생성한다.
` | 게시글 수정 | △ | - 태그는 수정이 불가하다.
` | 게시글 삭제  | △ | - 복구는 불가하다.
` | 게시글 상세보기 | △ | - 조회 시 조회수가 1 증가한다. </br> - 좋아요를 누를 수 있지만 한 사람당 제한이 없고 취소가 불가하다.
` | 게시글 목록 | △ | - 게시글 목록에는 제목, 작성자, 해시태그, 작성일, 좋아요 수, 조회수 가 포함된다.  </br> - 페이지 당 게시글 수를 조정할 수 있다(default: 10건). </br> - 오름차순으로만 정렬된다. </br> - 검색과 필터링 기능은 없다.


## 🛠 기술 스택
Language | Framework | Database | HTTP | Tools
| :----------------------------------------------------------------------------------------------------: | :----------------------------------------------------------------------------------------------------: | :--------------------------------------------------------------------------------------------------: | :----------------------------------------------------------------------------------------------------------: | :------------------------------------------------------------------------------------------------------: |
| <img src="https://img.shields.io/badge/python-3776AB?style=for-the-badge&logo=python&logoColor=white"> | <img src="https://img.shields.io/badge/DRF-092E20?style=for-the-badge&logo=django&logoColor=white"> | <img src="https://img.shields.io/badge/mysql-4479A1?style=for-the-badge&logo=mysql&logoColor=white">  | <img src="https://img.shields.io/badge/postman-FF6C37?style=for-the-badge&logo=postman&logoColor=white"> |  <img src="https://img.shields.io/badge/git-F05032?style=for-the-badge&logo=git&logoColor=white">


## 🎯 API Endpoints
| endpoint | HTTP Method | 기능 
|----------|-------------|------
|api-auth/ | POST | 회원가입
|users/ | GET | 회원 정보 조회 
|users/:pk/ | PATCH, DELETE | 회원 정보 수정/회원 탈퇴 
|users/signup/ | POST | 로그인 
|posts/ | GET | 메인페이지
|posts/:pk/ | GET/PATCH/DELETE | 상세페이지 조회/수정/삭제
|posts/board/ | POST| 게시글 생성
|posts/comment/ | POST | 댓글 생성
|posts/comment/:pk/ |PATCH, DELETE | 댓글 수정/삭제
|posts/:pk/like/ | GET | 좋아요 추가


## 📚 ERD
![](https://velog.velcdn.com/images/miracle-21/post/6e8dad6b-ca12-4e62-9f18-690fa72faf31/image.png)
1. User
- 회원 정보
- 보완할 부분: 로그인 시 토큰이 발급되지만 아직 사용되는 곳이 없다.

2. Holding
- 투자 종목의 종목명, ISIN, 현재가, 자산그룹 정보

3. Acccount
- 회원 계좌의 계좌명, 계좌번호, 총 자산 정보

4. Investment
- 증권사 이름, 투자원금 정보

5. HoldingsRegist
- 거래 전 거래 정보를 hashing한 정보.
- 거래정보: 회원 계좌번호, 회원 이름, 종목명, 거래량
- 계좌번호는 JWT, 거래량은 해시 테이블 사용.
![](https://velog.velcdn.com/images/miracle-21/post/8829083d-73b6-427d-99e2-dd57d7e040da/image.png)

6. FinalHolding
- HoldingsRegist에서 등록한 거래정보 검증 후 실제 고객의 자산을 업데이트.

## 🔖 참조 문서
- [postman API 링크](https://documenter.getpostman.com/view/18832289/2s7Z7YJuGb)

![](https://velog.velcdn.com/images/miracle-21/post/4578c1c3-016c-4bde-9ee1-9273abde90ed/image.gif)

