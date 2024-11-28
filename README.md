# 관객 호응도 기반 반응형 응원봉 서비스

## 1. 제안 대상 설정

### 1.1. 기업 중심

| 제안 대상                   | 국내                                         | 해외                                                        |
| --------------------------- | -------------------------------------------- | ----------------------------------------------------------- |
| **엔터테인먼트 기업**       | SM, YG, JYP, HYBE, FNC 등 주요 아이돌 기획사 | 유니버설 뮤직 그룹, 소니 뮤직, 라이브 네이션, 비거스티컬 등 |
| **콘서트 주최사 및 기획사** | CJ ENM, 드림메이커                           | 라이브 네이션(Live Nation), AEG Presents                    |
| **테마파크/브랜드 협업**    | 롯데월드, 에버랜드, K-pop 박물관             | 디즈니랜드, 유니버설 스튜디오                               |
| **이벤트 및 스포츠 브랜드** | 프로야구, 프로축구 리그 구단                 | NFL, NBA, FIFA 등 스포츠 이벤트                             |

### 1.2. 소비자 중심

-   **팬덤 기반**: 아이돌 그룹, 아티스트의 충성도 높은 팬덤
-   **행사 고객**: 뮤지컬, 스포츠 경기 등 참여형 굿즈 수요층

## 2. 발표자료 구성 아이디어

기존 발표 경험과 황교수님/KT교수님 피드백 의견 충돌을 고려하여 적절히 발표자료를 구성하면 좋을 것 같다.

| 황교수님           | KT교수님                                  |
| ------------------ | ----------------------------------------- |
| 실전처럼           | 실전처럼                                  |
| 코드 삽입 필수     | 코드 삽입 지양                            |
| EDA 상세 과정 필수 | 청중의 집중도 고려하여 불필요한 내용 생략 |

이번에는 (1) **실전형 발표내용**와 (2) **평가만을 위한 발표내용**을 구분하여 발표를 해보면 좋을 것 같다.

-   전반부는 실전형 발표내용으로 구성되며, 아래와 같은 내용이 주를 이룬다.
    -   1부. **서비스 제안**
        -   배경
        -   문제 정의
        -   솔루션
        -   기능
        -   기대 효과
-   후반부는 평가용 발표 보강 내용으로 구성되며, 아래와 같은 내용이 주를 이룬다.
    -   2부. **EDA**
        -   가설 정의
        -   결론 도출
        -   AI 모델링

## 3. 발표 내용

### 3.1. 소개

-   제목
-   팀 소개
-   Executive Summary
-   목차

#### 3.1.1. Executive Summary

경영진을 위한 핵심 요약이므로, 목차 이전에 배치하여 빠르게 요약된 정보를 전달한다.

> "바쁘신 분들은 이것만 보고 떠나시면 되고, 이 사업 제안에 관심이 있다면 이후 발표도 들어주세요."
> <br>...라는 컨셉을 갖고 발표의 초반에 배치하였다.

-   **문제 정의**
    -   응원봉 시장의 높은 매출/영업이익률을 이용하여 사업성을 높이고자 함
    -   사업성 단점 및 도전과제
        -   **높은 개발비와 단가**
            -   센서와 S/W 개발 비용 상승 → 생산 단가가 기존 대비 높아질 가능성 존재
            -   대량 생산 필요 → 초기 수요 예측 실패 시 재고 부담
        -   **기술적 제약**
            -   콘서트장의 네트워크 연결성 문제
            -   배터리 소모 문제 → 긴 공연 시간 대비 충분한 배터리 용량 필요
        -   **시장 반응 불확실성**
            -   기존 LED 응원봉과 큰 차별성을 느끼지 못할 경우 초기 수요 저조 가능성 존재
        -   **데이터 프라이버시 문제**
            -   센서 데이터를 통한 팬들 움직입 분석이 개인정보 침해로 인식될 가능성 존재
-   **솔루션**
    -   센서 데이터에 기반하여 무대 관람 경험을 극대화 시켜주는 응원봉 형태의 굿즈 제작
-   **기능**
    -   자세/상태 별로 응원봉의 LED 상태를 변경

#### 3.1.2. 목차 (발표 진행 순서)

-   1부. 서비스 제안
    -   배경
    -   문제 정의
    -   솔루션
    -   기능
    -   기대 효과
-   2부. EDA (서비스 제안에 대한 근거)
    -   가설 정의
    -   결론 도출
    -   AI 모델링

### 3.2. (1부) 서비스 제안

#### 3.2.1. 배경

> 배경 섹션에서는 청자로 하여금 발표 주제에 대한 공감대를 (짧고 빠르게) 형성할 수 있도록 하며,
> <br>현재 응원봉 시장의 현황과 동향을 브리핑해준다.

-   "배경" 섹션에서 소개하면 좋을 포인트:
    -   실제 콘서트 관객의 응원봉 소지율은 약 60%
    -   아티스트 별로 응원봉이 다르게 생겼다.
        -   아티스트 별로 하나 씩 여러 개의 응원봉을 구입하는 사람도 존재한다.
    -   버전이 붙어있는 것이 존재한다.
        -   여러 버전이 있었음을 알 수 있다.
        -   ~~버전 업그레이드에 따른 재구매율~~
    -   응원봉의 시중 가격대를 소개한다.

##### 3.2.1.1. 공감대 형성

교수님을 포함한 **대다수의 청자들은** 직책상 콘서트 문화를 잘 이해하지 못해 **본 주제에 공감하지 못할 가능성**이 높다.

→ 공감대를 형성할 수 있도록...

동영상으로도 10초정도 보여주면 좋을 것 같다.

![Live Clip 아이와 나의 바다](https://i.ytimg.com/vi/nn1pbxe8bAI/maxresdefault.jpg)

-   영상 출처: <https://www.youtube.com/watch?v=nn1pbxe8bAI>

실제 콘서트 이미지/영상을 보여준다.

![](https://images.squarespace-cdn.com/content/v1/6127bd65b111ea759eab3094/421a434d-4e79-432a-92eb-3bca3aad6891/purple+wave.jpg)

-   사진 자료 출처: <https://www.cherrychumagazine.com/entertainment/kpop-lighsticks>

![](https://seoulspace.com/wp-content/uploads/2021/03/lightsticks.jpg)

-   사진 자료 출처: <https://seoulspace.com/best-kpop-lightsticks-you-can-buy-online-right-now/>

##### 3.2.1.2. 시장 조사

시중에 출시된 응원봉들에는 어떤 것들이 있는지 보여준다.

평균적인 가격대는 약 $58.19 (한화 약 8만원)로 형성되어 있는 것을 알 수 있음.

| 아티스트명 | 응원봉 제품명                                        | 가격   | 응원봉 이미지                                                                | 스마트폰 연동 | 배터리                                   | 내장 스피커 탑재 |
| ---------- | ---------------------------------------------------- | ------ | ---------------------------------------------------------------------------- | ------------- | ---------------------------------------- | ---------------- |
| BTS        | BTS Official Lightstick ver. 3                       | $37.88 | ![](https://seoulspace.com/wp-content/uploads/2021/03/bts.png)               |               | AAA                                      |                  |
| BLACKPINK  | BLACKPINK Official Lightstick Ver. 2 Limited Edition | $50.85 | ![](https://seoulspace.com/wp-content/uploads/2021/03/blackpink.jpg)         |               |                                          |                  |
| NCT        | NCT Official Lightstick                              | $75.09 | ![](https://seoulspace.com/wp-content/uploads/2021/03/nct.jpg)               |               |                                          |                  |
| TWICE      | TWICE Official Candy Lightstick Ver. 2               | $57.99 | ![](https://seoulspace.com/wp-content/uploads/2021/03/twice.jpg)             |               |                                          |                  |
| SEVENTEEN  | SEVENTEEN Official CARAT BONG Lightstick Ver. 2      | $68.90 | ![](https://seoulspace.com/wp-content/uploads/2021/03/seventeen.jpg)         |               |                                          |                  |
| MAMAMOO    | MAMAMOO Official Lightstick Ver. 2.5                 | -      | ![](https://seoulspace.com/wp-content/uploads/2021/03/mamamoo-640x613-1.jpg) |               |                                          |                  |
| STRAY KIDS | STRAY KIDS Official Lightstick (NACHIMBONG)          | $44.99 | ![](https://seoulspace.com/wp-content/uploads/2021/03/straykids.jpg)         |               |                                          |                  |
| TXT        | TXT Official Lightstick                              | $64.99 | ![](https://seoulspace.com/wp-content/uploads/2021/03/txt.jpg)               |               |                                          | O                |
| ATEEZ      | ATEEZ Official Lightstick                            | $54.99 | ![](https://seoulspace.com/wp-content/uploads/2021/03/ateez.jpg)             | O             | X                                        |                  |
| WAYV       | WAYV Official Lightstick                             | $67.99 | ![](https://seoulspace.com/wp-content/uploads/2021/03/wavyv-640x634-1.jpg)   | X             | AAA (재충전 방식 사용시 블루투스 미지원) |                  |
| 평균       | -                                                    | $58.19 | -                                                                            | -             | -                                        | -                |

-   자료 출처: <https://seoulspace.com/best-kpop-lightsticks-you-can-buy-online-right-now/>

#### 3.2.2. 문제 정의

##### 3.2.2.1. 매출 추이

2019 - 2021 "[K팝 음반 이외 주요 상품 매출 추이(notebooks/K팝 음반 이외 주요 상품 매출 추이.ipynb)]"는 아래와 같다.

![K팝 음반 이외 주요 상품 매출 추이](https://github.com/user-attachments/assets/f9ca20b7-8a6d-44dc-bd6b-0803e746e691)
![K팝 음반 이외 주요 상품 매출 추이](https://github.com/user-attachments/assets/2ae0b6c4-34e4-4779-8e88-a28d5e694d62)

위의 장표로 두 가지를 알 수 있다.

1. 2021년 펜데믹 이후로 매출이 급감하였다.
2. (그럼에도 매해 년도) 응원봉의 매출액 비중이 굉장히 높다.

##### 3.2.2.1. 목표 설정

> 펜데믹이 종료된 이후 판매액이 다시 돌아오고 있다고 가정해보자.
> <br>
> (TODO: EDA 필요)

-   응원봉이 매출액의 상당부분을 차지한다는 점에 착안하여, **응원봉 판매를 촉진**시키고자 한다.
-   공연 기획자가 "**관객 호응도**"와 같은 향후 공연 기획에 참고할 수 있는 **데이터를 수집**할 수 있도록 하고자 한다.

#### 3.2.3. 솔루션

##### 3.2.3.1. 제품 소개

> 새로운 응원봉을 제안한다고 주장하자.

\[센서\] + \[응원봉\]

관객의 호응에 반응하는 뉴메타 응원봉을 제안.

-   자이로, 가속도 센서 기반 사용자 동작 감지
-   사용자의 동작의 맥락에 맞추어 응원봉의 색상, 밝기를 제어

정리하면,

-   주제: "제품명"
    -   제품명 아이디어 (하하)
        1. Dynamic Lightstick
        2. Vibestick
        3. Vibe Lightstick
        4. Lightstick Vibe edition
-   부제: 가속도/자이로 센서와 응원봉을 결합하여 관객의 동작에 반응하는 응원봉

<details>
<summary>Vibe의 뜻 (ft. ChatGPT)</summary>
<br>
<blockquote>

"**Vibe**"는 다양한 상황에서 사용되는 단어로, 주로 다음과 같은 뜻을 가집니다:

1.  감각적 분위기 (명사로 사용)

    -   어떤 장소, 사람, 상황 등이 풍기는 분위기나 느낌을 의미합니다.
    -   긍정적, 부정적, 중립적 느낌을 표현하는 데 자주 사용됩니다.
    -   예: “The cafe has a really cozy vibe.”

    (그 카페는 정말 아늑한 분위기를 풍겨.) - 예: “I got a strange vibe from him.”
    (그에게서 이상한 느낌을 받았어.)

2.  기분 또는 에너지 (명사로 사용)

    -   특정한 감정 상태나 에너지를 나타냅니다.
    -   예: “I’m in a chill vibe today.”

    (오늘은 편안한 기분이야.)

3.  사람 간의 화합 또는 텔레파시 느낌 (동사로 사용)

    -   서로 잘 통하거나 비슷한 에너지를 공유하는 상태를 표현.
    -   예: “We really vibed at the party.”

    (우린 파티에서 정말 잘 통했어.)

4.  음악적 맥락에서 리듬이나 느낌 (명사로 사용)

    -   곡이 주는 특유의 감성이나 리듬을 설명하는 데 사용됩니다.
    -   예: “This song has a good vibe.”

    (이 노래는 좋은 감성이 있어.)

5.  젊은 층의 은어 (일반적 사용)

    -   특정한 라이프스타일, 태도, 행동양식을 표현하기도 합니다.
    -   예: “She’s got that artistic vibe.”

    (그녀는 예술적인 느낌이 있어.)

**요약**:

> “Vibe”는 특정 감정, 에너지, 분위기를 표현하는 다재다능한 단어로, 상황에 따라 다양하게 활용됩니다. 감각적이고 직관적인 느낌을 전달하는 데 탁월합니다.

</blockquote>
</details>

> 관객이 제품을 사용하는 모습의 스케치를 이 섹션에서 보여주면 좋을 것 같다. (아이패드로 간단하게라도 그려보자.)

#### 3.2.4. 기능 및 활용 예시

##### 3.2.4.1. 동작 정의

사용자의 동작을 아래와 같이 다섯 가지로 정의한다.

| 동작 구분  | 설명                                                                                                                   | 감지 방법                                                                                                    |
| ---------- | ---------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------ |
| `SHAKING`  | 응원봉을 앞,옆,뒤로 흔드는 행위                                                                                        | 가속도 센서 + 자이로 센서 + Jerk 를 이용하여 감지한다. (반복적인 수평 이동이 감지되며, jerk가 심한 경우.)    |
| `JUMPING`  | 응원봉을 들고 위 아래로 뛰는 행위                                                                                      | 가속도 센서 + 자이로 센서 + Jerk 를 이용하여 감지한다. (반복적인 수직 이동이 감지되며, jerk가 심한 경우.)    |
| `LEAVING`  | 공연장을 떠나는 행위                                                                                                   | walking, staircase-up, staircase-down 과 같이 이동 중인 경우.                                                |
| `ROTATING` | 응원봉을 잡고 시계 방향, 혹은 반시계 방향으로 돌리는 행위                                                              | 가속도 센서 + 자이로 센서 + jerk 를 이용하여 감지한다. (jerk가 약하지만 지속적인 각속도의 변화가 있는 경우.) |
| `LOSTCTRL` | 응원봉의 전원이 켜져있지만 지면에 일정 시간 이상 수평으로 놓인 상태<br>혹은 사용자가 손에 쥐고 제어하지 않고 있는 상태 | laying 상태의 경우.                                                                                          |
| `NEUTRAL`  | 응원봉의 소지자의 움직임이 적거나 정적인 자세를 유지하고 있는 상태                                                     | standing, sitting 과 같은 정적인 상태인 경우.                                                                |

##### 3.2.4.2. 동작 별 활용 예시

동작 별 활용 예시를 아래와 같이 제안한다.

| 동작 구분  | 활용 예시                                                                                                                                                     |
| ---------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `SHAKING`  | 흔들면 응원봉이 더 밝게 빛나거나 색상이 변경됨 (긍정적인 분위기 조성 및 관객 호응도 혹은 흥분도의 지표를 측정하기 위해 참고 가능)                             |
| `JUMPING`  | 응원봉을 들고 뛰면 응원봉이 점멸함. (긍정적인 분위기 조성 및 관객 호응도 혹은 흥분도의 지표를 측정하기 위해 참고 가능)                                        |
| `LEAVING`  | 공연장을 떠나거나, 화장실 등에 방문하기 위해 관객이 이동 시에는 응원봉 LED의 밝기를 낮추어 관객과 아티스트의 몰입도가 분산되는 것을 방지.                     |
| `ROTATING` | 회전 방향에 따라 관객 투표용으로 활용 가능 (2지 선다형)                                                                                                       |
| `LOSTCTRL` | 분실로 판단하거나, 비상 상황(사용자가 쓰러진 경우)인 것으로 볼 수 있다. 스마트폰과 응원봉을 연동한 경우 - 이 상태가 지속되면 분실 안내 알림을 띄워줄 수 있다. |
| `NEUTRAL`  | 중앙제어를 통하여 응원봉을 제어하거나 일정한 색상으로 빛난다.                                                                                                 |

<details>
<summary><code>LOSTCTRL</code>상태 관련 "<b>안전 사고 관리</b>" 추가 아이디어</summary>
<br>
<blockquote>

-   응원봉에 비가시광선 LED (적외선 혹은 자외선)를 탑재한다.
-   응원봉이 `LOSTCTRL` 상태가 되면, 해당 응원봉에서 비가시광선을 높은 밝기로 출력하도록 한다.
-   제어실에 설치된 특수 카메라로 `LOSTCTRL`상태시 출력되는 비가시광선이 나타나는 지역을 파악한다.
-   비가시광선이 탐지된 지역을 안전사고 발생의 징후가 높은 지역으로 보고 해당 지역의 집중 관리를 시도할 수 있다.

</blockquote>
</details>

#### 3.2.5. 서비스 제안 근거

극복해야 할 한계들로 다음과 같은 것들이 존재:

-   **높은 개발비와 단가**
    -   센서와 S/W 개발 비용 상승 → 생산 단가가 기존 대비 높아질 가능성 존재
    -   대량 생산 필요 → 초기 수요 예측 실패 시 재고 부담
-   **기술적 제약**
    -   콘서트장의 네트워크 연결성 문제
    -   배터리 소모 문제 → 긴 공연 시간 대비 충분한 배터리 용량 필요
-   **시장 반응 불확실성**
    -   기존 LED 응원봉과 큰 차별성을 느끼지 못할 경우 초기 수요 저조 가능성 존재
-   **데이터 프라이버시 문제**
    -   센서 데이터를 통한 팬들 움직입 분석이 개인정보 침해로 인식될 가능성 존재

##### 3.2.5.1. 높은 개발비와 단가

> 이 정도 생산 단가면 감당 가능하다를 주장해야 함.
>
> P.S. 기존 응원봉의 평균 단가는 $58.19 이다.

-   예상 생산 단가: ~~~ (TODO: 산정하기)

    -   응원봉 디자인 개발 비용:
    -   HW 제작 단가:
    -   SW R&D 비용:

##### 3.2.5.2. 기술적 제약

-   (실습 과제) 센서 데이터 분석을 통해 현실적으로 구현 가능한 기술임을 시사
-   콘서트 장에서 블루투스를 통한 응원봉 제어 기술은 이미 존재하고 활용 사례가 다수 존재
-   대다수 콘서트에서 사용하는 AA, AAA 사이즈 건전지를 2~3개 사용하여 지속력 유지. (역시 기존 콘서트 사례들을 통해 가능함을 알 수 있음)

##### 3.2.5.3. 시장 반응 불확실성

> TODO: EDA를 통한 조사 후 데이터 통계를 넣을 것

-   기존 수요 및 매출액/판매량 추이를 통해 예측해본다.

##### 3.2.5.4. 데이터 프라이버시 문제

기술적으로는 두 가지 해결 방법이 존재한다.

-   데이터의 익명화를 철저히 한다.
-   애플리케이션 지원을 통해 자신의 정보를 제거할 수 있는 기능을 제공한다.

고객이 심리적으로 느낄 수 있는 거부감에 대해 완화하는 것도 중요하다.

-   애플리케이션에서 고객의 공연 호응/참여도를 토대로 감성적인 메시지를 출력하여 준다.
    -   예시 (GPT가 쓴거 아님.):
        -   "당신은 프로 쉐이커: 공연에서 응원봉을 가장 많이 흔든 상위 1%에요!" (SHAKING 상위 1%)
        -   "박차오르는 열정으로! 공연에서 가장 열정적으로 뛴 상위 1%에요!" (JUMPING 상위 1%)
        -   "가슴 깊이 응원하는 어른스런 마음으로." (NEUTRAL 상위 1%)
    -   상위 #% 이내는 퍼센트 수치를 출력해주고, 하위에 대해서는 수치는 제외하여 출력한다.
        -   상위권 쟁탈을 위한 경쟁 심리는 자극하되, 낮은 순위로 인한 좌절감을 느끼지는 못하도록 한다.
    -   SNS에 공유하는 기능을 통해 바이럴 마케팅을 노릴 수도 있다.

#### 3.2.6. 기대 효과

-   새로운 기능의 도입으로 기존의 응원봉과 차별성을 강조하여 성공적인 마케팅으로 이어질 수 있다.
-   아티스트와 상호작용을 하고자 하는 소비자의 니즈를 일부 충족시킬 수 있다.
-   매출액의 높은 비중을 차지했던 응원봉의 고객 수요를 이끌어 낼 수 있다.

### 3.3. (2부) EDA

> TODO
