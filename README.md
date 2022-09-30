## 📎 목차

1. [Posting Service](#-posting-service)
2. [개발 기간](#-개발-기간)
3. [개발 인원](#-개발-인원)
4. [요구사항 및 분석](#-요구사항-및-분석)
5. [기술 스택](#-기술-스택)
6. [API Endpoints](#-api-endpoints)
7. [ERD](#-erd)
8. [참조 문서](#-참조-문서)

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
![](https://velog.velcdn.com/images/miracle-21/post/badea2b8-6c6e-494a-8ef5-ea309837c689/image.png)

#### 1. 상세페이지

![](https://velog.velcdn.com/images/miracle-21/post/27ebb8e7-0aca-45f2-a01d-23e2bb87c408/image.png)

#### 2. 댓글

![](https://velog.velcdn.com/images/miracle-21/post/c50a03f1-515a-4b07-bfe6-c41b8cd70303/image.png)


## 🔖 참조 문서
- [postman API 링크](https://documenter.getpostman.com/view/18832289/2s83tCLDXm)

![](https://velog.velcdn.com/images/miracle-21/post/8d1a41ff-ba3c-401b-b254-c5a3aba25f12/image.gif)


